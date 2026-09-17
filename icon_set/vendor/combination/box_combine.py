"""Combine an icon's symbols at the boxes measured for them, not at anchors.

`icon_combination` combines a main and a sub icon, and decides where both go: the
main is always re-normalised to fill `1024 x aspect_ratio` and moved to an anchor
(process_main.py:140-149), so pre-positioning it is pointless — the engine
re-measures and overrides. That is right for "big icon plus a badge", and wrong for
putting an icon back together, where the library already knows where every symbol sat.

So this enters the engine at its THIRD step. `merged_icons_and_remove_overlapping`
takes already-positioned segments and a plain dict, so steps 1-2 are replaced with
box-driven placement — every symbol through one `fit_into`, main and sub alike —
while the erasure, the hull buffering it reads and the SVG writer are reused
untouched. The engine itself is a verbatim port (see icon_combination/PROVENANCE.md)
and nothing here modifies it.

What comes out is the writer's two groups: `main-icon-clipped` is the bottom layer
with every clearance above it cut out, `state-icon` is everything folded on top.

The fold, for symbols sorted bottom layer to top:

    pass 1   main A    sub B   ->  AB   = cut(A, hull B) + B
    pass 2   main AB   sub C   ->  ABC  = cut(AB, hull C) + C
    pass 3   main ABC  sub D   ->  ABCD = cut(ABC, hull D) + D

The lower layer is always the main, which is the one that gets cut. By default the
layers follow size — the biggest box is z=1, the bottom — and an item's own `z`
overrides its place in that order. Because each pass feeds its whole result back in
as the next main, a later symbol also erases strokes of the ones folded in before it
— which is what sitting on top means. One symbol is not a special case with its own
code path; it is simply a fold with nothing to fold in.
"""
from __future__ import annotations

import math
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

from shapely.geometry import LineString
from shapely.ops import unary_union

from icon_combination.combine import (
    merged_icons_and_remove_overlapping,
    save_clipped_result_to_svg,
)
from icon_combination.process_main import _remove_clip_path_elements
from icon_combination.utils import (
    create_convex_hull_buffer,
    get_buffer_outlines,
    parse_svg_geometric_elements,
)

#: The corpus grid every measured box is expressed on.
GRID = 24.0

#: The engine's canvas. Boxes are scaled from GRID onto this.
CANVAS = 1024

#: The shortest piece the erasure cuts exactly. The engine's own 1.0 is one
#: pixel of the 1024 canvas it was written for; on the 64 canvas a whole
#: flattened stroke is a fifth of that, so every segment falls under it and is
#: kept or dropped whole by a midpoint test instead of being cut where the
#: clearance actually falls. Hold the ratio, so the cut is as fine on any
#: canvas as it was on 1024.
MIN_SEGMENT_PER_CANVAS = 1.0 / 1024


class CombineError(RuntimeError):
    """A symbol's SVG could not be read, or a fold produced nothing."""


_GEOM = ("path", "circle", "ellipse", "rect", "line", "polygon", "polyline")


def _tag(el):
    return el.tag.rsplit("}", 1)[-1].lower()


def strip_unstroked(root):
    """Drop geometry that carries no stroke, before the engine ever sees it.

    Every final in the library opens with `<rect width="1024" height="1024"
    fill="white"/>` — a backing plate that renders white on white and reads as
    nothing. The engine's parser has no notion of visibility though: it turns that
    rect into four segments, and the combined icon comes out with a square drawn
    round each symbol. Icons here are stroke-only (`fill="none" stroke="black"`),
    so "has a stroke" is exactly the test for ink.

    Stroke can come from an ancestor group, so the check walks down carrying it.
    """
    def inherited(el, stroke):
        s = el.get("stroke", stroke)
        return None if (s or "none").strip().lower() == "none" else s

    def prune(parent, stroke):
        for el in list(parent):
            s = inherited(el, stroke)
            if _tag(el) in _GEOM:
                if s is None:
                    parent.remove(el)
                continue
            prune(el, s)

    prune(root, inherited(root, None))
    return root


