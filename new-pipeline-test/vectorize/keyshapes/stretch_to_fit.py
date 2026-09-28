#!/usr/bin/env python3
"""
Snap each input icon to the nearest grid_system shape (12 aspect-ratio buckets)
and bake the result into coordinates -- no transform attrs, output stroke = 51.2.

    outputs/{name}/{name}_fit.svg

Pipeline (per icon):
  1. Measure the icon geometry bbox (ink bbox minus the 51.2-wide stroke halo).
  2. Pick the grid shape whose aspect ratio is closest (log space) -> fit_shapes.
  3. Stretch onto that shape's box, keeping the grid shape's native padding
     (centered at 512,512). A single axis-aligned affine (sx,sy,ex,ey) is baked
     into every coordinate.

Element handling:
  * <path>   : every coordinate in `d` is transformed (M/L/H/V/C/S/Q/T/A/Z).
  * <line>   : endpoints transformed.
  * <rect>   : its full transform="..." list folded with the snap affine into a
               baked <path>.
  * <circle> : a BIG circle that wraps all content snaps (uniformly) to the
               circle grid shape; a small circle is skipped (would oval).
  * <ellipse>: near-round (rx/ry within CIRCLIFY_ASPECT, circle-preserving
               transform) -> normalized to a <circle> first; otherwise folded
               with its full transform list into a baked cubic-bezier <path>
               (exact under any affine).
  * <polyline>/<polygon>: every point transformed (transform list folded in).
  A transform="..." on <path>/<line>/<circle>, or one that fails to parse, is
  NOT folded: the element passes through untouched and a WARN is printed.

Run BEFORE generate_report.py.   Requires: cairosvg numpy pillow
"""

import json
import math
import os
import re
import shutil

import numpy as np

# Per-element snap logging (e.g. circlify rewrites) is opt-in: this runs on
# every execute_pipeline call from bulk_collect / the desktop server, so the
# chatter is gated behind SNAP_VERBOSE to keep those logs clean.
_VERBOSE = bool(os.environ.get("SNAP_VERBOSE"))

from bbox_preview import (
    INPUT_DIR, OUTPUT_DIR, VIEWBOX, RENDER_W, ALPHA_THRESHOLD,
    render_rgba, render_rgba_text, ink_bbox,
)
from fit_shapes import nearest_shape, FIT_SHAPES, GRID_DIR

# ---- constants ------------------------------------------------------------
STROKE = 51.2               # stroke width (= one 51.2 grid cell), used everywhere
HALF = STROKE / 2.0
CANVAS = VIEWBOX
CENTER = CANVAS / 2.0
KAPPA = 0.5522847498307936          # circle->cubic-bezier constant
MAX_FIT = CANVAS / 20 * 16          # 51.2 * 16 = 819.2 (16 grid cells)

# draw the matched grid shape into the output so you can see the target rect
DRAW_SHAPE = True
SHAPE_STROKE = "#3aa0ff"            # blue guide outline
SHAPE_WIDTH = 6
SHAPE_DASH = "18 12"

# thin white copy of the icon drawn on top of the black stroke -> shows the
# centerline (only added to the _fit.svg variant, not _fit_plain.svg)
DRAW_STROKE_LAYER = True
STROKE_LAYER_COLOR = "#ffffff"
STROKE_LAYER_WIDTH = 4

# circle handling thresholds
CIRCLE_SHAPE = next(s for s in FIT_SHAPES if s["category"] == "circle")
CIRCLE_GRID_R = CIRCLE_SHAPE["radius"]          # 409.6
MIN_BIG_R = 0.40 * CANVAS                        # circle must be >= grid circle radius
WRAP_TOL = 25.0                                  # content may exceed the circle by <= this
CONN_TOL = 2.0                  # path point within this of a circle radius = a connection
DOT_MAX_DIAM = 2 * STROKE       # 102.4 -- a standalone circle smaller than this -> a stroke dot
DOT_OFFSET = 0.1                # gap between the two dot points; the round cap does the rest
# a closed <path> this circular -> normalized to a true <circle> before any other handling
CIRCLIFY_TOL = 0.02             # a point is "on the circle" within 2% of the fitted radius
CIRCLIFY_MIN_FRAC = 0.99        # >= this fraction of sampled points must be on the circle
CIRCLIFY_ASPECT = (0.80, 1.25)  # bbox aspect must fall in here (rejects ovals)

SVG_OPEN_RE = re.compile(r"<svg[^>]*>", re.IGNORECASE)
HAS_CIRCLE_RE = re.compile(r"<circle[\s>]", re.IGNORECASE)
# match the OPENING tag whether self-closing (<path .../>) or paired (<path ...>),
# plus an immediately-following close tag if there is one -- name-CHANGING rewrites
# (rect/ellipse -> path, ellipse -> circle) must consume it or they'd leave a stray
# </rect>/</ellipse> behind that breaks XML parsing downstream. A paired tag with
# children keeps its close tag (the optional group won't match) -- fine for the
# name-preserving rewrites, which never see children in pipeline output.
ELEM_RE = re.compile(r"<(path|line|rect|circle|ellipse|polyline|polygon)\b[^>]*?/?>"
                     r"(?:\s*</\1\s*>)?",
                     re.IGNORECASE)
# elements the baker does NOT transform -- warn so they aren't silently passed through.
UNSUPPORTED_RE = re.compile(r"<(text|image|use)\b", re.IGNORECASE)
# a transform on a container would re-apply on top of the baked children -> warn too.
GROUP_TRANSFORM_RE = re.compile(r"<(g|svg)\b[^>]*\btransform\s*=", re.IGNORECASE)
CIRCLE_TAG_RE = re.compile(r"<circle\b[^>]*?/>", re.IGNORECASE)
ATTR_RE = re.compile(r'([\w:-]+)\s*=\s*"([^"]*)"')
TOKEN_RE = re.compile(r"([MLHVCSQTAZmlhvcsqtaz])|(-?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?)")
TRANSFORM_FN_RE = re.compile(r"([a-zA-Z]+)\s*\(([^)]*)\)")
ARITY = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "S": 4, "Q": 4, "T": 2, "A": 7, "Z": 0}


