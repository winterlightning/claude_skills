# Cloudflare architecture: what lives in D1 and R2, and how to merge the Mac mini into it

This is the reference for **what is stored where** in the Cloudflare deployment and the procedure for
**merging the data that is still on the Mac mini** (the machine that ran `deploy.py --production`,
the watcher and the generation jobs) into it.

Companion files: [`README.md`](README.md) (everyday use), [`MIGRATION.md`](MIGRATION.md) (the original
cutover runbook), [`data-model.html`](data-model.html) (the long-term data model),
[`worker/migrations/`](worker/migrations) (the exact D1 schema).

Numbers in this file were read from the live resources on **2026-09-28** (read-only queries).

---

## 1. Resources

| Thing | Name / id | Notes |
|---|---|---|
| Cloudflare account | `7a2ab07aab8b5b9a40885fa3546592fa` | also in `worker/wrangler.toml` |
| Worker | `pictographic-review` | Rust (workers-rs), code in `worker/app` + `worker/core`. URL `https://pictographic-review.pictographic.workers.dev` |
| D1 database | `pictographic-review`, id `1f671b1d-53c9-4083-8b3f-6cb77031bc36` | binding `DB`; 82.7 MB; schema = `worker/migrations/0001_schema.sql` + `0002_drawings_by_name.sql` |
| R2 bucket | `pictographic-review` | binding `FILES`; ~36.5k objects, ~0.8 GB |
| Worker secret | `PUSH_TOKEN` | guards the write-from-local-tools routes (section 4.3) |
| Worker vars | `ADMIN_USERS`, `BUILTIN_FAMILIES` | reviewer logins (5 users) and family → canvas size |
| Local secrets | `cloud/.env` (git-ignored) | `CLOUDFLARE_API_TOKEN`, `PICTOGRAPHIC_PUSH_TOKEN[_LOCAL]`, `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY` |

The account's older `pictographic` bucket and search Workers are separate and untouched.

## 2. The split: cloud stores, local computes

```
 reviewers (browser) ──┐                        ┌──► D1  pictographic-review
 work_queue.py /       ├──► Worker (Rust) ──────┤     all state: reviews, feedback, claims, activity,
 primitive_fix.py      │    same API as         │     catalog rows + every current drawing inline,
 (PICTOGRAPHIC_API)    │    deploy.py           │     uploads, primitive decisions, meaning layer
                       │                        └──► R2  pictographic-review
 deploy.py --cloud-api ┘                              files: gallery site, references, reference images
   └─ rendering, validation, stroke-edit geometry, artwork choice, QA, discard of Python
      sources, generation (Codex), builds — all stay on the local machine
```

* The Worker answers the same paths, JSON and errors as `icon_set/scripts/deploy.py`. Routes that need
  Python rendering or local files answer `501 {"local": true}` and are served by a local
  `deploy.py --cloud-api <worker>` instead (`/api/icon-artwork`, `/api/stroke-edits*`, `/api/qa-evidence*`,
  `/api/combinations/container/*`, the two generation queues, the pending-brief zip).
* **Combinations are built in the browser** (since the cloudflare-db merge, 2026-10-01): `combine.js`
  (container pairs) and `combine-side.js` + `normalize-ink32.js` (side pairs) are ports of the Python engines
  that give the same drawings (checked by `icon_set/tests/js`). `container-pairs.html` / `side-pairs.html` read
  `GET /api/combinations*` and post the drawing to `POST /api/combinations/build`; the Worker checks the parts
  and the SVG and stores it as the combined icon. A container build also carries its stroke graph
  (`svg-graph.js`, a port of `svg_graph.py`) into `icon_graphs`, so the geometry editor can select the
  container's and the symbol's strokes. The old routes (`container_pairs.rs`, `container_centers.rs`, `side.rs`,
  `side_pairs.rs`) and the graphics container's combination renders are gone.
* The **Python icon source** (`icon_set/model/icons/**`, `icon_set/metadata/**`) is **not** in the cloud.
  It lives in git. The cloud only holds what a build produced from it (catalog rows + SVG text).
  This matters for the merge: anything the Mac mini generated that exists only as Python on the mini
  must go through git and a build before the cloud can show it.

## 3. Identifiers that tie everything together

