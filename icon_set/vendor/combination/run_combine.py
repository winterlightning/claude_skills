#!/usr/bin/env python3
"""Combine one icon out of its symbols' finished SVGs. One job, then exit.

`app/combine.py` decides what goes in — which reading of each composite, which
variant of each symbol's final, and the box measured for it — writes that out as
a spec, and spawns this:

    python3 combination/run_combine.py --spec /path/to/spec.json

Spawned rather than imported for the same reason `processing_script/` is: the
fold needs numpy, scipy, shapely and matplotlib, and the server needs none of
them. A missing dependency then costs one Execute press a readable message
instead of stopping the app from starting, and the engine's matplotlib state
never has to be shared with a long-lived process.

The spec, every path absolute:

    {"name": "Multiple Users Network",
     "id": "ico_mRu4pQJ4v0gzeLjM5p4pQLXc",
     "out_dir": "/…/db/combined/ico_mRu4pQJ4v0gzeLjM5p4pQLXc",
     "buffer_px": 128, "stroke": 51.2, "color": "#000000",
     "canvas": 1024, "grid": 24,
     "symbols": [{"sid": "sym_000229",
                  "file": "/…/db/finals/sym_000229/combined.svg",
                  "box": {"x": 1.2, "y": 3.4, "w": 8.0, "h": 6.0},
                  "area": 48.0, "ink": 0.31, "z": 2,
                  "slice": {"left": 10, "right": 25}}, …]}

`slice` is optional and says how much to cut off each side of THAT DRAWING —
percentages of its own bounding box — before it is placed. It is for a symbol
that is partly hidden in the icon it was measured in: the box is its visible
strokes, the final drawn for it is the whole shape, and what is left after the
cut is what fills the box.

`z` is optional and says which layer this symbol folds in at — 1 is the
bottom, the one everything above it cuts into. Symbols without one follow the
size rule: the biggest box is the bottom (see box_combine.layered).

Drawings are uniformly centred in their placement boxes and keep their
proportions. A box said by hand — a layout's slot, a box edited in the
combined-position popup — is the exception: it was drawn on the whole units of
the output canvas, so what lands in it is snapped onto them too, at the cost of
up to two percent of the drawing's proportions (`box_combine.snapped_size`).

Boxes are in the corpus' 24-unit grid — the units the library measures in — and
are scaled onto the canvas by `box_combine`, so the caller never has to know the
canvas size. After placement they are measured as one group, uniformly fitted
into the canvas' fixed-stroke safe area when needed, and centred. The relative
layout and drawing proportions survive; stroke width does not participate in the
scale. A symbol carrying a manual combined-box target keeps those final
coordinates after the natural group is fitted, including a target that extends
beyond the canvas — and a fold holding any such target is not re-centred at the
end, because those coordinates are the position.

The SVG is written in the engine's two groups: `main-icon-clipped` is the bottom
layer with the clearance cut out of it, `state-icon` is every layer folded on top
of it.

stdout carries the result JSON and nothing else. The engine `print()`s its way
through every step, so all of that is captured and written to
`<out_dir>/combine.log` instead — losing it would make a fold that went wrong
unreadable.

    {"ok": true, "stem": "…", "file": "combined.svg",
     "snapped_file": null, "snap_meta": null, "snap_error": "",
     "fold": {"order": [sid, …], "passes": [{…}, …]},
     "log": "…"}

`snapped_file` / `snap_meta` / `snap_error` are always null/empty: the key-shape
snap was not ported with the engine. They are in the contract because that is
where it goes when it is — see PROVENANCE.md.

Anything that goes wrong is `{"ok": false, "error": "…"}` and exit 1, with the
job folder left on disk to be looked at.
"""
import argparse
import contextlib
import io
import json
import re
import shutil
import sys
import time
import traceback
import uuid
from pathlib import Path

HERE = Path(__file__).resolve().parent

#: How much of the engine's output comes back with the answer. All of it is on
#: disk in combine.log; this is the part worth putting in an HTTP response.
LOG_TAIL = 8000

#: The most an SVG may weigh. A final is a few KB of strokes — anything near
#: this is not one, and the engine would spend a long time finding that out.
MAX_BYTES = 8 * 1024 * 1024

