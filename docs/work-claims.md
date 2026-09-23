# Work claims: fixing disapproved icons from many machines

Reviews, approvals and feedback live in **one database**: the production
`feedback.sqlite3` behind the always-on production gallery. Several machines and
AI agents repair disapproved icons at the same time. Work claims are how they
avoid fixing the same icon twice: before a machine touches an icon it **claims**
it on production, and when it finishes it **reports** there. Everything below
is served by the production `deploy.py`; a local `dev` server forwards these
routes to production, so the review grid on localhost shows the same state.

## States

The review status stays what the gallery shows: **Ready**, **Disapproved**
(`pending` in the database, `disapprove` in the API), **Approved**, **Rejected**.
A work claim belongs to one icon *revision*, `icon` + `svg_sha256`, and adds a
`work.state` to that revision:

| Review status | Claim for the current revision | `work.state` | Claimable |
|---|---|---|---|
| Disapproved | none | `open` | yes |
| Disapproved | working, lease not expired | `working` | no |
| Disapproved | working, lease expired | `expired` | yes |
| Ready (set by a `done` report) | done | `done` | no |
| Disapproved again, later than the report | done or cannot-fix | `open` | yes |
| Disapproved | cannot-fix | `cannot-fix` | no |
| Ready / Approved / Rejected, no claim | none | `open` (not disapproved, so not in the queue) | no |

Rules that follow from the table:

- **Claim** writes the record: `working`, worker name, `claimed_at`, and
  `expires_at` three hours later (`lease_hours` 1–24 on request). `heartbeat`
  extends the lease. An expired claim is claimable by anyone and the takeover
  is logged as `work_expired`.
- **Claim** also saves a snapshot of the displayed SVG for that revision, so
  the reviewer can still see the disapproved drawing after the fix replaces it.