| Id | Example | Where used | Rules |
|---|---|---|---|
| **icon key** | `solo/about-me-logo`, `text/text-8k-…-94cd3ca3`, `solo/…-upload-289b77a645eb9952` | `icons.key`, `reviews.icon`, `feedback.icon`, `activity_log.icon`, `icon_types`, `icon_flags`, `work_results`, `split_requests`, store keys | `<family>/<icon_id>`. Stable across builds. Uploads contain `-upload-<16 hex>`. |
| **svg_sha256** | `61e5fd61…d74861` | `icons.svg_sha256` (current drawing), `revisions.svg_sha256`, `reviews`, `feedback`, `work_results`, `split_requests` | sha256 of the exact SVG text (text icons hash without the final newline). **A review belongs to one revision.** A rebuild that changes a drawing's bytes creates a new sha; the old review stays attached to the old sha. |
| **profile + icon_id** | `SOLO48` + `about-me-logo` | old folder URLs `/solo48/<id>.svg`, `/failed/sub32/<id>.svg` | Served from D1 (`icons` then `extra_drawings`), not from R2. |
| **reference UUID** | `5b795893-a150-4628-bb58-d92b32b39cdb` | `"references".reference_id`, `primitive_status.uuid`, `primitive_briefs.uuid`, `primitive_symbol_links.uuid`, `progression_imports.uuid`, activity icon `primitive:<uuid>` | The original source SVG's id from `pictographic-primitives/_manifest.csv` / `pictographic-combinations/_manifest.csv`. |
| **push_id** | `20260928T101812467000Z` | `icons.pushed_at` for built rows | The final chunk of a catalog push deletes every built row whose `pushed_at` differs (section 4.2). |
| **store key** | `solo/x` (artwork), `solo/x@<source sha>` (stroke edits) | `store_documents.key` | |
| **reference image id** | sha256 of the bytes | `reference_images.id`, R2 `stores/reference-images/<id>.<svg|png>`, `feedback.reference_images` JSON | content-addressed, so the same image merges to the same id everywhere |

Timestamps are ISO-8601 UTC strings with `+00:00`. Python writes microseconds
(`2026-09-24T05:28:22.284821+00:00`), the Worker writes milliseconds padded to six digits
(`2026-09-28T09:21:49.572000+00:00`). They compare correctly as strings, **except** Python's
`isoformat()` drops the fraction entirely when the microsecond is 0 — normalise before comparing when
a merge decides by "newer `updated_at` wins".

---

## 4. D1 in detail

Row counts are the live remote database on 2026-09-28.

### 4.1 Workflow tables (copied 1:1 from `feedback.sqlite3`)

These keep the **exact columns** of the Mac mini's `feedback.sqlite3`, so rows copy across unchanged
(`migrate/build_d1_import.py`). The Worker's SQL follows `deploy.py` statement for statement.

| Table | Rows | Primary / unique key | What a row is | Written by (Worker route) |
|---|---:|---|---|---|
| `reviews` | 17,986 | `(icon, svg_sha256)` | Review status of one revision: `ready`, `pending`, `re-generated`, `approve`, `rejected`, `claimed`, plus `updated_at/by`, and for the fix queue `worker`, `claimed_at`, `note`. Today: 10,685 approve · 5,293 pending · 1,280 ready · 728 rejected. | `/api/reviews`, `/api/feedback`, `/api/work/*`, `/api/reject-combination*`, upload |
| `feedback` | 1,602 (max id 1613) | `id` INTEGER | Reviewer text on a revision: `icon`, `svg_sha256`, `feedback`, `reason`, `reference_images` (JSON list of image ids), `author`, `edited_by/at`. **Deleted for the whole icon when it returns to Ready.** | `/api/feedback`, `/api/feedback/edit`, `/api/feedback/delete`, `/api/reviews` (ready clears) |
| `activity_log` | 25,077 (max id 25604) | `id` INTEGER | Append-only audit: `username`, `action` (`review`, `feedback`, `flag`, `work_claim`, `primitive_skip`, `discard`, `login`, …), `icon`, `details` JSON, `created_at`. Local tools rebuild primitive decision history from it (`GET /api/activity`, ordered by id). | every write route; `POST /api/activity` for local tools |
| `work_results` | 15 | `(icon, svg_sha256, stage)` | Fix-queue evidence: the `before` / `after` SVG, `python_path`, full `python_source`, `validation` JSON, `worker`, `note`, `saved_at`. | `/api/work/result` |
| `icon_types` | 2,912 | `icon` | Manual type label (`avatar`, `uploaded`, …). | `/api/icon-type`, upload |
| `icon_flags` | 285 | `icon` | One flag: `container_combination`, `combination`, `text`, `number`, `other`, `exception`. Unflag = row deleted. | `/api/icon-flag` |
| `split_requests` | 1 | `id`; unique `(icon, svg_sha256)` | "Reject as combination": `combination_type`, `reason`, `reference_path`, `active`, restore info. | `/api/reject-combination`, `/restore` |
| `pending_briefs` | 2 | `id`; unique `(split_id, position)` → `split_requests.id` | Component briefs produced by a split: `name`, `family`, `description`, `status`, `generated_icon`. | `/api/reject-combination`, `/api/pending-briefs/complete` |
| `upload_families` | 4 | `id` | Custom families for uploads (`icon-72` …) with `canvas_size`. | `/api/icon-families` |
| `uploaded_icons` | 2,900 | `icon` | A hand-uploaded SVG: `record` (full gallery record JSON incl. validation) + `svg`. Also mirrored into `icons` (`uploaded = 1`) and `revisions` (`origin = 'upload'`). | `/api/icons/upload` |
| `primitive_status` | 2,272 | `uuid` | A reference marked **skip** with `reason` (`combination`, `container`, `text_number`, `other`), `note`, and for combinations `combination_brief`, `main_brief`, `sub_brief`, `sub_position`. "Todo" = row deleted. | `/api/primitives/status` |
| `primitive_briefs` | 1 | `uuid` | Authoring brief for a reference: `family`, `brief`. | `/api/primitives/briefs` |
| `primitive_symbol_links` | 0 | `uuid` | Reference → existing symbol icon key. | `/api/primitives/symbol-link` |
| `progression_imports` | 2,236 | `uuid` | Which progression references were imported (historic). | import only |
| `progression_reviews` | 125 | `path` | Historic review JSON by file path. | import only |
| `review_data_migrations` | 1 | `id` | Data migrations already applied. | import only |
| `admin_sessions` | 1 | `token` (sha256 of cookie) | Reviewer sign-in sessions, 12 h. **Never merge** — sessions are per server. | `/api/auth/login|logout` |

