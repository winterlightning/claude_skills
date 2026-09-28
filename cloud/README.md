# Pictographic on Cloudflare

The review server's data and status move from `feedback.sqlite3` on one Mac mini to Cloudflare.
**The cloud stores data and marks status; all graphics processing stays on local machines.**

| Where | What |
|---|---|
| **D1** (database `pictographic-review`) | reviews, feedback, work claims, activity log, uploads, icon types/flags, primitive decisions and briefs, split briefs, sign-in sessions, the effective catalog (one row per icon) and every authored drawing (SVGs are ~450 bytes, stored inline) |
| **R2** (bucket `pictographic-review`) | files that never change or are large: the built gallery site (`site/`), reference SVGs (`references/`), uploaded reference images (`stores/reference-images/`), `icons.json` / `primitives.json` / `combinations.json` |
| **Worker** (`worker/`, Rust) | the same HTTP API as `icon_set/scripts/deploy.py`: same paths, JSON and errors |
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

* Routes that need Python rendering or local files answer `501 {"local": true}` in the cloud and
  run in `deploy.py --cloud-api`: `/api/icon-artwork` (JSON and save), `/api/stroke-edits*`,
  `/api/qa-evidence*`, `/api/combinations/container/*`, the two generation queues, the
  pending-brief zip. Development-only routes stay `403` as in production.
* Side-pair layouts (`/api/combinations/side/layout*`, `/recombine`, `/preview`) render, so they also
  answer `501 {"local": true}`; a local gallery keeps its layouts beside its state directory and
  republishes the combined previews (push them with `push_files.py`). In the cloud,
  `/api/combinations/side/layouts` is always `{}`.
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
