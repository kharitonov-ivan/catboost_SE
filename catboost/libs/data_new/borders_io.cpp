#include "borders_io.h"

#include <catboost/libs/helpers/exception.h>
#include <catboost/libs/logging/logging.h>

#include <util/generic/cast.h>
#include <util/generic/hash.h>
#include <util/generic/mapfindptr.h>
#include <util/generic/vector.h>
#include <util/stream/file.h>
#include <util/string/split.h>
#include <util/system/fs.h>


#include <catboost/libs/options/enums.h>
#include <catboost/libs/helpers/data_split.h>
#include <catboost/libs/logging/logging.h>

#include <util/generic/map.h>
#include <util/generic/string.h>




namespace NCB {
    void LoadBordersAndNanModesFromFromFileInMatrixnetFormat(
        const TString& path,
        TQuantizedFeaturesInfo* quantizedFeaturesInfo)
    {
        CB_ENSURE(NFs::Exists(path), "Borders file at [" << path << "] was not found");

        const auto featuresLayout = *quantizedFeaturesInfo->GetFeaturesLayout();

        THashMap<TFloatFeatureIdx, TVector<float>> borders;
        THashMap<TFloatFeatureIdx, ENanMode> nanModes;

        TIFStream in(path);
        TString line;
        for (size_t lineNumber = 0; in.ReadLine(line); lineNumber++) {
            try {
                TVector<TString> tokens;
                Split(line, "\t", tokens);
                CB_ENSURE(
                    tokens.ysize() == 2 || tokens.ysize() == 3,
                    "Each line should have two or three columns");

                const ui32 flatFeatureIdx = FromString<ui32>(tokens[0]);
                CB_ENSURE(
                    featuresLayout.IsCorrectExternalFeatureIdxAndType(flatFeatureIdx, EFeatureType::Float),
                    "Feature #" << flatFeatureIdx << " is not float");
                const auto floatFeatureIdx = featuresLayout.GetInternalFeatureIdx<EFeatureType::Float>(
                    flatFeatureIdx);

                const float featureBorder = FromString<float>(tokens[1]);
                borders[floatFeatureIdx].push_back(featureBorder);

                if (tokens.ysize() == 3) {
                    ENanMode nanMode = FromString<ENanMode>(tokens[2]);

                    if (nanModes.contains(floatFeatureIdx)) {
                        CB_ENSURE(
                            nanModes.at(floatFeatureIdx) == nanMode,
                            "NaN mode should be consistent in borders file");
                    } else {
                        nanModes[floatFeatureIdx] = nanMode;
                    }
                }
            } catch (const yexception& e) {
                throw TCatboostException() << "Incorrect file with borders. Error while parsing line #"
                    << lineNumber << ": " << e.what();
            }
        }

        for (auto& [floatFeatureIdx, singleFeatureBorders] : borders) {
            SortUnique(singleFeatureBorders);
            quantizedFeaturesInfo->SetBorders(floatFeatureIdx, std::move(singleFeatureBorders));

            auto* nanMode = MapFindPtr(nanModes, floatFeatureIdx);
            quantizedFeaturesInfo->SetNanMode(floatFeatureIdx, nanMode ? *nanMode : ENanMode::Forbidden);
        }
    }

    void SaveBordersAndNanModesToFileInMatrixnetFormat(
        const TString& file,
        const TQuantizedFeaturesInfo& quantizedFeaturesInfo)
    {
        const auto& featuresLayout = *quantizedFeaturesInfo.GetFeaturesLayout();

        TOFStream out(file);

        featuresLayout.IterateOverAvailableFeatures<EFeatureType::Float>(
            [&] (TFloatFeatureIdx floatFeatureIdx) {
                const ui32 flatFeatureIdx = featuresLayout.GetExternalFeatureIdx(
                    *floatFeatureIdx,
                    EFeatureType::Float);

                auto nanMode = quantizedFeaturesInfo.GetNanMode(floatFeatureIdx);

                for (const auto& border : quantizedFeaturesInfo.GetBorders(floatFeatureIdx)) {
                    out << flatFeatureIdx << "\t" << ToString<double>(border);
                    if (nanMode != ENanMode::Forbidden) {
                        out << "\t" << nanMode;
                    }
                    out << Endl;
                }
            }
        );
    }

}
