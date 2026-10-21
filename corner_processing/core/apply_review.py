#!/usr/bin/env python3
"""core/apply_review.py - write the AI corner review's sharp decisions into the sharp outputs.

The corner review (review/status.json + decisions.jsonl, the /corner-review skill) records each sharp-output fix as path
changes {id: {old, new}}; the processing never reads them. Run this after round_/sharp_corner_processing.py and
before core.publish, so the published sharp icons carry the reviewed corners. A re-run is safe: a path already
changed is skipped. An old path that is no longer in the output (the input was redrawn since the review) is left
alone and reported, so that icon can be reviewed again.

  python3 -m core.apply_review                 # outputs/solo48/sharp, every proposed / decided sharp fix
  python3 -m core.apply_review --out outputs/icon72
  python3 -m core.apply_review --dry-run       # report only
  python3 -m core.apply_review --files abdominal-torso.svg

Input redraws ("redraw input") are not applied here: they go into input_fixes/ (re-applied by core.fetch).
"""

import argparse
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

from .paths import OUT_DIR, SETS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REVIEW_DIR = os.path.join(ROOT, "review")
SHARP_DECISIONS = ("round or sharp", "adjust sharp output", "keep", "corner")
OPEN = ("proposed", "decided", "applied")
norm = lambda d: " ".join(d.split())


def reviewed(files=None):
    """{icon: decision} for every icon whose review is open and whose latest decision changes the sharp output."""
    status = {e["icon"]: e["status"] for e in json.load(open(os.path.join(REVIEW_DIR, "status.json"), encoding="utf-8"))["icons"]}
    last = {}
    for line in open(os.path.join(REVIEW_DIR, "decisions.jsonl"), encoding="utf-8"):
        if line.strip():
            try:
                d = json.loads(line)
            except ValueError:
                continue
            last[d["icon"]] = d
    return {i: d for i, d in last.items() if status.get(i) in OPEN and d.get("decision") in SHARP_DECISIONS
            and d.get("paths") and (not files or i in files)}


def apply_one(path, changes):
    """Apply {id: {old, new}} to the SVG file at path, in place. -> (changed, already, missing) path ids."""
    text = open(path, encoding="utf-8").read()
    root = ET.fromstring(text)
    by_id = {}
    for el in root.iter():
        if el.get("id"):                     # a clipPath's id names the path inside it (keyshape-cut)
            d = el.get("d") if el.get("d") is not None else next((c.get("d") for c in el.iter() if c.get("d") is not None), None)
            if d is not None:
                by_id[el.get("id")] = d
    ds = [el.get("d") for el in root.iter() if el.get("d") is not None]
    changed, already, missing = [], [], []
    for pid, c in changes.items():
        if "new" not in c:
            missing.append(pid)
            continue
        cur = by_id.get(pid)
        if "old" not in c:                   # an older record form: the path's whole new drawing, by id
            if cur is None:
                missing.append(pid)
            elif norm(cur) == norm(c["new"]):
                already.append(pid)
            else:
                text = text.replace(f'd="{cur}"', f'd="{c["new"]}"', 1)
                changed.append(pid)
            continue
        if cur is None:                      # id-less shape ("path#7"): found by its drawing
            cur = next((d for d in ds if norm(d) == norm(c["old"])), None) or \
                  next((d for d in ds if norm(d) == norm(c["new"])), None)
        if cur is None:
            missing.append(pid)
        elif norm(cur) == norm(c["new"]):
            already.append(pid)
        elif norm(cur) == norm(c["old"]):
            text = text.replace(f'd="{cur}"', f'd="{c["new"]}"', 1)
            changed.append(pid)
        else:
            missing.append(pid)
    return text, changed, already, missing


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default=os.path.join(OUT_DIR, SETS["solo"]), help="outputs folder (default: %(default)s)")
    ap.add_argument("--files", nargs="+", help="only these icons (file names, .svg optional)")
    ap.add_argument("--dry-run", action="store_true")
    cfg = ap.parse_args(argv)
    files = {f if f.endswith(".svg") else f + ".svg" for f in cfg.files} if cfg.files else None
    done, same, stale, absent = [], [], [], []
    for icon, dec in sorted(reviewed(files).items()):
        path = os.path.join(cfg.out, "sharp", icon)
        if not os.path.exists(path):
            absent.append(icon)
            continue
        text, changed, already, missing = apply_one(path, dec["paths"])
        if missing:                          # all or nothing: a half-applied fix is worse than none
            stale.append((icon, missing))
            continue
        if changed:
            if not cfg.dry_run:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(text)
            done.append(icon)
        else:
            same.append(icon)
    verb = "would apply" if cfg.dry_run else "applied"
    print(f"{verb} {len(done)} · already applied {len(same)} · stale {len(stale)} · no sharp output {len(absent)}")
    for icon, missing in stale:
        print(f"  stale (output changed since the review): {icon}  paths {', '.join(missing)}")
    for icon in absent:
        print(f"  no sharp output: {icon}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
