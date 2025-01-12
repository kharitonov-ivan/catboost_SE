#include "feature_parallel_dataset_builder.h"
#include "compressed_index_builder.h"
#include "feature_layout_feature_parallel.h"
#include "dataset_helpers.h"

#include <catboost/libs/helpers/vector_helpers.h>


namespace NCatboostCuda {

    TFeatureParallelDataSetsHolder TFeatureParallelDataSetHoldersBuilder::BuildDataSet(const ui32 permutationCount) {
        TFeatureParallelDataSetsHolder dataSetsHolder(DataProvider,
                                                      FeaturesManager);

        Y_ASSERT(dataSetsHolder.CompressedIndex);
        TSharedCompressedIndexBuilder<TDataSetLayout> compressedIndexBuilder(*dataSetsHolder.CompressedIndex);

        dataSetsHolder.CtrTargets = BuildCtrTarget(FeaturesManager,
                                                   DataProvider,
                                                   LinkedTest);
        auto& ctrsTarget = *dataSetsHolder.CtrTargets;

        {
            dataSetsHolder.LearnCatFeaturesDataSet = new TCompressedCatFeatureDataSet(CatFeaturesStorage);
            BuildCompressedCatFeatures(DataProvider,
                                       *dataSetsHolder.LearnCatFeaturesDataSet);

            if (LinkedTest) {
                dataSetsHolder.TestCatFeaturesDataSet = new TCompressedCatFeatureDataSet(CatFeaturesStorage);
                BuildCompressedCatFeatures(*LinkedTest,
                                           *dataSetsHolder.TestCatFeaturesDataSet);
            }
        }

        TAtomicSharedPtr<TPermutationScope> permutationIndependentScope = new TPermutationScope;

        dataSetsHolder.PermutationDataSets.resize(permutationCount);

        const auto learnWeights = NCB::GetWeights(DataProvider.TargetData);

        const bool isTrivialLearnWeights = AreEqualTo(learnWeights, 1.0f);
        {
            const auto learnMapping = NCudaLib::TMirrorMapping(ctrsTarget.LearnSlice.Size());

            if (isTrivialLearnWeights == ctrsTarget.IsTrivialWeights()) {
                dataSetsHolder.DirectWeights = ctrsTarget.Weights.SliceView(ctrsTarget.LearnSlice);
            } else {
                dataSetsHolder.DirectWeights.Reset(learnMapping);
                dataSetsHolder.DirectWeights.Write(learnWeights);
            }
            if (isTrivialLearnWeights && ctrsTarget.IsTrivialWeights()) {
                dataSetsHolder.DirectTarget = ctrsTarget.WeightedTarget.SliceView(ctrsTarget.LearnSlice);
            } else {
                dataSetsHolder.DirectTarget.Reset(learnMapping);
                dataSetsHolder.DirectTarget.Write(GetTarget(DataProvider.TargetData));
            }
        }

        for (ui32 permutationId = 0; permutationId < permutationCount; ++permutationId) {
            TDataPermutation permutation = NCatboostCuda::GetPermutation(DataProvider,
                                                                         permutationId,
                                                                         DataProviderPermutationBlockSize);

            const auto targetsMapping = NCudaLib::TMirrorMapping(ctrsTarget.LearnSlice.Size());

            TMirrorBuffer<ui32> indices;
            indices.Reset(targetsMapping);
            permutation.WriteOrder(indices);
            TMirrorBuffer<ui32> inverseIndices;

            TMirrorBuffer<float> targets;
            TMirrorBuffer<float> weights;

            if (permutation.IsIdentity()) {
                inverseIndices = indices.CopyView();
                targets = dataSetsHolder.DirectTarget.CopyView();
            } else {
                inverseIndices.Reset(targetsMapping);
                permutation.WriteInversePermutation(inverseIndices);

                targets.Reset(dataSetsHolder.DirectTarget.GetMapping());
                Gather(targets, dataSetsHolder.DirectTarget, indices);
            }

            if (isTrivialLearnWeights) {
                weights = dataSetsHolder.DirectWeights.CopyView();
            } else {
                weights.Reset(dataSetsHolder.DirectTarget.GetMapping());
                Gather(weights, dataSetsHolder.DirectWeights, indices);
            }

            dataSetsHolder.PermutationDataSets[permutationId] = new TFeatureParallelDataSet(DataProvider,
                                                                                            dataSetsHolder.CompressedIndex,
                                                                                            permutationIndependentScope,
                                                                                            new TPermutationScope(),
                                                                                            *dataSetsHolder.LearnCatFeaturesDataSet,
                                                                                            dataSetsHolder.GetCtrTargets(),
                                                                                            TTarget<NCudaLib::TMirrorMapping>(std::move(targets),
                                                                                                                              std::move(weights),
                                                                                                                              std::move(indices)),
                                                                                            std::move(inverseIndices),
                                                                                            std::move(permutation));
        }

        if (LinkedTest != nullptr) {
            BuildTestTargetAndIndices(dataSetsHolder, ctrsTarget);
        }

        auto allFeatures = GetLearnFeatureIds(FeaturesManager);
        TVector<ui32> permutationIndependent;
        TVector<ui32> permutationDependent;

        {
            SplitByPermutationDependence(FeaturesManager,
                                         allFeatures,
                                         permutationCount,
                                         &permutationIndependent,
                                         &permutationDependent);
        }

        auto learnMapping = dataSetsHolder.PermutationDataSets[0]->GetSamplesMapping();

        TBinarizationInfoProvider learnBinarizationInfo(FeaturesManager,
                                                        &DataProvider);

        const ui32 permutationIndependentCompressedDataSetId = compressedIndexBuilder.AddDataSet(learnBinarizationInfo,
                                                                                                 {"Learn permutation-independent features"},
                                                                                                 learnMapping,
                                                                                                 permutationIndependent);

        for (ui32 permutationId = 0; permutationId < permutationCount; ++permutationId) {
            auto& dataSet = *dataSetsHolder.PermutationDataSets[permutationId];
            if (permutationDependent.size()) {
                const auto& permutation = dataSet.GetCtrsEstimationPermutation();
                TVector<ui32> gatherIndices;
                permutation.FillOrder(gatherIndices);

                TDataSetDescription description;
                description.Name = TStringBuilder() << "Learn permutation dependent features #" << permutationId;
                dataSet.PermutationDependentFeatures = compressedIndexBuilder.AddDataSet(learnBinarizationInfo,
                                                                                         description,
                                                                                         learnMapping,
                                                                                         permutationDependent,
                                                                                         new TVector<ui32>(std::move(gatherIndices)));
            }
            dataSet.PermutationIndependentFeatures = permutationIndependentCompressedDataSetId;
        }

        ui32 testDataSetId = -1;
        if (LinkedTest) {
            TDataSetDescription description;
            description.Name = "Test dataset";
            TBinarizationInfoProvider testBinarizationInfo(FeaturesManager,
                                                           LinkedTest);

            auto testMapping = dataSetsHolder.TestDataSet->GetSamplesMapping();
            testDataSetId = compressedIndexBuilder.AddDataSet(testBinarizationInfo,
                                                              description,
                                                              testMapping,
                                                              allFeatures);

            dataSetsHolder.TestDataSet->PermutationIndependentFeatures = testDataSetId;
        }

        compressedIndexBuilder.PrepareToWrite();

        {
            TFloatAndOneHotFeaturesWriter<TFeatureParallelLayout> floatFeaturesWriter(FeaturesManager,
                                                                                      compressedIndexBuilder,
                                                                                      DataProvider,
                                                                                      permutationIndependentCompressedDataSetId);
            floatFeaturesWriter.Write(permutationIndependent);
        }

        if (LinkedTest) {
            TFloatAndOneHotFeaturesWriter<TFeatureParallelLayout> floatFeaturesWriter(FeaturesManager,
                                                                                      compressedIndexBuilder,
                                                                                      *LinkedTest,
                                                                                      testDataSetId);
            floatFeaturesWriter.Write(permutationIndependent);
        }

        {
            TBatchedBinarizedCtrsCalcer ctrsCalcer(FeaturesManager,
                                                   ctrsTarget,
                                                   DataProvider,
                                                   dataSetsHolder.PermutationDataSets[0]->GetTarget().GetIndices(),
                                                   LinkedTest,
                                                   LinkedTest ? &dataSetsHolder.TestDataSet->GetTarget().GetIndices() : nullptr);

            TCtrsWriter<TFeatureParallelLayout> ctrsWriter(FeaturesManager,
                                                           compressedIndexBuilder,
                                                           ctrsCalcer,
                                                           permutationIndependentCompressedDataSetId,
                                                           testDataSetId);
            ctrsWriter.Write(permutationIndependent);
        }

        if (permutationDependent.size()) {
            for (ui32 permutationId = 0; permutationId < permutationCount; ++permutationId) {
                auto& ds = *dataSetsHolder.PermutationDataSets[permutationId];
                //link common datasets
                if (permutationId > 0) {
                    ds.PermutationIndependentFeatures = permutationIndependentCompressedDataSetId;
                }

                {
                    const NCB::TTrainingDataProvider* linkedTest = permutationId == 0 ? LinkedTest : nullptr;
                    const TMirrorBuffer<const ui32>* testIndices = (permutationId == 0 && linkedTest)
                                                                   ? &dataSetsHolder.TestDataSet->GetTarget().GetIndices()
                                                                   : nullptr;

                    TBatchedBinarizedCtrsCalcer ctrsCalcer(FeaturesManager,
                                                           ctrsTarget,
                                                           DataProvider,
                                                           ds.GetIndices(),
                                                           linkedTest,
                                                           testIndices);

                    TCtrsWriter<TFeatureParallelLayout> ctrsWriter(FeaturesManager,
                                                                   compressedIndexBuilder,
                                                                   ctrsCalcer,
                                                                   ds.PermutationDependentFeatures,
                                                                   testDataSetId);
                    ctrsWriter.Write(permutationDependent);
                }
                CATBOOST_INFO_LOG << "Ctr computation for permutation #" << permutationId << " is finished" << Endl;
            }
        }
        compressedIndexBuilder.Finish();

        return dataSetsHolder;
    }