# ---- number / matrix helpers ---------------------------------------------
def fmt(v):
    if abs(v) < 5e-4:
        v = 0.0
    return f"{v:.3f}".rstrip("0").rstrip(".")


def set_stroke(tag):
    """Force the output stroke-width on a baked element tag."""
    return re.sub(r'\sstroke-width="[^"]*"', f' stroke-width="{fmt(STROKE)}"', tag)


def normalize_stroke(text):
    """Rewrite every stroke-width in the input to STROKE (51.2) so measuring and
    baking use one consistent stroke -> the snapped icon fills its target exactly."""
    return re.sub(r'stroke-width="[^"]*"', f'stroke-width="{fmt(STROKE)}"', text)


def mat_mul(m1, m2):                 # compose: apply m2 then m1
    a1, b1, c1, d1, e1, f1 = m1
    a2, b2, c2, d2, e2, f2 = m2
    return (a1 * a2 + c1 * b2, b1 * a2 + d1 * b2,
            a1 * c2 + c1 * d2, b1 * c2 + d1 * d2,
            a1 * e2 + c1 * f2 + e1, b1 * e2 + d1 * f2 + f1)


def apply_mat(m, x, y):
    a, b, c, d, e, f = m
    return a * x + c * y + e, b * x + d * y + f


def rotate_matrix(ang, cx, cy):
    th = math.radians(ang)
    co, si = math.cos(th), math.sin(th)
    rot = (co, si, -si, co, 0.0, 0.0)
    return mat_mul((1, 0, 0, 1, cx, cy), mat_mul(rot, (1, 0, 0, 1, -cx, -cy)))


# ---- path data transform (axis-aligned scale+translate) ------------------
def _snap(x, y, X, Y, round_map):
    """If original (x,y) sits on a circle, radially snap transformed (X,Y) to its
    re-rounded circle so the path keeps meeting the circle. Else return (X,Y)."""
    if round_map:
        for cx, cy, r, ncx, ncy, nr in round_map:
            if abs(math.hypot(x - cx, y - cy) - r) < CONN_TOL:
                dx, dy = X - ncx, Y - ncy
                L = math.hypot(dx, dy) or 1.0
                return ncx + nr * dx / L, ncy + nr * dy / L
    return X, Y


def transform_path(d, sx, sy, ex, ey, round_map=None):
    items = []
    for cmd, num in TOKEN_RE.findall(d):
        items.append(("c", cmd) if cmd else ("n", float(num)))

    def tx(x, y):
        return sx * x + ex, sy * y + ey

    out, i, emit = [], 0, None
    while i < len(items):
        if items[i][0] == "c":
            cmd = items[i][1]; i += 1
        else:
            cmd = emit
            if cmd == "M": cmd = "L"
            elif cmd == "m": cmd = "l"
        up = cmd.upper()
        rel = cmd.islower()
        if up == "Z":
            out.append(cmd); emit = cmd; continue       # keep original Z/z case
        n = ARITY[up]
        vals = [items[i + k][1] for k in range(n)]; i += n
        if up in ("M", "L", "T"):
            x, y = vals
            if rel:
                X, Y = sx * x, sy * y
            else:
                X, Y = _snap(x, y, *tx(x, y), round_map)
            out.append(f"{cmd}{fmt(X)} {fmt(Y)}")
        elif up == "H":
            X = sx * vals[0] if rel else sx * vals[0] + ex
            out.append(f"{cmd}{fmt(X)}")
        elif up == "V":
            Y = sy * vals[0] if rel else sy * vals[0] + ey
            out.append(f"{cmd}{fmt(Y)}")
        elif up in ("C", "S", "Q"):
            pts = []
            for k in range(0, n, 2):
                x, y = vals[k], vals[k + 1]
                if rel:
                    X, Y = sx * x, sy * y
                else:
                    X, Y = _snap(x, y, *tx(x, y), round_map)
                pts.append(f"{fmt(X)} {fmt(Y)}")
            out.append(f"{cmd}" + " ".join(pts))
        elif up == "A":
            # rx scales by sx, ry by sy, and rot is preserved as-is. This is exact
            # only when the arc's ellipse axes are coord-aligned (rot=0); under a
            # non-uniform scale a rotated arc would need its axes recomputed. Rare
            # in icons, so we keep the simpler axis-aligned approximation.
            rx, ry, rot, large, sweep, x, y = vals
            X, Y = (sx * x, sy * y) if rel else tx(x, y)
            out.append(f"{cmd}{fmt(rx * sx)} {fmt(ry * sy)} {fmt(rot)} "
                       f"{int(large)} {int(sweep)} {fmt(X)} {fmt(Y)}")
        emit = cmd
    return " ".join(out)


# ---- rect / ellipse (+optional transform list) -> baked path ---------------
def _parse_transform(s):
    """Compose a full SVG transform list (matrix|translate|scale|rotate|skewX|skewY)
    into one affine matrix. Returns None if any token is unrecognized or malformed --
    callers leave the element untouched (it lands on the WARN list upstream)."""
    m = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)
    pos = 0
    for fn in TRANSFORM_FN_RE.finditer(s):
        if s[pos:fn.start()].strip(" ,\t\r\n"):
            return None
        pos = fn.end()
        name = fn.group(1).lower()
        try:
            args = [float(v) for v in re.split(r"[\s,]+", fn.group(2).strip()) if v]
        except ValueError:
            return None
        if name == "matrix" and len(args) == 6:
            t = tuple(args)
        elif name == "translate" and len(args) in (1, 2):
            t = (1.0, 0.0, 0.0, 1.0, args[0], args[1] if len(args) == 2 else 0.0)
        elif name == "scale" and len(args) in (1, 2):
            t = (args[0], 0.0, 0.0, args[1] if len(args) == 2 else args[0], 0.0, 0.0)
        elif name == "rotate" and len(args) in (1, 3):
            t = rotate_matrix(args[0], *(args[1:] if len(args) == 3 else (0.0, 0.0)))
        elif name == "skewx" and len(args) == 1:
            t = (1.0, 0.0, math.tan(math.radians(args[0])), 1.0, 0.0, 0.0)
        elif name == "skewy" and len(args) == 1:
            t = (1.0, math.tan(math.radians(args[0])), 0.0, 1.0, 0.0, 0.0)
        else:
            return None
        m = mat_mul(m, t)              # list order: leftmost transform is outermost
    if s[pos:].strip(" ,\t\r\n"):
        return None
    return m


