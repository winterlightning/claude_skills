#!/usr/bin/env python3
"""Claim every liked run in output_png/verdicts.json on the Worker and upload its before / after drawings.

Usage: python3 new-pipeline-test/claim_liked.py --worker <name> [--base-url URL] [--run DIR ...]
                                                [--dry-run] [--retry] [--no-before]

Per liked run (verdict = like, no successful claim recorded yet):
  1. resolve the production icon key (verdict's icon_key, else the run's source id via build_report)
  2. GET  /api/work?icon=<key>            -> current svg_sha256
  3. POST /api/work/claim                  -> claimed by --worker
  4. POST /api/work/result stage=before    -> the current gallery SVG of that key
  5. POST /api/work/result stage=after     -> <slug>_redraw.svg + <slug>_redraw.py from the run folder
The outcome is written back into verdicts.json under "claim" so a rerun skips it. Nothing calls done:
report with work_queue.py done --icon <key> once the module is in icon_set/model/icons and built.

--finished DIR (a fetch_repeat_disapproved.py output folder) skips the Like step: every run in
output_png made after DIR was fetched, whose source id is one of DIR's icons and that has a finished
<slug>_redraw.svg, is claimed, gets before (production's current drawing) / after (redraw + module +
validation text) uploaded and is reported done, so the revision returns to Ready. The newest run per
source id wins; state goes to DIR/uploads.json so a rerun skips finished icons; --no-done holds the claim.

    python3 new-pipeline-test/claim_liked.py --finished new-pipeline-test/disapproved/repeat-20260929 --worker thuan-mac [--dry-run]
"""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(REPO / "icon_set" / "scripts"))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO))  # icon_set.scripts.primitive_fix / build_gate for --finished validation
import work_queue  # noqa: E402  (icon_set/scripts/work_queue.py)
import build_report  # noqa: E402
from serve_report import normalize  # noqa: E402

ROOT = HERE / "output_png"
VERDICTS = ROOT / "verdicts.json"


def now():
    return datetime.now(timezone.utc).isoformat()


def run_files(run_dir):
    m = build_report.RUN_RE.match(run_dir)
    slug = m.group(3) if m else run_dir
    d = ROOT / run_dir
    redraw_svg = d / f"{slug}_redraw.svg"
    redraw_py = next((p for p in (d / f"{slug.replace('-', '_')}_redraw.py", d / f"{slug}_redraw.py") if p.exists()), None)
    choice = build_report.load_json(d / "choice.json")
    return slug, redraw_svg, redraw_py, choice.get("source_icon_id")


def resolve_key(run_dir, entry, cache):
    if entry.get("icon_key"):
        return entry["icon_key"], None
    slug, _, _, source_id = run_files(run_dir)
    if not source_id:
        return None, None
    if source_id.lower() not in cache:
        cache.update(build_report.current_icons([source_id]))
    key, svg = build_report.pick_current(cache.get(source_id.lower(), []), re.sub(r"-\d+$", "", slug))
    return key, svg


