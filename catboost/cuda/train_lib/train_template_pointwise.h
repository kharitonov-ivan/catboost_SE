#pragma once

#include "train_template.h"
#include <catboost/cuda/cuda_lib/cuda_base.h>
#include <catboost/cuda/methods/dynamic_boosting.h>
#include <catboost/cuda/methods/feature_parallel_pointwise_oblivious_tree.h>
#include <catboost/cuda/methods/doc_parallel_pointwise_oblivious_tree.h>
#include <catboost/cuda/methods/doc_parallel_boosting.h>

namespace NCatboostCuda {
    template <template <class TMapping> class TTargetTemplate>
    THolder<TAdditiveModel<TObliviousTreeModel>> Train(TBinarizedFeaturesManager& featureManager,
                                                        const NCatboostOptions::TCatBoostOptions& catBoostOptions,
                                                        const NCatboostOptions::TOutputFilesOptions& outputOptions,
                                                        const NCB::TTrainingDataProvider& learn,
                                                        const NCB::TTrainingDataProvider* test,
                                                        TGpuAwareRandom& random,
                                                        ui32 approxDimension,
                                                        const TMaybe<TOnEndIterationCallback>& onEndIterationCallback,
                                                        TVector<TVector<double>>* testMultiApprox, // [dim][objectIdx]
                                                        TMetricsAndTimeLeftHistory* metricsAndTimeHistory) {
        if (catBoostOptions.BoostingOptions->DataPartitionType == EDataPartitionType::FeatureParallel) {
            using TFeatureParallelWeakLearner = TFeatureParallelPointwiseObliviousTree;
            using TBoosting = TDynamicBoosting<TTargetTemplate, TFeatureParallelWeakLearner>;
            return Train<TBoosting>(featureManager,
                                    catBoostOptions,
                                    outputOptions,
                                    learn,
                                    test,
                                    random,
                                    approxDimension,
                                    onEndIterationCallback,
                                    testMultiApprox,
                                    metricsAndTimeHistory);

        } else {
            using TDocParallelBoosting = TBoosting<TTargetTemplate, TDocParallelObliviousTree>;
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
        }
    };


    template <template <class> class TTargetTemplate>
    class TGpuTrainer: public IGpuTrainer {
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
            return Train<TTargetTemplate>(featuresManager,
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