- **Done** updates the claim to `done` **and** sets that revision's review
  status to Ready in the same transaction, attributed to the worker. The
  disapproval feedback is kept so the reviewer can compare the fix against the
  request. (The gallery's manual Ready button clears feedback; `done` does not.)
- **Never again until disapproved again.** A `done` or `cannot-fix` revision is
  not queued and cannot be claimed. When a reviewer disapproves the icon again,
  the review timestamp is newer than the report, so the icon is `open` again.
- **A deployed fix changes the hash.** The new revision has no claim and starts
  Ready, exactly as any new build does. The old claim becomes history
  (`superseded` in the claims listing).
- **Abandon** deletes a working claim; the icon is `open` at once. Only the
  owning worker may abandon, or a logged-in reviewer for any claim.
- Every transition is appended to `activity_log`: `work_claim`,
  `work_heartbeat`, `work_done` (+ a `review` entry), `work_cannot_fix`,
  `work_abandon`, `work_expired`.

## Machine A and machine B

```
machine A: next  → queue lists X (open) → claim X → X is working (A, 3 h)
machine B: next  → queue skips X → claims Y instead
machine A: fixes X, publishes, done X → X is done; review status Ready, feedback kept
machine B: next  → X is not listed (done); claim X → 409 "already fixed … waiting for review"
reviewer:  disapproves X again → X is open
machine B: next  → X is listed → claim X → working (B)
```

A crashed machine holds nothing forever: its `working` claim expires after the
lease and the next `next` takes the icon.

## API

Step-by-step request and response examples for the whole workflow are in
[work-claims-api.md](work-claims-api.md).

Production serves these; `python3 -m icon_set dev` forwards them to its
`--sync-source` (default `$PICTOGRAPHIC_SYNC_SOURCE`, then the tunnel recorded
in `deploy.py`). No login is required; the `worker` string is stored on the
record and must match on every later call.

| Route | Method | Body / query | Result |
|---|---|---|---|
| `/api/work/queue` | GET | `family`, `category`, `type`, `limit` (1–500, default 50), `offset` | `{total, offset, next_offset, items}`; items are claimable Disapproved icons, oldest disapproval first, each with `key`, `svg_sha256`, `family`, `python_source`, `reason`, `feedback`, `disapproved_by`, `disapproved_at`, `original_sources`, `work` |
| `/api/work/disapproved` | GET | same filters as the queue | every Disapproved icon, claimable or not, each with `status` and `work` (`open`, `working`, `expired`, `done`, `cannot-fix`) |
| `/api/work/review` | GET | `family`, `state`, `status`, `limit`, `offset` | every icon that is disapproved or carries a claim, newest work first, with `counts` per state; a claim on a revision that is no longer current is `superseded` (fix deployed) |
| `/api/work/history` | GET | `icon` | the icon's revisions (review, claim, feedback, snapshot flag per hash) and its full change log from `activity_log` |
| `/api/work/snapshot` | GET | `icon`, `svg_sha256` | `image/svg+xml`: the drawing as displayed when that revision was claimed (saved automatically on claim) |
| `/api/work` | GET | optional `icon` | all claims joined to the catalog (`current`, `status`), or one icon's `{status, svg_sha256, work}` |
| `/api/work/claim` | POST | `icon`, `svg_sha256`, `worker`, optional `lease_hours` | `201 {saved, work, item}`; `409` with the current `work` when taken, done or cannot-fix |
| `/api/work/claim` (batch) | POST | `worker`, `icons`: list of keys or `{icon, svg_sha256}` (max 500), optional `lease_hours` | `200 {saved, worker, claimed: [item…], refused: [{icon, status, error, work}]}`; each icon succeeds or is refused on its own; a bare key uses production's current hash |
| `/api/work/heartbeat` | POST | `icon`, `svg_sha256`, `worker`, optional `lease_hours` | `200 {saved, work}` |
| `/api/work/done` | POST | `icon`, `svg_sha256`, `worker`, optional `note` | `200 {saved, status: "ready", work}` |
| `/api/work/cannot-fix` | POST | `icon`, `svg_sha256`, `worker`, required `note` | `200 {saved, work}` |
| `/api/work/abandon` | POST | `icon`, `svg_sha256`, `worker` | `200 {saved, work: {state: "open"}}` |

`svg_sha256` must be production's current hash for the icon; a mismatch is a
`409` carrying the current hash. If your local `published/` is ahead of
production, wait for the production pull. `GET /api/icon-types` and
`GET /api/review-detail` also return the `work` field.

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

python3 icon_set/scripts/work_queue.py next --family sub --out fix-input.txt   # claim + brief; exit 3 = queue empty
python3 icon_set/scripts/work_queue.py queue --family sub                       # look without claiming
python3 icon_set/scripts/work_queue.py heartbeat --icon sub/plus                # extend the lease
python3 icon_set/scripts/work_queue.py done --icon sub/plus --note "sub/plus-v3"
python3 icon_set/scripts/work_queue.py cannot-fix --icon sub/plus --note "MIC 6 impossible with three bars"
python3 icon_set/scripts/work_queue.py abandon --icon sub/plus
python3 icon_set/scripts/work_queue.py status [--icon sub/plus]
```

`next` reads a small queue page and claims the first icon it wins; when another
machine claims the same row first it moves on to the next row. Every report
command looks up production's current hash unless `--svg-sha256` is given.
`--json` prints the raw response. The `/fix-icon-queue` skill wraps this
procedure for agents.

## The Fix queue page

`gallery/work.html` (nav: **Fix queue**) is read-only, for reviewing. It lists
every icon that is disapproved or carries a fix claim, with review status, work
state, worker, claim time, lease and note, plus family / state / status filters,
search and paging. **History** on a row opens:

- **What changed**: the drawing saved when the icon was claimed (before) next
  to the current drawing (now), with a sentence saying whether the fix has
  reached production yet;
- **Revisions**: every `svg_sha256` the icon has had, with its review decision,
  claim and feedback entries;
- **Change log**: every logged event for the icon, newest first (reviews,
  feedback, claims, heartbeats, done, cannot-fix, abandon, expiry).

Type your worker name (for example `thuan-mac` or `mac-mini`) in **Your worker
name**: it is remembered in the browser, your rows are highlighted, **Only my
claims** filters to them, and the on-page guide **How to fetch, claim and
finish a fix** fills its curl and CLI examples with that name and the server
URL. Claims are made by agents with `work_queue.py`, not from the page. On
localhost the page shows production's data because the dev server forwards
the work routes.

## What reviewers see

- Disapproved cards in the review grid carry a second badge: **Working · worker
  · Nh left**, **Fixed by worker · awaiting review**, **Cannot fix · worker**,
  or **Claim expired**. Hover for the note and timestamps.
- After a `done` report the icon appears under **Ready** with its feedback
  still attached. Approve it, or disapprove it again to send it back to the
  queue.
- The fixed drawing itself arrives with the next production pull as a new
  revision; that revision is Ready on its own.

## Recovery

- **Wrong worker name** on a report: the API answers `409 This claim belongs to
  …`. Repeat with the name used to claim, or log in to the gallery and
  `abandon` it.
- **A machine died mid-fix**: wait for the lease to expire (3 hours) or, logged
  in, `abandon` the claim; the icon is `open` immediately.
- **A `done` that was wrong**: disapprove the icon again in the gallery. The
  new disapproval reopens it for claiming.
- **`cannot-fix` that should be retried**: disapprove the icon again; that is
  the only way back into the queue.
- **Production unreachable**: the dev server answers `502 Production is
  unreachable at …` and the `work` field reads `unknown`. Nothing is written
  locally; retry when the tunnel is back or pass the new URL with
  `--sync-source` / `PICTOGRAPHIC_API`.