def clean_to(svg_path, out_path):
    """Write `svg_path` with its unstroked geometry removed.

    A file rather than an in-memory tree because the fold reads every symbol
    back off its path when it places it — the sub icons would otherwise keep the
    backing plate the main icon just had removed, and only half the fix would
    land.
    """
    root = ET.parse(str(svg_path)).getroot()
    _remove_clip_path_elements(root)
    strip_unstroked(root)
    ET.ElementTree(root).write(str(out_path), encoding="unicode",
                               xml_declaration=False)
    return Path(out_path)


def parse_segments(svg_path):
    """One SVG's geometry as line segments, the only form the engine works in.

    Curves are flattened here exactly as the engine flattens them, because it is
    the engine's own parser doing it.
    """
    root = ET.parse(str(svg_path)).getroot()
    _remove_clip_path_elements(root)
    strip_unstroked(root)
    segments, _points = parse_svg_geometric_elements(root, 1)
    if not segments:
        raise CombineError(f"no drawable geometry in {Path(svg_path).name}")
    return segments


def bbox(segments):
    """(x0, y0, x1, y1) of a segment list, or None when it is empty."""
    xs, ys = [], []
    for (a, b) in segments:
        xs += [a[0], b[0]]
        ys += [a[1], b[1]]
    return (min(xs), min(ys), max(xs), max(ys)) if xs else None


def box_to_canvas(box, grid=GRID, canvas=CANVAS):
    """A measured box in grid units -> (x, y, w, h) in canvas px."""
    k = canvas / grid
    return (box["x"] * k, box["y"] * k, box["w"] * k, box["h"] * k)


# ------------------------------------------------------------------ slicing
#
# A placement's box is measured off the icon the symbol was cut from, so for a
# symbol that is PARTLY HIDDEN there the box is the box of its visible strokes
# — while the final drawn for it is the whole shape. Placing the whole drawing
# in that box squeezes a whole person into the space of half a person, and no
# choice of variant fixes it. A slice cuts the drawing down to the part the box
# is about, first.
#
# Each side takes a percentage OFF itself, measured across the drawing's own
# bounding box: `{"left": 10, "right": 25}` keeps the middle 65%. The box, not
# the canvas — finals are not all drawn on the same one, and a percentage of
# the sheet would bite differently on every drawing.
#
# What is left is placed by the ordinary rule, so it fills the measured box:
# that is the point, since the box is the visible part.

#: The four sides, and which end of which axis each one eats.
SIDES = ("left", "right", "top", "bottom")


def keep_rect(segments, cuts):
    """The rectangle a slice keeps -> (x0, y0, x1, y1), in the drawing's units."""
    b = bbox(segments)
    if b is None:
        raise CombineError("cannot slice an empty symbol")
    x0, y0, x1, y1 = b
    w, h = x1 - x0, y1 - y0
    pct = lambda k: float(cuts.get(k) or 0) / 100.0   # noqa: E731
    return (x0 + w * pct("left"), y0 + h * pct("top"),
            x1 - w * pct("right"), y1 - h * pct("bottom"))


def _clip(seg, lo, hi, axis):
    """One segment against one axis' pair of bounds, or None when it is outside.

    Everything is straight by the time it gets here — the engine's parser
    flattens curves into segments — so a cut is exact: keep it, drop it, or move
    the outside end to where it crosses.
    """
    (ax, ay), (bx, by) = seg
    a, b = (ax, bx) if axis == 0 else (ay, by)
    t0, t1 = 0.0, 1.0
    d = b - a
    for sign, bound in ((-1.0, lo), (1.0, hi)):
        # sign*(a + t*d) <= sign*bound, i.e. t*(sign*d) <= sign*(bound - a)
        p, q = sign * d, sign * (bound - a)
        if abs(p) < 1e-12:                   # parallel to this bound
            if q < 0:
                return None                  # and outside it
            continue
        t = q / p
        if p > 0:
            t1 = min(t1, t)
        else:
            t0 = max(t0, t)
        if t0 > t1:
            return None
    if t0 <= 0 and t1 >= 1:
        return seg
    at = lambda t: (ax + (bx - ax) * t, ay + (by - ay) * t)   # noqa: E731
    return [at(max(t0, 0.0)), at(min(t1, 1.0))]


