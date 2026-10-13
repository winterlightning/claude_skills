#!/usr/bin/env python3
"""core/keyshape.py — each icon's SOLO48 keyshape, detected from the input's ink.

A keyshape is the centred visible-ink envelope an icon is drawn to. The SOLO48 choices and
sizes come from the claude_skills contract (circle 44, square 40, landscape 44x36 / 44x32,
portrait 36x44 / 32x44). Here the keyshape is RE-DETECTED from what the input actually draws,
not taken from the model's declaration:

  1. render the input (rsvg-convert, 0.1 u steps) and take its ink box and centre
  2. the keyshape whose box best matches the ink box's SIZE (smallest largest-edge gap), ties
     by proportions (smallest |log ratio|); CIRCLE is a candidate only when the ink is round:
     every inked pixel within the box's own half-width of its centre (ratio <= ROUND_RATIO; a
     square drawing reaches ~1.4 at its corners) and the box about square

Then, for the input and both outputs, how far the rendered ink (caps and joins included)
reaches past that keyshape. The model's declared keyshape is kept as "declared" for
comparison (claude_skills registry, read only; *-upload-* icons have none).

  python3 -m core.keyshape --input-only            # before core/toggle.py (its keyshape fit)
  python3 -m core.keyshape                         # -> corner48_outputs/keyshapes.json
  python3 -m core.keyshape --skills ../../claude_skills
"""

import argparse
import json
import math
import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from io import BytesIO

import numpy as np
from PIL import Image

from .svg_io import DEFAULT_INPUT

from .paths import OUT_DIR, SKILLS
PAD, PX = 8, 10        # raster: 8 u margin round the canvas, 10 px per u (0.1 u steps)
ROUND_RATIO = 1.05     # ink's farthest pixel / half its box width: <= this is a round drawing
SQUARE_ASPECT = 1.11   # a round drawing's box is about square (w/h within 1/1.11 .. 1.11)
OVER_TOL = 0.1         # u — ink this little past the keyshape is on it, not outside
PARTS = ("input", "round", "sharp")


def ink_mask(path):
    """Rendered ink of an SVG as a boolean array over (-PAD .. 48+PAD) u."""
    root = ET.parse(path).getroot()
    size = (48 + 2 * PAD) * PX
    root.set("viewBox", f"{-PAD} {-PAD} {48 + 2 * PAD} {48 + 2 * PAD}")
    root.set("width", str(size))
    root.set("height", str(size))
    png = subprocess.run(["rsvg-convert", "-f", "png"], input=ET.tostring(root), capture_output=True,
                         check=True).stdout
    return np.asarray(Image.open(BytesIO(png)).convert("RGBA"))[:, :, 3] > 127


def _box(xs, ys):
    return [round(float(xs.min()) / PX - PAD, 1), round(float(ys.min()) / PX - PAD, 1),
            round(float(xs.max() + 1) / PX - PAD, 1), round(float(ys.max() + 1) / PX - PAD, 1)]


def detect(mask, shapes):
    """Keyshape name for this ink, plus the ink box, aspect and roundness it was chosen on."""
    ys, xs = np.nonzero(mask)
    if not len(xs):
        return None, {}
    l, t, r, b = _box(xs, ys)
    w, h = r - l, b - t
    cx, cy = (l + r) / 2, (t + b) / 2
    reach = float(np.hypot((xs + .5) / PX - PAD - cx, (ys + .5) / PX - PAD - cy).max())
    ratio = reach / (max(w, h) / 2)
    aspect = w / h
    info = {"ink": [l, t, r, b], "aspect": round(aspect, 3), "roundness": round(ratio, 3)}
    round_ink = ratio <= ROUND_RATIO and 1 / SQUARE_ASPECT <= aspect <= SQUARE_ASPECT
    # the keyshape whose box best matches the ink's size (largest edge gap), then proportions;
    # CIRCLE only for round ink (a 40 x 40 plus sign reaches its circle only at its arm tips:
    # it is a SQUARE drawing, not a 44 circle)
    cands = [(round(max(abs(w - s["w"]), abs(h - s["h"])), 1), abs(math.log(aspect / (s["w"] / s["h"]))), n)
             for n, s in shapes.items() if round_ink or not s.get("r")]
    return min(cands)[2], info


def overflow(rec, mask):
    """How far the drawn ink reaches past the keyshape (u, 0 = inside) and on which sides."""
    ys, xs = np.nonzero(mask)
    if not len(xs):
        return 0.0, []
    l, t, r, b = rec["bounds"]
    if rec.get("r"):
        cx, cy = (l + r) / 2, (t + b) / 2
        ux, uy = (xs + .5) / PX - PAD - cx, (ys + .5) / PX - PAD - cy
        d = np.hypot(ux, uy)
        k = int(d.argmax())
        over = d[k] + .5 / PX - rec["r"]
        sides = [("top" if uy[k] < 0 else "bottom") if abs(uy[k]) > abs(ux[k]) else
                 ("left" if ux[k] < 0 else "right")]
    else:
        il, it, ir, ib = _box(xs, ys)
        by = {"left": l - il, "top": t - it, "right": ir - r, "bottom": ib - b}
        over = max(by.values())
        sides = [k for k, v in by.items() if v > OVER_TOL]
    over = round(float(over), 1)
    return (over, sides) if over > OVER_TOL else (0.0, [])


