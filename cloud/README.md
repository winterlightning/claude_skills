# Pictographic on Cloudflare

The review server's data and status move from `feedback.sqlite3` on one Mac mini to Cloudflare.
**The cloud stores data and marks status; graphics processing stays on local machines, except the gallery stroke editor, which runs the same Python in a Cloudflare Container (`graphics/`).**

| Where | What |
|---|---|
| **D1** (database `pictographic-review`) | reviews, feedback, work claims, activity log, uploads, icon types/flags, primitive decisions and briefs, split briefs, sign-in sessions, the effective catalog (one row per icon) and every authored drawing (SVGs are ~450 bytes, stored inline) |
| **R2** (bucket `pictographic-review`) | files that never change or are large: the built gallery site (`site/`), reference SVGs (`references/`), uploaded reference images (`stores/reference-images/`), `icons.json` / `primitives.json` / `combinations.json` |
| **Worker** (`worker/`, Rust) | the same HTTP API as `icon_set/scripts/deploy.py`: same paths, JSON and errors |
| **Graphics container** (`graphics/`, Python) | the gallery's stroke editor and artwork picks: edit geometry, validation, SVG render, run by the same `icon_set` modules as `deploy.py`, called by the Worker (service binding `GRAPHICS`) |
| **Local** (`deploy.py --cloud-api URL`) | rendering, validation, stroke-edit geometry, QA evidence, artwork choice, discard of Python sources, generation, AI feedback, combination experiments, builds |

The data model the cloud grows into (concepts, physicals, icons, revisions, releases) is in
[`data-model.html`](data-model.html); the schema already has those tables, seeded later.

## Layout

```
cloud/
  data-model.html      design: vocabulary, tables, diagrams
  MIGRATION.md         step-by-step migration and cutover runbook
  ARCHITECTURE.md      what D1 and R2 hold (every table and prefix) and how to merge the Mac mini's data
  .env                 CLOUDFLARE_API_TOKEN, push tokens, R2 keys (git-ignored, never commit)
  worker/
    core/              pure rules in Rust (no Cloudflare): reviews, stats, work claims, primitives, SVG safety
    app/               the Worker: routes, D1 and R2 access
    migrations/        D1 schema
    tests/http/        parity tests against the Python server
    wrangler.toml
  graphics/            Cloudflare Container: Dockerfile (+ allow-list .dockerignore), server.py, host Worker (worker.js, wrangler.jsonc)
  migrate/             Python scripts: snapshot, D1 import, catalog push, file upload, verify
```

## Everyday use

**Reviewers** open the Worker URL instead of the tunnel. Same pages, same logins.

**Workers and agents** point the existing tools at the cloud:

```bash
export PICTOGRAPHIC_API=https://pictographic-review.pictographic.workers.dev
python3 icon_set/scripts/work_queue.py next --worker thuan-mac      # unchanged tool, new URL
```

**Local processing** (stroke edits, artwork choice, generation, discard) runs the familiar gallery
on your machine; every read and write of shared data goes to the cloud:

```bash
python3 icon_set/scripts/deploy.py --cloud-api https://pictographic-review.pictographic.workers.dev --open
```

**After a build** (`python3 -m icon_set publish`), push the new catalog:

```bash
python3 cloud/migrate/push_catalog.py --base-url https://pictographic-review.pictographic.workers.dev
python3 cloud/migrate/push_files.py --backend s3 published=site     # only changed files are sent
```

## Develop and test

