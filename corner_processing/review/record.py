#!/usr/bin/env python3
"""review/record.py — record the review of one icon: its status and note in review/status.json, and a decision
(when there is one) as a line in review/decisions.jsonl.

  python3 review/record.py batch-001 north-east.svg --status ok --note "both outputs read as the input"
  python3 review/record.py batch-001 north-east.svg --status proposed --decision "adjust sharp output" \\
      --case "meaningful round corners" --paths '{"cover": {"old": "M40 4L8 4...", "new": "M40 4L14 4A6 6 ..."}}' --note "spine side kept round"
  python3 review/record.py batch-001 book-open-1.svg --status proposed --decision keep \\
      --corners '[{"p": [24, 8], "decision": "keep", "why": "..."}]' --note "..."

--status ok | proposed (the AI reviewer decides every icon; nothing is left for a human). decided | applied | todo
only with --reviewer "user ...". needs-user is gone (2026-10-08): earlier needs-user icons are taken again by
next_batch.py and decided.
"""

import argparse
import datetime
import json
import os
import sys

from next_batch import HERE, load_status, save_status, status_lock

STATUSES = ("ok", "proposed", "decided", "applied", "todo")
DECISIONS = ("round or sharp", "corner", "keep")   # older records also hold redraw input / adjust ... / report


def main(argv=None):
    ap = argparse.ArgumentParser(description="Record the review of one icon.")
    ap.add_argument("batch", help="the batch the icon was claimed in (batch-NNN)")
    ap.add_argument("icon")
    ap.add_argument("--status", required=True, choices=STATUSES)
    ap.add_argument("--note", required=True, help="one or two sentences: what you saw and why")
    ap.add_argument("--decision", choices=DECISIONS)
    ap.add_argument("--case", help="the skill case it follows (tight curve, meaningful round corners, ...)")
    ap.add_argument("--paths", help='JSON {"path id": {"old": d, "new": d}} (redraw / adjust decisions)')
    ap.add_argument("--corners", help='JSON [{"p": [x, y], "decision": "corner"|"keep", "why": ...}]')
    ap.add_argument("--reviewer", default=os.environ.get("CORNER_REVIEWER", "ai"), help="model id, or 'user ...'")
    cfg = ap.parse_args(argv)
    name = cfg.icon if cfg.icon.endswith(".svg") else cfg.icon + ".svg"
    if cfg.status == "proposed" and not cfg.decision:
        raise SystemExit("--status proposed needs a --decision")
    if cfg.status in ("decided", "applied", "todo") and not cfg.reviewer.startswith("user"):
        raise SystemExit(f"--status {cfg.status} is the user's; the AI records ok or proposed")

    with status_lock():
        return _record(cfg, name)


def _record(cfg, name):
    s = load_status()
    entry = next((e for e in s["icons"] if e["icon"] == name), None)
    if entry is None:
        raise SystemExit(f"{name} is not in status.json")
    claim = entry.get("claim") or {}
    if entry["status"] == "reviewing" and claim.get("batch") not in (None, cfg.batch):
        raise SystemExit(f"{name} is claimed by {claim.get('batch')} ({claim.get('by')}), not {cfg.batch}")
    t = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    if cfg.decision:
        rec = {"icon": name, "decision": cfg.decision, "batch": cfg.batch}
        if cfg.case:
            rec["case"] = cfg.case
        if cfg.paths:
            rec["paths"] = json.loads(cfg.paths)
        if cfg.corners:
            rec["corners"] = json.loads(cfg.corners)
        rec.update(why=cfg.note, reviewer=cfg.reviewer, at=t)
        with open(os.path.join(HERE, "decisions.jsonl"), "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        entry["decision"] = {k: rec[k] for k in ("decision", "case") if k in rec}
    else:
        entry.pop("decision", None)                       # an earlier decision no longer holds
    entry["status"] = cfg.status
    entry["note"] = cfg.note
    entry["reviewed"] = {"batch": cfg.batch, "by": cfg.reviewer, "at": t}
    entry.pop("claim", None)
    save_status(s)
    open_left = sum(e["status"] == "reviewing" and (e.get("claim") or {}).get("batch") == cfg.batch for e in s["icons"])
    print(f"{name}: {cfg.status}{' · ' + cfg.decision if cfg.decision else ''} ({open_left} left in {cfg.batch})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