### 4.2 Catalog tables (pushed by local builds)

The catalog is what the gallery shows: every built icon, every failed build, every upload. It is
computed locally (`python3 -m icon_set publish` → `published/gallery/icons.json`, plus saved artwork
choices applied by a running `deploy.py`) and pushed with `migrate/push_catalog.py`.

| Table | Rows | Key | What a row is |
|---|---:|---|---|
| `icons` | 17,778 | `key` | One catalog icon. Columns the routes check: `icon_id`, `name`, `family`, `category`, `profile`, `canvas_size`, **`svg_sha256` (current revision)**, `python_source` (JSON `{path, family, class_name}` → the module under `icon_set/model/icons/`), `preview_url`, `original_sources` (JSON; contains the reference UUID / `originals/<sha>.svg`), `variant_of/root/label`, `build_failed`, `uploaded`, `record` (full JSON; only filled for uploads), `pushed_at` (= push_id). Today: 13,985 built · 893 failed builds · 2,900 uploads. |
| `revisions` | 18,202 | `svg_sha256` | **Every drawing ever pushed**, inline SVG text (~450 B each), `icon` key, `origin` (`build` 15,090 · `upload` 2,882 · `extra` 230), `created_at`. Insert-only (`INSERT OR IGNORE`), never updated, never deleted by a push. |
| `extra_drawings` | 607 | `(profile, icon_id, failed)` | Drawings the review pages still link that are not the icon row's drawing: failed-build leftovers and the other sizes of multi-profile text icons (TEXT28/TEXT32 under one key). **Replaced as a whole** by each push that carries them. |
| `catalog_pushes` | 3 | `id` | One row per completed push: `details.icons_json` = `{tail, count}` layout of R2 `site/gallery/icons.json`, and a report (`icons`, `failed_icons`, `missing_svg`, `sha_mismatch`, `source`). The newest row decides how the Worker splices uploads into `icons.json`. |

Push semantics (`POST /api/catalog/push`, `worker/app/src/routes/internal.rs`):

1. Chunks of 250 rows upsert `icons` (`ON CONFLICT(key) … WHERE icons.uploaded = 0` — a push never
   overwrites an upload) and `INSERT OR IGNORE` the drawing into `revisions`.
2. Before the final chunk, `push_catalog.py` uploads `site/gallery/icons.json` (uploads removed,
   `icons` array last so the file ends in `]}`), `primitives.json`, `combinations.json` to R2.
3. The final chunk **deletes every built icon row not in this push** (`DELETE FROM icons WHERE uploaded = 0 AND pushed_at != <push_id>`),
   replaces `extra_drawings`, and inserts the `catalog_pushes` row.

> **A push is a full replacement of the built catalog.** Pushing a partial or older build deletes
> the missing icons from the gallery (their reviews and revisions stay, but nothing shows them).
> Always push from a build of the merged code.

The `icons` column `key` is unique while `icons.json` can list a key more than once (text icons at
several profiles): the last one wins the row, the others become `extra_drawings`. That is why the
last push reported 14,211 built records but D1 holds 13,985 built rows.

### 4.3 Stores (were folders beside `feedback.sqlite3`)

