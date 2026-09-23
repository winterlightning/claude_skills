# Work claims: fixing disapproved icons from many machines

Reviews, approvals and feedback live in **one database**: the production
`feedback.sqlite3` behind the always-on production gallery. Several machines and
AI agents repair disapproved icons at the same time. Work claims are how they
avoid fixing the same icon twice: before a machine touches an icon it **claims**
it on production, and when it finishes it **reports** there. Everything below
is served by the production `deploy.py`; a local `dev` server forwards these
routes to production, so the review grid on localhost shows the same state.

## One table, status based

A claim is not a separate record. It is the **review status** of an icon
revision (`icon` + `svg_sha256`, one row in `reviews`), plus three columns on
that row: `worker`, `claimed_at` and `note`.

| Review status (database) | Set by | Meaning | `work.state` | Claimable |
|---|---|---|---|---|
| `pending` (`disapprove` in the API) | reviewer | needs a fix, nobody on it | `open` | yes |
| `claimed`, `claimed_at` < 6 h ago | worker (`claim`) | a machine is fixing it | `working` | no |
| `claimed`, `claimed_at` ≥ 6 h ago | the clock | the machine went quiet | `expired` | yes |
| `ready` with a `worker` | worker (`done`) | fixed, waiting for the reviewer; feedback kept | `done` | no |
| `cannot-fix` | worker (`cannot-fix`) | gave up, `note` says why | `cannot-fix` | no |
| `ready` / `approve` / `rejected`, no worker | reviewer or build | nothing to fix | `none` | no |

Rules that follow from the table:

- **Claim** is one conditional update: `status = 'claimed'` with your worker
  name and `claimed_at = now`, applied only where the row is `pending` or an
  expired `claimed`. If no row changed, someone else won a moment earlier and
  the call is refused with `409`. Two machines can never both hold an icon.
- **Expiry needs no heartbeat.** The lease is `claimed_at` + `LEASE_HOURS`
  (six hours, `work.expires_at` in the API). The queue treats an older claim as
  claimable; the takeover is logged as `work_expired`. Six hours covers a long
  fix plus the production pull, so finish or abandon within that time.