#: The sides a slice can take a percentage off. `box_combine.SIDES` is the same
#: tuple, and is deliberately not imported here: the spec is checked before the
#: engine is loaded, so that a spec with a typo in it is answered in a sentence
#: even on an interpreter where the four dependencies are missing.
SIDES = ("left", "right", "top", "bottom")

#: The anchors the ORIGINAL engine pipeline places a badge at. A spec carrying
#: `"layout"` asks for that pipeline — `icon_combination.combine.
#: process_svg_icons_4_steps_with_dynamic_alignment`, the "big icon + badge"
#: algorithm with its own preset sizes and positions — instead of the
#: box-driven fold. It takes exactly one main and one badge, so exactly 2
#: symbols; the bigger box is the main.
LAYOUTS = ("bottom-right", "bottom", "bottom-left", "right", "left",
           "top-right", "top", "top-left", "center")


def out(payload, code=0):
    """The one thing this writes to stdout."""
    print(json.dumps(payload))
    raise SystemExit(code)


def fail(msg):
    out({"ok": False, "error": msg}, 1)


def engine():
    """`box_combine`, or a readable error about the four dependencies.

    Imported here rather than at module scope so that a spec that is malformed
    is answered without paying for matplotlib's import first, and so the
    "install these" message is produced by code that has already parsed its
    arguments.
    """
    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))
    try:
        import box_combine  # noqa: PLC0415 — see docstring
    except Exception as e:  # noqa: BLE001
        fail(f"the combination engine cannot start ({e}). It needs numpy, "
             f"scipy, shapely and matplotlib in {sys.executable} — "
             f"python3 -m pip install -r combination/requirements.txt")
    return box_combine


def slug(text):
    """A filename-safe stem from an icon's name."""
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return s[:60] or "icon"


def read_spec(path):
    try:
        spec = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        fail(f"cannot read the spec ({e})")
    if not isinstance(spec, dict):
        fail("the spec must be a JSON object")
    if not spec.get("out_dir"):
        fail("the spec has no out_dir")
    items = spec.get("symbols")
    if not isinstance(items, list) or not items:
        fail("the spec has no symbols to combine")
    layout = spec.get("layout")
    if layout is not None:
        if layout not in LAYOUTS:
            fail(f"{layout!r} is not a layout — say one of " + ", ".join(LAYOUTS))
        if len(items) != 2:
            fail(f"a layout combine takes exactly 2 symbols, not {len(items)}")
    return spec


def load(items):
    """Check every symbol's SVG and box before anything heavy is imported.

    The engine would fail on a non-SVG deep inside its own parser, and on a
    zero-width box with a division; these are the same refusals the utility
    app's route made, kept because the person pressing Execute has to be able
    to read what is wrong with which symbol.
    """
    out_items = []
    for n, it in enumerate(items):
        if not isinstance(it, dict):
            fail(f"symbols[{n}] is not an object")
        sid = str(it.get("sid") or f"symbol{n}")
        f = Path(str(it.get("file") or ""))
        if not f.is_file():
            fail(f"{sid}: its final is recorded but not on disk ({f})")
        size = f.stat().st_size
        if size == 0:
            fail(f"{sid}: its final is empty ({f})")
        if size > MAX_BYTES:
            fail(f"{sid}: its final is too large (max 8 MB)")
        with open(f, "rb") as fh:
            head = fh.read(4096).lower()
        if b"<svg" not in head:
            fail(f"{sid}: not an SVG (no <svg> element in the first 4 KB)")
        box = it.get("box") or {}
        try:
            box = {k: float(box[k]) for k in ("x", "y", "w", "h")}
        except Exception:  # noqa: BLE001
            fail(f"{sid}: box needs numeric x, y, w and h")
        if box["w"] <= 0 or box["h"] <= 0:
            fail(f"{sid}: box has no extent")
        natural_box = it.get("natural_box") or box
        try:
            natural_box = {k: float(natural_box[k])
                           for k in ("x", "y", "w", "h")}
        except Exception:  # noqa: BLE001
            fail(f"{sid}: natural_box needs numeric x, y, w and h")
        out_items.append({
            "candidate": it.get("candidate"),
            "sid": sid, "svg": f, "box": box, "natural_box": natural_box,
            "manual_combined": bool(it.get("manual_combined")),
            "preserve_geometry": bool(it.get("preserve_geometry")),
            "rounded_box": bool(it.get("rounded_box")),
            "area": float(it.get("area") or (box["w"] * box["h"])),
            "ink": float(it.get("ink") or 0.0),
            "z": read_z(sid, it.get("z")),
            "slice": read_slice(sid, it.get("slice")),
        })
    return out_items


