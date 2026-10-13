#!/usr/bin/env python3
"""review/build_status.py — the corner review list: every icon with corners, its warning flags and its review status.

Writes review/status.json from the latest run (outputs/solo48: corners48.json, toggle.json, keyshapes.json) and
the decisions in review/decisions.jsonl. Re-run it after every processing run: the status, decision and note of
each icon already in status.json are kept; flags and counts are refreshed. Icons are listed most-flagged first,
so the review goes through the likely problems before the rest.

  python3 review/build_status.py
  python3 review/build_status.py --out-dir outputs      # a partial run's folder

Statuses (edit them in status.json, or by recording a decision):
  todo        not reviewed yet
  reviewing   taken by review/next_batch.py (a batch); back to todo after 6 h or --release
  ok          reviewed, both outputs are right
  proposed    the AI reviewer proposed a decision; the user has not confirmed it
  needs-user  (old) left for the user; next_batch.py takes it again and the AI decides it
  decided     the decision is final (in decisions.jsonl); not applied to the outputs yet
  applied     the decision is applied and published
"""

import argparse
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                       # corner_processing/
STATUSES = ("todo", "reviewing", "ok", "proposed", "needs-user", "decided", "applied")
NARROW = 60.0                                      # deg — a sharp-output point narrower than this reaches > 4 u (case 2)

# what each flag means, in the order they rank an icon (first = most urgent)
FLAGS = {
    "check-fail":        "an output failed the re-detect check",
    "point-past-ink":    "sharp output reaches past the keyshape further than the input does",
    "narrow-points":     f"sharp output has mitre points narrower than {NARROW:g} deg (never move the corner; round if the point grows the shape)",
    "lone-round-in-sharp": "sharp output keeps a round corner with a curved side (the books: a lone round corner)",
    "no-room":           "a corner had no room for its band radius (reduced or kept as drawn: a small feature?)",
    "big-round-kept":    "a big round is kept as drawn in both outputs (could be a corner: big-round decision)",
    "new-contact":       "an output touches another stroke where the input did not",
    "round-past-ink":    "round output reaches past the keyshape further than the input does",
}


def load_jsonl(path):
    out = []
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            if line.strip():
                out.append(json.loads(line))
    return out


def flags_of(v, ks):
    rl, sl = v.get("round", {}).get("log", []), v.get("sharp", {}).get("log", [])
    checks = [v.get(m, {}).get("check") or {} for m in ("round", "sharp")]
    keep = v.get("shared_keep", [])
    over = (ks or {}).get("over") or {}
    f = []
    if any(c.get("status") == "fail" for c in checks):
        f.append("check-fail")
    if over.get("sharp", 0) > over.get("input", 0):
        f.append("point-past-ink")
    if any(e.get("angle") and e["angle"] < NARROW and e["status"] in ("kept sharp", "sharpened") for e in sl):
        f.append("narrow-points")
    if any(e["status"] == "kept round" and e.get("why") == "curved side" for e in sl):
        f.append("lone-round-in-sharp")
    if any(e.get("reduced") or e["status"] == "skipped" for e in rl) or \
            any(k["why"] in ("no room to re-round", "no corner to re-round") for k in keep):
        f.append("no-room")
    if any(k["why"] == "too large for a corner" for k in keep):
        f.append("big-round-kept")
    if any(c.get("status") == "contact" for c in checks):
        f.append("new-contact")
    if over.get("round", 0) > over.get("input", 0):
        f.append("round-past-ink")
    return f


def main(argv=None):
    sys.path.insert(0, HERE)
    from next_batch import status_lock
    with status_lock():                    # parallel record.py / next_batch.py wait until the rewrite is done
        return _main(argv)


