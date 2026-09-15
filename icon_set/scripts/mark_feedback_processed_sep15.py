#!/usr/bin/env python3
"""Remove processed feedback for 195 verified icons and set their reviewed versions Ready.
Also remove records for seven combinations explicitly discarded by the user.
Run after deploying the updated icons. Newer feedback and review decisions for retained icons are kept.
"""
import argparse
import hashlib
import json
import sqlite3
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
PROCESSED_AT = '2026-09-15T22:55:53.393007+07:00'
# Includes every resolved entry from the 63-icon local feedback audit.
# Seven user-discarded combinations are handled separately below.
# Fixed or visually verified icon IDs; hashes identify the exact reviewed drawings.
CHANGED_ICONS = {
    'solo/canoe': '0db3b6e2ec79e083e4f4a0997b0e0376ea1124688555648f466e14d540e03caf',
    'container/hexagonal-molecular-structure': '6dcf16cea10a97fcc11f6bb7acab5e36d8a76d300f4dc099d4a617d9c4bff4f6',
    'container/fringed-area-rug': '0d830c810ac3f78ec1d172eafb60626ec58bb7eb9a5e33732ec2c4ef35da8b3e',
    'container/clipboard': 'e8b53934e732262ad4e18c7cbb3f644d1a419f69cfe43ee195a1ecc65fb2cf31',
    'solo/anteater': 'c96f679fb822f9374ce29e2ec446596cb966fd6ad73e8c535d051fdb41978d1e',
    'solo/abyssinian-cat-face': '0bdcde6002836c0429824a42c3e2f495c9fdeba54d9d2142617e4a4a38e6aa39',
    'solo/action-camera-on-mount': 'ab34c19fab16a7d31de2d91a69bf13a3d6e260d2610cfa2f567a68e04e9ce535',
    'solo/aiming-rifle-shooter': 'c55b9d2e916698e35487ddf99bf6356fa1023d5c0afaca587b448732ef2699a2',
    'solo/aircraft-releasing-bomb': '90a110319ff266d8d5d4d38c54dc2ee10b20be4f82362cf10555f5365a7d36ce',
    'solo/airmail': '725f1be3fad38ab6b4203c257116c5e86a0a897e7d36923bfeeb4630d35ab111',
    'solo/airplane-departing-runway': 'b6fb2319aa475ca5b23971a803a6086c11e4f1840ad2610b31cd46f2ad67aea8',
    'solo/airplane-diagonal': '18751542dbde01cfb094a1b8c7802813a4663b68b6baae80902e7f2c9b4b69ac',
    'solo/airplane-horizontal': '7f18de3187a26821b07601651e3f8752c822fc967a58c096ce1e6485e04d658e',
    'solo/airplane-with-landing-wheel': '0a6e77e218d6f99058c2492af0a75311f1dec8028b7023f8fe4b4b2ca0a8f598',
    'solo/alarm-bell-with-pull-cord': '4703083a0c15e4247d77fb14cc4a5f5a116f5135fd204dd29b1e6c1413c504bb',
    'solo/alien-head-angular-eyes': '21fb150fda19c519be59df4af42d61408997b19aa2e2e9d43c702d6ceb9839d3',
    'solo/alien-head-slanted-eyes': '101d2924cde75b6ab9ed73f04919ed2819c8c7f8ae6d949e539f4e8211b64393',
    'solo/align-justify': '9941578131639b8d7845e80cebca4073fcc9a09bb605461415d89f58a670052e',
    'solo/align-left': '6e31ecfe369830b99d84c813aad453e298f33032476c771b4a928440811e119a',
    'solo/amazon-elastic-container-service': '3ad8fe2c686082eb142369096c162970727956aec498b4ba8369814795d58581',
    'solo/amazon-elastic-kubernetes-service': 'e8d9c4fd2d230a37f4dcee27b01a4b4dc55095e4826c0205f177d29b5f33daa7',
    'solo/amfitheater-in-delphi-top': '8cd24ccdead154b40ad7e169c2acf5276a0468ad5f370dc424c270d67906a13c',
    'solo/analogue-wristwatch': 'c3a83b23dd04780047ce6a5fe525c4eca5e63b9dfaea202eb0c851872ac9807d',
    'solo/ant-head': '493303ea7a17d3c9a61f63601b8cf6a6d2e5830af3881aa7e10d0210d6700902',
    'solo/antenna-mobile-phone': 'afd9bb861776d13e03cb6196d91c95f6c38a3493ed4d642c31b865380ba21ead',
    'solo/antique-axe': 'a72857c077e7c4e982c8dbfd3306390ee1c4c6743efb4057c61e966c4ab2b1e7',
    'solo/anxious-face-with-sweat': 'c9366500388f237d700a13be3aae05b62e8eeeb9ad3db1b11548e263b1457903',
    'solo/apple-logo': 'fafbc5784b10973c5fc4870e4f9681747d618c8ba8cf74555eb5679c14a2af29',
    'solo/arrow-corner-bottom': '621f75bae2214d096fd0317a778c1c05bca5368e98fcc20b30ce806191174368',
    'solo/arrow-corner-left': 'a2dd0898730e1ee2d7a9d1ba405cc198709eeb365dd092d605207b1a84ae21d7',
    'solo/arrow-corner-right': '974ec91f94fa7c836c45e35b1aa0dd5da787a11fd530712f950c4c4e1e43df0c',
    'solo/artboard-shapes': '6d8896ce158d29a73b0c7d41224fbc7cc3a4ed1e37920b25ed7a0a05e06d02fb',
    'solo/astrology-lilith': '32a8e7f1632eef897be98167d3c30e582ff0f6a0769d68a1fce0999badda369a',
    'solo/athlete-running-right': 'b93c8654d5659f43c3fc72a895775ff74e67b61eda502e0579a7c78aefbc1e64',
    'solo/atv-side-view': '43f276e4c3cfa4ea4cca6ec8eef722ac0e51ad6b50d442477c14624a92cc721a',
    'solo/baby-figure': '2c73a788be499b73ef24770b43b7618198e6e2995d07efe9524c66fb0709ce95',
    'solo/baby-girl-face': '68e2fa7ef0a8581ddf6accb5543966b60db43c5a758364205239f4cd412845c5',
    'solo/baby-head': '029846953260e4491d4d9e82ff15b32170ab817e7b90784f735f931a275184a7',
    'solo/baby-onesie': 'bf1e3c107b2e7b68f7d5d5b9812ff29849a6fe3bd1b3f842835aff5686e95735',
    'solo/badge-3': 'c26db7fb46b87eddac3637199448c90e2996636e4230c22341c981cf33560be3',
    'solo/badminton-shuttlecock': '22f33baf309cf4734803062e64e1744c4bc2ae6a0843df0de436d0c6bbb0791d',
    'solo/bag-1e030fe3': '928b16f1b2bc5a5dd3eb7469728ccca65499587417cea45b8fa73a994d335898',
    'solo/bag-bf5296da': '0d3e54d4ebae82f6556408da36d5672dcf9a2f3e9bbb340556f597b01b309b39',
    'solo/bag-photography': '5c4084c47141c4abfba65aa47a1e546adefa4b8b9ab74618ee1a45351481e632',
    'solo/bandaged-index-finger': '34f8dc53329d72fe0ec9b91e69a3ac7c8f30d1ee3cbf6c3eb9049dbb099b78a7',
    'solo/barcode-7283882e': '132d006d8db043e8a2f33b509edaa164a516ce7bd989436fd5b8c04412f22ad9',
    'solo/basket-shopping': '8af6c1dda3c39f245f6c44305239e760f8a51ceec043cdf45d0ba30b604ef672',
    'solo/basketball-ball': '763b13d4d70d1c78a61e47580f75d1b9ab3f4aabfcf237e3fa032d8866412781',
    'solo/bat-emblem': 'd7bc80ab9b8cc8c68c0f649e9dc9b89a2fde533e846acf7930c51f8d3d02de9a',
    'solo/bath-duck': '15b6d6e6c3d5cda869352b79b012118fbc4a9560bf552cf87fde412bf09ff592',
    'solo/bathrobe': 'b62d698241281ca83331c2ace03b08319d29702e18ed16c9c52941616617e6a6',
    'solo/beaded-necklace-with-hexagon-stone': 'dae574786197de261a736045b7012e9aec489ab4e9143f59d20fc0e46de048d8',
    'solo/bean': '940558fcc03307774ce1d5a8fa0f3ba05c0609029fa7b78748d74e78ecb831fc',
    'solo/beetle': '716c63fc6ccdafeb7fd017793ef07316b422f3379c2d384b6587340840824f92',
    'solo/bendable-phone': '08041af79c953f8c7b01569e27f4ad492bac6c9f62f6fb2ef454fd7f2edd458f',
    'solo/bengal-cat-face': 'cd4f856196271457c7cb4d6999f2cf9abc0216999738531fff19a49d0f9d95b8',
    'solo/bicycle-angled-handlebar': 'c2e32e8deaf68b7c3d988b1b458db6d58b4c1ea8ee512b77845a553fc7fcce9b',
    'solo/bicycle': 'a3fb7d39384910001e6e2bd9637724b247af22c47bc501e3dbf4b00c7ddf575a',
    'solo/bird-flock': 'e8fcffd6f06495c939f7caa9a6b3646094f35df6b4687a0970918f4413346146',
    'solo/bitcoin-with-graph': 'b0bedb4ad481d11b31e98a68435a0dc5b6d6981ed775db82da864a690089d993',
    'solo/blind': '8987aff9134f8ce77c93126ddee472645fd745b6ed1112aaf94d60ebeffe31ae',
    'solo/blockchain-blocks': 'e9b6ad7c6c680acdaa205d298a3fcfe8a40bd3f0d966b5ce9d155369622b3e3e',
    'solo/board-rider-over-waves': '6f12887aabbce1226fb066c478fb77f977942d351a31cb60b0f99fc866c4f858',
    'solo/boat-pose-upward-reach': 'ec6be5936ba1cd397a07a8975fb2a082b377a839e7e0a6050751ca4e5c83ff30',
    'solo/bobble-hat-with-panelled-cuff': '6c35a1293a288cbf5dae580e3ac840ac7d29ee3621ed8f15ddcbc05299202bcd',
    'solo/bobble-hat-with-seams': 'b0e2f683d2fbcc0faf6c80f3c941911e976779929e7b71fe40d5e076080da54a',
    'solo/bowling-pins-three': 'b915f0eecac959fee3252353ca9dfe3ef70216aa328a69120cafa55b17c7fbc5',
    'solo/broad-bladed-sword': 'bdcc6cae0967da5a411dfe944c6ae007355024419c7256e0e9fdcd6159c7066e',
    'solo/brontosaurus': '68ce43d1241b558614db0e7519285f3444830321a88a895fcd90331246d5d607',
    'solo/cactus-in-rimmed-pot': 'f9fef23bad8177b35b304503310780ba5b8269f8742badfc8ae9673a51c67e5b',
    'solo/cactus-in-rounded-pot': 'ee3766ce2803873184059ce7004da036983e2e2a713417a83755399b8024259f',
    'solo/camper-van': 'fb472525c4ea28afa8432901e074b9e7185c80b35dd8830574c59a70f1b9d97c',
    'solo/capped-glue-stick': '9247ff4e70d3aa2b8475c8c2104accdb336093e5b40f4ae5198a418875e0ce58',
    'solo/castle-tower-with-pennant': '37d9cca864e5cfb177a0fe35d322eef68ddc414e1e53609cd850619084ad28c5',
    'solo/castle-with-gate-tower': 'f0baf14384f80edf9c33d6e613325436bd1cf93f7e20de5d683554cb06813379',
    'solo/cd-rom-drive': '153e92787a4e79c9d683a2d4f104550aa98d2188b0f6db419d50fb351877c9f4',
    'solo/cockatoo': 'd7d866612af8c5a272a8db4f513a79a7a751a07c2101daec1c30cdd0d7ed95aa',
    'solo/coiled-snake': 'b679b98a583b0bb85bb74982d94c7804fcc47e8520f66519ce99c293555509b4',
    'solo/cologne-cathedral': '736a3dfd516fc35b3c24a98960b75bd9f74533033f1beef709c2545513ac5117',
    'solo/columned-gateway-monument': '6561f3ab23bab66d62fd08ebab0c103ddf3e9f658896ad34671904d5cd5cc6b1',
    'solo/compact-disc-with-partition-segment': 'b123110474660e8d779140fc8b5d71d5e0b8030cc4d943628f256b1535405a42',
    'solo/crab': 'a3d3f2015b8f4da1d182eb3402fb7f727ab443b99b575a4049b45fccb6b08298',
    'solo/cracked-compact-disc': '424a1df068b3608083d2884aa120098cec404441aa2ee1d8caffed77a8fa841a',
    'solo/crawling-beetle': '8d57cf1866b28c10c999b4ee8bb2c8f40d480edb11f0e24aa7f7852421ca2d2d',
    'solo/crescent-moon': '2331d1d41da19fc27e6b0de22699c9b70f697f4bd87e21ca02cf516ce39ab8af',
    'solo/crocodile-in-water': '1da7c246495db4a8daf9d5c4456dd8034d83c9d17e834858dc84a6456c86dea4',
    'solo/cursor-1': '80fb0408a4e5841fc8b84e2d7538c29aa41293050be38cc2e7518a9c3f20145f',
    'solo/curved-dam-wall': 'e8b40c2919d8f6c1c6ba0f5bf648e5bf6ff459045d63e4c0938a259a134c2f2d',
    'solo/curved-monitor': '3fabdfc14ae35dcae5d5b0116b800c210bdabaea830a60e2863f48d35faa145d',
    'solo/dam-spillway-water': 'b5865637a21ae6f40c0861c9949fc990a1fc3e8953d7132b560fa7f959b2dabf',
    'solo/diaper-change': '7e1b8520e236b1286b0ba12628b33fe39111a82d7f17e116416a2e1d7fd2a510',
    'solo/dinosaur-skull': '4aa29fc090758786d32e70a1aa8745480bc809bfce12ab38c323be266bb6e7d1',
    'solo/triceratops-head-side': 'd1683d46193586eb8c1edf34ee1bde2c258a0f52b423ad1ad605c4028c7a91ee',
    'solo/disc-player': 'f8064c6b4e7586c7d99ac410fbd069796c66830e8d82a282903c885825ad93c7',
    'solo/document-a4b94225': '056dc86723a16dbc123ef23903405821db98244445a68321643e5c63f29fe5f0',
    'solo/duck-silhouette': 'a5aa732df9dc3d805cd8fa34fffc56903a9bbf8e9bbc9a5d133eaa917fe2d5d9',
    'solo/elephant-head': '3930928c8d00df3967e1efaac2f97f8bbc625acf6c61cc721a77eac811aae035',
    'solo/winged-insect': 'a3dc4afe7e13428581970967b3d2c19638cbaaf0296256d921594009a301e610',
    'solo/floppy-disk': '062a10fe96799ad0229ef744e6c6ad919f41b8997a124d02c9e3338cae9a73bd',
    'solo/flying-bird': 'dfe0631a40e6ae29ef2019cf9d9670552462b1c1057a6e8873399a25ea923212',
    'solo/folding-hand-fan': '97b0c8a59ffd43467008953974792bd4e3fa6999cf911d37b90cec45a826db9c',
    'solo/standing-fox': '65795d36c3bb0a084c4203b1152472994ba277f5f2927991ab1174cc212941d7',
    'solo/sitting-fox': 'a5f474647cf627129e3b838c2f5f318134a2b926210e01fc24999d90fac50b3b',
    'solo/grand-canyon-with-river': '0c9564c788e8c03ffe14852dbf0f934c1282163004c936269e08a138e7767331',
    'solo/grizzly-head-profile': 'ab75d582f0351b14b7ca9a80eb80be018beaa4ce4656df75181a880cc8122900',
    'solo/hammerhead-shark': '1d27eacdfad00272457f0af5cb77cabca54e89eb1bdcfd3337fab1a914f1e2f2',
    'solo/hippo-head-open-mouth': 'c9c3ba9f5db9fd87f746a74dbb0396846a1fea95420c31264100ebbab3b02025',
    'solo/hooked-beak-bird-head': '5f7c301ee464e6ed2c847320ce13fb07f2dd05e9a33d395d47f5851243f37970',
    'solo/howling-wolf': '3eeb311eeb2b6dfb44f87f3d5a1fd683316c6ed4a009bf7df4980b9fc5346ecb',
    'solo/itsukushima-torii-gate': '58ea5cc9925407664a632501ac51c1e134eb43cdecdc1daeb7e311dcdba959a0',
    'solo/leaping-dolphin': '41b3c727c7021f503a824e19e4d8910935dc941856907c813972ba79a2eff0db',
    'solo/leaping-marlin': 'f02c663a298af7034aef1c04fced4390ebdab0c3e0ece27d50e2ba3d6c4dbf4b',
    'solo/leaping-rabbit': '9070dfcd64417a7c173e1497fc74403dc086ca56bb5ef3669a5eb18cf618c095',
    'solo/winged-lion': 'c19dc315dfed979520aff3a47fcbd120e0cfaff1e9755d4f99c7518bad277530',
    'solo/merlion-statue': 'bf4cd3e0cb68901598ae64149044c1e3e29b94569978fd47f611a856da9ecc4d',
    'solo/open-locket-with-portrait': 'ede2777f44da0acd6d37dbd368476f89aee5f2c3bc8bff909df72a43edf3e45d',
    'solo/painted-wall-mural-panel': 'a2614b271e223ae154b2022874457fa96877635f2c91d19d08f413c1eec38bf4',
    'solo/paw-print-small-outer-toes': '717220c227569055e7cd7601cbd7aefb819bed8c6570cbf67fccaee9cd6cf684',
    'solo/peacock-feather': '8342894cc65387112e405242aeed2e83930e304f9831384cc251ec6b05eea4aa',
    'solo/penguin-looking-down': 'cca5600ce00eb8be80e927fe120bb3e9f49d40d152fb37c5608da994bb47bfe9',
    'solo/pregnancy-test': '278deac797b54d966601428abc49f029042fd76fd2de03ecbef0df4f4fe2aa03',
    'solo/pregnant-belly-with-heart': 'df63340d698a95d1a9923e8f055335b9b4aca6d2ec6fdfc9fc1d7c646e0a652d',
    'solo/slithering-snake': 'b99415f0b9ab988ba66e7ceabcd9e5ff337e1c6e35f5455534ad42e2c3fecfbe',
    'solo/round-hand-fan': '024362287c520ab0c190d698f499e280763355141e87b768521c9a5a2974f273',
    'solo/scorpion': '61315379587d4a298651273e12c2e630f9150ceb89f97bd42d65641ea5100637',
    'solo/woolly-sheep': 'ce3616afb8185bd67f8a4f2ed3eecfcaf90f12ac5916ac4bd50e87c16718a84c',
    'solo/simple-gabled-shack': '5d56571ace4b65c768c8c9b985e5bdf8312284a7309d1422cabc9352db09be29',
    'solo/singing-bird': '8ff8cd259c73645dde2f9dd94fc5fa620ffcdddfd15bbe42fcf522df29bb3db9',
    'solo/sitting-baby': 'b501ab5b7d21e317df55a638a3184afdf4046e29e49b2628959562951889f0a1',
    'solo/spider-web': '97c471aa74ab429cd177a3e655eb090fb3c82b215abca621c6a8de57388ede1b',
    'solo/star-labelled-bottle': '63fcc5b9afc0670f663f2c6d308e376a7d3d48ddad4a6b61766cf8f6dde9d67b',
    'solo/swan-on-water': '5f0b3fbc38735536a79acbc3f521d245074d6be9fa0e6e78ef21f7ef705faa69',
    'solo/trailing-hanging-planter': 'cd331da1000bf5cc4e5a71ff1e81d79295c07e64df810560b5ce90983eb561c0',
    'solo/twin-bell-alarm-clock': 'c42a86ae14adcd83f002fd3837ca4fdb895b8264c5509709652d1024e2264e11',
    'solo/whale-with-spout': '92acf5b477db158ab4b4a5d0f86621bb85af270374d63570d76be917639acf74',
    'solo/whiskered-seal': 'b92ea9ac696000da4e2fc574c1c56c9f93ef7c8690659fb89e83c95dd1a6809b',
    'solo/standing-owl': 'eee72f395ba918f71ace9996b864f3e536feae10e0af03d802ba9bbb9557185a',
    'solo/toucan': '1bf88fc6a5482e6cafaca5b3dcc4e454e1988668cac83b89d8158f95c4531ec5',
    'solo/windmill': '4b82891448d0b9122b708112866139bdeb102b7d4602f7bdea273c102dd078d1',
    'solo/wolf-head': 'b69bb1af93407fa61fdfd97b8bdd59138f529f3c3203da791efa0c1f8ed3cc71',
    'container/counter-clockwise-circular-arrow': '00376c134f4ba11e63252be1363d873fa2fbb98c1328c2babad953cf5ffc74f1',
    'container/kitchen-oven-appliance': '1021b9870906bd83273c3098b7e70c31a0532830308ff389750630971235d2ba',
    'container/teacher-presenting-at-whiteboard': 'ed8c3fe6225e09c5a7c5030f00336b5ec1c5adad228a4dd6c493313496b2ef18',
    'solo/ant': 'a589757fb816452c9326b24e21719f44e3bd81108173ba64cc1b2cd35db2843e',
    'solo/arched-stone-bridge': '304e1fb47d9b650640c5ef5169cc3a9aa86797f19c004507839302c5bde9a058',
    'solo/baby-bottle': '7eab9b120dc95afb50baa610bd81f5888acdb72338054f839a375845bf509d78',
    'solo/baby-bottle-with-handles': '716f9d959e0bbb5cd416225d79e8fd19a70ee59aa6e725e9e136396d2537d544',
    'solo/beaded-loop-with-heart-charm': '348b4ba4a6056b616e8deeacd1a16cbefdb35236bb7538d07a4f616d2251e058',
    'solo/bell-shaped-stupa': '08bf96e019e82b6513331e1df7a877d04989885d45ba29448d5bf44aebddc809',
    'solo/bird-in-flight': '7142218d68c6d60e8b0d28a37eb5b39623b45b1035da4d48628e4946125c5270',
    'solo/buffalo-head': '6fb04602279c34193ecd329dd9129f04048b4caaf276a3f944220e23de7063e8',
    'solo/cat-paw': '24a68dc358f8f94770aebb5c2f4eaa390ba2bb2bf269e15aadfdc2d3191e0946',
    'solo/cobra-head': 'b6745ebbbd2fcb9e342e6683680f2f2b70b8ff5583af18e8348b47017e45932c',
    'solo/compact-disc-with-sheen-arcs': '7562a13c6f4ff88b8836545e007a80d778a099446be7e444f5af1a4d1b927b84',
    'solo/crested-penguin': '4abd8f93d59426cfc7cce9e852c4ad2d0e6b59b0876f353e4436451a3da64551',
    'solo/disk-platter-with-drive-slots': '71965fae6041ded4f4e319956bc762ed65e320da582e5123c51c17e57f3dfe08',
    'solo/face-wearing-round-glasses': 'ef0a136758def6cd6168020a061a769b0cf8557efcc00b10029721da4355785e',
    'solo/hydroelectric-dam': 'e9bd6aea9eeaa6d418f90c7d610995a8504d0c4faf4e79dea8d4f6b028b6565e',
    'solo/intertwined-snakes': '0d0631ae53568388e494a1edf75f27308ffd1614df32e7cb1fca6d5c5f30701a',
    'solo/leaning-tower-of-pisa': 'bb5f826af2fa2accc4093da8a486eb815db84e94e7cfbcbb6e756a78a0c87d2c',
    'solo/leaping-antelope': '40a4a4f206d35b694a4407b707b3de77af546185077583e87ba3c15243113a7d',
    'solo/lidded-ceremonial-urn': '9894c8a1a67e8d035aa239675e1094c9fede81102735dcba66534351e75ab38b',
    'solo/minoan-palace': '03b208343e22bae40937b97337a09f7cb70103690c1683a26ae2672f062e125f',
    'solo/necklace-bust-form': '999e7f77b41f3cd1c09492cfeec81fd48a8693ddb2472e52022169006f3652a7',
    'solo/necklace-with-three-beads': '8b87cdef13af231e238579f6e35ee3bea4b2e1ab74f2ad163716322f3a8fc16f',
    'solo/olive-laurel-wreath': '96be940ae140a0e4ea922d707a6ba6c93842f9f2f27f3aef20f626581600a479',
    'solo/open-folding-fan': '1377762de75e0061344d92f9a0e1e1c1f457a142a9f9ba65ffad3832cccee494',
    'solo/pair-of-teardrop-earrings': '5219fcbe1e7541014a2b50f277997fabfe905557c6735f7c47c82faf377c1c58',
    'solo/paw-print': '432aeddc96782c78f476322bb99d487be4f335ed4cfa424a544b155c6b7c8a9f',
    'solo/pelican-on-water': 'ed840e421930815da95e1121e8bde2baf365666ebe0cb49d62e2f45552a4b14b',
    'solo/round-bud-vase': '897e0056b6c30a3a3e5cef3a9d1e0e3f00175a6e1ccab75620fbd337d19e7904',
    'solo/rubber-duck': '9ddfd438bca6961452b47f0f559e7f275f989614f4247ad47282f9112ef64ad1',
    'solo/saturn-astrological-symbol': 'bc42d7824bfbfded937fa39f0aaf879291e9904f1856e668ece8dccad386007b',
    'solo/scorpio-zodiac-symbol': '81ce8b8e68e7167ea830a712e031ae4d111246f7ebb39d0f794522c2191e535e',
    'solo/selene-astrological-symbol': '960249b40a8541ac7955051a98f725e7a2725f687d81f463b6e995be1a845e77',
    'solo/shanty-village-row': 'd872a392bb0e88a4ff59d8430a5794e25aa9074c5246120b0d048633a0513bc7',
    'solo/shopping-bag-with-loop-handle': '2da92a76719028d472779e3cf39e4f3750a4029c41d5642c0551a47dbdec90f8',
    'solo/sitting-penguin': 'ee2581bdbea44a227357a9803d1dc57678ba5f699ad50f9534be920b05eb3660',
    'solo/sitting-rabbit': 'c447ce19ae1e1f6dec6bb010ac25d31e5934720ae183cb1aa2b110321bc659c6',
    'solo/skunk': 'd21ee9be3eedfb9250d5c739d920f1de86ba977e5704bbb66a4ea3b9fcfcce06',
    'solo/sloth-face': 'f1c20ed1d992f934e528fac17a6518003d855981ac69c9ff59dba84e0b73e3c3',
    'solo/stacking-ring-toy': '2abf45def645a8c1b710583a23a9e6cf5542702e5ccd5dfb01eeae662972177e',
    'solo/standing-giraffe': '50fc3846d28aa4d20bbb2b7e092b22a60c9516d87f4eeba21a2a62b1afa47fa4',
    'solo/standing-lion': 'ab953e032cda4bc76ffa4241a4eaba6e1a98753b94e2d33c0cce51f77ec55b50',
    'solo/standing-stag': 'c8b8ee286635a5f6c7af6d3142e9f158b3510ee3a7df4c2298a5184dfbb6b187',
    'solo/three-bead-drop-earring': 'd7d1c768a0ef88613de8efa5c18d2a85e74de28d0aa27d3a8b325c8c806726f9',
    'solo/three-flying-birds': '39efc31bf066e790c0399641deba4040c8486e214c1edc23e2e2f3c586f10abb',
    'solo/tropical-island-with-palm-tree': '36f8dc9b6a46961cd8fdb19b57c84cedaa8a570cfca9b28449b79cebc6f7184b',
    'solo/turreted-chateau-hotel': '3ab5d78c978cfac2488e88cc8afd81ff7707981c51dd6a16f1844b98a716ef5c',
    'solo/vintage-studio-microphone': '7c8bc2c7b9f7132dd7f5a45c70b291265fe32169ef3e77fdbbfa9d4acf937cc5',
    'solo/witches-cauldron': 'ad3ce3c5b9a42b96c1dbd0b517f75e2e8c4fd7330c648868183c8be6a6f13ced',
    'solo/wolf-face': 'b9bde389bf24473041ddeb887dea0106ceef86dc3ab7eb9eac1752873aba30c8',
    'solo/wolf-head-profile': 'b6d335ddc8a0463d3448b888963b6c737707e17fbb782cf362f11bc7598ebec3',
    'solo/woolly-lamb-front': '0af31fcae81d5782dd6400f8ec29549208920d97a0b82f159089abdc1052e3f2',
    'sub/hexagon': 'cbbafd7994fa5b4f304398922846d19de1311068797b39557de93b4c43d8c110',
}
ICON_ALIASES = {
    'solo/crocodile-in-water-v2': 'solo/crocodile-in-water',
    'solo/swan-on-water-v2': 'solo/swan-on-water',
    'solo/analogue-wristwatch-v2': 'solo/analogue-wristwatch',
    'solo/diaper-change-v2': 'solo/diaper-change',
    'solo/grand-canyon-with-river-v2': 'solo/grand-canyon-with-river',
    'solo/baby-girl-face-v2': 'solo/baby-girl-face',
    'solo/leaping-dolphin-v2': 'solo/leaping-dolphin',
    'solo/leaping-rabbit-v2': 'solo/leaping-rabbit',
    'solo/baby-head-v3': 'solo/baby-head',
    'solo/baby-figure-v2': 'solo/baby-figure',
    'container/fringed-area-rug-v2': 'container/fringed-area-rug',
    'container/hexagonal-molecular-structure-v2': 'container/hexagonal-molecular-structure',
}