def slice_segments(segments, cuts, what=""):
    """Trim a drawing to `cuts` — the percentages taken off each of its sides."""
    x0, y0, x1, y1 = keep_rect(segments, cuts)
    out = []
    for seg in segments:
        s = _clip(seg, x0, x1, 0)
        s = None if s is None else _clip(s, y0, y1, 1)
        if s is not None:
            out.append(s)
    if not out:
        raise CombineError(
            f"{what or 'this symbol'} has no ink left after the slice "
            f"({_said(cuts)}) — the strokes are all outside what it keeps")
    return out


def _said(cuts):
    """A slice as a person reads it: `left 10%, right 25%`."""
    return ", ".join(f"{k} {cuts[k]:g}%" for k in SIDES if cuts.get(k))


def slice_to(svg_path, out_path, cuts, canvas=CANVAS, stroke=51.2,
             color="#000000", what=""):
    """Write `svg_path` trimmed by `cuts`, and return the path written.

    A file rather than segments because that is what the rest of the fold reads:
    every symbol is placed out of the cleaned drawing on disk. Writing the
    trimmed one out beside the spec also leaves the record of what was actually
    combined.
    """
    return write_svg(slice_segments(parse_segments(svg_path), cuts, what),
                     out_path, stroke=stroke, color=color, canvas=canvas)


# -------------------------------------------------------------- snapping
#
# A box said by hand — a layout's slot, a box edited in the combined-position
# popup — is drawn on the whole units of the output canvas, and what lands in it
# should read the same way. The uniform fit does not: a 32x40 drawing fitted
# into a 32x36 slot comes out 28.8 wide, and centring halves the 3.2 left over,
# so it starts at 7.6. Nothing in that chain ever asks for a whole unit.
#
# So a hand-said placement is snapped: the uniform fit's width and height are
# rounded to whole units, and if a whole-unit size within one unit of that is
# EXACTLY proportional to the drawing it is preferred — which is what keeps a
# 4:5 or 3:4 drawing mathematically unchanged instead of a percent off. What is
# left is a genuinely non-uniform scale, but only by the rounding: at most
# SNAP_TOLERANCE, which is the price of the whole numbers.
#
# The measured-box fold is not snapped. Its boxes come off the icon a symbol was
# cut from, on the 24 grid, and land wherever the canvas puts them; there is no
# grid there to snap to and rounding to one would only move every existing icon.

#: How far a snapped size may sit off the drawing's own proportions.
SNAP_TOLERANCE = 0.02

#: The smallest axis worth snapping. Below four units the whole-unit grid is
#: coarser than the drawing, and rounding to it distorts more than it tidies.
SNAP_MIN_UNITS = 4

#: A size this close to the drawing's proportions counts as exact — loose enough
#: to catch 4:5 and 3:4 through the float a bounding box is measured in.
SNAP_EXACT = 0.001


