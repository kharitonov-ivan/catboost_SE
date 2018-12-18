###  Model data
class catboost_model(object):
    float_features_index = [
        0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 31, 32, 33, 34, 35, 36, 37, 38, 39, 46, 47, 48, 49,
    ]
    float_feature_count = 50
    cat_feature_count = 0
    binary_feature_count = 39
    tree_count = 40
    float_feature_borders = [
        [0.00092654896, 0.022489902, 0.105616, 0.19453999, 0.33330449, 0.71445751],
        [0.0013257549, 0.0071699149, 0.0114448, 0.01517855, 0.016585499, 0.039583351, 0.053003252, 0.0622565, 0.068122499, 0.096787147, 0.098820299, 0.1254825, 0.130032, 0.138787, 0.20436451, 0.2343325],
        [0.02119715, 0.20238599, 0.52136999, 0.90201151, 0.903754, 0.93767154, 0.93831098],
        [0.5],
        [0.5],
        [0.5],
        [0.5],
        [0.5],
        [0.5],
        [0.5],
        [0.5],
        [0.5],
        [0.33529401, 0.55098051, 0.66078448],
        [0.32183897, 0.57890052, 0.83402205, 0.913037, 0.98012],
        [0.01041666, 0.075502649, 0.152098, 0.2284745, 0.250328, 0.39003402],
        [0.070455149, 0.070463002, 0.077536345, 0.122849, 0.13628601, 0.237433, 0.29751498, 0.29760849, 0.34176701, 0.35739702, 0.37005252, 0.40465051],
        [0.5],
        [0.5],
        [0.26470602, 0.3313725, 0.46078449, 0.47254902, 0.5, 0.51960802, 0.5862745, 0.629412, 0.67254901],
        [0.5],
        [0.5],
        [0.16666651, 0.27777749, 0.41666651, 0.58333349, 0.83333349],
        [0.022544799, 0.022629999, 0.17426199, 0.223333, 0.22895449, 0.93935096, 0.95256799, 0.977382],
        [0.5],
        [0.5],
        [0.5],
        [0.061012201, 0.1110935, 0.134183, 0.17011049, 0.245272, 0.36303151, 0.4535355, 0.53050601, 0.65397501, 0.80409098],
        [0.5],
        [0.25707501, 0.56904697, 0.60275245, 0.60982096, 0.92974299, 0.94102502],
        [0.5],
        [-0.1450465, -0.060957454, 0.245041, 0.25577599, 0.498234, 0.6135205, 0.7837165, 0.91910648],
        [0.5],
        [0.00075808598, 0.0021057948, 0.0036219701, 0.035124701, 0.1600275],
        [0.72683001, 0.784554],
        [2.3705601e-05, 0.00038780703, 0.00040105497, 0.00071648997, 0.00074743002, 0.00185755, 0.0066647353, 0.0127325],
        [0.192167, 0.312599, 0.33873349, 0.34025601, 0.50021201, 0.65224147],
        [0.39747551, 0.41530049, 0.58605748, 0.62173098, 0.69472051, 0.71177602, 0.73340154, 0.75300753, 0.76223701, 0.77230752, 0.96042001, 0.98502851, 0.98554349],
        [0.01705455, 0.089835256, 0.1459935, 0.157988, 0.25077748, 0.26409501, 0.31733251, 0.3445805, 0.34512851, 0.3670935, 0.46864849, 0.79704249],
        [0.5],
    ]
    tree_depth = [6, 6, 3, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 3, 5, 4, 5, 6, 6, 6, 6, 6, 6]
    tree_split_border = [3, 3, 1, 1, 5, 1, 1, 1, 1, 1, 13, 1, 4, 1, 1, 6, 1, 1, 1, 1, 9, 6, 2, 1, 3, 3, 1, 2, 8, 1, 2, 5, 1, 14, 1, 3, 6, 3, 4, 1, 6, 7, 1, 1, 1, 3, 6, 1, 1, 1, 5, 8, 12, 1, 3, 10, 2, 2, 10, 8, 11, 1, 1, 1, 1, 1, 10, 1, 1, 4, 3, 1, 1, 4, 9, 2, 1, 11, 5, 3, 4, 1, 1, 1, 1, 7, 12, 5, 1, 1, 8, 13, 9, 3, 1, 2, 5, 2, 1, 7, 5, 9, 1, 1, 1, 5, 2, 9, 3, 2, 1, 1, 11, 3, 8, 1, 6, 3, 1, 4, 1, 1, 7, 2, 4, 1, 3, 4, 4, 12, 7, 1, 3, 1, 7, 1, 4, 1, 4, 1, 1, 4, 1, 5, 5, 1, 8, 1, 1, 1, 7, 2, 2, 3, 4, 10, 1, 2, 2, 1, 8, 1, 5, 6, 1, 2, 2, 4, 7, 7, 1, 5, 1, 1, 1, 1, 1, 10, 6, 7, 6, 1, 1, 1, 11, 1, 1, 1, 1, 1, 1, 6, 6, 5, 1, 1, 4, 1, 5, 5, 4, 12, 5, 5, 1, 6, 1, 16, 2, 9, 8, 1, 1, 15, 2, 6, 1, 8, 1, 3, 1, 1, 1, 6, 4, 1, 8]
    tree_split_feature_index = [2, 26, 1, 34, 37, 29, 27, 16, 3, 38, 1, 11, 36, 20, 29, 34, 31, 8, 38, 25, 36, 26, 2, 30, 37, 22, 10, 12, 1, 3, 26, 1, 23, 1, 23, 28, 0, 13, 28, 9, 22, 18, 23, 27, 31, 36, 30, 16, 3, 33, 36, 26, 15, 32, 21, 15, 30, 0, 1, 18, 1, 31, 11, 4, 21, 8, 26, 26, 27, 34, 18, 29, 17, 0, 37, 37, 19, 36, 26, 30, 1, 27, 38, 9, 5, 36, 36, 13, 38, 9, 34, 36, 15, 0, 22, 36, 2, 18, 3, 37, 28, 18, 7, 20, 26, 21, 28, 26, 14, 32, 35, 23, 15, 34, 1, 10, 36, 15, 20, 18, 6, 9, 2, 15, 35, 3, 12, 30, 14, 1, 22, 20, 1, 10, 30, 12, 13, 8, 26, 38, 15, 21, 3, 22, 18, 29, 37, 13, 18, 23, 15, 34, 22, 32, 32, 37, 9, 14, 13, 0, 15, 11, 14, 15, 14, 35, 1, 22, 26, 1, 9, 32, 31, 3, 24, 23, 27, 36, 14, 34, 28, 31, 31, 2, 37, 19, 27, 3, 31, 20, 24, 2, 35, 15, 10, 3, 37, 36, 34, 30, 2, 37, 35, 0, 37, 18, 10, 1, 21, 1, 36, 29, 10, 1, 33, 1, 5, 30, 8, 35, 20, 38, 9, 37, 15, 28, 22]
    tree_split_xor_mask = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cat_features_index = []
    one_hot_cat_feature_index = []
    one_hot_hash_values = [
    ]
    ctr_feature_borders = [
    ]

    ## Aggregated array of leaf values for trees. Each tree is represented by a separate line:
    leaf_values = [
        0.0005996913577188494, 0, 0, 0, 0, 0, 0, 0, 0.000221052627579162, 0, 0, 0, 0.0009768016478353648, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.001960402433831547, 0, 0, 0, 0.0004199999924004077, 0, 0, 0, 0, 0, 0, 0, 0.0006999999873340129, 0, 0, 0, 0.001368055558297782, 0.0001866665999591365, 0, 0.001679999969601631, 0.001604166730772702, 0.001049999981001019, 0.001499999972858599, 0.003954763324079735, 0, 0, 0, 0, 0, 0, 0.001049999981001019, 0, 0.001779299344200712, 0.001465909057127481, 0.002944927643757796, 0.003975728267858036,
        0.0008915419558863947, 0, 0.0003512460733605982, 0, 0.0004428744834216426, 0.0005497278883047848, 0.0007437548665033633, 0, 0, 0, 0, 0, 0.001210233305897622, 0.003847465523299554, 0.001161668204743658, 0.002286348013900796, 0, 0, 0, 0, 0.001845609629668785, 0.00280269449486017, 0.001692741537757669, 0, 0, 0, 0, 0, 0.002007853056220058, 0.003279802623184852, 0.002235919726910874, 0.003849602074058009, -1.028042304539491e-05, 0, -4.497685082360273e-06, 0, 0.001735347943945, 0, -1.657894669786881e-06, 0, 0, 0, 0, 0, 0.002337718806557816, 0.001027913024166518, 0.0008234633792182209, 0, 0, 0, 0, 0, 0, 0, 0.0008223767607047237, 0, 0, 0, 0, 0, 0.002439206489894105, 0.001638476035060068, 0.003277561698191198, 0,
        0.001115175391429931, 0, 0.001344163744511274, 0, 0.0006886572331234234, 0.002010658585504059, 0.00176180956006071, 0.003364531120166381,
        0.0007001043874697266, 0.001565358125621322, 0.000790318731645663, 0.001261642829027043, 0, 0, 0, 0, 0.0007282047889366907, 0.001739968144354273, 0.0009170350894746803, 0.002059767340194571, 0, 0, -2.648398964486864e-05, 0.0004833827767271159, 0, 0, 0, 0, 0, 0, 0, 0, 0.0006376374515972743, 0.001368010970518884, 0.002882356782477335, 0.001753595456400311, 0, 0.0001061981777880467, 0.001017813481797178, 0.001008382767227625, 0, 0, -4.902085946679998e-05, 0.003603009688849495, 0, 0, 0, 0, 0, 0, 0.00324350546113319, 0.00330696753612189, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0009738230505495285, 0.003867212537495351, 0, 0, 0.0009950183889524376, 0,
        0, 0, 0, 0, 0.0009926099080845279, 0, -4.788464153762725e-05, 0, 0, 0, 0, 0, 0.001120846692614249, 0, 0.001521842871073689, 0, -6.851005466688717e-05, 0, 0, 0, 0.0007515473270327074, 0, 0.002008695824013786, 0, 0.001245695609171827, -9.034917708324798e-05, 0.002040613344653574, 0.00267230676344944, 0.001544469265806889, 0.001106556513958779, 0.002204748351127536, 0.004303490962327717, 0, 0, 0, 0, 0.0010180544555612, 0, 0, 0, 0, 0, 0, 0, 0.001016044261479889, 0, 0.0009578572108665229, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0009357312634785961, 0, 0.0005573392686172548, 0,
        0.0003681399348688985, 0.0009213955570035212, 0, 0, 0.0001903923840453577, 0.0009975813657912269, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.000685280329140634, 0.0003431211548483469, 0, 0, 0, 0, 0, 0, 0.002798671392999942, 0.001531627284268913, 0, 0, 0, 0, 0, 0, 0.00128610915712453, 0.001034103824197486, 0.00197278953928373, 0.001181309391884795, 0, 0, 0, 0, 0.002997754571378857, 0.002409575270006088, 0.002935374663320512, 0.003260514706815098,
        0.000883969181616782, 0, 0.0009800435949594379, 0.001812100453728323, 0, 0, 0, -0.0001587442102491358, 0.0006288189431500763, 0, 0.003571199162326904, 0.002764134041068148, 0, 0, 0, 0.0008870539333355012, 0.0001993910982700259, 0, 0.001323663621019298, 0.003044736339820406, 0, 0, 0, 0, -3.358950893995706e-05, 0, 0.00187461610803578, 0.001435796338177524, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0008436848558935606, 0.002688603088733836, 0, 0, 0, 0, 0, 0, 0.001462682973306029, 0.001435796338177524, 0, 0, 0, 0, 0, 0, 0.002205512948051461, -0.0001924954577187771, 0, 0, 0, 0, 0, 0, 0.0008803579114080992, 0.001419228966641085,
        0.0005318901391266999, -3.82173170468491e-05, 0, 0, -7.919175396907944e-05, -4.236673412011207e-05, 0, 0, 0.001259703191061918, 0.0006779079498708105, 0.0005524232618989082, 0, 0.0009958630603536709, 0.0004956085153705448, 0.0003883496090855102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0006365842168027292, 0.0003111063205110507, 0.0008259677167975821, 0, -4.636970787917017e-05, 0, -4.123537236883085e-05, 0, 0.001761452580321467, 0.0002407736396457147, 0.001595124023568703, 0, 0.0005031566932951927, 0.0007224177453379825, 0.001304965335324801, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.001598022486642396, 0, 0.003337933971175408, 0, 0.0003863851792443703, 0, 0.002609648185136009, 0,
        0.000531461999171976, 0, 0.0007979165454358117, 0, 0.0002488577315936277, 0, -6.460045686667672e-05, 0, 0.001191060687356299, 0.002629602440528619, 0.001422292739762325, 0.001253091921761506, 0.001259281922148388, 0.0004860222802947284, 0.001529178634113907, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0003498423340500816, 0.001271474417728284, 0.0006295810890384946, 0.001350547158955745, 0.0003976087211085566, 0, 0.0008730735394662914, -0.0001554167002954416, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.002479031969721231, 0, 0.003719691565838987, 0, 0.003325923459085354, 0, -0.0001086574644508986, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.003110811353583324, 0, 0.002136654894501596, 0, 0.00218195254479005, 0, 0,
        0, 0, 0, 0, 0.001777392451367983, 0.00219212246125666, 0, 0, 0, 0, 0, 0, 0.001394595563148512, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.001171028145930034, 0, 0, 0, 0.001805827601823571, 0.00405945657418201, 0, 0, 0.0008060341004233186, 0, 0, 0, 0.002004369049040504, 0.003209748546128202, 0, 0, 0.0005489319255887005, 0, -0.0002072354024236573, 0, -9.414589808057395e-05, 0, -4.382396780500043e-05, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0.0001018120462154894, 0.0006990509255585921, 0, 0.0009587500922109485, -8.969060100616636e-05, 0.0007092320313304033, 0, 0, 0, 0, 0.001322666143555734, 0.001537522555499616, 0, 0, 0.002246687123812084, 0.0001582736573611846, 0, 0.001377767259198816, 0, 0.00065931312195204, 0, 0.0009467257380284019, 0, 0.0005363731641564384, 0, 0, 0, 0.002286903376574838, 0, 0, 0, 0.0007557151173505838,
        0.0004959504635120924, 0.0003743296344756362, 0.001108209923890898, 0.002480224137791672, 0.0001062990496756386, -0.0001251991127429854, 0.000764811871993753, 0, 0, 0, 0.0006413179227410805, 0, 0, 0, 0.0009610765143855152, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.002426230737592248, 0, 0.002472346133156958, 0.001453447499621435, 0.001533391218854882, 0, 0.002611576558272303, 0.0005717082920784483, 0, 0, 0.000861188043204663, 0, 0, 0, 0, 0, 0, 0, 0.002114977908801552, 0, 0, 0, 0.001764015074872636, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0.0004372933093939062, 0, 0.00145450203830376, 0, 0.0001756319537947484, 0, 0.0009583519153359258, 0, 0.001410684190869881, 0.001230121830107576, 0.001705280221449592, 0.002811567106970031, 0.0002129610981744471, 0.003438497921285487, 0.0006162022204262424, 0.002522767921063808,
        0.0003506579497331724, -0.0002168755248847155, 0, 8.573827502841444e-05, 0, 0, 0, 0, 0.000938581504521116, 0.0005296778935138733, 0.001066138841191965, 0.0006120324405417703, 0.001347396774760239, 0.00118185562288629, 0.001846610682191694, 0.00231925131101607, 0.000629213927176124, -0.0001234768067197158, 0.0006611188983654901, 0.0002911761153846639, 0, 0, 0, 0, 0.0003721029484091946, 0, 0.000845841356243302, 0.0005947935829472411, 0.001412013618809272, 0.0004295286089074638, 0.001277133055128042, 0.002359699948382647, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.001420713373456629, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.001763482997561104, 0.003644130612308877,
        0.0001779501172478757, 0, 0.0003886431314236458, 0, 0.001016429193234574, 0, 0.001256499225767723, 0, 0.0003148338112217238, -0.000223574906443404, -0.0001825088608413159, 0, 0, -0.0003655530873919145, 0.0001973232527747041, 0.002494391992654917, 0.0003535582342381542, 0, 0.000576185795352587, 0, 0.001173119346968611, 0, 0.001543124067250544, 0, 0.001261303251976811, 0.0001901480516652801, 0.001817796648762282, 0.005265647675201306, 0.002116985211012866, 0.002584965535344852, 0.00210966292143372, 0.002838815047152443, -0.0002636371882226714, 0, 0.0001521137467107627, 0, 0.001124070150495063, 0, -0.0001060195377272934, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0009454272623078491, 0, 0.0002216394266388237, 0, 0.0003745607733778193, 0, 0.0003885143248962982, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0.0005560554124002692, 0, 0.00212265950616846, 0, 0, 0, 0, 0, -0.0001075557941516086, 0, 0, 0, 0, 0, 0, 0, 0.001107353474671096, 0.001317459161793323, 0.001950716411568663, 0.00278164438537992, 0, 0, 0.003722245020945641, 0.001895593980872395, 0.0003297402281062402, 0.0004618882692612322, 0.0008100773229281519, 0.0007830987041961848, 0, 0, 0, 0, 0.0002123917436942488, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0005622470544148319, -0.0001492395090808873, 0.001197158222740338, 0.0001717994230122837, 0, 0, 0, 0, -0.0001051686337785569, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, -6.093464782020011e-05, 0, 0, 0, 0.003583998432917425, 0.0006945651018272995, 0, 0, 0.0003358541390948894, 0, 0, 0, 0.0002753906648922765, 0.001949273808381531, 0, 0, -7.848585538993691e-05, 0.0007687847576183056, 0, 0, 0.0008035367131658735, 0.001538522810487071, 0, 0, 0.0002709831848583995, 0.002182515845079924, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.002186064618058493, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.001624705173472713, 0.002009555582916558, 0.003431564474494742, 0.001586795577110294, 0, 0, 0, 0,
        3.234963936831048e-05, 0, 0.0007611093755034918, 0, 0.0007934927309911625, -0.0001752498366606419, 0.0003031355394777104, 0, 0, 0, 0, 0, 0.0016423547466107, 0.00222546319881775, 0.001215446869379598, 0.006051938098050287, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8.936464345441203e-05, 0, -0.0003337732271455833, 0, 0, 0, -0.0001548984740786621, 0, 0, 0, 0.0004909729983651922, 0.0007918164546133076, 0, 0, 0, 0, 0, 0, 0.0005694069696065264, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0.0005488784968638945, -0.0001815291505389873, 0.0008862698359071583, 0.0009579187306105818, -0.0001425649835173674, -8.989045844683459e-05, 0.002099021215214123, 0.002472742889596524, 0, 0, 0.0007939021542560606, 0.0005101277548400449, -9.863200906856767e-06, 0.0002033215947086935, 0.001014627750663734, 0.002362430853160798, 0, -0.0001968360777367012, 0.001143322333726168, 0.001555797924375037, 0.0006057128185406116, 0.0001069822227084331, 0.001128254251262634, 0.001476093837323307, 0, 0, 0, 0, 0, 0, -0.0002793907248673093, 0, 0, 0, 0, 0, 0.004136864307419476, 0, 0.002634373992259184, 0.001248750143102836, 0, 0, 0, 0, 0, 0.0006504968936468144, 0.003009317968546972, 0.002008462726707915, 0, 0, 0, 0, -0.0004596204814452665, 0, 0, 0.001870092162544904, 0, 0, 0, 0, 0, 0.0001976340913752286, 0, 0.0006571504933936842,
        0.0006211067652594002, 0, 0.0002077781083346736, 0, 0, 0, 0, 0, 0.000232559848057202, -0.0003060491438610802, 0.001083455831365045, 0, 0.0002115520326285771, 0.000334620015302241, -0.0004114381695139204, 0, -0.0001811066806793216, 0, -0.00012546011765494, 0, 0, 0, 0, 0, -0.0002517783085692576, 0.0009356281994604072, 0, 0, 0, -0.0002296162631860002, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.001106046423204371, -0.0003661898508262893, 0.001133258835244265, -0.0001363278076224819, 0.0005661814838379564, 0.001286325919924356, 0.002098088446645207, 0.002299689894557664, 0, 0, 0, 0, 0, 0, 0, 0, -0.0001630818651168435, 0.0001191185941590054, 0, 0, -0.0003295871814312832, 0.001016598864001773, 0, 0,
        -0.000269320065796034, -0.0004792174219017899, 0, 0, 0, 0.000870304059336601, 0, 0, 0.0004375660220770932, 0.0006799759101603749, 0.000890567484457693, 0, 0.002342552516938329, -0.0004316505207410675, 0, 0, 0.001204873518650545, -0.0006541237942818111, 0, 0, -0.0004176059863812788, 0.001491311233249385, 0, 0, 0.0005364090072825868, 0.001542402437108869, 0.0006062763135137364, 0.0009602589991793951, 0.001944748208475747, 0.002463093423903797, 0, 0.001132053444731997, -0.0002260229203110145, -0.0004894499963636196, 0, 0, 0, 0, 0, 0, -7.280275581426447e-05, 0.0005132170938532856, 0, -0.0001731419501800435, 0, 0, 0, 0, -1.9086919728349e-05, -0.0004859908650684485, 0, 0, 0.000634418044572124, 0.0006143408328538429, 0, 0, 0.0003587747024198594, 0.0007459137082808815, 0, -2.853279761524419e-05, 0.002751362387767803, 0.00141885059383878, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0.0003531097500469749, 0, 6.456246549950682e-05, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -0.0003450496828505628, 0.0003421756621835829, -0.0001346372440409684, -0.0002998432165018889, 0, 0, 0, 0, 0.000349274153982381, 0.001893658253304531, 0.0004568500398632514, 3.026557414097765e-05, 0, 0.0003167521012948148, 0, 0, -5.111400832757081e-05, 6.314178403407862e-05, 0, -0.0001486247668700232, 0, 0, 0, 0, 0.001383502340750862, 0.001351415252361741, 0.0003031289329710041, 0.0002072668213697418, 0.002916052755187511, 0.003677418471894497, 0, 0,
        0.0001084697883069082, -0.0002376444316321586, -0.0003257952822511372, 0.0007792567290212076, 8.295617019649783e-05, 0.0001567115573522986, 0.001827007504352988, 0, -0.0001535487524767764, -0.0001935858332822322, 6.216680215229146e-06, -0.0001775351843479854, 0.0002111500565533458, 0.002870195384119947, 0.002318849144077889, 0, -0.0001387641276002234, 0, 0.001943827900241193, 0, 0, 0, 0, 0, 0.0001164385347913935, 0, 9.933390778112293e-05, 0, 0, 0, 0, 0, 0.0004745591356455093, 0.0001712269211927701, 0.0009015101340591556, 0.0004079916287358698, 0.000553936911705296, 0.0006260629316611142, 0.0007549028199517325, 0.0002359512549857445, 0.00107351806250922, 0.0006635636830426201, 0.001382819467416637, 0.0003173006217426744, 0.001571121482087855, 0.001160251797227886, 0.001915009806113323, 0.0001527084781621977, 0.001736879832777978, 0, 0.001862952900243785, 0.001845079049665954, 0, 0, 0.002868454246258689, 0, 0.001682147825166652, 0, 0.001317691203719382, 0, 0.001630852534431467, 0, 0.002782654296760058, 0,
        -4.581218739712377e-05, 0.0008130960267393499, 0, 0, -0.000368204596216374, 0.0005524698258039517, 0, 0, 0.000356910317399019, 0.001096387575933837, 0.001431357747919484, 0.0006579958277883903, 0.0006790496571061049, 0.001012921335647288, 0, -8.797130807880086e-05, -0.0004183810681848082, 0.00100599959089259, 0, 0, -0.0001117161369349767, -0.000216978854592081, 0, 0, -0.0002604565356227542, 0.0007923275132743585, 0, 0.0008673990345144128, 0.0001560840247806933, 0.001908169895969148, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.000109824676279608, 0, 0, 0, 0.0008371327478318773, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0008750842987643943, 0.0004817888590140442, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0.0003437167423071686, 0, 0, 0, 0, 0, 0, 0, 0.0004126408261913018, 0, 0, 0, 0, 0, -0.0001984393064582875, 0, 0.0005377224239931148, 0, 0.0007675776378099409, 0.0009157689310978047, 0, 0, 0, 0, -0.0002292357060095686, 0, 0.0008672856913599779, 0.0007081499952897309, 0, 0, 0, 0, 0.0002244988424796241, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6.395641765815101e-05, 0.0004788701782436641, 0.0002969159154066853, 0.0006868414639590962, 0.0009486029606611632, 0.002291233652724736, 0, 0, 0, 0.001525382085285142, 0.0002411736299502209, 0.001164984552766168, 0.001135579179449838, 0.001792007306951761,
        -0.0001891694987313259, 0, -0.0002683207381347735, 0, 0, 0, 0.0003038470986833831, 0, -7.516824345897631e-05, 0, 0, 0, 0, 0, 0, 0, -0.0001492738500612015, 0, 0, 0, 0, 0, 0.0008533879414634704, 0, 0.0007065713188159022, -9.646856777499973e-05, 0, 0, 0, 0, 0, 0, -0.0002051276185142443, 0, 0, 0, 0.0009188756574018637, 0, 0.00135702805358007, 0, 0.0005237715635757343, 0, 0.001256382499102256, 0, 0.001351566988435411, 0, 0.001321165343550881, 0, -0.0002581123362812606, -0.0001567466173220893, 0, 0, 0.00065884805245951, 0.000446678252802154, 0.001186586915555346, 3.718599911098078e-05, 0.0003969720057411912, -8.838812715828218e-05, 0.0008410681121623163, 0.0004202758864021473, 0.001512763045525965, 0.0007809180198392176, 0.001532873514702901, 0.0004338104440455887,
        0.0005884787487221806, -0.0002212271975414216, 0.002546099596236484, 0.0006862821199858507, 0.0002141754305757485, -0.0001863712387931631, 0.0007419590134634663, 0.0003815817011162484, 0, 0, 0, 0, 1.299305024486395e-05, -0.0002502158754023601, 0.0009229380065524113, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7.71908860431621e-05, 0, 0.0001886049854380727, 0, 0, 0, 0.002762130516434542, -0.0004059724351893947, 0.001092619428309505, -0.0001549322702525783, 0.0007840699967983971, 0.001325646374527323, 0, 0, 0, 0, -0.0002355362103493091, 0, 0.002042755465477771, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.003666857054121061, 0, 0.00200266282671599, 0,
        -0.0003879802746744917, 0, 0.0004338742922975212, 0.0001143134181602823, -0.0003420570144658638, 0, 0.0003092595918255519, 0.0005616085700683219, 0.0007269936512853893, -0.00031270322049286, 0.0006432102273380233, 7.155519272516301e-05, 0.0006297942257454345, 0.0005333402326125667, 0.00152710204874104, 0.0001067302892194053, -0.0001756979714100424, 0, 0.0007144623842245382, 0, -0.0002049055867616298, 0, -0.0004392578255357336, 0, -0.0004698368895410398, 0.000369329092761888, 0.000671306214994722, -0.0004877755904455261, 0.000376267363116673, -0.0001123578201422933, 0.000508041644838094, 0.0005283320186031275, 0, 0, 0.0007845358687683867, 0, 0, 0, 0, 0, -0.0003031254949315303, -0.0002187263602762093, 0.0006058510444415579, 0, 0.001400516524564693, 0.0008315280638836104, 0.00235418641312936, 0.0006000302731993454, -0.0001072304492818551, 0, 0, 0, 0, 0, 0, 0, -0.0002065517147853016, 0, -0.0004011007660760121, 0, 0.0005396812228845356, 0, 0.00052580397812645, 0,
        0.0009639080798673603, 0, -0.0001605118585156504, 0, 0.0006458991509455805, 0, -0.0002011224763828924, 0, 0, 0, 0, 0, -0.000161030632340901, 0, -0.000166468755748907, -0.0001575805905027751, -0.0001356203329931457, 0, 0, 0, 0.000401916627542644, -0.0002345935987555198, 0.0006128359800809114, 0.0009619828363947867, 0, 0, 0, 0, 0.0005922404299273387, 0.0007761253105375915, 7.139726377768561e-05, 0.001560646982536332, 0.001319871431847576, 0, -8.139718529330981e-05, 0, 7.02275590878299e-05, 0, -0.0003594503594348131, 0, 0.0003400425760803624, 0, 0, 0, -0.0003758486666676372, 0, -0.0001680341274462953, 0, 0, 0, 0, 0, 0.0009969225621329488, -0.0001694683348203854, 0.0002832652076740348, 0.002415138281681641, 0, 0, 0, 0, 0.0009946908612934091, 0.001455162607658265, 0.0008003080858256859, 0.001491124217245254,
        0.0002217392707308075, 0, 0, 0, -0.000142332118333976, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.000331468624753271, 0, 0, 0, 0.0002491406559818378, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0001250712914341081, 0, 0.000829053383863452, 0, 0.0003329442608061386, 0, 2.190966473966862e-06, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0006833883945071551, 0.003131211590614581, 0.001198966111238945, 0.002176945456254555, -5.679059619954723e-05, 0, 0.0003047457662684977, 0, 0.0001121775953284161, 1.658985488669853e-05, 0, 0.001068271208185246, 0, 0, 0, 0,
        0.0002786310183215105, 0, 0.0005399178467600591, 0.0008717786726038121, 0, 0, 0.001845503858041507, 0.001190959070860392,
        0.0001629843659254365, 0, 0.001770958069941212, 0, 0.0006905792824379723, 0, 0.001491189107255537, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0003791301010432653, 0.001901219662545992, 0.002443545052942862, 0, 0.00117548659575248, 0.002024609247365522, 0.00107833221966036, 0.0007709722291321044, 0, -0.0004041614461737223, 0, 0, 0, 0, 0, -0.000502401174872578,
        0.0004919360206178057, 0.0004017201764296887, 0.0006708508146815293, 0.001320839140448653, 0.0004799190552252512, 0.0009346732627898931, 0.0003132402985085068, 0.001310837328074259, 0.0003792547918446902, 0.0005008689901846606, 0.0002390304609287893, 0.0006477763550871949, 0.0006542989836437067, 0.001110910598042001, 0.0007458997209980715, 0.001295190988684698,
        0.0003296784143947246, 0, 5.050857202275768e-06, 0, 0, 0, -0.0001253511875117662, -0.0001347750753712925, 0.0001211796441871492, 0, 0.0004442338966145014, 0, 0.0003148198216080807, 0, 0.0006543648229674517, 0.001853168386274467, 0, 0, 6.570002146205975e-05, 0, 0, 0, 0.001050405349735835, 0.002071016752926403, 0, 0, 0.000767274929540101, 0, 0, 0, 0.001056107176593677, -0.0001967867919602101,
        0, 0, 0, 0, 0.0002298528046874685, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0006113588663376637, 0, 0, 0, 0.0001876421717706336, 0.0006437171041158953, 0, 0, 0, 0, 0, 0, 0.0008599653428090447, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0005849725981706858, 0.001296303357406744, -0.000137208953758492, 0, 0.0006541805613210502, 0.005069456268053003, 0.001637060901766257, 0, 0.0006335393282019403, 0, 0, 0, 0.0005056010467936474, 0, 0, 0,
        3.708529596339839e-07, 0.0005628246723184112, 0.0005676819522636077, 0.001003201884187646, 0.0001517650784604059, 0.001012462143558467, 0.0006277175999070499, 0.0008238512435983703, 0, -0.0003976066983674363, 0, 0.00454406815700489, 0, 0, -0.0002677164577058427, 0, 0, -0.0004475133605614644, 0, 0.001367932791812788, 0, -0.0005925174555789478, 0, 0.001609065240727499, 0, -0.0005047256906693366, 0, 0.001867523160752832, 0, 0.005977980197808881, 0, 0.0009138153779434364, 0.0002542307208419368, 0, 0.0007915813627905346, 0.0007557846387601526, 0, 0.0007489390871519836, 0.0007537351641950159, 0.0005934012664224481, 0, 0, 0, 0.0006048231587969055, 0, 0, 0, 0, 0, 0, -0.0001750671514442453, 0.0009707800108142566, 0, 0, 0, 8.89040739294321e-05, 0, 0, 0, 0.001073095479571064, 0, 0, 0, 0,
        0.0002628163483774516, 0.0003752472095641065, 0.0004347770249484435, 0.001087143192394916, -0.0002461498327567337, -0.0001267975572449418, 0.0001110667267354545, 0.0002421817522468099, 0, 0, 0.001219524475864166, 0, 0, 0, 0, 0, 0, 0, 0.001139643826995975, 0.001755659127383571, 0, 0, 0.0003816054242452769, -0.0004114475504723119, 0, 0, 0, 0, 0, 0, -0.0004507224930581125, -1.61192057170124e-05, 0.0003795035615165344, -0.0001571202478978378, 0.0005948528498950696, 0.001191243855810523, 0, 0, -0.0001348316458489476, 0.0009997535187543309, 0, 0, 0, 0.0008753589541292928, 0, 0, 0, 0, 0, 0, -0.0001089156955352932, 0.0011174181289731, 0, 0, -0.0002993424825162549, 0.0005981651188475746, 0, 0, 0, 0, 0, 0, 0, 0,
        7.121910077314396e-05, 0.0004212249628879691, 0, 0, 0.0003624765830099314, 0.0006434103713190792, 0.001382207183890511, 0.001356311958812913, 0.0009354772382379164, 0.0007865332019922565, 0, 0, 0, 0.0002035677255564882, 0, 0.0008648546469145309, 0, 0.001475729937856201, 0, 0, 0, 0.0009718310838246426, 0, 0.001635410696448945, 0, 0, 0, 0, 0, 3.367921695665623e-06, 0, 0, 0.0008517928416804843, 7.719540967020116e-05, 0, 0, 0.001515629012823438, 0.0001383553430925797, 0.002234769892086311, 0.001456964017148257, 0, 0, 0, 0, 0, 0, 0, 0, 0, -0.0006936547983337635, 0, 0, 0, -0.0005682494268577804, 0, 0.001052020134772174, 0, 0, 0, 0, 0, -0.0004646075202107057, 0, 0,
        -1.414670752915612e-05, -0.0003051008382638358, 0.0002322350387263611, -0.0001827231118451878, 0.001555972047592276, -0.0004391189961613681, 0, -0.0003863574394619638, 0, 0, 0, 0, 0, 0, 0, 0, 6.873848687882682e-05, 0.0003290209144251239, -0.000339008698855036, -0.0002225327434700225, 0.0008746880671915071, 0.001244584266273848, -0.0003091093284861162, -4.664861932393712e-05, 0, 0, 0, 0, 0, 0, 0, 0, 0.0001496288074757636, 0.000632503454315145, 0.0003920458496809732, 0.0008661704580104964, 4.838263419108773e-05, 7.279022397967403e-05, 0.002603799703665154, 0.0009812190414700995, 0, 0.0002959890790700751, 0.0008062337639435861, 0, 0, 0, 0, 0, -2.496968843709161e-05, 0.0008601629123416811, 0.0002556813057295827, 0.001187033151847673, -0.0005655118261505624, 0.0006876010215383692, -0.0004419537768440884, 0.0010057605074953, 0, -4.04397613948422e-05, 0, 0.000476150596708057, 0, 0, 0, 0,
        0, 7.092218454108536e-05, 0, -0.0003928767312290849, 0, -7.736927409029528e-05, 0, -0.0005627532361562294, 0.0001976272123916138, -2.915806531185791e-06, -5.735731426333909e-05, 0.0002371089332599398, 0.0005656537845900776, 0.001063673041235117, 9.612746061669635e-05, 0.0001231746989599039, 0, 0.001460450961108325, 0, 0, 0, 0.0003162998748430366, 0, -0.000477948386523904, 0, 0.001753611066478137, 0, 0, -0.0005045837298397101, 0.001747458776373694, 0, 2.236364032636108e-05, 0, 0, 0, 0, 0, 0.00164469708131503, 0, 0, 0, -0.000158252435183759, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0004606527828066446, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ]
