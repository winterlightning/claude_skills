#!/usr/bin/env python3
"""Remove processed feedback for 135 changed icons and put their new versions in Ready.
Run after deploying the updated icons. Newer feedback and review decisions are kept.
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
# Changed icon IDs; hashes ensure we only mark the actual fixed drawings.
CHANGED_ICONS = {
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
}
ICON_ALIASES = {'solo/diaper-change-v2': 'solo/diaper-change'}

def as_utc(value):
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    return parsed.replace(tzinfo=timezone.utc) if parsed.tzinfo is None else parsed.astimezone(timezone.utc)


def mark_processed(database, dist):
    database, dist = Path(database).resolve(), Path(dist).resolve()
    if not database.is_file():
        raise ValueError(f'Database not found: {database}')
    if database.is_relative_to(dist):
        raise ValueError('Keep the database outside the public build folder')
    data = json.loads((dist / 'gallery/icons.json').read_text())
    records = {r['family'] + '/' + r['icon_id']:r for r in data['icons']}
    backup = database.with_name(database.name + '.before-ready-' +
                                datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%f') + '.bak')
    with closing(sqlite3.connect(database)) as source, closing(sqlite3.connect(backup)) as destination:
        source.backup(destination)
        if destination.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
            raise ValueError('Could not verify the database backup')
    result = {'updated':[], 'already_ready':[], 'skipped':{}, 'feedback_deleted':0, 'backup':str(backup)}
    with closing(sqlite3.connect(database, timeout=30)) as db, db:
        db.execute('BEGIN IMMEDIATE')
        for key, expected_hash in CHANGED_ICONS.items():
            icon_id = key.split('/')[1]
            svg = dist / 'solo48' / (icon_id + '.svg')
            if (key not in records or records[key]['svg_sha256'] != expected_hash or
                    not svg.is_file() or hashlib.sha256(svg.read_bytes()).hexdigest() != expected_hash):
                result['skipped'][key] = 'Updated icon has not been deployed'
                continue
            aliases = [old for old,new in ICON_ALIASES.items() if new == key]
            names = [key, *aliases]
            placeholders = ','.join('?' for _ in names)
            if db.execute("SELECT 1 FROM reviews WHERE status='rejected' AND icon IN ("+placeholders+')',names).fetchone() or db.execute('SELECT 1 FROM split_requests WHERE active=1 AND icon IN ('+placeholders+')',names).fetchone():
                result['skipped'][key] = 'Rejected icon or combination'
                continue
            current = db.execute('SELECT status,updated_at FROM reviews WHERE icon=? AND svg_sha256=?',(key,expected_hash)).fetchone()
            if current and (current[0] == 'approve' or as_utc(current[1]) > as_utc(PROCESSED_AT)):
                result['skipped'][key] = 'Existing approval or newer review'
                continue
            feedback_times = db.execute('SELECT COALESCE(edited_at,created_at) FROM feedback WHERE icon IN ('+placeholders+')',names)
            if any(as_utc(at) > as_utc(PROCESSED_AT) for (at,) in feedback_times):
                result['skipped'][key] = 'Newer feedback needs review'
                continue
            result['feedback_deleted'] += db.execute(
                'DELETE FROM feedback WHERE icon IN ('+placeholders+')',names).rowcount
            if current and current[0] == 'ready':
                result['already_ready'].append(key)
                continue
            db.execute("""INSERT INTO reviews(icon,svg_sha256,status,updated_at,updated_by)
                VALUES (?,?,'ready',?,'feedback-script')
                ON CONFLICT(icon,svg_sha256) DO UPDATE SET status=excluded.status,
                updated_at=excluded.updated_at,updated_by=excluded.updated_by""",(key,expected_hash,PROCESSED_AT))
            result['updated'].append(key)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database',type=Path,default=PACKAGE/'data/feedback.sqlite3')
    parser.add_argument('--dist',type=Path,default=PACKAGE/'dist')
    args = parser.parse_args()
    try:
        result = mark_processed(args.database,args.dist)
    except (OSError,ValueError,KeyError,sqlite3.Error) as error:
        parser.exit(1,f'{error}\n')
    print(f"Ready: {len(result['updated'])}; already ready: {len(result['already_ready'])}; feedback deleted: {result['feedback_deleted']}; skipped: {len(result['skipped'])}")
    print(f"Backup: {result['backup']}")
    for key in result['updated']:
        print(f'Updated {key}')
    for key,reason in result['skipped'].items():
        print(f'Skipped {key}: {reason}')


if __name__ == '__main__':
    main()