def snapped_size(w, h, bw, bh):
    """The whole-unit size a `w` x `h` drawing takes in a `bw` x `bh` box.

    None when there is no size worth snapping to: a drawing flat on one axis, a
    box too small for the grid to describe (SNAP_MIN_UNITS), or a rounding that
    would bend the drawing further than SNAP_TOLERANCE. The caller then places
    it the ordinary uniform way.
    """
    if w <= 1e-9 or h <= 1e-9 or bw <= 1e-9 or bh <= 1e-9:
        return None
    ratio = w / h
    s = min(bw / w, bh / h)
    # the rounded uniform fit, and its three neighbours a unit down: one of the
    # four is the largest whole-unit size that still fits the box
    wide, tall = round(w * s), round(h * s)
    seen, best, exact = set(), None, None
    for W in (wide, wide - 1):
        for H in (tall, tall - 1):
            if W < 1 or H < 1 or W > bw + 1e-9 or H > bh + 1e-9 or (W, H) in seen:
                continue
            seen.add((W, H))
            off = abs((W / H) / ratio - 1)
            if best is None or (W * H, -off) > (best[0] * best[1], -best[2]):
                best = (W, H, off)
            if off <= SNAP_EXACT and (exact is None or W * H > exact[0] * exact[1]):
                exact = (W, H, off)
    got = exact or best
    if got is None:
        return None
    W, H, off = got
    if min(W, H) < SNAP_MIN_UNITS or off > SNAP_TOLERANCE:
        return None
    return W, H


def fit_into(segments, box_px, snap=False, exact_box=False):
    """Scale `segments` into `box_px` and centre them there.

    Uniform and centred is the same rule `app.place.fit` uses in the library, so
    a symbol placed here lands where the Positions view drew its box. `snap`
    asks for a box that was said by hand instead: the size is rounded onto the
    canvas' whole units (`snapped_size`) and the offset with it, so the drawing
    reads off the same grid the box was drawn on. A box the grid cannot describe
    falls back to the uniform fit, so `snap` never makes a placement worse.
    """
    b = bbox(segments)
    if b is None:
        raise CombineError("cannot place an empty symbol")
    x0, y0, x1, y1 = b
    w, h = x1 - x0, y1 - y0
    bx, by, bw, bh = box_px
    if exact_box:
        sx = bw/w if w>1e-9 else 1
        sy = bh/h if h>1e-9 else 1
        return [[(bx+(p[0]-x0)*sx, by+(p[1]-y0)*sy) for p in seg] for seg in segments]
    got = snapped_size(w, h, bw, bh) if snap else None
    if got is not None:
        tw, th = got
        sx, sy = tw / w, th / h
        dx = round(bx) + math.floor((round(bw) - tw) / 2) - x0 * sx
        dy = round(by) + math.floor((round(bh) - th) / 2) - y0 * sy
        return [[(p[0] * sx + dx, p[1] * sy + dy) for p in seg]
                for seg in segments]
    # a flat symbol - a rule, a row of dots - has no extent on one axis and that
    # axis carries no scale information, so only axes with real extent get a vote
    votes = [d / s for s, d in ((w, bw), (h, bh)) if s > 1e-9 and d > 1e-9]
    s = min(votes) if votes else 1.0
    dx = bx + (bw - w * s) / 2 - x0 * s
    dy = by + (bh - h * s) / 2 - y0 * s
    return [[(p[0] * s + dx, p[1] * s + dy) for p in seg] for seg in segments]


def transform_segments(segments, scale, dx, dy):
    """Apply one uniform group transform without changing stroke width."""
    return [[(p[0] * scale + dx, p[1] * scale + dy) for p in seg]
            for seg in segments]


def group_transform(segment_groups, canvas=CANVAS, stroke=51.2):
    """Fit and centre a placed symbol group in the fixed-stroke safe area.

    Bounds here are path centrelines. Half of the output stroke is reserved on
    every side, so a centreline at ``stroke / 2`` paints exactly to zero and a
    centreline at ``canvas - stroke / 2`` paints exactly to the far edge. Only
    path coordinates and relative placements scale; the writer still emits the
    original stroke width.
    """
    if stroke < 0 or stroke >= canvas:
        raise CombineError(
            f"stroke {stroke:g} leaves no drawable area on canvas {canvas:g}")
    segments = [seg for group in segment_groups for seg in group]
    bounds = bbox(segments)
    if bounds is None:
        raise CombineError("cannot normalize an empty symbol group")
    x0, y0, x1, y1 = bounds
    width, height = x1 - x0, y1 - y0
    available = canvas - stroke
    votes = [1.0]
    if width > 1e-9:
        votes.append(available / width)
    if height > 1e-9:
        votes.append(available / height)
    scale = min(votes)
    half = stroke / 2
    # Centre the complete composition as one group. The same uniform scale and
    # translation apply to every symbol, preserving proportions and offsets.
    left = (canvas - width * scale) / 2
    top = (canvas - height * scale) / 2
    dx, dy = left - x0 * scale, top - y0 * scale
    after = (left, top, left + width * scale, top + height * scale)
    return scale, dx, dy, {
        "scale": scale,
        "before_px": [x0, y0, x1, y1],
        "after_px": list(after),
        "painted_px": [after[0] - half, after[1] - half,
                       after[2] + half, after[3] + half],
    }