def _fold_transform(a, snap):
    """Compose the snap affine with the element's own transform="..." list.
    Returns (matrix, had_transform, ok); ok=False -> unparseable transform, the
    caller must pass the tag through untouched."""
    tr = a.get("transform")
    if not tr or not tr.strip():
        return snap, False, True
    own = _parse_transform(tr)
    if own is None:
        return snap, True, False
    return mat_mul(snap, own), True, True


def _keep_paint_attrs(a):
    """fill/stroke attrs carried onto a baked path, with the forced stroke-width."""
    keep = {k: v for k, v in a.items()
            if k == "fill" or (k.startswith("stroke") and k != "stroke-width")}
    keep["stroke-width"] = fmt(STROKE)
    return " ".join(f'{k}="{v}"' for k, v in keep.items())


def rect_to_path(a, snap):
    """Bake a <rect> into a <path> under snap + its own transform list.
    Returns None on an unparseable transform (caller keeps the tag as-is)."""
    m, _, ok = _fold_transform(a, snap)
    if not ok:
        return None
    x = float(a.get("x", 0)); y = float(a.get("y", 0))
    w = float(a["width"]); h = float(a["height"])
    rx = float(a.get("rx", a.get("ry", 0)) or 0)
    ry = float(a.get("ry", a.get("rx", 0)) or 0)
    rx = min(rx, w / 2); ry = min(ry, h / 2)

    P = lambda px, py: apply_mat(m, px, py)
    seg = []
    if rx <= 0 or ry <= 0:
        pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        seg.append("M" + " ".join(fmt(v) for v in P(*pts[0])))
        for p in pts[1:]:
            seg.append("L" + " ".join(fmt(v) for v in P(*p)))
        seg.append("Z")
    else:
        kx, ky = rx * KAPPA, ry * KAPPA
        def M(px, py): return " ".join(fmt(v) for v in P(px, py))
        seg.append("M" + M(x + rx, y))
        seg.append("L" + M(x + w - rx, y))
        seg.append("C" + M(x + w - rx + kx, y) + " " + M(x + w, y + ry - ky) + " " + M(x + w, y + ry))
        seg.append("L" + M(x + w, y + h - ry))
        seg.append("C" + M(x + w, y + h - ry + ky) + " " + M(x + w - rx + kx, y + h) + " " + M(x + w - rx, y + h))
        seg.append("L" + M(x + rx, y + h))
        seg.append("C" + M(x + rx - kx, y + h) + " " + M(x, y + h - ry + ky) + " " + M(x, y + h - ry))
        seg.append("L" + M(x, y + ry))
        seg.append("C" + M(x, y + ry - ky) + " " + M(x + rx - kx, y) + " " + M(x + rx, y))
        seg.append("Z")
    d = " ".join(seg)
    return f'<path d="{d}" {_keep_paint_attrs(a)}/>'


def ellipse_to_path(a, snap):
    """Bake an <ellipse> (optionally with a transform="..." list) into a cubic-bezier
    <path> under the full affine. Bezier control points transform exactly, so a rotated
    ellipse survives a non-uniform snap correctly (a cx/cy/rx/ry rewrite would not).
    Returns None on an unparseable transform (caller keeps the tag as-is)."""
    m, _, ok = _fold_transform(a, snap)
    if not ok:
        return None
    cx = float(a.get("cx", 0)); cy = float(a.get("cy", 0))
    rx = float(a.get("rx", a.get("ry", 0)) or 0)
    ry = float(a.get("ry", a.get("rx", 0)) or 0)
    if rx <= 0 or ry <= 0:
        return ""                  # rx/ry of 0 disables rendering per the SVG spec

    kx, ky = rx * KAPPA, ry * KAPPA
    def M(px, py): return " ".join(fmt(v) for v in apply_mat(m, px, py))
    seg = ["M" + M(cx + rx, cy),
           "C" + M(cx + rx, cy + ky) + " " + M(cx + kx, cy + ry) + " " + M(cx, cy + ry),
           "C" + M(cx - kx, cy + ry) + " " + M(cx - rx, cy + ky) + " " + M(cx - rx, cy),
           "C" + M(cx - rx, cy - ky) + " " + M(cx - kx, cy - ry) + " " + M(cx, cy - ry),
           "C" + M(cx + kx, cy - ry) + " " + M(cx + rx, cy - ky) + " " + M(cx + rx, cy),
           "Z"]
    d = " ".join(seg)
    return f'<path d="{d}" {_keep_paint_attrs(a)}/>'