- **Done** sets the row to `ready`, attributed to the worker, and keeps `worker`
  and `note` so the reviewer sees who fixed it. The disapproval feedback is
  deliberately kept so the fix can be compared against the request. (The
  gallery's manual Ready button clears feedback; `done` does not.)
- **Cannot fix** is its own status, so the icon stays out of the queue with its
  note until a reviewer or `abandon` sends it back.
- **Every reviewer decision clears the claim.** Setting Ready, Approved,
  Disapproved or Rejected from the gallery nulls `worker` and `claimed_at`, so
  disapproving a `done` or `cannot-fix` icon again puts it straight back in the
  queue as `open`. Adding more feedback to a `claimed` icon does **not** take it
  away from the worker.
- **A deployed fix changes the hash.** The new revision has no row and starts
  Ready, exactly as any new build does. The old row stays as history and is
  shown under **Revisions** in the Fix queue page.
- **Abandon** sets a `claimed` or `cannot-fix` row back to `pending`. Anyone
  may do it; the icon is `open` at once.
- **Results** are what a worker uploads to `work_results`: the drawing, module
  and validation `before` the fix (the first version) and `after` it. The Fix
  queue History panel shows Before / Fixed / Now from them; `history` lists
  them per revision under `results`. (The old claim-time snapshot table was
  folded into `before` results by the migration.)
- Every transition is appended to `activity_log`: `work_claim`, `work_done`
  (+ a `review` entry), `work_cannot_fix`, `work_abandon`, `work_expired`,
  `work_result`.

## Machine A and machine B

```
machine A: next  → queue lists X (open) → claim X → X is claimed (A, 6 h)
machine B: next  → queue skips X → claims Y instead
machine A: fixes X, publishes, done X → X is ready with worker A; feedback kept
machine B: next  → X is not listed (ready); claim X → 409 "Only disapproved icons can be claimed"
reviewer:  disapproves X again → worker cleared, X is open
machine B: next  → X is listed → claim X → claimed (B)
```

A crashed machine holds nothing forever: six hours after its claim the icon is
`expired` and the next `next` takes it.

## API

Step-by-step request and response examples for the whole workflow are in
[work-claims-api.md](work-claims-api.md).

Production serves these; `python3 -m icon_set dev` forwards them to its
`--sync-source` (default `$PICTOGRAPHIC_SYNC_SOURCE`, then the tunnel recorded
in `deploy.py`). No login is required; the `worker` string is stored on the
row and must match on `done`, `cannot-fix` and `result`.

| Route | Method | Body / query | Result |
|---|---|---|---|
| `/api/work/queue` | GET | `family`, `category`, `type`, `reason`, `limit` (1–500, default 50), `offset` | `{total, offset, next_offset, items}`; items are claimable icons (`open` or `expired`), oldest disapproval first, each with `key`, `svg_sha256`, `family`, `python_source`, `reason`, `feedback`, `disapproved_by`, `disapproved_at`, `original_sources`, `work` |
| `/api/work/disapproved` | GET | same filters as the queue | every icon whose status is `disapprove`, `claimed` or `cannot-fix`, with `status` and `work` (`open`, `working`, `expired`, `cannot-fix`) |
| `/api/work/review` | GET | `family`, `reason`, `state`, `status`, `limit`, `offset` | the disapproved list plus `done` icons awaiting review, newest work first, with `counts` per state and `work.results` |
| `/api/work/history` | GET | `icon` | the icon's revisions (review, claim, feedback and results per hash) and its full change log from `activity_log` |
| `/api/work/result` | POST | `icon`, `svg_sha256`, `worker`, `stage` (`before`/`after`), `svg`, optional `python_path`, `python_source`, `validation`, `note` | stores a fix result for the worker's own claim (`before` while working; `after` while working or after done / cannot-fix); each ≤ 512 KB; the SVG must be a clean 0 0 N N document for the icon's canvas |
| `/api/work/result` | GET | `icon`, `svg_sha256`, `stage`, `part` = `svg` (default), `python`, `validation` | the uploaded drawing (`image/svg+xml`) or text |
| `/api/work` | GET | optional `icon` | every current revision with a worker (`claims: [{icon, svg_sha256, state, worker, claimed_at, expires_at, note, status, current}]`), or one icon's `{status, svg_sha256, work}` |
| `/api/work/claim` | POST | `icon`, `svg_sha256`, `worker` | `201 {saved, work, item}`; `409` with the current `work` when taken or cannot-fix |
| `/api/work/claim` (batch) | POST | `worker`, `icons`: list of keys or `{icon, svg_sha256}` (max 500) | `200 {saved, worker, claimed: [item…], refused: [{icon, status, error, work}]}`; each icon succeeds or is refused on its own; a bare key uses production's current hash |
| `/api/work/done` | POST | `icon`, `svg_sha256`, `worker`, optional `note` | `200 {saved, status: "ready", work}` |
| `/api/work/cannot-fix` | POST | `icon`, `svg_sha256`, `worker`, required `note` | `200 {saved, work}` |
| `/api/work/abandon` | POST | `icon`, `svg_sha256`, `worker` | `200 {saved, work: {state: "open"}}` |

`svg_sha256` must be production's current hash for the icon; a mismatch is a
`409` carrying the current hash. If your local `published/` is ahead of
production, wait for the production pull. `GET /api/icon-types`,
`GET /api/review-detail` and `GET /api/reviews` report the same statuses
(`claimed` and `cannot-fix` included); the review grid files them under
**Disapproved** with a work badge.

```bash
API_BASE='https://<production>'
curl --fail-with-body "$API_BASE/api/work/queue?family=sub&limit=5"
curl --fail-with-body -H 'Content-Type: application/json' \
  --data '{"icon":"sub/plus","svg_sha256":"<hash>","worker":"mac-a/claude-fable-5-1"}' \
  "$API_BASE/api/work/claim"
curl --fail-with-body -H 'Content-Type: application/json' \
  --data '{"icon":"sub/plus","svg_sha256":"<hash>","worker":"mac-a/claude-fable-5-1","note":"sub/plus-v3"}' \
  "$API_BASE/api/work/done"
```

## CLI for agents

`icon_set/scripts/work_queue.py` talks to production over HTTP only; it needs
no local server or database.

```bash
export PICTOGRAPHIC_WORKER="$(hostname -s)/claude-fable-5-1"   # default: hostname/user
export PICTOGRAPHIC_API='https://<production>'                  # default: the recorded tunnel

python3 icon_set/scripts/work_queue.py next --limit 1 --offset 0 --disapprove-status bad-stroke   # claim + brief; exit 3 = nothing to claim
python3 icon_set/scripts/work_queue.py next --family sub --limit 3 --out fix-input.txt            # several at once
python3 icon_set/scripts/work_queue.py queue --family sub                       # look without claiming
python3 icon_set/scripts/work_queue.py done --icon sub/plus --note "sub/plus-v3"
python3 icon_set/scripts/work_queue.py cannot-fix --icon sub/plus --note "MIC 6 impossible with three bars"
python3 icon_set/scripts/work_queue.py abandon --icon sub/plus
python3 icon_set/scripts/work_queue.py status [--icon sub/plus]
```

`next` reads a small queue page and claims the first icon it wins; when another
machine claims the same row first it moves on to the next row. Every report
command looks up production's current hash unless `--svg-sha256` is given.
`upload --icon KEY --stage before|after --svg FILE [--python FILE] [--validation FILE] [--note]`
sends a fix result. `--json` prints the raw response. The `/fix-icon-queue`
skill wraps this procedure for agents; `/primitive-fix-thuan <count>` runs the
whole loop for solo icons through `icon_set/scripts/primitive_fix.py`
(`start` claims and records the first version, `finish` validates, uploads
the after result and reports done or cannot-fix).

## The Fix queue page

`gallery/work.html` (nav: **Fix queue**) is read-only, for reviewing. It lists
every icon that is disapproved, claimed, cannot-fix or freshly fixed, with
review status, work state, worker, claim time, expiry and note, plus family /
state / status / reason filters, search and paging. **History** on a row opens:

- **What changed**: the uploaded before drawing, the uploaded fixed drawing
  when the worker sent one, and the current drawing (now), with a sentence
  saying whether the fix has reached production yet; the uploaded Python
  source before/after and the validation text open underneath;
- **Revisions**: every `svg_sha256` the icon has had, with its review decision,
  claim and feedback entries;
- **Change log**: every logged event for the icon, newest first (reviews,
  feedback, claims, done, cannot-fix, abandon, expiry).

Type your worker name (for example `thuan-mac` or `mac-mini`) in **Your worker
name**: it is remembered in the browser, your rows are highlighted, **Only my
claims** filters to them, and the on-page guide **How to fetch, claim and
finish a fix** fills its curl and CLI examples with that name and the server
URL. Claims are made by agents with `work_queue.py`, not from the page. On
localhost the page shows production's data because the dev server forwards
the work routes.

## What reviewers see

- Claimed and cannot-fix icons stay under **Disapproved** in the review grid,
  with a second badge: **Working · worker · Nh left**, **Fixed by worker ·
  awaiting review**, **Cannot fix · worker**, or **Claim expired**. Hover for
  the note and timestamps.
- After a `done` report the icon appears under **Ready** with its feedback
  still attached. Approve it, or disapprove it again to send it back to the
  queue.
- The fixed drawing itself arrives with the next production pull as a new
  revision; that revision is Ready on its own.

## Recovery

- **Wrong worker name** on a report: the API answers `409 This claim belongs to
  …`. Repeat with the name used to claim, or `abandon` it (anyone may) and
  claim again.
- **A machine died mid-fix**: wait six hours for the claim to expire, or
  `abandon` it; the icon is `open` immediately.
- **A `done` that was wrong**: disapprove the icon again in the gallery. The
  new decision clears the worker and reopens it for claiming.
- **`cannot-fix` that should be retried**: disapprove the icon again in the
  gallery, or `abandon` it; either puts it back in the queue.
- **Production unreachable**: the dev server answers `502 Production is
  unreachable at …` and the `work` field reads `unknown`. Nothing is written
  locally; retry when the tunnel is back or pass the new URL with
  `--sync-source` / `PICTOGRAPHIC_API`.

## Migration from the separate tables

Older databases had `work_claims` (state, worker, lease) and `work_snapshots`
next to `reviews`. On start-up production adds the `worker`, `claimed_at` and
`note` columns to `reviews`, rebuilds the status check to allow `claimed` and
`cannot-fix`, moves each claim onto its review row (`working` → `claimed`,
`cannot-fix` → `cannot-fix`, `done` → the worker on the `ready` row), copies
each snapshot into `work_results` as a `before` result, and drops the two old
tables. A `cannot-fix` that a reviewer had already re-disapproved stays
Disapproved. The `/api/work/heartbeat` and `/api/work/snapshot` routes are
gone; `lease_hours` is ignored.