Rust must come from rustup (Homebrew's `rustc` has no wasm target): put `~/.cargo/bin` first on PATH.

```bash
cd cloud/worker
cargo test -p pictographic-core                         # 26 rule tests, native, < 1 s
wrangler d1 migrations apply pictographic-review --local
wrangler dev --port 8787                                 # builds the Worker, emulates D1 and R2
```

Parity against the Python server (always on **copies** of the database):

```bash
python3 cloud/migrate/export_snapshot.py --out cloud/exports/rehearsal.sqlite3
python3 cloud/migrate/build_d1_import.py cloud/exports/rehearsal.sqlite3
wrangler d1 execute pictographic-review --local --file cloud/exports/d1-import.sql       # (from cloud/worker)
python3 cloud/migrate/push_catalog.py --base-url http://127.0.0.1:8787
cp cloud/exports/rehearsal.sqlite3 /tmp/parity/feedback.sqlite3
python3 icon_set/scripts/deploy.py --production --dist published --database /tmp/parity/feedback.sqlite3 --port 8799
python3 cloud/migrate/verify.py --old http://127.0.0.1:8799 --new http://127.0.0.1:8787     # reads: 272/272 identical
PICTOGRAPHIC_OLD=http://127.0.0.1:8799 PICTOGRAPHIC_NEW=http://127.0.0.1:8787 python3 -m pytest cloud/worker/tests/http -q
```

## Graphics container

`graphics/` is a second Worker, `pictographic-graphics`, that only hosts a Cloudflare Container
(Python 3.12, cairo, OpenCV and the `icon_set` edit/validation/render modules, no authored icon
modules). It is not public; the review Worker reaches it through its `GRAPHICS` service binding.
It sleeps after 10 idle minutes (the first request after that waits a few seconds) and needs the
Workers Paid plan. Deploy it first; Docker must be running and wrangler needs Node 22:

```bash
cd cloud/graphics && npm install
npx wrangler deploy                          # builds the image (linux/amd64) from the repo root
cd ../worker && npx wrangler d1 migrations apply pictographic-review --remote
npx wrangler deploy
```

Redeploy it when `icon_set/model`, `validation`, `renderers` or the edit scripts change, so the cloud
validates exactly like the build. Test the image on its own:

```bash
docker build --platform linux/amd64 -f cloud/graphics/Dockerfile -t pictographic-graphics:dev .
docker run --rm -p 8932:8080 pictographic-graphics:dev      # POST /edit, /validate, /render, /artwork
```

Locally, run both Workers together: `npx wrangler dev -c wrangler.toml -c ../graphics/wrangler.jsonc`
(from `cloud/worker`). Without a push token, fill `icon_graphs` from a build with
`python3 cloud/migrate/push_catalog.py --sql /tmp/graphs.sql --graphs-only` and run each
`/tmp/graphs-NNN.sql` with `npx wrangler d1 execute pictographic-review --remote --file ...`.

## Test copy (pictographic-review-next)

A second Worker runs this branch on copies of production, so changes can be tried on a second site
without touching `pictographic-review`: <https://pictographic-review-next.pictographic.workers.dev>
(`worker/wrangler.next.toml`: D1 `pictographic-review-next`, R2 `pictographic-review-next`, the shared
graphics container). Production is only read while the copy is made or refreshed:

```bash
cd cloud/worker
npx wrangler d1 export pictographic-review --remote --output /tmp/combo/prod.sql     # read-only
sqlite3 /tmp/combo/prod.sqlite < /tmp/combo/prod.sql
cp /tmp/combo/prod.sqlite /tmp/combo/next.sqlite
for f in migrations/0009_combination_parts.sql migrations/00{10,11,12,14}_*.sql; do sqlite3 /tmp/combo/next.sqlite < $f; done   # the ones prod lacks
npx wrangler r2 object get pictographic-review/site/gallery/experiment-combination.json --remote --file /tmp/combo/experiment-combination.json
npx wrangler r2 object get pictographic-review/site/gallery/combinations.json --remote --file /tmp/combo/combinations.json
python3 ../migrate/backfill_combinations.py --db /tmp/combo/prod.sqlite --pairs /tmp/combo/experiment-combination.json \
    --combinations /tmp/combo/combinations.json --out /tmp/combo/fill.sql
sqlite3 -bail /tmp/combo/next.sqlite < /tmp/combo/fill.sql
python3 ../migrate/copy_bucket.py pictographic-review pictographic-review-next      # only copies what changed
```

The backfill must read a snapshot taken **before** 0010: it carries `reference_uploads` into the parts' icons, and
takes the container and symbol icons the old Container pairs page showed from `combinations.json`. Without
`--combinations` only pairs with a single icon of each family get one (239 of 2,773 locally, against 2,215 with it).
Container placements are not a table: they live in each pair's symbol layout (container-pairs.html). 0013 created a
`container_placements` table that only production ever had; 0014 drops it.
Placements saved in the old `container_centers` table (0006 / 0008, dropped by 0010) are carried into those layouts
when the snapshot still has it (container-placement.js describes the fields).

`wrangler d1 export --remote` stops at 260 MiB: the file ends mid-statement and every table after that point is
missing (it happened on 2026-10-01 inside `store_documents`). Check the end of the file and each table's row count
against `d1 execute --remote`, and export what is missing with `--table`.

Two migrations share the number 0009: `0009_primitive_state_version.sql` (icon-lib, applied in production
2026-09-30) and `0009_combination_parts.sql` (this branch, applied on the test copy). D1 records applied
migrations by file name, so each database applies only the one it lacks; neither may be renamed, or it would
run twice.

Then load `next.sqlite` into the (emptied) `pictographic-review-next` database: record the applied
migrations in `d1_migrations`, dump it without `BEGIN`/`COMMIT`/`sqlite_sequence`, run the dump with
`wrangler d1 execute pictographic-review-next --remote -c wrangler.next.toml --file`, and insert rows
over D1's 100 KB statement limit (`progression_reviews`) through the D1 query API with bound parameters.
Deploy with `npx wrangler deploy -c wrangler.next.toml`.

Locally, `wrangler.next.local.toml` (git-ignored) is `wrangler.next.toml` with `remote = true` on the R2
binding, so `npx wrangler dev -c wrangler.next.local.toml --persist-to /tmp/combo/state` serves the real
site from the test bucket with a local D1.

## Icon list (GET /api/icons)

Icon review, the approved collection, Home and the Design Document list icons a page at a time from D1 instead of
downloading `icons.json` (~90 MB). Migration 0015 adds the list columns; the catalog push stores each icon's full
record and fills them, uploads and combination builds keep them current. After applying 0015 to a database whose
icons were pushed before it, fill the columns once from the stored rows, then push the catalog for full records:

```sh
npx wrangler d1 migrations apply <database> --remote [-c wrangler.next.toml]
npx wrangler deploy [-c wrangler.next.toml]
# list columns of uploads and browser-built combinations, 500 rows a request (push token):
curl -X POST "$WORKER/api/icons/reindex" -H "Authorization: Bearer $PICTOGRAPHIC_PUSH_TOKEN" -d '{"offset": 0}'   # repeat with next_offset
python3 cloud/migrate/push_catalog.py --base-url "$WORKER"   # full records, list columns and symmetry of built icons
```

The query is core/src/icon_query.rs, checked against the old page's own list functions over a made-up catalog
(core/tests/icon_query.rs; tests/icon_list/check_local.py does the same through a local Worker); deploy.py answers
the same routes from its catalog (icon_set/scripts/icon_query.py, icon_set/tests/test_icon_query.py).

## Secrets

| Name | Where | Used by |
|---|---|---|
| `CLOUDFLARE_API_TOKEN` | `cloud/.env` | wrangler (deploy, D1, R2) |
| `PUSH_TOKEN` | Worker secret (`wrangler secret put PUSH_TOKEN`), `worker/.dev.vars` locally | guards catalog push, file upload, stores, discard, activity |
| `PICTOGRAPHIC_PUSH_TOKEN` / `PICTOGRAPHIC_PUSH_TOKEN_LOCAL` | `cloud/.env` | local tools calling those routes (remote / wrangler dev) |
| `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY` | `cloud/.env` | `push_files.py --backend s3` |

Reviewer sign-in is unchanged by decision: the five users and passwords from `deploy.py` are in
`ADMIN_USERS` in `wrangler.toml` (change them there, no code change). Anyone who has the URL can
sign in with them; put the Worker behind Cloudflare Access if that stops being acceptable.

## What differs from deploy.py

* The stroke editor and Pick panel run in the cloud: `/api/stroke-edits*`, `/api/icon-artwork` and
  `/api/icon-artwork/svg?variant=` call the graphics container for geometry, validation and rendering
  and store the documents in D1 (`store_documents`, same keys as the local gallery). They need each
  icon's generated geometry in D1 `icon_graphs`, which every catalog push writes. A pick updates the
  icon's row, drawing and approval at once; because the built `icons.json` in R2 does not change, the
  gallery applies `/api/icon-artwork/overrides` after loading it (the next catalog push bakes them in).
  Uploaded icons' Manual Edit and Pick still run on a local gallery (`501 {"local": true}`).
* Routes that need Python rendering or local files answer `501 {"local": true}` in the cloud and
  run in `deploy.py --cloud-api`: `/api/qa-evidence*`, `/api/combinations/container/*`, the two generation queues, the
  pending-brief zip. Development-only routes stay `403` as in production.
* Side and container pairs are built in the browser and stored through `/api/combinations/*`
  (ARCHITECTURE.md, "Combinations"); the local gallery's own side-layout routes stay local.
* `/api/side-components` serves the pushed `side-components.json`; the local gallery re-pushes it,
  with each drawing's current status, together with `icons.json` after an artwork change.
* Workers' uploaded fixes (`/api/work/fixes`) are shown by `/api/icon-artwork/svg` straight from D1;
  the `artwork_source: work_fix` labels in `icons.json` appear when the local gallery next pushes it.
* `/api/primitives/categories` needs the SQLite mirror views and is not served by the cloud.
* Uploads get the static SVG safety checks in the cloud; the optional "visible artwork" render
  check and holes/pinches validation need rendering, so choose bypass or upload through a local gallery.
* `/api/feedback-db/export|sync` and `/api/review-data/export` are gone: there is one database.
  Backups: D1 Time Travel (30 days) and `wrangler d1 export`.
* Timestamps written by the Worker have millisecond precision (Python: microseconds); they sort
  and compare the same way.