def read_z(sid, z):
    """One symbol's layer as the fold wants it -> int, or None for "follow the
    size rule". Checked before the engine loads, for the same reason
    `read_slice` is: a spec can be written by hand, and a layer that is not a
    whole number should be a sentence rather than a TypeError out of a sort."""
    if z is None:
        return None
    try:
        f = float(z)
        if not f.is_integer() or f < 1:
            raise ValueError
        return int(f)
    except (TypeError, ValueError):
        fail(f"{sid}: z must be a whole number of 1 or more (1 is the bottom "
             f"layer), not {z!r}")


def read_slice(sid, cuts):
    """One symbol's slice as the fold wants it -> {side: percent}, or None.

    Checked here rather than trusted from the spec, because this is a CLI and a
    spec can be written by hand: a side that is not a side, or a pair that would
    leave nothing, should be a sentence rather than an exception out of the
    middle of the fold. The app checks the same things when the numbers are
    typed (db.clean_slice) — a rule worth having in both places, since either
    end can be used without the other.
    """
    if not cuts:
        return None
    if not isinstance(cuts, dict):
        fail(f"{sid}: slice must be an object of side -> percent")
    out = {}
    for k, v in cuts.items():
        if k not in SIDES:
            fail(f"{sid}: {k!r} is not a side to slice — "
                 f"say {', '.join(SIDES)}")
        try:
            v = float(v)
        except (TypeError, ValueError):
            fail(f"{sid}: slice {k} must be a number of percent, not {v!r}")
        if v < 0 or v >= 100:
            fail(f"{sid}: slice {k} must be between 0 and 100, not {v:g}")
        if v:
            out[k] = v
    for a, b in (("left", "right"), ("top", "bottom")):
        if out.get(a, 0) + out.get(b, 0) >= 100:
            fail(f"{sid}: slice {a} and {b} come to "
                 f"{out.get(a, 0) + out.get(b, 0):g}% — that leaves nothing of "
                 f"the drawing to place")
    return out or None