| Table | Rows | Key | Content |
|---|---:|---|---|
| `store_documents` | **0** | `(store, key)` | `store = 'icon-artwork'`: artwork choice per icon (key = icon key; was `state/icon-artwork/<hash>/artwork.json`). `store = 'stroke-edits'`: stroke-edit document per `<icon>@<source svg sha>` (was `state/stroke-edits/<hash>/<hash>.json`). Opaque JSON — only local Python reads it. Writes can pass `expected_revision` (optimistic lock; 409 on a lost race). |
| `reference_images` | **0** | `id` (content sha) | Metadata of reviewer-uploaded reference images: `name`, `mime`, `size`, `r2_key` (→ R2 `stores/reference-images/<id>.<ext>`), `uploaded_by/at`. |

**Both are empty today: the Mac mini's state folders have not been pushed yet** (section 7).

Routes that write here (`/api/store/*`, `/api/files/*`, `/api/catalog/push`, `/api/icons/discard-record`,
`POST /api/activity`) require `Authorization: Bearer $PUSH_TOKEN`. `/api/reference-images` is a
normal reviewer route.

### 4.4 Meaning layer (seeded, curated later)

Seeded by `migrate/seed_reference.py` from the repo's reference data; read by the reference-copy
routes today, and the base for search/releases later (see `data-model.html`).

| Table | Rows | Content / source |
|---|---:|---|
| `"references"` | 24,042 | Every original SVG: `reference_id` (UUID, or `library:<path>` for `icon_set/references`), `kind` (`single`/`combination`), `concept`, `old_concept`, `categories`, `folder`, `file`, **`r2_key`** (`references/primitives/…`, `references/combinations/…`, `references/library/…`), `source`, `license`, `sha256` (`<sha>.svg`, used to serve `gallery/originals/<sha>.svg`), `concept_id`, `physical_id`. |
| `reference_parts` | 12,477 | Combination → parts (`main`/`sub` with `tl|tr|bl|br`, or `container`/`symbol` at `center`) from `combination_data.json`. Since migrations 0009_combination_parts/0011 also each part's `icon`, `layout` (boxes on the 64 grid), `built_sha`, `form` and `updated_at/by`: the one set of combination tables (`backfill_combinations.py` fills them from the old stores). A combined side icon cannot be approved while a part is not; a combined container icon can. |
| `concepts` | 13,240 | From `concepts_streamline.json`. |
| `categories` | 866 | The `(parent) - (child)` tree of `concepts_streamline.json`. |
| `concept_categories`, `concept_aliases`, `concept_physicals` | — | Links (aliases not seeded yet). |
| `physicals` | 9,392 | **Candidates** from `main_icon`/`sub_icon` names (numbered sets folded); `status = 'candidate'` until reviewed. |
| `physical_parts` | — | Composite physicals (not seeded yet). |
| `icon_references` | 14,591 | Authored icon key → reference UUID it was drawn from (from `original_sources`). |

The meaning layer is derived from files in git, not from the Mac mini's database — regenerate it
with `seed_reference.py` after the merge rather than merging it.

---

## 5. R2 in detail

Bucket `pictographic-review`, live contents:

| Prefix | Objects | Size | Source (local path) | Served at |
|---|---:|---:|---|---|
| `references/primitives/` | 14,278 | 233 MB | `pictographic-primitives/` (original single SVGs + manifests) | `/primitives/<path>`; `gallery/originals/<sha>.svg` via `"references".sha256` |
| `references/combinations/` | 6,241 | 383 MB | `pictographic-combinations/` | `gallery/combination-originals/<reference id>.svg` via `"references".reference_id` |
| `references/library/` | 3,599 | 4.7 MB | `icon_set/references/` (Lucide + human library) | via `"references".sha256` |
| `site/gallery/` | 12,113 | 166 MB | `published/gallery/` — HTML/CSS/JS pages and `sub-profiles/`, `sub-usage/`, `combination-previews/`, `combination-sub32/`, `ai-review-data/`, … | `/gallery/<path>` |
| `site/gallery/icons.json` | 1 | ~67 MB | written by `push_catalog.py` (uploads stripped) | `/gallery/icons.json`, with D1 `uploaded_icons.record` spliced in before the closing `]}` |
| `site/gallery/primitives.json`, `combinations.json` | 2 | | written by `push_catalog.py` | as is |
| `site/<profile>/manifest.json`, `site/failed/<profile>/manifest.json` | 13 | ~57 MB (solo48 is 49.7 MB) | `published/<profile>/manifest.json` | as is |
| `stores/reference-images/` | **0** | | Mac mini `state/reference-images/` | `/api/reference-images?id=` |

Not in R2 on purpose:

* **Per-icon SVGs** (`published/solo48/*.svg`, `sub32/`, `failed/…`): answered from D1 by
  `(profile, icon_id, build_failed)` so the image and the review status always name the same revision.
* `published/previews-png/`, `compositions/`, `reports/`, `text-native-v2/`, `release.json`: not needed by
  the review pages (only `.html .json .svg .png .css .js` under the mapped folders were sent).

`push_files.py --backend s3 SRC=PREFIX` skips objects whose MD5 already matches, so it is safe to
rerun with the Mac mini's folders — only new or changed files are sent. The Worker's `PUT /api/files/<key>`
only accepts keys under `site/`, `references/`, `stores/`.

---

## 6. What stays local (never in the cloud)

| Local data | Mac mini path (production) | Why |
|---|---|---|
| Python icon modules and metadata | release workspaces under `/srv/pictographic/releases/…` and any dev checkout: `icon_set/model/icons/**`, `icon_set/metadata/**` | source of truth is **git**; the cloud gets build output |
| `generation-jobs/<32-hex id>/` (`job.json`, `prompt.txt`, candidate workspace) | `/srv/pictographic/state/generation-jobs/` | Codex candidates; only an explicit **accept** writes a module into `icon_set/model/icons/<family>/` |
| `ai-feedback-jobs/` | `…/state/ai-feedback-jobs/` | AI review runs, recomputable |
| `qa-evidence/` | `…/state/qa-evidence/` | rendered QA evidence, recomputable |
| `discarded-icons/` | `…/state/discarded-icons/` | archive of discarded Python sources |
| `published/` build | release `dist` | rebuilt from git; pushed with `push_catalog.py` + `push_files.py` |

Optional: archive these folders to R2 for safekeeping with `push_files.py --backend s3` under a
`stores/archive/mac-mini-<date>/…` prefix — nothing reads them there.

---

## 7. Current state and what must be merged

**Where the cloud's data came from.** The workflow tables were imported from the repo's copy of
`feedback.sqlite3` on this laptop (file time 2026-09-24 13:54 +07; newest activity id 25579 at
`2026-09-24T05:28:22Z`; newest review `2026-09-24T04:38:22Z`), **not** from a fresh snapshot of the Mac
mini's `/srv/pictographic/state/feedback.sqlite3`. The catalog was pushed from this laptop's
`published/` (push 3, 2026-09-28 10:18 UTC). The store folders were never pushed.

**Everything written in the cloud since the import is test data.** Activity ids 25580–25604
(2026-09-28 09:20–09:21 UTC) are the 56-step parity write scenario run against production D1 plus two
logins by `ray`. It left these rows changed:

| Table | Row | Test value |
|---|---|---|
| `reviews` | `solo/about-me-logo` @ `61e5fd61…` | `ready` by ray (reject-combination + restore) |
| `reviews` | `solo/active-sporting-figure` @ `1cf3bf52…` | `ready` by ray |
| `reviews` | `solo/bernese-mountain-dog-face` @ `f04740d8…` | `ready`, worker `parity-worker` |
| `icon_types` | `solo/about-me-logo` | `avatar` |
| `work_results` | `solo/bernese-mountain-dog-face` / `before` | worker `parity-worker` |
| `primitive_briefs` | `5b795893-a150-4628-bb58-d92b32b39cdb` | a test brief |
| `split_requests` / `pending_briefs` | id 1 / 2 rows for `solo/about-me-logo` | inactive test split |
| `feedback` | rows of `solo/about-me-logo`, `solo/active-sporting-figure` | deleted when they went to Ready |
| `activity_log` | ids 25580–25604 | test actions |

So the cloud has **no real reviewer work yet**. Check before merging that this is still true:

```bash
cd cloud/worker && set -a && . ../.env && set +a
wrangler d1 execute pictographic-review --remote --command \
  "SELECT id, username, action, icon, created_at FROM activity_log WHERE id > 25604 ORDER BY id"
```

**What the Mac mini has that the cloud does not:**

1. Every review, feedback, claim, flag, type, primitive decision and upload made on production after
   the laptop copy was taken (after ~2026-09-24 05:28 UTC), and anything the laptop copy never had.
2. `state/icon-artwork/`, `state/stroke-edits/`, `state/reference-images/` (cloud stores are empty).
3. Icons generated or fixed on the mini that exist only as Python in its checkouts (not yet in git),
   and possibly reference files added to `pictographic-primitives/` / `pictographic-combinations/` there.
4. Local-only archives (section 6).

---

## 8. Merge procedure

Two paths. **Use A while the check above returns no rows** — the Mac mini is the authority for all
real workflow data and the cloud only holds test residue, so replacing is exact and needs no conflict
rules. Use B only if reviewers or agents have started working in the cloud before the merge.