cat_features_hashes = {
}

def hash_uint64(string):
    return cat_features_hashes.get(str(string), 0x7fFFffFF)


### Applicator for the CatBoost model

def apply_catboost_model(float_features, cat_features=[], ntree_start=0, ntree_end=catboost_model.tree_count):
    """
    Applies the model built by CatBoost.

    Parameters
    ----------

    float_features : list of float features

    cat_features : list of categorical features
        You need to pass float and categorical features separately in the same order they appeared in train dataset.
        For example if you had features f1,f2,f3,f4, where f2 and f4 were considered categorical, you need to pass here float_features=f1,f3, cat_features=f2,f4


    Returns
    -------
    prediction : formula value for the model and the features

    """
    if ntree_end == 0:
        ntree_end = catboost_model.tree_count
    else:
        ntree_end = min(ntree_end, catboost_model.tree_count)

    model = catboost_model

    assert len(float_features) >= model.float_feature_count
    assert len(cat_features) >= model.cat_feature_count

    # Binarise features
    binary_features = [0] * model.binary_feature_count
    binary_feature_index = 0

    for i in range(len(model.float_feature_borders)):
        for border in model.float_feature_borders[i]:
            binary_features[binary_feature_index] += 1 if (float_features[model.float_features_index[i]] > border) else 0
        binary_feature_index += 1
    transposed_hash = [0] * model.cat_feature_count
    for i in range(model.cat_feature_count):
        transposed_hash[i] = hash_uint64(cat_features[i])

    if len(model.one_hot_cat_feature_index) > 0:
        cat_feature_packed_indexes = {}
        for i in range(model.cat_feature_count):
            cat_feature_packed_indexes[model.cat_features_index[i]] = i
        for i in range(len(model.one_hot_cat_feature_index)):
            cat_idx = cat_feature_packed_indexes[model.one_hot_cat_feature_index[i]]
            hash = transposed_hash[cat_idx]
            for border_idx in range(len(model.one_hot_hash_values[i])):
                binary_features[binary_feature_index] |= (1 if hash == model.one_hot_hash_values[i][border_idx] else 0) * (border_idx + 1)
            binary_feature_index += 1

    if hasattr(model, 'model_ctrs') and model.model_ctrs.used_model_ctrs_count > 0:
        ctrs = [0.] * model.model_ctrs.used_model_ctrs_count;
        calc_ctrs(model.model_ctrs, binary_features, transposed_hash, ctrs)
        for i in range(len(model.ctr_feature_borders)):
            for border in model.ctr_feature_borders[i]:
                binary_features[binary_feature_index] += 1 if ctrs[i] > border else 0
            binary_feature_index += 1

    # Extract and sum values from trees
    result = 0.
    tree_splits_index = 0
    current_tree_leaf_values_index = 0
    for tree_id in range(ntree_start, ntree_end):
        current_tree_depth = model.tree_depth[tree_id]
        index = 0
        for depth in range(current_tree_depth):
            border_val = model.tree_split_border[tree_splits_index + depth]
            feature_index = model.tree_split_feature_index[tree_splits_index + depth]
            xor_mask = model.tree_split_xor_mask[tree_splits_index + depth]
            index |= ((binary_features[feature_index] ^ xor_mask) >= border_val) << depth
        result += model.leaf_values[current_tree_leaf_values_index + index]
        tree_splits_index += current_tree_depth
        current_tree_leaf_values_index += (1 << current_tree_depth)
    return result