# ---- per-element rewrite --------------------------------------------------
def make_rewriter(sx, sy, ex, ey, round_map=None, dot_keys=None):
    """round_map set -> re-round circles + snap connected path/line points to them.
    round_map None -> circles stay ovalized under a non-uniform scale (no snap).
    dot_keys: set of (cx,cy,r) standalone circles to collapse into a stroke dot."""
    snap = (sx, 0.0, 0.0, sy, ex, ey)
    round_on = round_map is not None

    def rewrite(match):
        tag = match.group(0)
        name = match.group(1).lower()
        a = dict(ATTR_RE.findall(tag))
        # path/line/circle rewrites can't fold a general matrix into their coords;
        # a transform on one of those passes through untouched (warned upstream).
        if name == "path":
            if "transform" in a:
                return tag
            d2 = transform_path(a["d"], sx, sy, ex, ey, round_map)
            tag = re.sub(r'\sd="[^"]*"', f' d="{d2}"', tag)
            return set_stroke(tag)
        if name == "line":
            if "transform" in a:
                return tag
            (x1, y1), (x2, y2) = (float(a["x1"]), float(a["y1"])), (float(a["x2"]), float(a["y2"]))
            nx1, ny1 = _snap(x1, y1, sx * x1 + ex, sy * y1 + ey, round_map)
            nx2, ny2 = _snap(x2, y2, sx * x2 + ex, sy * y2 + ey, round_map)
            for k, v in (("x1", nx1), ("y1", ny1), ("x2", nx2), ("y2", ny2)):
                tag = re.sub(rf'\s{k}="[^"]*"', f' {k}="{fmt(v)}"', tag)
            return set_stroke(tag)
        if name == "rect":
            baked = rect_to_path(a, snap)
            return baked if baked is not None else tag
        if name == "ellipse":
            baked = ellipse_to_path(a, snap)
            return baked if baked is not None else tag
        if name in ("polyline", "polygon"):
            m, had_tr, ok = _fold_transform(a, snap)
            if not ok:
                return tag
            nums = [float(v) for v in re.findall(r"-?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?",
                                                 a.get("points", ""))]
            pts = []
            for x, y in zip(nums[0::2], nums[1::2]):
                X, Y = apply_mat(m, x, y)
                if not had_tr:                 # radial circle snap only when untransformed
                    X, Y = _snap(x, y, X, Y, round_map)
                pts.append(f"{fmt(X)},{fmt(Y)}")
            tag = re.sub(r'\spoints="[^"]*"', f' points="{" ".join(pts)}"', tag)
            return set_stroke(re.sub(r'\stransform="[^"]*"', "", tag))
        if name == "circle":
            if "transform" in a:
                return tag
            cx, cy, r = float(a["cx"]), float(a["cy"]), float(a["r"])
            ncx, ncy = sx * cx + ex, sy * cy + ey
            if abs(sx - sy) >= 1e-6 and not round_on:        # leave it ovalized
                keep = {k: v for k, v in a.items()
                        if k == "fill" or k.startswith("stroke")}
                attrs = " ".join(f'{k}="{v}"' for k, v in keep.items())
                return (f'<ellipse cx="{fmt(ncx)}" cy="{fmt(ncy)}" '
                        f'rx="{fmt(sx*r)}" ry="{fmt(sy*r)}" {attrs}/>')
            # a standalone circle too small to read as a ring -> a single stroke dot
            # (two points 0.1 apart + round linecap = a dot of diameter = STROKE).
            if round_on and dot_keys and (cx, cy, r) in dot_keys:
                color = a.get("stroke", "#000000")
                idattr = f'id="{a["id"]}" ' if "id" in a else ""
                d = f"M{fmt(ncx)} {fmt(ncy)}l{fmt(DOT_OFFSET)} 0"
                return (f'<path {idattr}d="{d}" fill="none" stroke="{color}" '
                        f'stroke-width="{fmt(STROKE)}" stroke-linecap="round"/>')
            # under a non-uniform scale the circle would oval-ize; instead keep it ROUND,
            # centered at the oval's bbox center, radius = average of the oval semi-axes.
            # (avg-semi-axis = (sx+sy)*r/2; an area-preserving choice would be r*sqrt(sx*sy).)
            nr = sx * r if abs(sx - sy) < 1e-6 else (sx * r + sy * r) / 2
            for k, v in (("cx", ncx), ("cy", ncy), ("r", nr)):
                tag = re.sub(rf'\s{k}="[^"]*"', f' {k}="{fmt(v)}"', tag)
            return set_stroke(tag)
        return tag

    return rewrite


# ---- shape overlay --------------------------------------------------------
def shape_overlay(shape):
    """An SVG snippet outlining the matched grid shape at its native coords."""
    style = (f'fill="none" stroke="{SHAPE_STROKE}" stroke-width="{SHAPE_WIDTH}" '
             f'stroke-dasharray="{SHAPE_DASH}"')
    if shape["category"] == "circle":
        return f'<circle cx="512" cy="512" r="{shape["radius"]:g}" {style}/>'
    x, y, w, h, rx = (shape["x"], shape["y"], shape["width"],
                      shape["height"], shape["rx"])
    return (f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" '
            f'rx="{rx:g}" ry="{rx:g}" {style}/>')


def add_overlay(svg_text, snippet):
    """Insert an overlay snippet right after the opening <svg ...> tag."""
    m = SVG_OPEN_RE.search(svg_text)
    return svg_text[:m.end()] + "\n" + snippet + svg_text[m.end():]


def add_shape(svg_text, shape):
    return add_overlay(svg_text, shape_overlay(shape))


# background grid (from grid_system/background-grid.svg), wrapped in a removable
# group so it can be stripped later by deleting the <g id="background-grid"> element.
def _load_grid_group():
    txt = (GRID_DIR / "background-grid.svg").read_text()
    m = SVG_OPEN_RE.search(txt)
    inner = txt[m.end():txt.rindex("</svg>")].strip()
    return f'<g id="background-grid">\n{inner}\n</g>'


GRID_GROUP = _load_grid_group()


def assemble(icon_svg, guide=None):
    """Stack layers back->front: background grid, optional blue guide, then icon."""
    body = add_overlay(icon_svg, guide) if guide else icon_svg
    return add_overlay(body, GRID_GROUP)


def append_before_close(svg_text, snippet):
    """Insert a snippet just before </svg> (so it renders on top of everything)."""
    end = svg_text.rindex("</svg>")
    return svg_text[:end] + snippet + "\n" + svg_text[end:]