    void TFeatureParallelDataSetHoldersBuilder::BuildTestTargetAndIndices(TFeatureParallelDataSetsHolder& dataSetsHolder,
                                                                          const TCtrTargets<NCudaLib::TMirrorMapping>& ctrsTarget)  {
        const auto testMapping = NCudaLib::TMirrorMapping(ctrsTarget.TestSlice.Size());

        TMirrorBuffer<ui32> indices;
        indices.Reset(testMapping);
        MakeSequence(indices);
        TMirrorBuffer<ui32> inverseIndices = indices.CopyView();

        auto targets = TMirrorBuffer<float>::CopyMapping(indices);
        targets.Write(GetTarget(LinkedTest->TargetData));
        auto weights = TMirrorBuffer<float>::CopyMapping(indices);
        weights.Write(GetWeights(LinkedTest->TargetData));

        dataSetsHolder.TestDataSet.Reset(new TFeatureParallelDataSet(*LinkedTest,
                                                                     dataSetsHolder.CompressedIndex,
                                                                     new TPermutationScope(),
                                                                     new TPermutationScope(),
                                                                     *dataSetsHolder.TestCatFeaturesDataSet,
                                                                     dataSetsHolder.GetCtrTargets(),
                                                                     TTarget<NCudaLib::TMirrorMapping>(std::move(targets),
                                                                                                       std::move(weights),
                                                                                                       std::move(indices)),
                                                                     std::move(inverseIndices),
                                                                     GetPermutation(*LinkedTest, 0u, 1u))

        );

        dataSetsHolder.TestDataSet->LinkedHistoryForCtrs = dataSetsHolder.PermutationDataSets[0].Get();
    }

    void TFeatureParallelDataSetHoldersBuilder::BuildCompressedCatFeatures(const NCB::TTrainingDataProvider& dataProvider,
                                                                           TCompressedCatFeatureDataSet& dataset) {
        TCompressedCatFeatureDataSetBuilder builder(dataProvider,
                                                    FeaturesManager,
                                                    dataset);
        for (ui32 catFeature : FeaturesManager.GetCatFeatureIds()) {
            if (FeaturesManager.UseForTreeCtr(catFeature)) {
                builder.Add(catFeature);
            }
        }
        builder.Finish();
    }
}
