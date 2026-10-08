#!/usr/bin/env python3
"""core/locks.py — review status of icons, and whether a locked one changed since.

Three statuses: READY (not reviewed yet: no record), LOCKED (reviewed, OK) and PENDING
(reviewed, not OK: needs fixing). Only LOCKED icons raise the changed-since warning; a pending
icon changing is expected (that is the fix), the page just notes it so it gets re-checked.

Locking an icon on the review page records a fingerprint of the three files it was judged on —
the input SVG, the all-round output and the all-sharp output. The lock list lives in
locks.json next to this file (NOT in corner48_outputs/, which every run rebuilds), so it
survives reruns and can be committed. After a run, any locked icon whose files no longer match
its fingerprint is reported as changed: core/toggle.py prints a warning, and the review
page marks the icon.

  python3 -m core.locks                 # list locked icons and which ones changed
"""

import hashlib
import json
import os
import sys
import tempfile
from datetime import datetime, timezone

from .svg_io import DEFAULT_INPUT

from .paths import LOCKS_PATH, OUT_DIR
PARTS = ("input", "round", "sharp")


def _digest(path):
    try:
        with open(path, "rb") as fh:
            return hashlib.sha1(fh.read()).hexdigest()[:12]
    except FileNotFoundError:
        return None


def fingerprint(name, input_dir=DEFAULT_INPUT, out_dir=OUT_DIR):
    """{'input': hash, 'round': hash, 'sharp': hash} of one icon's files (None if missing)."""
    return {"input": _digest(os.path.join(input_dir, name)),
            "round": _digest(os.path.join(out_dir, "round", name)),
            "sharp": _digest(os.path.join(out_dir, "sharp", name))}


def load(path=None):
    path = path or LOCKS_PATH
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return {}


def save(locks, path=None):
    """Write atomically, so a crash never leaves a half-written lock list."""
    path = path or LOCKS_PATH
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        json.dump(dict(sorted(locks.items())), fh, indent=1)
        fh.write("\n")
    os.replace(tmp, path)


STATUSES = ("locked", "pending")


def lock(locks, name, fp, note="", status="locked"):
    """Record a review: status 'locked' (OK) or 'pending' (not OK)."""
    locks[name] = {"fp": fp, "at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
                   "status": status, **({"note": note} if note else {})}


def status(rec):
    return rec.get("status", "locked")          # records from before statuses existed: locked


def changed_parts(rec, fp, parts=PARTS):
    """Which of input / round / sharp differ from the locked fingerprint ([] = unchanged)."""
    return [p for p in parts if rec["fp"].get(p) != fp.get(p)]


def changed_locks(names=None, input_dir=DEFAULT_INPUT, out_dir=OUT_DIR, locks=None, parts=PARTS):
    """{name: [changed parts]} for locked icons (optionally only those in names, and only the
    given parts — a run that built only the sharp output compares input + sharp)."""
    locks = load() if locks is None else locks
    out = {}
    for name, rec in locks.items():
        if status(rec) != "locked" or (names is not None and name not in names):
            continue
        diff = changed_parts(rec, fingerprint(name, input_dir, out_dir), parts)
        if diff:
            out[name] = diff
    return out


def warn(changed, stream=sys.stdout):
    if not changed:
        return
    print(f"  WARNING: {len(changed)} LOCKED icon(s) changed since lock-in "
          f"(review them, then re-lock or unlock on the report page):", file=stream)
    for name, parts in sorted(changed.items()):
        print(f"    {name}: {', '.join(parts)} changed", file=stream)


def main():
    locks = load()
    changed = changed_locks(locks=locks)
    n_locked = sum(status(r) == "locked" for r in locks.values())
    print(f"{n_locked} locked, {len(locks) - n_locked} pending (reviewed, not OK) in {LOCKS_PATH} | "
          f"{len(changed)} locked changed since lock-in")
    warn(changed)
    return 1 if changed else 0


if __name__ == "__main__":
    sys.exit(main())