def center_segments(segments, canvas=CANVAS):
    """Translate a completed fold to the canvas centre without scaling it."""
    bounds = bbox(segments)
    if bounds is None:
        raise CombineError("cannot centre an empty combined icon")
    x0, y0, x1, y1 = bounds
    dx = canvas / 2 - (x0 + x1) / 2
    dy = canvas / 2 - (y0 + y1) / 2
    centred = transform_segments(segments, 1.0, dx, dy)
    return centred, {
        "dx": dx,
        "dy": dy,
        "before_px": [x0, y0, x1, y1],
        "after_px": [x0 + dx, y0 + dy, x1 + dx, y1 + dy],
    }


def transform_box(box, scale, dx, dy, canvas=CANVAS):
    """Apply an engine-pixel group transform to one 24-grid placement box."""
    k = canvas / GRID
    return {
        "x": (box["x"] * k * scale + dx) / k,
        "y": (box["y"] * k * scale + dy) / k,
        "w": box["w"] * scale,
        "h": box["h"] * scale,
    }


def _main_data(segments):
    """The main-icon dict the erasure step reads.

    Only `segments` is geometry; the rest feeds its stats and combined-bbox maths.
    Derived from the placed segments so an accumulated fold describes itself
    correctly on the next pass instead of still describing the first symbol.
    """
    x0, y0, x1, y1 = bbox(segments)
    w, h = x1 - x0, y1 - y0
    if w > h:
        ratio, orientation = (w / h if h else float("inf")), "Horizontal"
    elif h > w:
        ratio, orientation = (h / w if w else float("inf")), "Vertical"
    else:
        ratio, orientation = 1.0, "Square"
    return {
        "segments": segments,
        "aspect_ratio": ratio,
        "orientation": orientation,
        "scaled_dimensions": (w, h),
        "final_icon_position": (x0, y0),
    }


def _state_data(segments, buffer_radius):
    """The sub-icon dict the erasure step reads, from already-placed segments.

    `process_state_icon` is the engine's own step 2: it scales a drawing into a
    box, centres it there, and buffers what comes out. Here the placing is
    already done — by the same `fit_into` the bottom layer went through — so
    only the buffering is wanted, and it is built out of the engine's own
    helpers round segments that are already on the output canvas.

    Doing it this way is what lets a snapped placement stay snapped: fitting the
    drawing a second time into a box would put back exactly the fractional
    centring the snap took out. It also means every symbol in a fold is placed
    by one rule rather than by two that merely agree.
    """
    areas = [LineString(seg).buffer(buffer_radius, cap_style=1, join_style=1)
             for seg in segments]
    stroke_area = unary_union(areas)
    if not stroke_area.is_valid:
        stroke_area = stroke_area.buffer(0)
    convex_area = create_convex_hull_buffer(segments, buffer_radius=0)
    if not convex_area.is_valid:
        convex_area = convex_area.buffer(0)
    x0, y0, x1, y1 = bbox(segments)
    return {
        "segments": segments,
        "buffer_area_by_stroke": stroke_area,
        "buffer_area_by_convex": convex_area,
        "buffer_outlines_stroke": get_buffer_outlines(stroke_area),
        "buffer_outlines_convex": get_buffer_outlines(convex_area),
        "dimensions": (x1 - x0, y1 - y0),
    }