def gallery_svg_for(key):
    """Look the key up in icons.json to find its preview_url."""
    try:
        data = json.loads((REPO / "published" / "gallery" / "icons.json").read_text())
    except (OSError, ValueError):
        return None
    items = data if isinstance(data, list) else data.get("icons", data)
    items = list(items.values()) if isinstance(items, dict) else items
    for icon in items:
        if icon.get("key") == key and icon.get("preview_url"):
            p = REPO / "published" / "gallery" / icon["preview_url"]
            return p if p.exists() else None
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--worker", help=work_queue.WORKER_HELP)
    ap.add_argument("--base-url", help="Worker URL (default: $PICTOGRAPHIC_API or the recorded production URL)")
    ap.add_argument("--run", action="append", help="only these run folders (repeatable)")
    ap.add_argument("--dry-run", action="store_true", help="show what would be claimed, call nothing")
    ap.add_argument("--retry", action="store_true", help="retry runs whose last claim attempt failed")
    ap.add_argument("--no-before", action="store_true", help="skip the 'before' upload")
    ap.add_argument("--claim-only", action="store_true", help="claim now, upload later (rerun without the flag to upload)")
    ap.add_argument("--done", action="store_true",
                    help="protect uploaded runs: re-claim each one whose claim expired and report done, so the revision "
                         "becomes Ready with the liked drawing and leaves the fix queue")
    ap.add_argument("--note", default="png pipeline redraw", help="note attached to the uploads")
    ap.add_argument("--finished", metavar="DIR",
                    help="upload + done every finished redraw for the icons of this fetch_repeat_disapproved.py folder (no Like step)")
    ap.add_argument("--no-done", action="store_true", help="with --finished: upload but keep the claim instead of reporting done")
    args = ap.parse_args()
    if args.finished:
        return upload_finished(args)

    base_url = args.base_url or work_queue.default_base_url()
    worker = args.worker or (None if args.dry_run else work_queue.default_worker())
    try:
        verdicts = normalize(json.loads(VERDICTS.read_text()))
    except (OSError, ValueError):
        raise SystemExit(f"no verdicts yet: {VERDICTS} (run serve_report.py and click Like)")
    if args.done:
        return report_done(base_url, worker, verdicts, args)

    todo = []
    for run_dir, entry in sorted(verdicts.items()):
        if entry.get("verdict") != "like" or (args.run and run_dir not in args.run):
            continue
        claim = entry.get("claim") or {}
        if claim.get("ok") and (claim.get("after") or args.claim_only):
            continue  # fully done, or already claimed and we only claim today
        if claim and not claim.get("ok") and not args.retry:
            continue
        todo.append((run_dir, entry))
    if not todo:
        print("nothing to claim (no liked runs without a claim)")
        return 0
    print(f"{len(todo)} liked run(s) to claim on {base_url} as {worker or '<dry-run>'}")

    cache = {}
    for run_dir, entry in todo:
        slug, redraw_svg, redraw_py, _ = run_files(run_dir)
        key, before_svg = resolve_key(run_dir, entry, cache)
        before_svg = before_svg or (gallery_svg_for(key) if key else None)
        prior = entry.get("claim") or {}
        held = prior.get("ok") and prior.get("svg_sha256")  # claimed on an earlier --claim-only run
        record = dict(prior) if held else {}
        record.update(at=now(), worker=worker, base_url=base_url)
        problems = []
        if not key:
            problems.append("no production icon key (not in local gallery)")
        if not args.claim_only and not redraw_svg.exists():
            problems.append(f"missing {redraw_svg.name}")
        if not args.claim_only and not args.no_before and not before_svg:
            problems.append("no current gallery SVG for the before upload")
        line = f"  {run_dir}: {key or '?'}"
        if problems:
            record.update(ok=False, error="; ".join(problems))
            print(f"{line}  SKIP {record['error']}")
            if args.dry_run:
                continue
        elif args.dry_run:
            print(f"{line}  would claim, before={before_svg.name if before_svg else '-'}, after={redraw_svg.name}"
                  f"{' + ' + redraw_py.name if redraw_py else ''}")
            continue
        else:
            try:
                if held:
                    sha = prior["svg_sha256"]
                else:
                    sha = work_queue.call(base_url, "GET", "/api/work", query={"icon": key})["svg_sha256"]
                    claimed = work_queue.call(base_url, "POST", "/api/work/claim", {"icon": key, "svg_sha256": sha, "worker": worker})
                    record.update(icon=key, svg_sha256=sha, state=claimed.get("work", {}).get("state"), ok=True)
                if args.claim_only:
                    print(f"{line}  claimed @{sha[:8]} · work={record['state']} · upload pending")
                else:
                    if not args.no_before and not record.get("before"):
                        work_queue.upload_result(base_url, worker, key, sha, "before", before_svg, note=args.note)
                        record["before"] = str(before_svg.relative_to(REPO))
                    work_queue.upload_result(base_url, worker, key, sha, "after", redraw_svg, redraw_py, note=args.note)
                    record["after"] = str(redraw_svg.relative_to(REPO))
                    record["ok"] = True
                    print(f"{line}  {'held' if held else 'claimed'} @{sha[:8]} · before/after uploaded · work={record['state']}")
            except work_queue.ApiError as e:
                if e.status == 409 and "already hold" in str(e) and not held:
                    record.update(icon=key, svg_sha256=sha, state="claimed", ok=True)
                    print(f"{line}  already held @{sha[:8]} · upload pending")
                else:
                    record.update(ok=False, error=f"{e.status}: {e}")
                    print(f"{line}  FAILED {record['error']}")
            except Exception as e:  # network, missing file
                record.update(ok=False, error=str(e))
                print(f"{line}  FAILED {e}")
        entry["icon_key"] = key or entry.get("icon_key", "")
        entry["claim"] = record
        verdicts[run_dir] = entry
        VERDICTS.write_text(json.dumps(verdicts, indent=2, sort_keys=True) + "\n")
    done = sum(1 for _, e in todo if (e.get("claim") or {}).get("ok"))
    print(f"{done}/{len(todo)} {'claimed (uploads pending)' if args.claim_only else 'claimed and uploaded'}; results in {VERDICTS}")
    return 0