### 8.0 Prepare (both paths)

1. **Freeze the mini.** Stop `watch_deploy.py` and `deploy.py`; stop agents whose `PICTOGRAPHIC_API`
   points at the tunnel. Finish or abandon open claims first (a claim leases for 6 h;
   `work_queue.py queue` on the mini shows the queue). From here on the mini's database must not change.
2. **Save the generated code.** In every checkout on the mini (dev checkout and the newest release
   workspace), `git status` under `icon_set/model/icons/`, `icon_set/metadata/`, `icon_set/typeface/`,
   `pictographic-primitives/`, `pictographic-combinations/`. Commit what is not in git on a branch,
   push, and merge it into the branch the cloud builds from. Accepted generation jobs are already
   modules; `generation-jobs/*/job.json` with `status: done` but not accepted are candidates only —
   accept them locally first if they should become icons.
3. **Snapshot the mini's database read-only** (never open the original for writing):
   ```bash
   python3 cloud/migrate/export_snapshot.py --database /srv/pictographic/state/feedback.sqlite3 \
       --out cloud/exports/mini-<date>.sqlite3
   ```
   Copy the snapshot and the three store folders to the machine that runs the merge:
   `state/icon-artwork/`, `state/stroke-edits/`, `state/reference-images/`.
4. **Keep the merge base.** Snapshot the laptop's `feedback.sqlite3` too
   (`--out cloud/exports/base-20260924.sqlite3`); path B needs it, and it proves which rows the cloud
   started from.
5. **Sanity check lineage:** the base's `activity_log` ids 1–25579 should be identical (username,
   action, icon, created_at) in the mini snapshot. If they are not, the laptop copy was not taken from
   the mini and every table needs path B's full comparison.
6. **Bookmark D1** so any step can be undone:
   ```bash
   cd cloud/worker && wrangler d1 time-travel info pictographic-review      # note the bookmark
   # undo: wrangler d1 time-travel restore pictographic-review --bookmark <bookmark>
   ```
   and take a plain export as well: `wrangler d1 export pictographic-review --remote --output ../exports/before-merge.sql`.

### 8.A Replace workflow data with the mini's (recommended now)

1. Build the import from the mini snapshot:
   ```bash
   python3 cloud/migrate/build_d1_import.py cloud/exports/mini-<date>.sqlite3 --out cloud/exports/mini.sql
   ```
   It emits plain `INSERT`s for the 17 workflow tables plus `icons` (uploads) and `revisions`
   (`origin = 'upload'`). Upload drawings may already be in `revisions`, so make those idempotent:
   ```bash
   sed -i '' 's/^INSERT INTO "revisions"/INSERT OR IGNORE INTO "revisions"/' cloud/exports/mini.sql
   ```
2. Empty the workflow tables and the upload rows (test residue included). Built catalog rows,
   revisions, extra drawings and the meaning layer stay:
   ```sql
   -- cloud/exports/clear-workflow.sql
   DELETE FROM pending_briefs;  DELETE FROM split_requests;
   DELETE FROM reviews;         DELETE FROM feedback;        DELETE FROM activity_log;
   DELETE FROM work_results;    DELETE FROM icon_types;      DELETE FROM icon_flags;
   DELETE FROM upload_families; DELETE FROM uploaded_icons;  DELETE FROM icons WHERE uploaded = 1;
   DELETE FROM primitive_status; DELETE FROM primitive_briefs; DELETE FROM primitive_symbol_links;
   DELETE FROM progression_imports; DELETE FROM progression_reviews; DELETE FROM review_data_migrations;
   DELETE FROM admin_sessions;
   ```
   ```bash
   cd cloud/worker
   wrangler d1 execute pictographic-review --remote --file ../exports/clear-workflow.sql
   wrangler d1 execute pictographic-review --remote --file ../exports/mini.sql
   ```
   Ids (`feedback.id`, `activity_log.id`, `split_requests.id`) come from the mini unchanged, so
   `pending_briefs.split_id` and history order stay correct.
3. Stores:
   ```bash
   python3 cloud/migrate/push_stores.py --state <copied mini state folder> \
       --base-url https://pictographic-review.pictographic.workers.dev
   ```
   Artwork choices keep their `revision` numbers; reference images come back with the same content-hash
   id (the script stops if not), so `feedback.reference_images` keeps resolving.
4. References (only if the mini had files the laptop did not; unchanged files are skipped):
   ```bash
   python3 cloud/migrate/push_files.py --backend s3 \
       pictographic-primitives=references/primitives pictographic-combinations=references/combinations \
       icon_set/references=references/library
   python3 cloud/migrate/seed_reference.py        # then re-run the seed if manifests changed (see 8.C)
   ```