def stroke_layer(icon_svg):
    """A thin white copy of the icon's geometry -> marks the stroke centerline."""
    m = SVG_OPEN_RE.search(icon_svg)
    inner = icon_svg[m.end():icon_svg.rindex("</svg>")].strip()
    inner = re.sub(r'stroke="[^"]*"', f'stroke="{STROKE_LAYER_COLOR}"', inner)
    inner = re.sub(r'stroke-width="[^"]*"', f'stroke-width="{STROKE_LAYER_WIDTH}"', inner)
    inner = inner.replace('id="skeleton-shapes"', 'id="stroke-layer"')
    return inner


def write_outputs(out_dir, stem, icon_oval, icon_final, guide):
    """Emit the pipeline steps:
      _scale      : raw stretch (ovals), no overlays
      _oval       : raw stretch (ovals) + grid + blue guide
      _fit        : round + connections fixed + grid + guide + white centerline
      _fit_plain  : round + connections fixed + grid + blue guide (no centerline)
      _final      : round + connections fixed + grid (clean final result)"""
    g = guide if DRAW_SHAPE else None
    fit_body = icon_final
    if DRAW_STROKE_LAYER:
        fit_body = append_before_close(fit_body, stroke_layer(icon_final))
    out_dir.joinpath(f"{stem}_scale.svg").write_text(icon_oval)
    out_dir.joinpath(f"{stem}_oval.svg").write_text(assemble(icon_oval, g))
    out_dir.joinpath(f"{stem}_fit.svg").write_text(assemble(fit_body, g))
    out_dir.joinpath(f"{stem}_fit_plain.svg").write_text(assemble(icon_final, g))
    out_dir.joinpath(f"{stem}_final.svg").write_text(assemble(icon_final, None))


# ---- circle detection -----------------------------------------------------
def parse_circles(text):
    out = []
    for m in CIRCLE_TAG_RE.finditer(text):
        a = dict(ATTR_RE.findall(m.group(0)))
        try:
            out.append((float(a["cx"]), float(a["cy"]), float(a["r"])))
        except (KeyError, ValueError):
            pass
    return out


def _abs_path_points(d):
    """Absolute endpoint/control points in a path `d` -- the points _snap acts on."""
    items = [("c", c) if c else ("n", float(n)) for c, n in TOKEN_RE.findall(d)]
    pts, i, emit = [], 0, None
    while i < len(items):
        if items[i][0] == "c":
            cmd = items[i][1]; i += 1
        else:
            cmd = "L" if emit == "M" else ("l" if emit == "m" else emit)
        up = cmd.upper()
        if up == "Z":
            emit = cmd; continue
        n = ARITY[up]
        vals = [items[i + k][1] for k in range(n)]; i += n
        if not cmd.islower():                       # absolute only (matches _snap)
            if up in ("M", "L", "T"):
                pts.append((vals[0], vals[1]))
            elif up in ("C", "S", "Q"):
                pts += [(vals[k], vals[k + 1]) for k in range(0, n, 2)]
        emit = cmd
    return pts


def standalone_circles(text, circles):
    """Subset of `circles` (cx,cy,r) with NO path/line point within CONN_TOL of the radius."""
    pts = []
    for m in re.finditer(r'<path\b[^>]*?/?>', text, re.I):
        d = dict(ATTR_RE.findall(m.group(0))).get("d")
        if d:
            pts += _abs_path_points(d)
    for m in re.finditer(r'<line\b[^>]*?/?>', text, re.I):
        a = dict(ATTR_RE.findall(m.group(0)))
        try:
            pts += [(float(a["x1"]), float(a["y1"])), (float(a["x2"]), float(a["y2"]))]
        except (KeyError, ValueError):
            pass
    out = set()
    for cx, cy, r in circles:
        if not any(abs(math.hypot(x - cx, y - cy) - r) < CONN_TOL for x, y in pts):
            out.add((cx, cy, r))
    return out


# ---- near-circular <path> -> true <circle> --------------------------------
def _cubic(p0, p1, p2, p3, n):
    """n on-curve sample points along a cubic bezier (t in (0,1])."""
    out = []
    for k in range(1, n + 1):
        t = k / n; mt = 1 - t
        a, b, c, dd = mt * mt * mt, 3 * mt * mt * t, 3 * mt * t * t, t * t * t
        out.append((a * p0[0] + b * p1[0] + c * p2[0] + dd * p3[0],
                    a * p0[1] + b * p1[1] + c * p2[1] + dd * p3[1]))
    return out


def _quad(p0, p1, p2, n):
    out = []
    for k in range(1, n + 1):
        t = k / n; mt = 1 - t
        a, b, c = mt * mt, 2 * mt * t, t * t
        out.append((a * p0[0] + b * p1[0] + c * p2[0],
                    a * p0[1] + b * p1[1] + c * p2[1]))
    return out