def report_done(base_url, worker, verdicts, args):
    """For every run whose after drawing is uploaded: hold the claim (re-claim if it expired) and report done."""
    todo = [(r, e) for r, e in sorted(verdicts.items())
            if e.get("verdict") == "like" and (e.get("claim") or {}).get("after") and not (args.run and r not in args.run)]
    print(f"{len(todo)} uploaded run(s) to report done on {base_url} as {worker or '<dry-run>'}")
    count = 0
    for run_dir, entry in todo:
        claim = entry["claim"]
        key, sha = claim["icon"], claim["svg_sha256"]
        line = f"  {run_dir}: {key}"
        if claim.get("done"):
            print(f"{line}  already done {claim['done'][:16]}")
            continue
        try:
            cur = work_queue.call(base_url, "GET", "/api/work", query={"icon": key})
            work, status = cur.get("work") or {}, cur.get("status")
            if cur.get("svg_sha256") != sha:
                print(f"{line}  SKIP production moved to another revision @{cur.get('svg_sha256', '')[:8]}")
                continue
            if work.get("state") == "done":
                print(f"{line}  SKIP already done by {work.get('worker')} at {work.get('updated_at', '')[:16]} (the liked upload may be overwritten)")
                continue
            if work.get("state") == "working" and work.get("worker") != worker:
                print(f"{line}  SKIP {work.get('worker')} is working on it")
                continue
            if args.dry_run:
                print(f"{line}  would {'re-claim and ' if work.get('state') != 'working' else ''}report done (status {status})")
                continue
            if work.get("state") != "working":
                work_queue.call(base_url, "POST", "/api/work/claim", {"icon": key, "svg_sha256": sha, "worker": worker})
            work_queue.call(base_url, "POST", "/api/work/done", {"icon": key, "svg_sha256": sha, "worker": worker, "note": args.note})
            claim["done"] = now()
            claim["state"] = "done"
            count += 1
            VERDICTS.write_text(json.dumps(verdicts, indent=2, sort_keys=True) + "\n")
            print(f"{line}  done @{sha[:8]} · revision Ready with the liked drawing")
        except work_queue.ApiError as e:
            print(f"{line}  FAILED {e.status}: {e}")
    print(f"{count}/{len(todo)} reported done; results in {VERDICTS}")
    return 0


def finished_runs(folder):
    """(source id -> icon key, [(run dir, slug, redraw svg, redraw py, source id)]) for a fetch folder.

    Keys follow the batch scripts: icons another worker held are left out and the first icon per
    source id wins. Only runs started after the fetch count, so older redraws never go up."""
    data = json.loads((folder / "icons.json").read_text())
    keys = {}
    for icon in data["icons"]:
        sid = (icon.get("source_icon_id") or "").lower()
        if sid and icon.get("work_state") != "working":
            keys.setdefault(sid, icon["key"])
    since = datetime.fromisoformat(data["generated"]).strftime("%Y%m%d-%H%M")
    newest = {}
    for d in sorted(p for p in ROOT.iterdir() if p.is_dir() and build_report.RUN_RE.match(p.name)):
        if d.name[:13] < since:
            continue
        slug, redraw_svg, redraw_py, sid = run_files(d.name)
        sid = (sid or "").lower()
        if sid in keys and redraw_svg.exists():
            newest[sid] = (d.name, slug, redraw_svg, redraw_py, sid)  # sorted by name = time: last wins
    return keys, sorted(newest.values())


def validation_text(module_path):
    """validate_icon() plus the build gate, as primitive_fix.finish reports them; never raises."""
    if not module_path:
        return "no redraw module\n"
    try:
        from icon_set.scripts import build_gate, primitive_fix
        report = primitive_fix.load_icon(module_path).validate_icon()
        gate = build_gate.gate(module_path)
        lines = [f"validation: {report.status}"]
        lines += [f"  error: {m}" for m in getattr(report, "errors", []) or []]
        lines += [f"  warning: {m}" for m in getattr(report, "warnings", []) or []]
        lines += [f"build gate: {gate['status']}"] + [f"  {m}" for m in gate["errors"] + gate["warnings"]]
        return "\n".join(lines) + "\n"
    except Exception as e:  # informational only: the redraw goes up either way
        return f"validation could not run: {type(e).__name__}: {e}\n"