5. Catalog from the merged code — continue with 8.C.

### 8.B Three-way merge (only if the cloud has real work)

Three sides: **base** = `base-20260924.sqlite3` (what the cloud was imported from), **mini** = the
mini snapshot, **cloud** = `wrangler d1 export` of the live database loaded into a local SQLite file
(`sqlite3 cloud/exports/cloud-now.sqlite3 < cloud/exports/cloud-now.sql`). Compute every decision
locally from these three files (`ATTACH` them in one SQLite session), write the result as SQL, then run
it against D1 once. First delete the test residue listed in section 7 from the cloud side so it is not
mistaken for real work.

For each row, compare mini with base: *added* (not in base), *changed* (in base, different),
*deleted* (in base, missing in mini). Then:

| Table | Match rows by | Mini added | Mini changed | Mini deleted |
|---|---|---|---|---|
| `reviews` | `(icon, svg_sha256)` | insert; if the cloud also has it, newer `updated_at` wins | newer `updated_at` wins; a `claimed` row only if its lease (6 h) is still live, else as `pending` with `worker`/`claimed_at` cleared | rare (discard); follow the `discard` entry in activity |
| `feedback` | `(icon, svg_sha256, author, created_at)` — **not** `id` | insert **without** `id` (D1 assigns a new one) — unless the icon's merged review went to `ready` after `created_at` (Ready resolves feedback) | edited text: newer `edited_at` wins | delete in cloud if the cloud row is unchanged from base |
| `activity_log` | `(username, action, icon, created_at, details)` | insert without `id`, in `created_at` order | — (append-only) | — |
| `work_results` | `(icon, svg_sha256, stage)` | insert | newer `saved_at` wins | — |
| `icon_types`, `icon_flags` | `icon` | insert; newer `updated_at` wins | newer `updated_at` wins | unflag: delete if cloud row unchanged from base |
| `primitive_status`, `primitive_briefs`, `primitive_symbol_links` | `uuid` | insert; newer `updated_at` wins | newer `updated_at` wins | "todo"/unlink: delete if cloud row unchanged from base |
| `split_requests` | `(icon, svg_sha256)` | insert without `id`; then insert its `pending_briefs` with the **new** `split_id` | newer of `created_at` / `restored_at` wins; replace its briefs with the winner's | — |
| `pending_briefs` | `(split, position)` | with its split | newer `completed_at` wins | with its split |
| `upload_families` | `id` | insert or ignore | — | — |
| `uploaded_icons` | `icon` | insert, **plus** the rows the upload route writes: `icons` (`uploaded = 1`), `revisions` (`origin 'upload'`, `INSERT OR IGNORE`), `reviews` (`ready`), `icon_types` (`uploaded`) — copy them from the mini's rows | — (immutable) | — |
| `progression_*`, `review_data_migrations` | primary key | insert or ignore | — | — |
| `admin_sessions` | — | skip | skip | skip |

Conflicts (both sides changed the same row differently) go to a report for a human; the default above
is "newer timestamp wins". When both sides changed a review of the same icon, look at the activity
entries around it before accepting the default.

Useful SQL shapes for D1 (SQLite; UPSERT is supported):

```sql
-- newer wins for keyed tables
INSERT INTO reviews(icon, svg_sha256, status, updated_at, updated_by, worker, claimed_at, note)
VALUES (...)
ON CONFLICT(icon, svg_sha256) DO UPDATE SET status = excluded.status, updated_at = excluded.updated_at,
  updated_by = excluded.updated_by, worker = excluded.worker, claimed_at = excluded.claimed_at, note = excluded.note
WHERE excluded.updated_at > reviews.updated_at;

-- append without id, skipping rows already present
INSERT INTO activity_log(username, action, icon, details, created_at)
SELECT 'hina', 'review', 'solo/x', '{...}', '2026-09-25T01:02:03.000000+00:00'
WHERE NOT EXISTS (SELECT 1 FROM activity_log WHERE username = 'hina' AND action = 'review'
                  AND icon IS 'solo/x' AND created_at = '2026-09-25T01:02:03.000000+00:00');
```

Keep every statement under 100 KB (reuse `inserts()` from `build_d1_import.py`, which splits
large rows). Then do the stores (8.A step 3) — with a non-empty cloud store, use `expected_revision`
or compare `revision` fields and keep the higher one — and continue with 8.C.

### 8.C Catalog, images and meaning layer from the merged code

The catalog must be built from code that contains **both** the mini's generated/fixed modules and
everything committed elsewhere, because a push replaces the whole built catalog (section 4.2).

1. On one machine, check out the merged branch and build:
   `python3 -m icon_set publish` (writes `published/`).