def _flatten_path_points(d, n=16):
    """Dense on-curve sample points of a path `d` (absolute coords, relatives resolved)."""
    items = [("c", c) if c else ("n", float(num)) for c, num in TOKEN_RE.findall(d)]
    pts, i, emit = [], 0, None
    cx = cy = sx0 = sy0 = 0.0          # current point, subpath start
    pcx = pcy = None                   # previous cubic/quad control (for S/T reflection)
    while i < len(items):
        if items[i][0] == "c":
            cmd = items[i][1]; i += 1
        else:
            cmd = "L" if emit == "M" else ("l" if emit == "m" else emit)
        up = cmd.upper(); rel = cmd.islower()
        if up == "Z":
            cx, cy = sx0, sy0; pts.append((cx, cy)); emit = cmd; pcx = pcy = None; continue
        k = ARITY[up]
        vals = [items[i + j][1] for j in range(k)]; i += k
        ctrl = None
        if up in ("M", "L", "T"):
            x, y = (cx + vals[0], cy + vals[1]) if rel else (vals[0], vals[1])
            if up == "T":
                qx, qy = (2 * cx - pcx, 2 * cy - pcy) if pcx is not None else (cx, cy)
                pts += _quad((cx, cy), (qx, qy), (x, y), n); ctrl = (qx, qy)
            else:
                pts.append((x, y))
            cx, cy = x, y
            if up == "M":
                sx0, sy0 = x, y
        elif up == "H":
            cx = cx + vals[0] if rel else vals[0]; pts.append((cx, cy))
        elif up == "V":
            cy = cy + vals[0] if rel else vals[0]; pts.append((cx, cy))
        elif up in ("C", "S", "Q"):
            pairs = [(vals[j], vals[j + 1]) for j in range(0, k, 2)]
            if rel:
                pairs = [(cx + px, cy + py) for px, py in pairs]
            if up == "C":
                c1, c2, end = pairs
            elif up == "S":
                c1 = (2 * cx - pcx, 2 * cy - pcy) if pcx is not None else (cx, cy)
                c2, end = pairs
            else:  # Q
                qc, end = pairs
            if up == "Q":
                pts += _quad((cx, cy), qc, end, n); ctrl = qc
            else:
                pts += _cubic((cx, cy), c1, c2, end, n); ctrl = c2
            cx, cy = end
        elif up == "A":
            cx, cy = (cx + vals[5], cy + vals[6]) if rel else (vals[5], vals[6])
            pts.append((cx, cy))
        pcx, pcy = (ctrl if ctrl is not None else (None, None))
        emit = cmd
    return pts


def _fit_circle(points):
    """Kasa algebraic least-squares circle fit. Returns (cx,cy,r) or None."""
    if len(points) < 12:
        return None
    p = np.asarray(points, dtype=float)
    x, y = p[:, 0], p[:, 1]
    A = np.c_[2 * x, 2 * y, np.ones(len(x))]
    b = x * x + y * y
    try:
        sol, *_ = np.linalg.lstsq(A, b, rcond=None)
    except np.linalg.LinAlgError:
        return None
    a, bb, c = sol
    rad2 = c + a * a + bb * bb
    if rad2 <= 0:
        return None
    return float(a), float(bb), float(math.sqrt(rad2))


