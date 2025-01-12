#pragma once

#include "train_template.h"
#include <catboost/cuda/methods/doc_parallel_boosting.h>
#include <catboost/cuda/methods/pairwise_oblivious_trees/pairwise_oblivious_tree.h>

namespace NCatboostCuda {
    template <template <class TMapping> class TTargetTemplate>
    THolder<TAdditiveModel<TObliviousTreeModel>> TrainPairwise(TBinarizedFeaturesManager& featureManager,
                                                                const NCatboostOptions::TCatBoostOptions& catBoostOptions,
                                                                const NCatboostOptions::TOutputFilesOptions& outputOptions,
                                                                const NCB::TTrainingDataProvider& learn,
                                                                const NCB::TTrainingDataProvider* test,
                                                                TGpuAwareRandom& random,
                                                                ui32 approxDimension,
                                                                const TMaybe<TOnEndIterationCallback>& onEndIterationCallback,
                                                                TVector<TVector<double>>* testMultiApprox, // [dim][objectIdx]
                                                                TMetricsAndTimeLeftHistory* metricsAndTimeHistory) {
        CB_ENSURE(catBoostOptions.BoostingOptions->DataPartitionType == EDataPartitionType::DocParallel,
                    "NonDiag learning works with doc-parallel learning");
        CB_ENSURE(catBoostOptions.BoostingOptions->BoostingType == EBoostingType::Plain,
                    "Boosting scheme should be plain for nonDiag targets");

        using TDocParallelBoosting = TBoosting<TTargetTemplate, TPairwiseObliviousTree>;
        return Train<TDocParallelBoosting>(featureManager,
                                            catBoostOptions,
                                            outputOptions,
                                            learn,
                                            test,
                                            random,
                                            approxDimension,
                                            onEndIterationCallback,
                                            testMultiApprox,
                                            metricsAndTimeHistory);
    };


    template <template <class> class TTargetTemplate>
    class TPairwiseGpuTrainer: public IGpuTrainer {
        virtual THolder<TAdditiveModel<TObliviousTreeModel>> TrainModel(TBinarizedFeaturesManager& featuresManager,
                                                                        const NCatboostOptions::TCatBoostOptions& catBoostOptions,
                                                                        const NCatboostOptions::TOutputFilesOptions& outputOptions,
                                                                        const NCB::TTrainingDataProvider& learn,
                                                                        const NCB::TTrainingDataProvider* test,
                                                                        TGpuAwareRandom& random,
                                                                        ui32 approxDimension,
                                                                        const TMaybe<TOnEndIterationCallback>& onEndIterationCallback,
                                                                        TVector<TVector<double>>* testMultiApprox, // [dim][objectIdx]
                                                                        TMetricsAndTimeLeftHistory* metricsAndTimeHistory) const {
            return TrainPairwise<TTargetTemplate>(featuresManager,
                                                    catBoostOptions,
                                                    outputOptions,
                                                    learn,
                                                    test,
                                                    random,
                                                    approxDimension,
                                                    onEndIterationCallback,
                                                    testMultiApprox,
                                                    metricsAndTimeHistory);
        };
    };
}
