#pragma once

#include "column_printer.h"
#include "pool_printer.h"

#include <catboost/libs/data_new/data_provider.h>
#include <catboost/libs/data_util/line_data_reader.h>
#include <catboost/libs/data_util/path_with_scheme.h>
#include <catboost/libs/labels/external_label_helper.h>

#include <util/generic/fwd.h>
#include <util/generic/maybe.h>
#include <util/generic/ptr.h>
#include <util/generic/string.h>
#include <util/generic/vector.h>
#include <util/stream/output.h>
#include <util/system/types.h>

#include <utility>


namespace NCB {

    class TEvalResult {
    public:
        TEvalResult() {
            RawValues.resize(1);
        }

        TVector<TVector<TVector<double>>>& GetRawValuesRef();
        const TVector<TVector<TVector<double>>>& GetRawValuesConstRef() const;
        void ClearRawValues();

        /// *Move* data from `rawValues` to `RawValues[0]`
        void SetRawValuesByMove(TVector<TVector<double>>& rawValues);

    private:
        TVector<TVector<TVector<double>>> RawValues; // [evalIter][dim][docIdx]
    };

    void ValidateColumnOutput(
        const TVector<TString>& outputColumns,
        const TDataProvider& pool,
        bool isPartOfFullTestSet=false,
        bool CV_mode=false);

    TIntrusivePtr<IPoolColumnsPrinter> CreatePoolColumnPrinter(
        const TPathWithScheme& testSetPath,
        const TDsvFormatOptions& testSetFormat,
        const TMaybe<TDataColumnsMetaInfo>& columnsMetaInfo = {}
    );

    void OutputEvalResultToFile(
        const TEvalResult& evalResult,
        NPar::TLocalExecutor* executor,
        const TVector<TString>& outputColumns,
        const TExternalLabelsHelper& visibleLabelsHelper,
        const TDataProvider& pool,
        bool isPartOfTestSet, // pool is a part of test set, can't output testSetPath columns
        IOutputStream* outputStream,
        TIntrusivePtr<IPoolColumnsPrinter> poolColumnsPrinter,
        std::pair<int, int> testFileWhichOf,
        bool writeHeader = true,
        ui64 docIdOffset = 0,
        TMaybe<std::pair<size_t, size_t>> evalParameters = TMaybe<std::pair<size_t, size_t>>());

    void OutputEvalResultToFile(
        const TEvalResult& evalResult,
        int threadCount,
        const TVector<TString>& outputColumns,
        const TExternalLabelsHelper& visibleLabelsHelper,
        const TDataProvider& pool,
        bool isPartOfTestSet, // pool is a part of test set, can't output testSetPath columns
        IOutputStream* outputStream,
        const NCB::TPathWithScheme& testSetPath,
        std::pair<int, int> testFileWhichOf,
        const NCB::TDsvFormatOptions& testSetFormat,
        bool writeHeader = true,
        ui64 docIdOffset = 0);

} // namespace NCB