def circular_path_circle(d):
    """If path `d` is a closed near-circle, return its fitted (cx,cy,r); else None."""
    if "z" not in d and "Z" not in d:          # must be a closed loop
        return None
    pts = _flatten_path_points(d)
    fit = _fit_circle(pts)
    if fit is None:
        return None
    cx, cy, r = fit
    if r <= 0:
        return None
    p = np.asarray(pts, dtype=float)
    dev = np.abs(np.hypot(p[:, 0] - cx, p[:, 1] - cy) - r)
    if np.mean(dev <= CIRCLIFY_TOL * r) < CIRCLIFY_MIN_FRAC:
        return None
    w = p[:, 0].max() - p[:, 0].min()
    h = p[:, 1].max() - p[:, 1].min()
    if h <= 0 or not (CIRCLIFY_ASPECT[0] <= w / h <= CIRCLIFY_ASPECT[1]):
        return None
    # full-loop guard: sampled points must reach all four quadrants around the center
    ang = np.arctan2(p[:, 1] - cy, p[:, 0] - cx)
    quads = set(((ang + math.pi) // (math.pi / 2)).astype(int).tolist())
    if len(quads) < 4:
        return None
    return cx, cy, r


def circlify_paths(text):
    """Replace every closed near-circular <path> with a true <circle> (round-shape normalize)."""
    def repl(m):
        a = dict(ATTR_RE.findall(m.group(0)))
        d = a.get("d")
        if not d or "transform" in a:      # transformed path -> warn path, not circlify
            return m.group(0)
        fit = circular_path_circle(d)
        if fit is None:
            return m.group(0)
        cx, cy, r = fit
        idattr = f'id="{a["id"]}" ' if "id" in a else ""
        fill = a.get("fill", "none")
        stroke = a.get("stroke", "#000000")
        sw = a.get("stroke-width", fmt(STROKE))
        if _VERBOSE:
            print(f"  circlify: <path {a.get('id', '?')}> -> <circle> "
                  f"(cx={cx:.1f} cy={cy:.1f} r={r:.1f})")
        return (f'<circle {idattr}cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(r)}" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    return re.sub(r'<path\b[^>]*?/?>(?:\s*</path\s*>)?', repl, text, flags=re.I)


def circlify_ellipses(text):
    """Replace every near-round <ellipse> (rx/ry within CIRCLIFY_ASPECT) with a true
    <circle> of r=(rx+ry)/2 so all the circle handling (wrap/round/dot) applies. A
    circle-preserving transform (rotation + translation + uniform scale, any center)
    is folded into cx/cy/r -- an off-center rotate MOVES the shape, so the center
    must ride through the matrix, not be copied verbatim. Anything else (non-uniform
    scale, skew, unparseable) is left for ellipse_to_path to bake exactly."""
    def repl(m):
        a = dict(ATTR_RE.findall(m.group(0)))
        try:
            cx = float(a.get("cx", 0) or 0)
            cy = float(a.get("cy", 0) or 0)
            rx = float(a.get("rx", a.get("ry", 0)) or 0)
            ry = float(a.get("ry", a.get("rx", 0)) or 0)
        except ValueError:
            return m.group(0)
        if rx <= 0 or ry <= 0 or not (CIRCLIFY_ASPECT[0] <= rx / ry <= CIRCLIFY_ASPECT[1]):
            return m.group(0)
        r = (rx + ry) / 2
        tr = a.get("transform")
        if tr and tr.strip():
            mtx = _parse_transform(tr)
            if mtx is None:
                return m.group(0)          # unparseable -> warned + passed through
            ma, mb, mc, md = mtx[0], mtx[1], mtx[2], mtx[3]
            n1, n2 = math.hypot(ma, mb), math.hypot(mc, md)
            eps = 1e-6 * max(n1, n2, 1.0)
            if abs(n1 - n2) > eps or abs(ma * mc + mb * md) > eps * max(n1, 1.0):
                return m.group(0)          # not circle-preserving -> ellipse_to_path
            cx, cy = apply_mat(mtx, cx, cy)
            r *= n1
        idattr = f'id="{a["id"]}" ' if "id" in a else ""
        fill = a.get("fill", "none")
        stroke = a.get("stroke", "#000000")
        sw = a.get("stroke-width", fmt(STROKE))
        if _VERBOSE:
            print(f"  circlify: <ellipse {a.get('id', '?')}> -> <circle> "
                  f"(cx={cx:.1f} cy={cy:.1f} r={r:.1f})")
        return (f'<circle {idattr}cx="{fmt(cx)}" cy="{fmt(cy)}" '
                f'r="{fmt(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    return re.sub(r'<ellipse\b[^>]*?/?>(?:\s*</ellipse\s*>)?', repl, text, flags=re.I)


def wrapping_circle(text, ink):
    """Return (cx,cy,r) of a big circle that encloses all content, else None."""
    circles = parse_circles(text)
    if not circles:
        return None
    cx, cy, r = max(circles, key=lambda c: c[2])
    ix0, iy0, ix1, iy1 = ink
    beyond = max((cx - r - HALF) - ix0, ix1 - (cx + r + HALF),
                 (cy - r - HALF) - iy0, iy1 - (cy + r + HALF))
    if r >= MIN_BIG_R and beyond <= WRAP_TOL:
        return (cx, cy, r)
    return None


# ---- measurement / target -------------------------------------------------
def ink_bbox_units(svg):
    rgba, (w, _h) = render_rgba(svg, RENDER_W)
    bb = ink_bbox(rgba[:, :, 3] > ALPHA_THRESHOLD)
    if bb is None:
        return None
    s = VIEWBOX / w
    return tuple(v * s for v in bb)


def ink_bbox_units_text(text):
    """Ink bbox (user units) of rendered SVG markup (already stroke-normalized)."""
    rgba, (w, _h) = render_rgba_text(text, RENDER_W)
    bb = ink_bbox(rgba[:, :, 3] > ALPHA_THRESHOLD)
    if bb is None:
        return None
    s = VIEWBOX / w
    return tuple(v * s for v in bb)


def fit_ink_size(shape):
    """Target INK size = the grid shape's OWN dimensions (centered at 512,512),
    so the icon keeps the same padding the grid shape has within the canvas."""
    return shape["width"], shape["height"]


def uniform_fit_params(ink, target_max=MAX_FIT):
    """Uniform scale (aspect locked) so the longer ink side = target_max, centered."""
    ix0, iy0, ix1, iy1 = ink
    gmax = max(ix1 - ix0, iy1 - iy0) - STROKE      # geometry long side (ink - stroke halo)
    s = (target_max - STROKE) / gmax
    gcx, gcy = (ix0 + ix1) / 2, (iy0 + iy1) / 2
    return s, CENTER - s * gcx, CENTER - s * gcy


def snap_params(ink, shape):
    ix0, iy0, ix1, iy1 = ink
    gx0, gy0 = ix0 + HALF, iy0 + HALF
    gw, gh = (ix1 - ix0) - STROKE, (iy1 - iy0) - STROKE
    fw, fh = fit_ink_size(shape)
    fgw, fgh = fw - STROKE, fh - STROKE
    fgx0, fgy0 = CENTER - fgw / 2, CENTER - fgh / 2
    sx, sy = fgw / gw, fgh / gh
    ex, ey = fgx0 - sx * gx0, fgy0 - sy * gy0
    return sx, sy, ex, ey, fw, fh


# ---- driver ---------------------------------------------------------------
MANIFEST = OUTPUT_DIR / "manifest.json"


def _box(x, y, w, h):
    return [round(x, 1), round(y, 1), round(w, 1), round(h, 1)]


def snap_svg_text(text):
    """Snap one icon SVG (1024 viewBox) onto its nearest grid shape -- the pure core
    of the pipeline, no file I/O. Reusable from execution.py and process() alike.

    Returns (icon_oval, icon_final, shape, meta):
      icon_oval   : raw non-uniform stretch (ovals); == icon_final for uniform branches
      icon_final  : the GRIDLESS baked icon (what the _final.svg embeds, before the grid
                    overlay is assembled on top) -- this is the snapped output to ship
      shape       : the matched grid-shape dict (for shape_overlay), or None if empty
      meta        : { status: 'ok'|'empty', label, before[x,y,w,h], after[x,y,w,h],
                      affine[sx,sy,ex,ey], branch, log_suffix, unsupported[...] }
    On an empty icon (no ink) returns (None, None, None, {status:'empty', unsupported}).
    """
    text = normalize_stroke(text)                # input stroke -> 51.2 (consistent)
    text = circlify_paths(text)                  # near-circular <path> -> true <circle>
    text = circlify_ellipses(text)               # near-round <ellipse> -> true <circle>

    unsupported = {m.group(1).lower() for m in UNSUPPORTED_RE.finditer(text)}
    for m in GROUP_TRANSFORM_RE.finditer(text):
        unsupported.add(f"{m.group(1).lower()} transform=...")
    # geometry elements whose transform the baker will NOT fold: path/line/circle
    # (their rewriters can't take a general matrix) and anything unparseable.
    for m in ELEM_RE.finditer(text):
        tr = dict(ATTR_RE.findall(m.group(0))).get("transform")
        if not tr or not tr.strip():
            continue
        name = m.group(1).lower()
        if name in ("path", "line", "circle") or _parse_transform(tr) is None:
            unsupported.add(f"{name} transform=...")
    unsupported = sorted(unsupported)

    ink = ink_bbox_units_text(text)
    if ink is None:
        return None, None, None, {"status": "empty", "unsupported": unsupported}
    ix0, iy0, ix1, iy1 = ink
    bw, bh = ix1 - ix0, iy1 - iy0
    before = _box(ix0, iy0, bw, bh)

    # ---- circle branch -----------------------------------------------------
    if HAS_CIRCLE_RE.search(text):
        wc = wrapping_circle(text, ink)
        if wc is None:                         # small circle -> rect/square stretch
            shape = nearest_shape(bw, bh)
            sx, sy, ex, ey, fw, fh = snap_params(ink, shape)
            circles = parse_circles(text)
            # round map: each circle -> new round circle (avg-semi-axis radius
            # (sx+sy)*r/2; area-preserving alt would be r*sqrt(sx*sy)), used to re-round
            # and to radially snap any path/line points that connect to it.
            round_map = [(cx, cy, r, sx * cx + ex, sy * cy + ey, (sx * r + sy * r) / 2)
                         for cx, cy, r in circles]
            # standalone circles too small to read as a ring -> collapse to a stroke dot
            # in the final variants only (re-rounded diameter (sx+sy)*r < DOT_MAX_DIAM).
            free = standalone_circles(text, circles)
            dot_keys = {(cx, cy, r) for (cx, cy, r) in circles
                        if (cx, cy, r) in free and (sx * r + sy * r) < DOT_MAX_DIAM}
            icon_oval = ELEM_RE.sub(make_rewriter(sx, sy, ex, ey, None), text)
            icon_final = ELEM_RE.sub(
                make_rewriter(sx, sy, ex, ey, round_map, dot_keys), text)
            after = _box(CENTER - fw / 2, CENTER - fh / 2, fw, fh)
            log_suffix = (f"small circle -> rect stretch {shape['name']} "
                          f"(round {len(round_map)} circle(s))")
            return icon_oval, icon_final, shape, {
                "status": "ok", "label": "small-circle-fit", "before": before,
                "after": after, "affine": [float(sx), float(sy), float(ex), float(ey)],
                "branch": "small-circle", "log_suffix": log_suffix,
                "unsupported": unsupported}
        cx, cy, r = wc
        # match the circle's INK (not centerline) to the grid circle dimension,
        # like the rects do -> output ink Ø = 819.2 = 16 cells (was 17 cells).
        s = (CIRCLE_GRID_R - HALF) / r
        ex, ey = CENTER - s * cx, CENTER - s * cy
        icon = ELEM_RE.sub(make_rewriter(s, s, ex, ey), text)   # uniform -> stays round
        rad = CIRCLE_GRID_R                    # ink radius now = grid radius
        after = _box(CENTER - rad, CENTER - rad, 2 * rad, 2 * rad)
        log_suffix = f"circle r={r:5.0f} -> shape-circle (uniform s={s:.2f}, centered)"
        return icon, icon, CIRCLE_SHAPE, {
            "status": "ok", "label": "circle", "before": before, "after": after,
            "affine": [float(s), float(s), float(ex), float(ey)], "branch": "circle",
            "log_suffix": log_suffix, "unsupported": unsupported}

    # ---- rect branch -------------------------------------------------------
    shape = nearest_shape(bw, bh)              # excludes circle by default
    sx, sy, ex, ey, fw, fh = snap_params(ink, shape)

    icon = ELEM_RE.sub(make_rewriter(sx, sy, ex, ey), text)   # no circles here
    label = shape["name"].replace("shape-", "")
    after = _box(CENTER - fw / 2, CENTER - fh / 2, fw, fh)
    log_suffix = (f"{bw:5.0f}x{bh:<5.0f} ar={bw/bh:4.2f} -> "
                  f"{label:<20} fill {fw:.0f}x{fh:.0f}  (sx={sx:.2f}, sy={sy:.2f})")
    return icon, icon, shape, {
        "status": "ok", "label": label, "before": before, "after": after,
        "affine": [float(sx), float(sy), float(ex), float(ey)], "branch": "rect",
        "log_suffix": log_suffix, "unsupported": unsupported}


def process(svg):
    """Bake one icon to its 5 output variants; return a manifest record (or None if
    empty/skipped). Thin wrapper over snap_svg_text() that does the file I/O + logging."""
    out_dir = OUTPUT_DIR / svg.stem
    out_dir.mkdir(parents=True, exist_ok=True)

    icon_oval, icon_final, shape, meta = snap_svg_text(svg.read_text())

    if meta["unsupported"]:
        print(f"WARN: {svg.name} contains untransformed "
              f"<{'>, <'.join(meta['unsupported'])}> -- left as-is (not baked).")

    if meta["status"] == "empty":
        for suffix in ("_scale.svg", "_oval.svg", "_fit.svg", "_fit_plain.svg", "_final.svg"):
            shutil.copyfile(svg, out_dir / f"{svg.stem}{suffix}")
        print(f"SKIP (empty): {svg.name}")
        return None

    write_outputs(out_dir, svg.stem, icon_oval, icon_final, shape_overlay(shape))
    print(f"{svg.name:<46} {meta['log_suffix']}")
    return {"name": svg.name, "before": meta["before"],
            "after": meta["after"], "label": meta["label"]}


def main():
    svgs = sorted(p for p in INPUT_DIR.glob("*.svg"))
    if not svgs:
        raise SystemExit(f"No SVGs found in {INPUT_DIR}")
    print(f"Baking {len(svgs)} icons -> {OUTPUT_DIR}/<name>/<name>_fit.svg\n")
    records = [r for s in svgs if (r := process(s))]

    # manifest: all per-icon bbox/shape data, so the report needs no re-rendering
    MANIFEST.write_text(json.dumps({"items": records}, separators=(",", ":")))
    print(f"\nDone: {len(records)} baked, {len(svgs) - len(records)} skipped.")
    print(f"Wrote {MANIFEST.name} ({len(records)} records).")
    tally = {}
    for r in records:
        tally[r["label"]] = tally.get(r["label"], 0) + 1
    print("\n=== shape tally ===")
    for name, n in sorted(tally.items(), key=lambda kv: -kv[1]):
        print(f"  {name.replace('shape-',''):<22} {n}")


if __name__ == "__main__":
    main()