def upload_finished(args):
    folder = Path(args.finished).resolve()
    state_path = folder / "uploads.json"
    base_url = args.base_url or work_queue.default_base_url()
    worker = args.worker or (None if args.dry_run else work_queue.default_worker())
    state = json.loads(state_path.read_text()) if state_path.is_file() else {}
    keys, runs = finished_runs(folder)
    todo = []
    for run in runs:
        key = keys[run[4]]
        record = state.get(key) or {}
        if record.get("done") or (args.no_done and record.get("after")):
            continue
        if record.get("error") and not args.retry:
            continue
        if args.run and run[0] not in args.run:
            continue
        todo.append((key, run))
    print(f"{len(runs)} finished redraw(s) for {len(keys)} icons in {folder.name}; "
          f"{len(todo)} to upload{'' if args.no_done else ' + done'} on {base_url} as {worker or '<dry-run>'}")
    count = 0
    for key, (run_dir, slug, redraw_svg, redraw_py, sid) in todo:
        line = f"  {key} <- {run_dir}"
        record = dict(state.get(key) or {})
        record.update(run=run_dir, at=now(), worker=worker)
        record.pop("error", None)
        try:
            cur = work_queue.call(base_url, "GET", "/api/work", query={"icon": key})
            sha, status, work = cur["svg_sha256"], cur.get("status"), cur.get("work") or {}
            mine = work.get("state") == "working" and work.get("worker") == worker
            if work.get("state") == "done" or (status not in ("disapprove", "pending", "claimed") and not mine):
                print(f"{line}  SKIP status {status}, work {work.get('state')} (no longer disapproved)")
                continue
            if work.get("state") == "working" and not mine:
                print(f"{line}  SKIP {work.get('worker')} is working on it")
                continue
            if work.get("state") == "cannot-fix":
                print(f"{line}  SKIP reported cannot-fix by {work.get('worker')}")
                continue
            if args.dry_run:
                print(f"{line}  would {'' if mine else 'claim, '}upload before/after{'' if args.no_done else ', report done'} @{sha[:8]}")
                continue
            if not mine:
                work_queue.call(base_url, "POST", "/api/work/claim", {"icon": key, "svg_sha256": sha, "worker": worker})
            record.update(icon=key, svg_sha256=sha, state="working")
            work_dir = folder / "uploads" / slug
            work_dir.mkdir(parents=True, exist_ok=True)
            if not args.no_before and record.get("before_sha") != sha:
                before = work_dir / "before.svg"
                url = base_url.rstrip("/") + "/api/icon-artwork/svg?icon=" + quote(key, safe="")
                with work_queue.open_url(url) as response:
                    before.write_bytes(response.read())
                work_queue.upload_result(base_url, worker, key, sha, "before", before, note=args.note)
                record["before_sha"] = sha
            validation = work_dir / "validation.txt"
            validation.write_text(validation_text(redraw_py))
            work_queue.upload_result(base_url, worker, key, sha, "after", redraw_svg, redraw_py, validation, note=args.note)
            record["after"] = str(redraw_svg.relative_to(REPO))
            record["validation"] = validation.read_text().splitlines()[0]
            if not args.no_done:
                work_queue.call(base_url, "POST", "/api/work/done",
                                {"icon": key, "svg_sha256": sha, "worker": worker, "note": args.note})
                record.update(done=now(), state="done")
            count += 1
            print(f"{line}  @{sha[:8]} uploaded{'' if args.no_done else ' + done'} · {record['validation']}")
        except work_queue.ApiError as e:
            record["error"] = f"{e.status}: {e}"
            print(f"{line}  FAILED {record['error']}")
        except Exception as e:  # network, missing file
            record["error"] = f"{type(e).__name__}: {e}"
            print(f"{line}  FAILED {record['error']}")
        state[key] = record
        state_path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    if not args.dry_run:
        print(f"{count}/{len(todo)} {'uploaded' if args.no_done else 'uploaded and reported done'}; state in {state_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
