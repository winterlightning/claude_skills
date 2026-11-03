# Edited thumbnail verification

`check_thumbnails_local.py` exercises the real Worker and Python graphics service
with synthetic 36/48/54/64/72px uploads. It checks save/reopen, Original and Manual
Upload preview bases, selected thumbnail URLs **and SVG contents**, stale saves,
restoring the original, and a validated Browser Edit pick. Rendering an unvalidated
custom edit must not make it eligible for selection. All mutating requests are
restricted to a loopback HTTP address.

`check_thumbnails_browser.py` opens the real gallery in installed **Microsoft
Edge**, decodes the grid image and all three Pick images for both edit bases, and
saves screenshots. It blocks non-GET browser requests. With `--stored-assets`, the
gallery assets are also read through the Worker from local R2.

## Prepare isolated storage

Install Python dependencies with `python3 -m pip install -r icon_set/requirements-qa.txt`
and `python3 -m pip install playwright`. Use the project Python environment, not
an older system Python. No browser download is required; Edge must be installed.
Build `cloud/worker/app` with `worker-build --release` using the rustup toolchain.

From the repository root, generate temporary configs (never copy production
bindings, account IDs, secrets, or `.dev.vars`):

```sh
python3 - <<'PY'
import json, tempfile
from pathlib import Path
repo = Path.cwd()
scratch = Path(tempfile.mkdtemp(prefix='thumbnail-verification-'))
config = {
    'name': 'thumbnail-verification',
    'main': str(repo/'cloud/worker/app/build/worker/shim.mjs'),
    'compatibility_date': '2026-07-17',
    'd1_databases': [{'binding': 'DB', 'database_name': 'thumbnail-verification',
        'database_id': '00000000-0000-0000-0000-000000000025',
        'migrations_dir': str(repo/'cloud/worker/migrations')}],
    'r2_buckets': [{'binding': 'FILES', 'bucket_name': 'thumbnail-verification'}],
    'vars': {'ADMIN_USERS': json.dumps({'tester': 'preview-only'}),
        'BUILTIN_FAMILIES': json.dumps([['sub',32],['solo',48],['container',64],
                                      ['combination_main',48],['symbol',32]])},
    'services': [{'binding': 'GRAPHICS', 'service': 'thumbnail-graphics'}],
}
(scratch/'wrangler.json').write_text(json.dumps(config))
(scratch/'graphics.json').write_text(json.dumps({'name': 'thumbnail-graphics',
    'main': 'graphics.js', 'compatibility_date': '2026-07-17'}))
(scratch/'graphics.js').write_text("export default {fetch(r){return fetch(new Request('http://127.0.0.1:8894'+new URL(r.url).pathname,r));}};")
print(scratch)
PY
```

Set `thumbnail_state` to the printed directory, then apply local migrations:

```sh
wrangler d1 migrations apply thumbnail-verification --local \
  --config "$thumbnail_state/wrangler.json" --persist-to "$thumbnail_state/state"
```

Run the Python service from the repository root in one terminal:

```sh
PORT=8894 PYTHONPATH=. python3 cloud/graphics/server.py
```

Run the Worker and local graphics proxy in another terminal:

```sh
wrangler dev --local --config "$thumbnail_state/wrangler.json" \
  --config "$thumbnail_state/graphics.json" --persist-to "$thumbnail_state/state" \
  --ip 127.0.0.1 --port 8893 --inspector-port 9239
```

## Run HTTP and browser checks

```sh
python3 cloud/worker/tests/artwork/check_thumbnails_local.py \
  --output "$thumbnail_state/fixtures.json"
python3 cloud/worker/tests/artwork/check_thumbnails_browser.py \
  --fixtures "$thumbnail_state/fixtures.json" --screenshots "$thumbnail_state/screenshots"
```

To also verify R2 asset delivery, put `index.html`, `laboratory.json`, and each
local script/stylesheet referenced by `index.html` into the **local** bucket:

```sh
wrangler r2 object put thumbnail-verification/site/gallery/index.html --local \
  --config "$thumbnail_state/wrangler.json" --persist-to "$thumbnail_state/state" \
  --file published/gallery/index.html
# Repeat for each asset, keeping its filename under site/gallery/.
python3 cloud/worker/tests/artwork/check_thumbnails_browser.py --stored-assets \
  --fixtures "$thumbnail_state/fixtures.json" --screenshots "$thumbnail_state/r2-screenshots"
```

Stop the local servers after verification. These tests do not deploy a Worker or
migrate production. Production and `review-next` share D1; live verification of a
released fix still requires an explicitly authorized release.