2. Check that approvals survive: for icons reviewed on the mini, the rebuilt `svg_sha256` should equal
   the sha in `reviews`. A different sha means the drawing's bytes changed (different code or renderer
   than the mini used) and the icon will show as not yet reviewed on the new revision. Spot-check:
   ```bash
   python3 - <<'EOF'
   import json, sqlite3
   c = json.load(open('published/gallery/icons.json'))
   current = {r['key']: r['svg_sha256'] for r in c['icons'] + c.get('failed_icons', [])}
   db = sqlite3.connect('file:cloud/exports/mini-<date>.sqlite3?mode=ro', uri=True)
   approved = db.execute("SELECT icon, svg_sha256 FROM reviews WHERE status='approve'").fetchall()
   moved = [(k, s) for k, s in approved if k in current and current[k] != s]
   print(len(approved), 'approved;', len(moved), 'now build a different drawing')
   EOF
   ```
3. Push with artwork choices applied. Run a local gallery against the cloud (the stores are there
   after 8.A step 3) and push from it:
   ```bash
   python3 icon_set/scripts/deploy.py --cloud-api https://pictographic-review.pictographic.workers.dev --port 8000 &
   python3 cloud/migrate/push_catalog.py --base-url https://pictographic-review.pictographic.workers.dev \
       --from-server http://127.0.0.1:8000
   python3 cloud/migrate/push_files.py --backend s3 published=site
   ```
   Read the push report: `missing_svg` and `sha_mismatch` must be 0; `removed` is how many built icons
   disappeared — it should match icons intentionally discarded.
4. If reference manifests or `concepts_streamline.json` / `combination_data.json` changed, regenerate
   the meaning layer: empty the meaning tables (`icon_references`, `reference_parts`, `"references"`,
   `concept_physicals`, `concept_categories`, `concept_aliases`, `physical_parts`, `physicals`,
   `concepts`, `categories`, children first), then run `python3 cloud/migrate/seed_reference.py` and
   `wrangler d1 execute pictographic-review --remote --file ../exports/seed-reference.sql`.

### 8.D Verify

1. **Counts:** `build_d1_import.py` wrote `mini.counts.json`; compare with
   `SELECT count(*)` per table in D1 (path A: equal; path B: mini + cloud-only − deletions).
2. **Routes:** run the old server read-only on a *copy* of the mini snapshot with the merged build and
   compare every read route:
   ```bash
   cp cloud/exports/mini-<date>.sqlite3 /tmp/parity/feedback.sqlite3
   python3 icon_set/scripts/deploy.py --production --dist published --database /tmp/parity/feedback.sqlite3 --port 8799 &
   python3 cloud/migrate/verify.py --old http://127.0.0.1:8799 --new https://pictographic-review.pictographic.workers.dev
   ```
   (Path A should be identical; path B differs exactly where cloud-only work was kept.)
3. **Spot checks in the browser:** the review queue counts on the home page, one icon with feedback and
   a reference image, one upload, one artwork choice, one stroke-edited icon, the fix queue
   (`python3 icon_set/scripts/work_queue.py queue --limit 5`, which lists without claiming).
4. **Test residue is gone:** no `parity-worker` in `reviews.worker`, `work_results.worker` or
   `activity_log.username`.

### 8.E Switch over

Reviewers use the Worker URL; every worker machine sets
`PICTOGRAPHIC_API=https://pictographic-review.pictographic.workers.dev`; local galleries run
`deploy.py --cloud-api …`. Keep the Mac mini's `state/` folder and database untouched as the rollback
copy until the cloud has run cleanly for a while. Backups from here on: D1 Time Travel (30 days) and a
periodic `wrangler d1 export` stored in R2.

---

## 9. Pitfalls checklist

* **Never write to the mini's `feedback.sqlite3`.** Open it with `-readonly` / `?mode=ro`; work on snapshots.
* **A catalog push deletes what it does not contain.** Push only from a full build of merged code.
* **Reviews follow the SVG bytes, not the icon.** Rebuilding with different code can "un-review" icons.
* **`feedback` and `activity_log` ids collide** between the mini and the cloud past id 25579 / 1613
  — merge those by natural key, never by id (path B).
* **Ready deletes feedback** for the whole icon; re-adding old feedback can reopen resolved requests.
* **Deletions leave no row** (unflag, primitive todo, feedback delete, discard) — detect them against
  the base or from `activity_log`.
* **Uploads live in four tables** (`uploaded_icons`, `icons`, `revisions`, `reviews` + `icon_types`) —
  merge them together.
* **Sessions don't merge**; reviewers sign in again.
* **D1 limits:** statements under 100 KB (the scripts split them); run large imports with
  `wrangler d1 execute --file`.