def _main(argv=None):
    ap = argparse.ArgumentParser(description="Build review/status.json, the corner review list.")
    ap.add_argument("--out-dir", default=os.path.join(ROOT, "outputs", "solo48"))
    ap.add_argument("--input", default=os.path.join(ROOT, "input", "solo48", "svg"))
    ap.add_argument("--status", default=os.path.join(HERE, "status.json"))
    cfg = ap.parse_args(argv)

    det = json.load(open(os.path.join(cfg.out_dir, "corners48.json"), encoding="utf-8"))
    tog = json.load(open(os.path.join(cfg.out_dir, "toggle.json"), encoding="utf-8"))["icons"]
    kp = os.path.join(cfg.out_dir, "keyshapes.json")
    kss = json.load(open(kp, encoding="utf-8")) if os.path.exists(kp) else {}
    old = {}
    if os.path.exists(cfg.status):
        old = {e["icon"]: e for e in json.load(open(cfg.status, encoding="utf-8"))["icons"]}
    decided = {}
    for e in load_jsonl(os.path.join(HERE, "decisions.jsonl")):
        decided[e["icon"]] = e                     # the latest decision per icon wins

    icons, no_corners = [], 0
    for name in sorted(tog):
        if not os.path.exists(os.path.join(cfg.input, name)) or name not in det:
            continue
        d, v = det[name], tog[name]
        n_corners = len(d["sharp"]) + len(d["round"])
        if not n_corners and name not in old and name not in decided:
            no_corners += 1
            continue
        prev = old.get(name, {})
        entry = {
            "icon": name,
            "status": prev.get("status", "todo"),
            "flags": flags_of(v, kss.get(name)),
            "corners": {"sharp": len(d["sharp"]), "round": len(d["round"])},
            "round": {"rounded": sum(e["status"] == "rounded" for e in v.get("round", {}).get("log", [])),
                      "check": (v.get("round", {}).get("check") or {}).get("status")},
            "sharp": {"sharpened": sum(e["status"] == "sharpened" for e in v.get("sharp", {}).get("log", [])),
                      "check": (v.get("sharp", {}).get("check") or {}).get("status")},
            "shared_keep": len(v.get("shared_keep", [])),
            "decision": prev.get("decision"),
            "note": prev.get("note", ""),
            **{k: prev[k] for k in ("claim", "reviewed") if k in prev},
        }
        if name in decided:                        # a recorded decision: the user's is final, the AI's a proposal
            e = decided[name]
            entry["decision"] = {k: e[k] for k in ("decision", "case") if k in e}
            final = str(e.get("reviewer", "")).startswith("user")
            if final and entry["status"] in ("todo", "proposed", "needs-user"):
                entry["status"] = "decided"
            elif not final and entry["status"] == "todo":
                entry["status"] = "proposed"
        icons.append(entry)

    rank = {f: i for i, f in enumerate(FLAGS)}
    icons.sort(key=lambda e: (STATUSES.index(e["status"]) if e["status"] in ("ok", "applied") else -1,
                              -len(e["flags"]), min((rank[f] for f in e["flags"]), default=99), e["icon"]))
    by_status = {s: sum(e["status"] == s for e in icons) for s in STATUSES}
    by_flag = {f: sum(f in e["flags"] for e in icons) for f in FLAGS}
    out = {
        "generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "source": os.path.relpath(cfg.out_dir, ROOT),
        "summary": {"icons_with_corners": len(icons), "icons_without_corners": no_corners,
                    "no_flags": sum(not e["flags"] for e in icons), "by_status": by_status, "by_flag": by_flag},
        "statuses": {s: l.split(None, 1)[1].strip() for s, l in
                     ((l.split()[0], l) for l in __doc__.split("Statuses")[1].splitlines()[1:] if l.strip())},
        "flags": FLAGS,
        "icons": icons,
    }
    with open(cfg.status, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"wrote {os.path.relpath(cfg.status, ROOT)}: {len(icons)} icons with corners "
          f"({no_corners} without) | " + ", ".join(f"{k} {v}" for k, v in by_status.items() if v))
    print("  flags: " + ", ".join(f"{k} {v}" for k, v in by_flag.items()) + f", none {out['summary']['no_flags']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
