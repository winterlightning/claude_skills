# Migration runbook: Mac mini → Cloudflare

Every step reads the source data and writes only copies. The Mac mini's database and folders
stay untouched until you decide to retire them, so rollback is always "point back to the Mac mini".

Commands run from the repo root unless noted; wrangler reads `CLOUDFLARE_API_TOKEN` from the
environment (`set -a; . cloud/.env; set +a`).

## What moves where

| Source (today) | Size | Destination |
|---|---|---|
| `feedback.sqlite3`: reviews, feedback, activity_log, work_results, icon_types, icon_flags, split_requests, pending_briefs, upload_families, uploaded_icons, primitive_status/briefs/symbol_links, progression_*, admin_sessions | 25 MB, 17 tables | D1, same tables and columns (`build_d1_import.py`) |
| `uploaded_icons` (2,900 SVG uploads) | 1.4 MB | D1 `uploaded_icons` + catalog rows in `icons`/`revisions` |
| `published/gallery/icons.json` (14,211 built + 893 failed) | 67 MB | D1 `icons` + `revisions` (drawings inline) and R2 `site/gallery/icons.json` (`push_catalog.py`) |
| `published/` (gallery site, family folders, previews) | ~78k files, 1 GB | R2 `site/` (`push_files.py`) |
| `pictographic-primitives/` | 14,204 SVGs, 221 MB | R2 `references/primitives/` (served at `/primitives/...`) |
| `pictographic-combinations/` | 6,240 SVGs, 364 MB | R2 `references/combinations/` |
| `icon_set/references/` | 3,601 files, 15 MB | R2 `references/library/` |
| state folder `reference-images/` | small | R2 `stores/reference-images/` + D1 `reference_images` |
| state folders `icon-artwork/`, `stroke-edits/` | small | D1 `store_documents` |
| state folders `qa-evidence/`, `generation-jobs/`, `ai-feedback-jobs/`, `discarded-icons/` | local work output | stay local (recomputable / archives) |
| `concepts_streamline.json`, manifests, `combination_data.json`, `icon_set/metadata/` | ~30 MB | D1 meaning layer (`concepts`, `physicals`, `references`, …) — seeded after cutover, curated later |

## 0. One-time setup (needs confirmation: creates cloud resources)

```bash
cd cloud/worker
wrangler d1 create pictographic-review            # copy the database_id into wrangler.toml
wrangler r2 bucket create pictographic-review
wrangler d1 migrations apply pictographic-review --remote
python3 -c "import secrets;print(secrets.token_urlsafe(32))"        # new push token
wrangler secret put PUSH_TOKEN                                       # paste it
echo "PICTOGRAPHIC_PUSH_TOKEN=<same token>" >> ../.env
wrangler deploy                                                      # prints the workers.dev URL
```

Create an R2 API token (dashboard → R2 → Manage API tokens, Object Read & Write on
`pictographic-review`) and add `R2_ACCESS_KEY_ID` / `R2_SECRET_ACCESS_KEY` to `cloud/.env`.

## 1. Rehearsal on this machine (done, repeatable)

Uses the repo's copy of `feedback.sqlite3`; see README "Develop and test". Results on 2026-09-25:
all 17 tables imported (activity_log 25,052 rows: one more than `count(*)` on the source, whose
`activity_log_icon`/`activity_log_user` indexes are missing row 25052 — the import reads the
table itself, so the cloud copy is complete); 272/272 read routes identical to deploy.py; 56-step
write scenario identical; 8 concurrent claims → exactly one winner.

## 2. Files that never change (any time before cutover; safe to rerun)

```bash
python3 cloud/migrate/push_files.py --backend s3 \
    pictographic-primitives=references/primitives \
    pictographic-combinations=references/combinations \
    icon_set/references=references/library \
    published=site
```

Skips objects whose MD5 already matches, so an interrupted run just continues.

## 3. Cutover (needs confirmation: imports production data)

1. Announce a short pause; on the Mac mini stop the watcher and `deploy.py` (no more writes).
2. Snapshot production, read-only:
   ```bash
   python3 cloud/migrate/export_snapshot.py --database /srv/pictographic/state/feedback.sqlite3 \
       --out cloud/exports/production.sqlite3
   python3 cloud/migrate/build_d1_import.py cloud/exports/production.sqlite3 --out cloud/exports/production.sql
   ```
3. Import into the (empty) remote database:
   `cd cloud/worker && wrangler d1 execute pictographic-review --remote --file ../exports/production.sql`
4. Stores (artwork choices, stroke edits, reference images), read-only from the state folder:
   `python3 cloud/migrate/push_stores.py --state /srv/pictographic/state --base-url <worker>`
5. Catalog with artwork choices applied: run the old server read-only on the snapshot copy and
   push from it: `python3 cloud/migrate/push_catalog.py --base-url <worker> --from-server http://127.0.0.1:8799`.
6. Verify: row counts (`build_d1_import.py` writes `production.counts.json`; compare with
   `wrangler d1 execute pictographic-review --remote --command "SELECT count(*) FROM ..."`) and
   `verify.py --old <old server on the copy> --new <worker>`: every route identical.
7. Switch: reviewers use the Worker URL; set `PICTOGRAPHIC_API=<worker>` on every worker machine;
   local galleries run `deploy.py --cloud-api <worker>`.

## 4. Rollback

The Mac mini's database and folders were only read. Restart its `deploy.py` and point
`PICTOGRAPHIC_API` back to the tunnel. (Writes made in the cloud after cutover would need a
reverse export: `wrangler d1 export pictographic-review --remote --output cloud-backup.sql`.)

## 5. After cutover

* Backups: D1 Time Travel restores any minute of the last 30 days; add a weekly
  `wrangler d1 export` to R2 for long-term copies.
* Seed the meaning layer (concepts, physicals, references) from the manifests — the six steps in
  `data-model.html` → "Organizing physicals".
* Later: publish released icons to R2 as static files so they are served without the Worker.