def _survivors(info, n):
    """How many pieces the first `n` segments handed to the clip are still in
    its result.

    `clipping_info` is one entry per input segment, in the order they went in,
    and the surviving entries' `new_segments` concatenate to exactly the clipped
    list — so counting the pieces the first `n` left is the whole mapping from
    "what went in" to "what came out". That is what carries the bottom layer's
    identity through a fold, so the writer can put it in its own group.

    `new_segments` rather than the action, because a segment survives under two
    names: `kept` when it missed the clearance entirely, `clipped_and_kept` when
    it crossed the edge and one or more pieces of it came back. A removed
    segment carries no pieces at all, so the key is the whole test.
    """
    if not info:                      # nothing was cut: the list came back whole
        return n
    return sum(len(i.get("new_segments") or []) for i in info[:n])


def fold(items, buffer_radius=128.0, canvas=CANVAS, stroke=51.2,
         min_segment_length=None, work_dir=None, on_pass=None):
    """Place every symbol at its box and fold them bottom layer first.

    `items` is one dict per symbol: `sid`, `svg` (path to its final), `box` in grid
    units, `area`/`ink` to order by, optionally `z` — the layer said by hand, 1
    being the bottom — optionally `slice` — the percentages to take off the
    drawing's own sides before it is placed. Every drawing is uniformly scaled
    and centred in its box, so its proportions never change. All natural
    placements are then normalized as one group into the fixed-stroke safe area.
    A `manual_combined` placement keeps its final edited coordinates after that
    fit, and is snapped onto the canvas' whole units (`fit_into`) because the box
    it was given was drawn on them.

    Returns (main, state, record): the bottom layer's surviving segments, every
    layer folded on top of it, and a record describing each erasure in order —
    what cut what, and how much came off. The two lists are what the writer's
    two groups are, so a combined icon says which strokes are the main icon and
    which are the sub icons that cut it.

    `work_dir` is where the cleaned inputs are written; a temporary directory is
    used when none is given. `on_pass(n, sid, segments)` is called after each
    erasure, for callers that want to keep the intermediates.
    """
    if not items:
        raise CombineError("nothing to combine")
    if min_segment_length is None:
        min_segment_length = canvas * MIN_SEGMENT_PER_CANVAS

    ordered = layered(items)

    tmp = None
    if work_dir is None:
        tmp = tempfile.TemporaryDirectory()
        work_dir = tmp.name
    work_dir = Path(work_dir)
    work_dir.mkdir(parents=True, exist_ok=True)
    try:
        return _fold(ordered, work_dir, buffer_radius, canvas, stroke,
                     min_segment_length, on_pass)
    finally:
        if tmp is not None:
            tmp.cleanup()


def layered(items):
    """The fold order: bottom layer first.

    By default a layer is its size — the biggest box is the bottom, z=1, the
    one everything else cuts into; box area is what "bigger" means to the eye
    and ink breaks the ties a box cannot. An item's own `z` overrides its place
    in that order, so two items can be told to swap without renumbering the
    rest: the explicit number simply replaces the rank the size rule gave. On
    a tie the item that was told its layer beats the one that fell there, so
    "z=1" puts a small symbol at the very bottom rather than just near it.
    """
    by_size = sorted(items, key=lambda i: (-i["area"], -i.get("ink", 0),
                                           i["sid"]))
    rank = {id(it): n for n, it in enumerate(by_size, start=1)}
    return sorted(by_size,
                  key=lambda i: (i.get("z") or rank[id(i)],
                                 i.get("z") is None, rank[id(i)]))


