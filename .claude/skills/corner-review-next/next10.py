#!/usr/bin/env python3
"""next10.py — claim the next icons nobody has reviewed yet (status `todo`) and print a short summary of each.

Runs corner_processing/review/next_batch.py (most-flagged first; a `reviewing` claim older than 6 h counts as free
again), then prints, per icon: its sheet, flags, the sharp check, and the corners the sharp output changed or kept.

  python3 .claude/skills/corner-review-next/next10.py              # 10 icons
  python3 .claude/skills/corner-review-next/next10.py --take 5 --offset 20   # skip the first 20 free icons
  python3 .claude/skills/corner-review-next/next10.py --flag narrow-points    # only icons with this flag
"""
import argparse
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "corner_processing"))


def corners(log):
    out = []
    for c in log:
        p = "%g,%g" % tuple(c["p"])
        r = " r%g" % c["r"] if "r" in c else ""
        why = " (%s)" % c["why"] if c.get("why") else ""
        out.append(f"{p} {c.get('status', 'kept')}{r}{why}")
    return "; ".join(out) or "-"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--take", "--count", dest="take", type=int, default=10, help="how many icons (default 10)")
    ap.add_argument("--offset", type=int, default=0, help="skip this many free todo icons first (list order)")
    ap.add_argument("--flag", help="only icons with this flag (see review/status.json)")
    cfg = ap.parse_args()
    args = ["--count", str(cfg.take), "--offset", str(cfg.offset)] + (["--flag", cfg.flag] if cfg.flag else [])
    run = subprocess.run([sys.executable, "review/next_batch.py", *args],
                         cwd=ROOT, capture_output=True, text=True)
    print(run.stdout.strip().splitlines()[0] if run.stdout.strip() else "")
    if run.returncode:
        sys.exit(run.stderr or "next_batch.py failed")
    m = re.search(r"(batch-\d+)", run.stdout)
    if not m:
        sys.exit("no batch claimed (nothing todo?)\n" + run.stdout)
    batch = m.group(1)
    data = json.load(open(os.path.join(ROOT, "review", "batches", batch, "batch.json")))
    print(f"\nbatch {batch}: {len(data['icons'])} icons (corner_processing/review/batches/{batch}/)\n")
    for e in data["icons"]:
        print(f"== {e['icon']}  flags: {', '.join(e['flags']) or 'none'}  sharp check: {e['check']['sharp']}")
        print(f"   sheet: corner_processing/{e['sheet']}")
        print(f"   sharp: {corners(e['sharp_log'])}")
        if e.get("shared_keep"):
            print(f"   kept in both: {corners(e['shared_keep'])}")
    print(f"\nrecord each:  cd corner_processing && python3 review/record.py {batch} ICON --status ok|proposed ...")


if __name__ == "__main__":
    main()