# Completion times for additional fixes or visual reviews; earlier cutoffs stay unchanged.
PROCESSED_TIMES = {
    'solo/canoe': '2026-09-15T17:07:56.518959+00:00',
    'solo/anteater': '2026-09-15T16:52:25.357440+00:00',
    'container/clipboard': '2026-09-15T16:52:25.357440+00:00',
    'container/fringed-area-rug': '2026-09-15T16:52:25.357440+00:00',
    'container/hexagonal-molecular-structure': '2026-09-15T16:52:25.357440+00:00',
    'container/counter-clockwise-circular-arrow': '2026-09-15T17:07:56.518959+00:00',
    'container/kitchen-oven-appliance': '2026-09-15T17:07:56.518959+00:00',
    'container/teacher-presenting-at-whiteboard': '2026-09-15T17:07:56.518959+00:00',
    'solo/ant': '2026-09-15T17:07:56.518959+00:00',
    'solo/arched-stone-bridge': '2026-09-15T17:07:56.518959+00:00',
    'solo/baby-bottle': '2026-09-15T17:07:56.518959+00:00',
    'solo/baby-bottle-with-handles': '2026-09-15T17:07:56.518959+00:00',
    'solo/beaded-loop-with-heart-charm': '2026-09-15T17:07:56.518959+00:00',
    'solo/bell-shaped-stupa': '2026-09-15T17:07:56.518959+00:00',
    'solo/bird-in-flight': '2026-09-15T17:07:56.518959+00:00',
    'solo/buffalo-head': '2026-09-15T17:07:56.518959+00:00',
    'solo/cat-paw': '2026-09-15T17:07:56.518959+00:00',
    'solo/cobra-head': '2026-09-15T17:07:56.518959+00:00',
    'solo/compact-disc-with-sheen-arcs': '2026-09-15T17:07:56.518959+00:00',
    'solo/crested-penguin': '2026-09-15T17:07:56.518959+00:00',
    'solo/disk-platter-with-drive-slots': '2026-09-15T17:07:56.518959+00:00',
    'solo/face-wearing-round-glasses': '2026-09-15T17:07:56.518959+00:00',
    'solo/hydroelectric-dam': '2026-09-15T17:07:56.518959+00:00',
    'solo/intertwined-snakes': '2026-09-15T17:07:56.518959+00:00',
    'solo/leaning-tower-of-pisa': '2026-09-15T17:07:56.518959+00:00',
    'solo/leaping-antelope': '2026-09-15T17:07:56.518959+00:00',
    'solo/lidded-ceremonial-urn': '2026-09-15T17:07:56.518959+00:00',
    'solo/minoan-palace': '2026-09-15T17:07:56.518959+00:00',
    'solo/necklace-bust-form': '2026-09-15T17:07:56.518959+00:00',
    'solo/necklace-with-three-beads': '2026-09-15T17:07:56.518959+00:00',
    'solo/olive-laurel-wreath': '2026-09-15T17:07:56.518959+00:00',
    'solo/open-folding-fan': '2026-09-15T17:07:56.518959+00:00',
    'solo/pair-of-teardrop-earrings': '2026-09-15T17:07:56.518959+00:00',
    'solo/paw-print': '2026-09-15T17:07:56.518959+00:00',
    'solo/pelican-on-water': '2026-09-15T17:07:56.518959+00:00',
    'solo/round-bud-vase': '2026-09-15T17:07:56.518959+00:00',
    'solo/rubber-duck': '2026-09-15T17:07:56.518959+00:00',
    'solo/saturn-astrological-symbol': '2026-09-15T17:07:56.518959+00:00',
    'solo/scorpio-zodiac-symbol': '2026-09-15T17:07:56.518959+00:00',
    'solo/selene-astrological-symbol': '2026-09-15T17:07:56.518959+00:00',
    'solo/shanty-village-row': '2026-09-15T17:07:56.518959+00:00',
    'solo/shopping-bag-with-loop-handle': '2026-09-15T17:07:56.518959+00:00',
    'solo/sitting-penguin': '2026-09-15T17:07:56.518959+00:00',
    'solo/sitting-rabbit': '2026-09-15T17:07:56.518959+00:00',
    'solo/skunk': '2026-09-15T17:07:56.518959+00:00',
    'solo/sloth-face': '2026-09-15T17:07:56.518959+00:00',
    'solo/stacking-ring-toy': '2026-09-15T17:07:56.518959+00:00',
    'solo/standing-giraffe': '2026-09-15T17:07:56.518959+00:00',
    'solo/standing-lion': '2026-09-15T17:07:56.518959+00:00',
    'solo/standing-stag': '2026-09-15T17:07:56.518959+00:00',
    'solo/three-bead-drop-earring': '2026-09-15T17:07:56.518959+00:00',
    'solo/three-flying-birds': '2026-09-15T17:07:56.518959+00:00',
    'solo/tropical-island-with-palm-tree': '2026-09-15T17:07:56.518959+00:00',
    'solo/turreted-chateau-hotel': '2026-09-15T17:07:56.518959+00:00',
    'solo/vintage-studio-microphone': '2026-09-15T17:07:56.518959+00:00',
    'solo/witches-cauldron': '2026-09-15T17:07:56.518959+00:00',
    'solo/wolf-face': '2026-09-15T17:07:56.518959+00:00',
    'solo/wolf-head-profile': '2026-09-15T17:07:56.518959+00:00',
    'solo/woolly-lamb-front': '2026-09-15T17:07:56.518959+00:00',
    'sub/hexagon': '2026-09-15T17:07:56.518959+00:00',
}
PROFILE_FOLDERS = {'solo': 'solo48', 'container': 'container64', 'sub': 'sub32'}

