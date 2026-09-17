"""Pull a combined icon back inside its canvas, stroke halo included.

The engine lays icons out on their CENTERLINES and allows nothing for stroke
width: `bottom-right`, say, puts the sub icon's box flush against
`final_canvas_width`, so its outermost centerline sits exactly on the canvas
edge. At the engine's native stroke of 25 that costs 12.5px off each side and
is easy to miss. At this repo's 51.2 it costs 25.6px, and the result is visibly
guillotined.

It also breaks the key-shape snap downstream. `snap_svg_text` measures ink by
RENDERING the SVG, so clipped ink measures as a box exactly the size of the
canvas; `snap_params` then subtracts a full stroke width from a bbox that never
contained one, computes too small a geometry, and lands the icon off the grid
(observed: ink at 136..888 where shape-square wants 153.6..870.4).

So: measure the real geometry from the path data, and if the stroked box does
not fit, scale about the canvas centre until it does. The transform is applied
only when it is actually needed, which keeps every already-fitting combination
byte-identical to the upstream engine's output.
"""
from __future__ import annotations

import re

_NUM_RE = re.compile(r"-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?")
_PATH_D_RE = re.compile(r'(<path\b[^>]*?\sd=")([^"]*)(")')


def _fmt(v: float) -> str:
    return f"{v:.2f}".rstrip("0").rstrip(".") if v % 1 else str(int(v))


def geometry_bbox(text: str):
    """(x0, y0, x1, y1) over every coordinate in every `<path d>`, or None.

    The engine's writer emits nothing but `M x,y L x,y` pairs, so every number
    in `d` is a coordinate and they alternate x, y — no command letters take
    arguments that would break the pairing. This is deliberately NOT a general
    SVG path parser; it is a reader for one known producer.
    """
    xs: list[float] = []
    ys: list[float] = []
    for m in _PATH_D_RE.finditer(text):
        nums = [float(n) for n in _NUM_RE.findall(m.group(2))]
        xs.extend(nums[0::2])
        ys.extend(nums[1::2])
    if not xs or not ys:
        return None
    return min(xs), min(ys), max(xs), max(ys)


def fit_svg_to_canvas(text: str, stroke: float, canvas: float = 1024.0,
                      margin: float = 0.0):
    """Scale + centre the icon so its STROKED extent fits the canvas.

    `stroke` is the widest stroke in the document (the halo is half of it on
    each side). `margin` keeps that many px clear of every edge.

    Returns `(svg_text, info)`. `info` is None when the icon already fitted and
    nothing was touched; otherwise it reports the scale, the translation, and
    the before/after stroked boxes.
    """
    box = geometry_bbox(text)
    if box is None:
        return text, None
    x0, y0, x1, y1 = box
    half = stroke / 2.0
    gw, gh = x1 - x0, y1 - y0
    avail = canvas - 2 * margin

    # Room the geometry may occupy once its halo is accounted for. A degenerate
    # (zero-width or zero-height) icon still needs the halo to fit, hence max().
    room = max(avail - stroke, 1.0)
    scale = min(1.0, room / gw if gw > 0 else 1.0, room / gh if gh > 0 else 1.0)

    cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    tx = canvas / 2.0 - scale * cx
    ty = canvas / 2.0 - scale * cy

    # Already inside the canvas with its halo? Leave it exactly as the engine
    # wrote it — recentring a fitting icon would diverge from upstream for no
    # gain, and this path is the common one for centre/container combinations.
    fits = (x0 - half >= margin - 1e-6 and y0 - half >= margin - 1e-6
            and x1 + half <= canvas - margin + 1e-6
            and y1 + half <= canvas - margin + 1e-6)
    if fits:
        return text, None

    def _rewrite(m):
        nums = [float(n) for n in _NUM_RE.findall(m.group(2))]
        out = []
        for i in range(0, len(nums) - 1, 2):
            out.append((_fmt(scale * nums[i] + tx), _fmt(scale * nums[i + 1] + ty)))
        # Rebuild in the producer's own shape: one M/L pair per segment.
        d = " ".join(f"M{out[i][0]},{out[i][1]}L{out[i + 1][0]},{out[i + 1][1]}"
                     for i in range(0, len(out) - 1, 2))
        return m.group(1) + d + m.group(3)

    return _PATH_D_RE.sub(_rewrite, text), {
        "scale": round(scale, 6),
        "translate": [round(tx, 3), round(ty, 3)],
        "before": [round(x0 - half, 2), round(y0 - half, 2),
                   round(x1 + half, 2), round(y1 + half, 2)],
        "after": [round(scale * x0 + tx - half, 2), round(scale * y0 + ty - half, 2),
                  round(scale * x1 + tx + half, 2), round(scale * y1 + ty + half, 2)],
    }
