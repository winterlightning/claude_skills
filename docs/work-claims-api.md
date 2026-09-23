# Fix workflow API: fetch → claim → fix → done → result

This is the request-by-request guide for a machine or agent that repairs
disapproved icons. Concepts and the state table are in
[work-claims.md](work-claims.md); this page only shows the calls, in order.

## Before you start

| | |
|---|---|
| Base URL | the production gallery, e.g. `https://<production>`. A local `python3 -m icon_set dev` server forwards every `/api/work*` call there, so `http://127.0.0.1:8000` works too. |
| Login | none. Send `Content-Type: application/json` on POST. |
| Worker | a name you choose once per machine and reuse on every call, e.g. `thuan-mac`. Required: `--worker` or `PICTOGRAPHIC_WORKER`, no default. It is stored on the review row as `worker`; only the same worker may report it. |
| Hash | every write names the revision with `svg_sha256`. Use the value the API just gave you; a stale hash is refused with `409`. |

```bash
API_BASE='https://<production>'
WORKER='thuan-mac'
```

## 1. Fetch the disapproved icons

Two lists. `disapproved` is every icon whose review status is Disapproved or
Claimed, with its work state, for looking. `queue` is the subset you may claim
right now.

```bash
curl --fail-with-body "$API_BASE/api/work/disapproved?family=sub&limit=50&offset=0"
curl --fail-with-body "$API_BASE/api/work/queue?family=sub&limit=5"
```

Filters: `family`, `category`, `type`, `reason` (`bad-stroke`, `meaning`,
`manual-fix-request`, `other`), `limit` (1–500, default 50), `offset`.
Oldest disapproval first. Page with `next_offset` until it is `null`.

```json
{
  "total": 12, "offset": 0, "next_offset": null,
  "items": [
    {
      "key": "sub/plus", "icon_id": "plus", "name": "plus", "family": "sub", "category": "math",
      "svg_sha256": "5a1c…e9", "python_source": {"path": "icon_set/model/icons/sub/plus.py", "class": "Plus"},
      "preview_url": "../sub32/plus.svg", "original_sources": [{"source_path": "pictographic-primitives/math/plus.svg"}],
      "status": "disapprove",
      "reason": "bad-stroke", "feedback": "Bad stroke drawn\n\nThe arms are not equal.",
      "disapproved_by": "hina", "disapproved_at": "2026-09-23T06:20:37+00:00", "feedback_by": "hina",
      "icon_type": null,
      "work": {"state": null}
    }
  ]
}
```

`work.state` follows the worker's path, `claimed` → `done` or `cannot-fix`, and tells you what to do:

| state | meaning | in `queue`? |
|---|---|---|
| `null` | nobody has worked on it; Disapproved, so claimable (a claim older than six hours is set back to this) | yes |
| `claimed` | review status `claimed`: another machine holds it (`work.worker`, `work.expires_at` = `claimed_at` + 6 h) | no |
| `done` | review status `ready` set by a worker's report; waiting for the reviewer | no |
| `cannot-fix` | Disapproved, but a worker gave up (`work.worker`, `work.note`); a reviewer decision or `abandon` reopens it | no |

## 2. Claim

One icon:

```bash
curl --fail-with-body -H 'Content-Type: application/json' --data '{
  "icon": "sub/plus", "svg_sha256": "5a1c…e9", "worker": "'"$WORKER"'"
}' "$API_BASE/api/work/claim"
```

```json
HTTP 201
{
  "saved": true, "icon": "sub/plus", "svg_sha256": "5a1c…e9",
  "work": {"state": "claimed", "worker": "thuan-mac", "note": "",
           "claimed_at": "2026-09-23T07:00:00+00:00", "updated_at": "2026-09-23T07:00:00+00:00",
           "expires_at": "2026-09-23T10:00:00+00:00", "svg_sha256": "5a1c…e9"},
  "item": { "...the same object as in step 1, now with work.state = claimed..." }
}
```