# Explicitly discarded by the user after viewing the seven-entry comparison.
DISCARDED_ICONS = (
    'solo/butterfly-in-heart',
    'solo/classical-head-with-book',
    'solo/knight-helm-on-shield',
    'solo/monitor-download-arrow',
    'solo/monitor-in-security-shield',
    'solo/right-double-click-mouse',
    'solo/sunglasses-with-sun',
)

def as_utc(value):
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    return parsed.replace(tzinfo=timezone.utc) if parsed.tzinfo is None else parsed.astimezone(timezone.utc)


def remove_discarded_records(db, dist, records, result):
    """Clean only the named discarded icons, once their removal has been deployed."""
    for key in DISCARDED_ICONS:
        family, icon_id = key.split('/')
        folder = PROFILE_FOLDERS[family]
        if (key in records or (dist / folder / (icon_id + '.svg')).exists()
                or (dist / 'failed' / folder / (icon_id + '.svg')).exists()):
            result['skipped'][key] = 'Discarded icon is still deployed; deploy its removal first'
            continue
        db.execute('DELETE FROM pending_briefs WHERE split_id IN (SELECT id FROM split_requests WHERE icon=?)', (key,))
        db.execute('DELETE FROM split_requests WHERE icon=?', (key,))
        result['feedback_deleted'] += db.execute('DELETE FROM feedback WHERE icon=?', (key,)).rowcount
        db.execute('DELETE FROM reviews WHERE icon=?', (key,))
        db.execute('DELETE FROM icon_flags WHERE icon=?', (key,))
        result['discarded'].append(key)