def _fold(ordered, work_dir, buffer_radius, canvas, stroke, min_segment_length,
          on_pass=None):
    # named by position as well as by sid: one symbol placed twice is ordinary
    # (two users out of one drawing), and the two placements can carry different
    # slices — with a sid-only name one would overwrite the other and both would
    # be combined from whichever was written last
    for n, it in enumerate(ordered):
        stem = f"{n}_{it['sid']}"
        it["clean"] = clean_to(it["svg"], work_dir / f"in_{stem}.svg")
        if it.get("slice"):
            it["clean"] = slice_to(it["clean"], work_dir / f"cut_{stem}.svg",
                                   it["slice"], canvas=canvas,
                                   what=it["sid"])
        # Keep the cleaned proportional source used by both Reset and placement.
        it["natural_source"] = parse_segments(it["clean"])
        it["placed_source"] = parse_segments(it["clean"])

    # First place every symbol without normalization, then measure the NATURAL
    # union. Its one uniform transform is the automatic starting layout. A box
    # edited in the combined-box tool is already in final 24-grid coordinates
    # and deliberately skips that transform: the human edit has final say, even
    # when it places painted ink outside the canvas.
    raw_placed, raw_natural = [], []
    for it in ordered:
        snap = (bool(it.get("manual_combined")) and not it.get("preserve_geometry"))
        raw_placed.append(fit_into(
            it["placed_source"], box_to_canvas(it["box"], canvas=canvas),
            snap=snap, exact_box=bool(it.get("rounded_box"))))
        raw_natural.append(fit_into(
            it["natural_source"],
            box_to_canvas(it.get("natural_box") or it["box"], canvas=canvas),
            snap=snap, exact_box=bool(it.get("rounded_box"))))

    ns, ndx, ndy, normalization = group_transform(
        raw_natural, canvas=canvas, stroke=stroke)
    normalization["manual_candidates"] = [
        it.get("candidate") for it in ordered if it.get("manual_combined")]

    for it, raw, raw_reset in zip(ordered, raw_placed, raw_natural):
        key = it.get("candidate") or it["sid"]
        # Raw artifacts make a normalization problem inspectable without
        # changing what the Positions view reads as the executed placement.
        write_svg(raw, work_dir / f"raw_placed_{key}.svg", stroke=stroke,
                  canvas=canvas)
        write_svg(raw_reset, work_dir / f"raw_natural_{key}.svg",
                  stroke=stroke, canvas=canvas)
        original_box = it["box"]
        natural_box = it.get("natural_box") or original_box
        if not it.get("manual_combined"):
            it["box"] = transform_box(
                original_box, ns, ndx, ndy, canvas=canvas)
        it["natural_box"] = transform_box(
            natural_box, ns, ndx, ndy, canvas=canvas)
        natural = transform_segments(raw_reset, ns, ndx, ndy)
        write_svg(natural, work_dir / f"natural_{key}.svg", stroke=stroke,
                  canvas=canvas)

    first = ordered[0]
    segments = fit_into(parse_segments(first["clean"]),
                        box_to_canvas(first["box"], canvas=canvas),
                        snap=(bool(first.get("manual_combined")) and not first.get("preserve_geometry")), exact_box=bool(first.get("rounded_box")))
    # how many of the accumulated segments are still the bottom layer's — the
    # one the writer calls the main icon. Every pass cuts into it, so the count
    # has to be carried through the cut rather than measured at the end.
    main_count = len(segments)
    first_key = first.get("candidate") or f"0_{first['sid']}"
    write_svg(segments, work_dir / f"placed_{first_key}.svg", stroke=stroke,
              canvas=canvas)
    passes = []

    for it in ordered[1:]:
        # placed by the same rule the bottom layer was, so a box said by hand is
        # snapped once and stays where the snap put it; only the buffering the
        # erasure reads is the engine's (_state_data), and the segments handed to
        # it are already on the canvas, so there is no offset left to apply
        placed = fit_into(parse_segments(it["clean"]),
                          box_to_canvas(it["box"], canvas=canvas),
                          snap=(bool(it.get("manual_combined")) and not it.get("preserve_geometry")), exact_box=bool(it.get("rounded_box")))
        state = _state_data(placed, buffer_radius)

        before = len(segments)
        merged = merged_icons_and_remove_overlapping(
            _main_data(segments), state, 0.0, 0.0, canvas, canvas,
            show_matplotlib=False, min_segment_length=min_segment_length,
            alignment="middle")
        if not merged:
            raise CombineError(f"erasing against {it['sid']} produced nothing")

        kept = merged.get("clipped_segments") or []
        sub = merged.get("positioned_state_segments") or []
        main_count = _survivors(merged.get("clipping_info"), main_count)
        placed_key = it.get("candidate") or f"{len(passes) + 1}_{it['sid']}"
        write_svg(sub, work_dir / f"placed_{placed_key}.svg", stroke=stroke,
                  canvas=canvas)
        # the whole result becomes the next main, which is what makes a third
        # symbol cut the second and not only the first
        segments = kept + sub
        # the state after this pass, so a fold that goes wrong can be looked at
        # at the step it went wrong rather than only at the end
        if on_pass is not None:
            on_pass(len(passes) + 1, it["sid"], segments)
        pb = bbox(placed)
        passes.append({
            "sid": it["sid"],
            # the box asked for and the box the drawing actually took in it —
            # two lines rather than one, because a snapped placement rounds onto
            # the canvas' whole units and "it did not land where I drew it" is
            # answered by the difference between these
            "box_px": [round(v, 2)
                       for v in box_to_canvas(it["box"], canvas=canvas)],
            "placed_px": [round(v, 2) for v in (pb[0], pb[1],
                                                pb[2] - pb[0], pb[3] - pb[1])],
            "main_segments_before": before,
            "main_segments_kept": len(kept),
            "sub_segments": len(sub),
        })

    # Cutting overlaps can change the visible bounds of the placed group. Do a
    # translation-only final pass so the actual combined drawing, rather than
    # its pre-fold boxes, owns the exact centre of the output canvas.
    #
    # Unless a placement was said by hand. A layout's slots and a box edited in
    # the combined-position popup are final coordinates ON THIS CANVAS — the
    # whole point of snapping them onto its whole units — and re-centring the
    # fold afterwards would slide the drawing off the target it was told to land
    # on. `any` rather than `all`: one hand-said box in a mixed fold is moved
    # off target by this just as a whole layout would be.
    if any(it.get("manual_combined") for it in ordered):
        normalization["final_centering"] = None
    else:
        segments, final_centering = center_segments(segments, canvas=canvas)
        normalization["final_centering"] = final_centering

    return segments[:main_count], segments[main_count:], {
        "order": [i["sid"] for i in ordered],
        # one entry per placement, in fold order, so a repeated symbol is two
        # lines and the slice each of them was given is on its own line
        "placed": [{"sid": i["sid"], "slice": i.get("slice") or None}
                   for i in ordered],
        "normalization": normalization,
        "passes": passes,
    }


def write_svg(segments, out_path, stroke=51.2, color="#000000", canvas=CANVAS,
              state=None):
    """Write folded segments with the engine's own writer.

    `segments` is the bottom layer — the main icon, with the clearance cut out
    of it — and `state` is every layer folded on top, so the two groups the
    writer emits mean what they are named: `main-icon-clipped` and `state-icon`.
    The fold knows which is which (it carries the bottom layer's count through
    every cut), so the split is the one the layout asked for rather than one
    guessed back out of the finished drawing.

    A caller with nothing to distinguish — a work-in-progress pass, one raw
    placement — passes only `segments` and gets the one group it had before.
    """
    ok = save_clipped_result_to_svg(
        {"clipped_segments": segments,
         "positioned_state_segments": list(state or [])},
        str(out_path), canvas_width=canvas, canvas_height=canvas,
        main_stroke_width=stroke, state_stroke_width=stroke,
        main_color=color, state_color=color)
    if not ok or not Path(out_path).is_file():
        raise CombineError("the SVG writer produced no file")
    return out_path