def _one(args):
    name, files, shapes = args
    try:
        m = ink_mask(files["input"])
        ks, info = detect(m, shapes)
        if ks is None:
            return name, {"keyshape": None, "source": "no ink"}
        rec = {"keyshape": ks, **shapes[ks], **info, "source": "ink", "over": {}, "sides": {}}
        for part in PARTS:
            if part in files:
                rec["over"][part], rec["sides"][part] = overflow(rec, m if part == "input" else ink_mask(files[part]))
        return name, rec
    except Exception as e:                           # noqa: BLE001 — report, keep going
        return name, {"keyshape": None, "source": "error", "error": f"{type(e).__name__}: {e}"[:200]}


def skills_shapes_and_declared(skills, names):
    """SOLO48 keyshape choices {name: {bounds, size, w, h[, r]}} and each icon's declared keyshape."""
    sys.dont_write_bytecode = True                   # read only towards claude_skills
    sys.path.insert(0, os.path.abspath(skills))
    from icon_set.model import contracts
    from icon_set.model.icons.registry import create, factories
    from icon_set.model.keyshapes import Keyshape
    from icon_set.model.profiles import Profile

    solo = Profile.SOLO48
    shapes = {}
    for n in contracts.icon_profile()["profiles"][solo.name]["keyshape_choices"]:
        k = Keyshape[n]
        l, t, r, b = k.bounds_for(solo)
        shapes[n] = {"bounds": [l, t, r, b], "size": f"{r - l}×{b - t}", "w": r - l, "h": b - t}
        if k.is_radial:
            shapes[n]["r"] = k.visible_radius_for(solo)
    known, declared = factories(), {}
    for name in names:
        if name[:-4] in known:
            try:
                declared[name] = create(name[:-4]).keyshape.name
            except Exception:                        # noqa: BLE001
                pass
    return shapes, declared


def main(argv=None):
    ap = argparse.ArgumentParser(description="Each icon's SOLO48 keyshape, detected from its ink.")
    ap.add_argument("--input", default=DEFAULT_INPUT)
    ap.add_argument("--out", default=os.path.join(OUT_DIR, "keyshapes.json"))
    ap.add_argument("--skills", default=SKILLS, help="claude_skills repo (default: %(default)s)")
    ap.add_argument("--input-only", action="store_true",
                    help="detect and measure the input only (before core/toggle.py, which "
                         "needs the keyshapes; the outputs are measured by a full run after)")
    cfg = ap.parse_args(argv)

    names = sorted(n for n in os.listdir(cfg.input) if n.endswith(".svg"))
    shapes, declared = skills_shapes_and_declared(cfg.skills, names)
    csv_path = os.path.join(os.path.dirname(os.path.abspath(cfg.input)), "icons.csv")
    if os.path.exists(csv_path):                     # core/fetch.py: the Worker's declared
        import csv                                   # keyshape (also for icons whose model the
        with open(csv_path, encoding="utf-8") as f:  # local claude_skills checkout lacks)
            for row in csv.DictReader(f):
                if row.get("keyshape") and row["key"].startswith("solo/"):
                    declared[row["key"][5:] + ".svg"] = row["keyshape"]
    outs = os.path.dirname(cfg.out) or "."
    jobs = []
    for name in names:
        files = {"input": os.path.join(cfg.input, name)}
        for part in () if cfg.input_only else ("round", "sharp"):
            f = os.path.join(outs, part, name)
            if os.path.exists(f):
                files[part] = f
        jobs.append((name, files, shapes))
    out = {}
    with ProcessPoolExecutor() as ex:
        for name, rec in ex.map(_one, jobs, chunksize=16):
            rec.pop("w", None), rec.pop("h", None)
            if name in declared:
                rec["declared"] = declared[name]
            out[name] = rec

    os.makedirs(outs, exist_ok=True)
    with open(cfg.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=0, ensure_ascii=False)
    ks = Counter(v["keyshape"] or "—" for v in out.values())
    print(f"wrote {cfg.out} ({len(out)} icons) | detected from ink: " +
          ", ".join(f"{k} {n}" for k, n in ks.most_common()))
    # SOLO48 legacy names are the same box (HRECT_XL = HRECT_L): compare by size
    same = lambda v: v["declared"] == v["keyshape"] or (v["declared"].replace("_XL", "_L") == v["keyshape"])  # noqa: E731
    dec = [v for v in out.values() if v.get("declared") and v.get("keyshape")]
    print(f"  vs model's declared keyshape: {sum(map(same, dec))} same, {sum(not same(v) for v in dec)} different "
          f"({len(out) - len(dec)} without a model)")
    for part in PARTS:
        o = [v["over"].get(part, 0) for v in out.values() if v.get("over")]
        print(f"  ink outside keyshape · {part}: {sum(x > 0 for x in o)} icons (max {max(o, default=0):g} u)")
    for n, v in [(n, v) for n, v in out.items() if v["source"] == "error"][:10]:
        print("  ERROR", n, v["error"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