Several icons in one call (each succeeds or is refused on its own; a bare key
uses production's current hash):

```bash
curl --fail-with-body -H 'Content-Type: application/json' --data '{
  "worker": "'"$WORKER"'",
  "icons": [{"icon": "sub/plus", "svg_sha256": "5a1c…e9"}, "sub/minus"]
}' "$API_BASE/api/work/claim"
```

```json
HTTP 200
{"saved": true, "worker": "thuan-mac",
 "claimed": [ { "key": "sub/plus", "...": "..." } ],
 "refused": [ {"icon": "sub/minus", "status": 409, "error": "mac-mini is working on this icon.",
               "work": {"state": "claimed", "worker": "mac-mini", "...": "..."}} ]}
```

Refusals you will see:

| HTTP | error | do |
|---|---|---|
| `409` | `… is working on this icon.` | take the next queue item |
| `409` | `Another worker claimed this icon just now.` | take the next queue item |
| `409` | `Icon changed on production; refresh the queue …` (`svg_sha256` in the body is the current one) | re-fetch, claim with that hash |
| `409` | `Restore this rejected icon before working on it.` | skip |
| `400` | `worker must be a name …` | send a worker string |

The claim is one conditional update on the review row (`status = 'claimed'`
only where it was Disapproved with no worker, or an expired claim), so two
machines can never both win. Six hours after `claimed_at` the row goes back to
Disapproved with no work state; there is nothing to extend.
Upload the current drawing as the `before` result (step 4a) if you want the
before/after view in step 5.

Or let the CLI do steps 1–2 in one go and print the brief:

```bash
python3 icon_set/scripts/work_queue.py next --limit 1 --offset 0 --disapprove-status bad-stroke --worker "$WORKER"
```

`--limit` is how many icons to claim, `--offset` skips the first claimable
ones, `--disapprove-status` (alias `--reason`) keeps one disapproval reason.

## 3. Fix it and build only that icon (outside the API)

Author the repair as a new variant and validate it. Then build and publish
**only the icon you fixed**; a full library build is never needed for one fix:

```bash
python3 -m icon_set build --icon icon_set/model/icons/sub/plus_v3.py --no-png --no-report   # this icon only
python3 -m icon_set publish --no-build            # compact the catalogs and write release.json, no rebuild
git add icon_set/model/icons/sub/plus_v3.py published/sub32 published/gallery/icons.json published/release.json
git commit -m "Fix sub/plus" && git push origin icon-lib
```

The per-icon build writes that icon's SVG, manifest row, metadata and gallery
entry into `published/`. Production receives the new drawing on its next pull.
Finish within six hours of the claim; after that the icon is Disapproved and
claimable by other machines again.

## 4a. Upload the result

Before reporting, upload the fixed drawing so the Fix queue page shows it next
to the before drawing at once (the deployed drawing only changes after the
production pull). The same call with `stage: "before"` stores the first
version; `primitive_fix.py start` does that automatically when it claims.

```bash
python3 icon_set/scripts/work_queue.py upload --worker "$WORKER" --icon sub/plus --stage after \
  --svg published/sub32/plus.svg --python icon_set/model/icons/sub/plus.py --validation validation.txt --note "equalised the arms"
```

Raw API: `POST /api/work/result` with `{icon, svg_sha256, worker, stage, svg, python_path?, python_source?, validation?, note?}`
(`before` only while you hold the claim; `after` while working or after
`done` / `cannot-fix`; each text ≤ 512 KB; the SVG must be a clean `0 0 N N` document for the
icon's canvas). Read it back with
`GET /api/work/result?icon=sub/plus&svg_sha256=5a1c…e9&stage=after&part=svg|python|validation`.

```json
HTTP 200
{"saved": true, "icon": "sub/plus", "svg_sha256": "5a1c…e9",
 "result": {"stage": "after", "worker": "thuan-mac", "saved_at": "2026-09-23T08:05:00+00:00",
            "python_path": "icon_set/model/icons/sub/plus.py", "note": "equalised the arms", "has_python": true, "has_validation": true},
 "work": {"state": "claimed", "...": "..."}}
```

## 4. Mark done

```bash
curl --fail-with-body -H 'Content-Type: application/json' --data '{
  "icon": "sub/plus", "svg_sha256": "5a1c…e9", "worker": "'"$WORKER"'", "note": "sub/plus-v3, commit 2c1c69d"
}' "$API_BASE/api/work/done"
```

```json
HTTP 200
{
  "saved": true, "icon": "sub/plus", "svg_sha256": "5a1c…e9", "status": "ready",
  "work": {"state": "done", "worker": "thuan-mac", "note": "sub/plus-v3, commit 2c1c69d",
           "claimed_at": "2026-09-23T07:00:00+00:00", "updated_at": "2026-09-23T08:10:00+00:00",
           "svg_sha256": "5a1c…e9"}
}
```

What this did on production: the revision's review status became **Ready**
(attributed to your worker, `worker` and `note` kept on the row) and the
disapproval feedback was **kept** so the reviewer can compare. The icon leaves
`disapproved` and `queue`; it cannot be claimed again until a reviewer
disapproves it again, which clears the worker.

The two other ways to end a claim:

```bash
# no meaning-preserving drawing passes; note is required. The icon is Disapproved again but keeps
# your worker and note (work.state cannot-fix), so the queue skips it until a reviewer decides.
curl ... --data '{"icon":"sub/plus","svg_sha256":"5a1c…e9","worker":"'"$WORKER"'","note":"MIC 6 impossible with three bars"}' "$API_BASE/api/work/cannot-fix"
# set it back to plain Disapproved for the queue (anyone may; also reopens a cannot-fix)
curl ... --data '{"icon":"sub/plus","svg_sha256":"5a1c…e9","worker":"'"$WORKER"'"}' "$API_BASE/api/work/abandon"
```

## 5. See the final result

**Current state of one icon** (review status + work state):

```bash
curl --fail-with-body "$API_BASE/api/work?icon=sub/plus"
```

```json
{"icon": "sub/plus", "svg_sha256": "5a1c…e9", "status": "ready",
 "work": {"state": "done", "worker": "thuan-mac", "note": "sub/plus-v3, commit 2c1c69d", "...": "..."}}
```

**Everything that happened to it** (revisions, reviews, feedback, claims, log):

```bash
curl --fail-with-body "$API_BASE/api/work/history?icon=sub/plus"
```

```json
{
  "icon": "sub/plus", "name": "plus", "family": "sub", "preview_url": "../sub32/plus.svg",
  "python_source": {"path": "icon_set/model/icons/sub/plus.py", "class": "Plus"},
  "current": {"svg_sha256": "9f02…b1", "status": "ready", "updated_by": null, "updated_at": null,
              "work": {"state": "none"}},
  "revisions": [
    {"svg_sha256": "5a1c…e9", "current": false,
     "review": {"status": "ready", "updated_by": "thuan-mac", "updated_at": "2026-09-23T08:10:00+00:00"},
     "claim": {"state": "done", "worker": "thuan-mac", "note": "sub/plus-v3, commit 2c1c69d", "...": "..."},
     "feedback": [{"id": 41, "reason": "bad-stroke", "feedback": "Bad stroke drawn\n\nThe arms are not equal.",
                   "author": "hina", "created_at": "2026-09-23T06:20:37+00:00", "edited_by": null, "edited_at": null}],
     "results": {"before": {"worker": "thuan-mac", "saved_at": "2026-09-23T07:00:01+00:00", "python_path": "icon_set/model/icons/sub/plus.py", "note": "first version, before the fix", "has_python": true, "has_validation": false},
                 "after": {"worker": "thuan-mac", "saved_at": "2026-09-23T08:05:00+00:00", "python_path": "icon_set/model/icons/sub/plus.py", "note": "equalised the arms", "has_python": true, "has_validation": true}}},
    {"svg_sha256": "9f02…b1", "current": true,
     "review": {"status": "ready", "updated_by": null, "updated_at": null}, "claim": null, "feedback": [], "results": {}}
  ],
  "events": [
    {"at": "2026-09-23T06:20:37+00:00", "user": "hina", "action": "feedback", "details": {"status": "pending", "reason": "bad-stroke", "feedback_id": 41}},
    {"at": "2026-09-23T07:00:00+00:00", "user": "system", "action": "work_claim", "details": {"worker": "thuan-mac", "expires_at": "2026-09-23T13:00:00+00:00"}},
    {"at": "2026-09-23T08:10:00+00:00", "user": "system", "action": "work_done", "details": {"worker": "thuan-mac", "note": "sub/plus-v3, commit 2c1c69d"}},
    {"at": "2026-09-23T08:10:00+00:00", "user": "thuan-mac", "action": "review", "details": {"status": "ready", "source": "work_done", "feedback_kept": true}}
  ]
}
```

Read it like this:

- Right after `done`, `current.svg_sha256` still equals the claimed hash and
  `current.work.state` is `done`: the fix is reported but the new drawing has
  not been pulled on production yet.
- After the production pull, `current.svg_sha256` is the new hash and the
  new revision is `ready` with no claim (the example above); the old revision
  keeps its `done` row as history. The reviewer then approves it
  (`current.status` becomes `approve`) or disapproves it again (`disapprove`,
  which clears the worker and puts the icon back in the queue).

**Before and after drawings**, for comparing:

```bash
curl "$API_BASE/api/work/result?icon=sub/plus&svg_sha256=5a1c…e9&stage=before" -o before.svg   # uploaded before the fix
curl "$API_BASE/api/icon-artwork/svg?icon=sub/plus" -o now.svg                                  # what production shows now
```

`result` answers `404` when no `before` drawing was uploaded for that revision.

**All fixed icons awaiting review**, or any other state:

```bash
curl --fail-with-body "$API_BASE/api/work/review?state=done"        # done, claimed, cannot-fix
curl --fail-with-body "$API_BASE/api/work/review?status=approve"    # by review status
```

Each item has the same shape as step 1 plus `work.results` (the uploaded
stages). The response also carries `counts` per state. The gallery's **Fix queue** page (`gallery/work.html`) is
this call plus `history`, rendered.

## Quick reference

| Step | Call |
|---|---|
| fetch all disapproved | `GET /api/work/disapproved?family=&category=&type=&limit=&offset=` |
| fetch claimable | `GET /api/work/queue?…` |
| claim one / many | `POST /api/work/claim` `{icon, svg_sha256, worker}` or `{worker, icons: [...]}` |
| upload before / after | `POST /api/work/result` `{icon, svg_sha256, worker, stage, svg, python_path?, python_source?, validation?, note?}` · `GET /api/work/result?icon=&svg_sha256=&stage=&part=` |
| mark done → Ready | `POST /api/work/done` `{icon, svg_sha256, worker, note?}` |
| give up | `POST /api/work/cannot-fix` `{…, note}` · `POST /api/work/abandon` `{…}` |
| one icon now | `GET /api/work?icon=` |
| full history | `GET /api/work/history?icon=` |
| before / now SVG | `GET /api/work/result?icon=&svg_sha256=&stage=before` · `GET /api/icon-artwork/svg?icon=` |
| everything tracked | `GET /api/work/review?state=&status=&family=&limit=&offset=` |
| all claims raw | `GET /api/work` |

CLI equivalents: `work_queue.py next | queue | upload | done | cannot-fix | abandon | status`.
Whole loop for solo icons: `/primitive-fix-thuan <count> [--offset N] [--disapprove-status R] [--worker name]`
(`primitive_fix.py start` / `finish`).