def mark_processed(database, dist, *, reset_review_status=False):
    database, dist = Path(database).resolve(), Path(dist).resolve()
    if not database.is_file():
        raise ValueError(f'Database not found: {database}')
    if database.is_relative_to(dist):
        raise ValueError('Keep the database outside the public build folder')
    data = json.loads((dist / 'gallery/icons.json').read_text())
    records = {r['family'] + '/' + r['icon_id']:r for r in data['icons'] + data.get('failed_icons', [])}
    backup = database.with_name(database.name + '.before-ready-' +
                                datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%f') + '.bak')
    with closing(sqlite3.connect(database)) as source, closing(sqlite3.connect(backup)) as destination:
        source.backup(destination)
        if destination.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
            raise ValueError('Could not verify the database backup')
    result = {'updated':[], 'already_ready':[], 'skipped':{}, 'feedback_deleted':0, 'discarded':[], 'backup':str(backup)}
    with closing(sqlite3.connect(database, timeout=30)) as db, db:
        db.execute('BEGIN IMMEDIATE')
        for key, expected_hash in CHANGED_ICONS.items():
            family, icon_id = key.split('/')
            processed_at = PROCESSED_TIMES.get(key, PROCESSED_AT)
            svg = dist / PROFILE_FOLDERS[family] / (icon_id + '.svg')
            if (key not in records or records[key]['svg_sha256'] != expected_hash or
                    not svg.is_file() or hashlib.sha256(svg.read_bytes()).hexdigest() != expected_hash):
                result['skipped'][key] = 'Updated icon has not been deployed'
                continue
            aliases = [old for old,new in ICON_ALIASES.items() if new == key]
            names = [key, *aliases]
            placeholders = ','.join('?' for _ in names)
            if db.execute('SELECT 1 FROM split_requests WHERE active=1 AND icon IN ('+placeholders+')',names).fetchone():
                result['skipped'][key] = 'Active combination split'
                continue
            rejection_times = db.execute("SELECT updated_at FROM reviews WHERE status='rejected' AND icon IN ("+placeholders+')',names)
            if not reset_review_status and any(as_utc(at) > as_utc(processed_at) for (at,) in rejection_times):
                result['skipped'][key] = 'Newer rejection needs review'
                continue
            current = db.execute('SELECT status,updated_at FROM reviews WHERE icon=? AND svg_sha256=?',(key,expected_hash)).fetchone()
            # Ready is already the requested outcome; regeneration also awaits review.
            # Neither status should prevent removing the verified older feedback.
            if (not reset_review_status and current and current[0] not in ('ready', 're-generated')
                    and as_utc(current[1]) > as_utc(processed_at)):
                result['skipped'][key] = f'Newer review decision ({current[0]} at {current[1]}); use --reset-review-status to reset this batch'
                continue
            feedback_times = db.execute('SELECT COALESCE(edited_at,created_at) FROM feedback WHERE icon IN ('+placeholders+')',names)
            if any(as_utc(at) > as_utc(processed_at) for (at,) in feedback_times):
                result['skipped'][key] = 'Newer feedback needs review'
                continue
            result['feedback_deleted'] += db.execute(
                'DELETE FROM feedback WHERE icon IN ('+placeholders+')',names).rowcount
            # The app treats rejection on ANY old SVG as an icon-wide block.
            # Match its restore behavior before setting the fixed version Ready.
            db.execute("UPDATE reviews SET status='pending',updated_at=?,updated_by='feedback-script' "
                       "WHERE status='rejected' AND icon IN ("+placeholders+')',[processed_at,*names])
            if current and current[0] == 'ready':
                result['already_ready'].append(key)
                continue
            db.execute("""INSERT INTO reviews(icon,svg_sha256,status,updated_at,updated_by)
                VALUES (?,?,'ready',?,'feedback-script')
                ON CONFLICT(icon,svg_sha256) DO UPDATE SET status=excluded.status,
                updated_at=excluded.updated_at,updated_by=excluded.updated_by""",(key,expected_hash,processed_at))
            result['updated'].append(key)
        remove_discarded_records(db, dist, records, result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database',type=Path,default=PACKAGE/'data/feedback.sqlite3')
    parser.add_argument('--dist',type=Path,default=PACKAGE/'dist')
    parser.add_argument('--reset-review-status', action='store_true',
                        help='Reset later review statuses for the verified batch to Ready; keep newer feedback, active splits, and SVG version checks')
    args = parser.parse_args()
    try:
        result = mark_processed(args.database,args.dist,reset_review_status=args.reset_review_status)
    except (OSError,ValueError,KeyError,sqlite3.Error) as error:
        parser.exit(1,f'{error}\n')
    print(f"Ready: {len(result['updated'])}; already ready: {len(result['already_ready'])}; feedback deleted: {result['feedback_deleted']}; discarded: {len(result['discarded'])}; skipped: {len(result['skipped'])}")
    print(f"Backup: {result['backup']}")
    for key in result['updated']:
        print(f'Updated {key}')
    for key in result['discarded']:
        print(f'Discarded {key}')
    for key,reason in result['skipped'].items():
        print(f'Skipped {key}: {reason}')


if __name__ == '__main__':
    main()