def prepare(out_dir):
    """The job folder, emptied of what the last run left.

    `work/` goes entirely: it holds one cleaned input per symbol and one SVG per
    fold pass, and a re-run against a different set of symbols would otherwise
    leave files describing a fold that no longer happened. A stale
    `combined_snapped.svg` goes for the same reason — this build does not snap,
    so any copy of that name is from a run that did, and reading it beside a
    fresh `combined.svg` would be comparing two different icons.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    work = out_dir / "work"
    shutil.rmtree(work, ignore_errors=True)
    work.mkdir(parents=True, exist_ok=True)
    (out_dir / "combined_snapped.svg").unlink(missing_ok=True)
    return work


def run_layout(layout, items, boxer, work, target, stroke, buffer_px,
               canvas, color):
    """The original main+badge pipeline at its preset places -> a fold record.

    The bigger box is the main; the engine decides where both go — its
    per-position scale for the main, the badge's 512x512 canvas at the anchor
    — so the measured boxes of the spec are deliberately unused. The spec's
    `stroke` and `buffer_px` DO apply, the same way they do to the box fold:
    stroke is the width the result is drawn at (the library's finals are
    51.2 on the 1024 canvas; the engine's own default of 25 comes out
    visibly thinner next to them), and buffer_px is the clearance cut round
    the badge's hull. The colours are black because the engine's defaults are
    its red/blue debug pair (the same override its own example usage makes).

    The engine places centrelines out to the canvas edge, so half the stroke
    would paint outside it and be clipped. Its own raw write is kept in
    `work/layout_raw.svg`; the file that counts is the merged segments put
    through the same normalization the box fold uses — `group_transform`
    fits them into the fixed-stroke safe area and centres them — and written
    by the same writer, main and badge each in its own group.
    """
    from icon_combination.combine import (  # noqa: PLC0415 — needs engine()'s
        process_svg_icons_4_steps_with_dynamic_alignment)  # sys.path insert
    a, b = items
    main_item, state_item = (a, b) if a["area"] >= b["area"] else (b, a)
    main_svg = boxer.clean_to(main_item["svg"], work / "layout_main.svg")
    state_svg = boxer.clean_to(state_item["svg"], work / "layout_state.svg")
    result = process_svg_icons_4_steps_with_dynamic_alignment(
        str(main_svg), str(state_svg), str(work / "layout_raw.svg"),
        position=layout, buffer_radius=buffer_px,
        main_stroke_width=stroke, state_stroke_width=stroke,
        main_color="#000000", state_color="#000000")
    if not result or not result.get("step4_saved"):
        raise RuntimeError(
            f"the {layout} layout produced nothing for "
            f"{main_item['sid']} + {state_item['sid']}")
    merged = result.get("step3_merged") or {}
    main = merged.get("clipped_segments") or []
    badge = merged.get("positioned_state_segments") or []
    # measured together and moved together, so the one uniform transform keeps
    # the badge exactly where the engine put it against the main
    scale, dx, dy, norm = boxer.group_transform(
        [main, badge], canvas=canvas, stroke=stroke)
    main = boxer.transform_segments(main, scale, dx, dy)
    badge = boxer.transform_segments(badge, scale, dx, dy)
    boxer.write_svg(main, target, stroke=stroke, color=color, canvas=canvas,
                    state=badge)
    return {"order": [main_item["sid"], state_item["sid"]], "layout": layout,
            "normalization": norm}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--spec", required=True,
                    help="the JSON spec to combine (see this file's docstring)")
    args = ap.parse_args(argv)

    spec = read_spec(args.spec)
    items = load(spec["symbols"])
    boxer = engine()

    # int when it is whole: the writer interpolates the canvas straight into
    # width/height/viewBox, so a float would ship `1024.0` where every other
    # producer in the library writes `1024`
    canvas = spec.get("canvas") or boxer.CANVAS
    canvas = int(canvas) if float(canvas).is_integer() else float(canvas)
    stroke = spec.get("stroke", 51.2)
    stroke = int(stroke) if float(stroke).is_integer() else float(stroke)
    # The UI and current specs use exact engine pixels. Keep both older units
    # readable so an existing saved job can still be reproduced.
    if spec.get("buffer_px") is not None:
        buffer_px = float(spec["buffer_px"])
    elif spec.get("buffer_strokes") is not None:
        buffer_px = float(spec["buffer_strokes"]) * stroke
    else:
        buffer_px = float(spec.get("buffer_pct", 12.5)) * canvas / 100
    color = spec.get("color") or "#000000"
    out_dir = Path(spec["out_dir"])
    work = prepare(out_dir)
    target = out_dir / "combined.svg"

    # each pass written out as it happens: with three symbols or more the fold
    # is several erasures deep, and "the result is wrong" is not a useful thing
    # to be told without the step it went wrong at
    def keep_pass(n, sid, segs):
        boxer.write_svg(segs, work / f"pass{n}_{sid}.svg",
                        stroke=stroke, color=color, canvas=canvas)

    buf = io.StringIO()
    fold = None
    try:
        with contextlib.redirect_stdout(buf):
            if spec.get("layout"):
                fold = run_layout(spec["layout"], items, boxer, work, target,
                                  stroke, buffer_px, canvas, color)
            else:
                segments, state, fold = boxer.fold(
                    items, buffer_radius=buffer_px, canvas=canvas,
                    stroke=stroke,
                    work_dir=work, on_pass=keep_pass if len(items) > 2 else None)
                boxer.write_svg(segments, target, stroke=stroke, color=color,
                                canvas=canvas, state=state)
    except Exception as e:  # noqa: BLE001 — the caller shows this to a person
        log = buf.getvalue()
        (out_dir / "combine.log").write_text(
            log + "\n" + traceback.format_exc(), encoding="utf-8")
        fail(f"combine failed: {e}\n{log[-600:]}")

    log = buf.getvalue()
    (out_dir / "combine.log").write_text(log, encoding="utf-8")

    out({
        "ok": True,
        # kept for the record the library holds of this combination; the job
        # folder is named by icon id, so this is the only thing that says when
        "stem": (f"{slug(spec.get('name'))}-{time.strftime('%Y%m%d-%H%M%S')}"
                 f"-{uuid.uuid4().hex[:4]}"),
        "file": target.name,
        "snapped_file": None,      # not built here — see PROVENANCE.md
        "snap_meta": None,
        "snap_error": "",
        "buffer_px": buffer_px,
        "fold": fold,
        "log": log[-LOG_TAIL:],
    })


if __name__ == "__main__":
    main()
