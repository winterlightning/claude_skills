#!/usr/bin/env python3
"""Convert icons-json construction graphs into SOLO48 model modules.

    python3 icon_set/scripts/json_to_solo.py run --mode fit
    python3 icon_set/scripts/json_to_solo.py run --mode bezier
    python3 icon_set/scripts/json_to_solo.py run --mode fit --limit 40

Each JSON file already holds the icon as a graph -- nodes, typed elements,
contours, relations -- so conversion is code generation, not re-authoring.
Lines, arcs, circles and dots map one-to-one onto the model API. Curves
(``bezier`` and traced ``polyline`` elements) are the only lossy part:

* ``--mode fit``    replaces every curve with integer lines and integer-radius
                    arcs, so the module runs on the engine as it is today.
* ``--mode bezier`` keeps the cubics through ``add_bezier`` (the ``Bezier``
                    primitive).

Everything is written under ``staging/json-solo/<mode>/`` and nothing touches
``icon_set/model/icons/solo`` -- promotion is a separate, approved step.
Icons are scaled into their SOLO48 keyshape box first: the JSON is drawn edge
to edge on the 48 canvas, the keyshapes are not.
Validation and raster fidelity run in a process pool, one icon per task.
"""

from __future__ import annotations

import argparse
import glob
import importlib
import io
import json
import keyword
import math
import os
import re
import sys
import time
import types
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HERE = REPO / "staging" / "json-solo"
JSON_ROOT = REPO / "icons-json"
MAIN_SOLO = REPO / "icon_set" / "model" / "icons" / "solo"
ENGINE = {"fit": REPO, "bezier": REPO}

KEYSHAPES = {"square": "SQUARE", "circle": "CIRCLE", "h-rect": "HRECT_L", "v-rect": "VRECT_L"}
UUID = re.compile(r"_([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$")

#: SOLO48 centerline boxes (visible ink minus the 2-unit stroke radius).
TARGET_BOX = {"SQUARE": (6, 6, 42, 42), "HRECT_L": (4, 8, 44, 40), "VRECT_L": (8, 4, 40, 44)}
CIRCLE_RADIUS = 20

#: Largest allowed distance, in canvas units, between a fitted run and its curve.
FIT_TOLERANCE = 0.75
#: Recursion cap for splitting one curve into lines and arcs.
FIT_DEPTH = 7


# -- geometry --------------------------------------------------------------

def _cubic(p0, c1, c2, p3, t):
    u = 1.0 - t
    return (
        u**3 * p0[0] + 3 * u * u * t * c1[0] + 3 * u * t * t * c2[0] + t**3 * p3[0],
        u**3 * p0[1] + 3 * u * u * t * c1[1] + 3 * u * t * t * c2[1] + t**3 * p3[1],
    )


def _curve_samples(start, element, per_segment=40):
    """Dense centerline samples for a bezier/polyline element."""
    cubics = element.get("cubics")
    if not cubics:
        return [tuple(map(float, p)) for p in element["points"]]
    points = [start]
    p0 = start
    for c1, c2, p3 in cubics:
        for index in range(1, per_segment + 1):
            points.append(_cubic(p0, c1, c2, p3, index / per_segment))
        p0 = tuple(p3)
    return points


def _hausdorff(a, b):
    import numpy as np
    d = np.linalg.norm(a[:, None, :] - b[None, :, :], axis=2)
    return float(max(d.min(axis=1).max(), d.min(axis=0).max()))


def _line_points(a, b):
    import numpy as np
    n = max(2, int(math.dist(a, b) * 3) + 1)
    return np.linspace(a, b, n)


def _arc_candidates(a, b, samples):
    """Integer-radius circular arcs from integer ``a`` to ``b`` near ``samples``."""
    import numpy as np
    from icon_set.model.primitives import Arc, Point
    from icon_set.validation.envelope import DegenerateArcError, arc_geometry, centerline_points, _radial_extent

    chord = math.dist(a, b)
    if chord < 1:
        return []
    # Least-squares circle, then read its radius; try the neighbouring integers.
    x, y = samples[:, 0], samples[:, 1]
    matrix = np.column_stack((2 * x, 2 * y, np.ones_like(x)))
    try:
        (cx, cy, k), *_ = np.linalg.lstsq(matrix, x * x + y * y, rcond=None)
    except np.linalg.LinAlgError:
        return []
    radius = math.sqrt(max(k + cx * cx + cy * cy, 0.0))
    if not math.isfinite(radius) or radius > 80:
        return []
    radii = {max(math.ceil(chord / 2), r) for r in (math.floor(radius), math.ceil(radius))}
    out = []
    for r in sorted(radii):
        for large in (False, True):
            for sweep in (False, True):
                arc = Arc("fit", Point(*a), Point(*b), r, r, large, sweep)
                try:
                    g = arc_geometry(arc)
                except (DegenerateArcError, ValueError, ZeroDivisionError):
                    continue
                n = max(8, int(abs(g.delta_angle) * r * 3))
                pts = np.array([g.point(g.start_angle + g.delta_angle * i / n) for i in range(n + 1)])
                # Exact extent from the validator's own closed-form extrema.
                extent = np.array(centerline_points(arc))
                reach = _radial_extent(arc, (24, 24))
                out.append((_hausdorff(samples, pts), ("arc", a, b, r, large, sweep), (extent, reach)))
    return out


def _inside(extent, box):
    """True when an arc's exact extrema stay within the keyshape centerline limit."""
    points, reach = extent
    eps = 1e-9
    if box[0] == "circle":
        return reach <= CIRCLE_RADIUS + eps
    l, t, r, b = box
    return bool((points[:, 0] >= l - eps).all() and (points[:, 0] <= r + eps).all()
                and (points[:, 1] >= t - eps).all() and (points[:, 1] <= b + eps).all())


def _edge_node(point, box):
    """Round a sample to the grid, seated on the edge it touches, never outside."""
    x, y = point
    if box[0] == "circle":
        options = [(fx, fy) for fx in (math.floor(x), math.ceil(x)) for fy in (math.floor(y), math.ceil(y))
                   if math.dist((fx, fy), (24, 24)) <= CIRCLE_RADIUS]
        return min(options, key=lambda o: math.dist(o, point)) if options else (int(round(x)), int(round(y)))
    l, t, r, b = box
    nx, ny = min(max(int(round(x)), l), r), min(max(int(round(y)), t), b)
    for edge, value in ((l, x), (r, x)):
        if abs(value - edge) < 0.5:
            nx = edge
    for edge, value in ((t, y), (b, y)):
        if abs(value - edge) < 0.5:
            ny = edge
    return (nx, ny)


def _edge_touches(pts, box):
    """Sample indices where the curve kisses the keyshape limit (one per run)."""
    import numpy as np
    if box[0] == "circle":
        gap = CIRCLE_RADIUS - np.hypot(pts[:, 0] - 24, pts[:, 1] - 24)
    else:
        l, t, r, b = box
        gap = np.min(np.abs(np.column_stack((pts[:, 0] - l, r - pts[:, 0], pts[:, 1] - t, b - pts[:, 1]))), axis=1)
    near = gap < 0.5
    found, index = [], 0
    while index < len(pts):
        if near[index]:
            end = index
            while end + 1 < len(pts) and near[end + 1]:
                end += 1
            found.append(index + int(gap[index:end + 1].argmin()))
            index = end + 1
        else:
            index += 1
    return found


def fit_curve(samples, start, end, box):
    """Replace one sampled curve with integer lines and arcs.

    Returns ``(pieces, worst_deviation)``. Each piece is ``("line", a, b)`` or
    ``("arc", a, b, r, large, sweep)`` with integer endpoints, head to tail.
    Where the curve touches the keyshape limit it is split on a node seated
    exactly on that limit, and no fitted arc may bulge past it.
    """
    import numpy as np

    pts = np.array(samples, dtype=float)
    worst = 0.0

    def solve(i, j, a, b, depth):
        nonlocal worst
        span = pts[i:j + 1]
        if len(span) > 160:
            span = span[np.linspace(0, len(span) - 1, 160).astype(int)]
        options = []
        if a != b:
            options.append((_hausdorff(span, _line_points(a, b)), ("line", a, b), None))
            options.extend(o for o in _arc_candidates(a, b, span) if o[2] is None or _inside(o[2], box))
        best = min(options, default=(math.inf, None, None), key=lambda o: o[0])
        if best[1] is not None and (best[0] <= FIT_TOLERANCE or depth >= FIT_DEPTH or j - i < 6):
            worst = max(worst, best[0])
            return [best[1]]
        if j - i < 6:
            return []
        # Split where the curve leaves the chord furthest, nudged to a sample
        # that rounds cleanly so the new node sits on the grid.
        ax, ay = a
        bx, by = b
        if a == b:
            dev = np.hypot(pts[i:j + 1, 0] - ax, pts[i:j + 1, 1] - ay)
        else:
            dev = np.abs((by - ay) * pts[i:j + 1, 0] - (bx - ax) * pts[i:j + 1, 1] + bx * ay - by * ax) / math.dist(a, b)
        k = i + int(dev.argmax())
        window = max(2, (j - i) // 8)
        lo, hi = max(i + 3, k - window), min(j - 3, k + window)
        if lo > hi:
            k = (i + j) // 2
        else:
            idx = np.arange(lo, hi + 1)
            err = np.hypot(*(pts[idx] - np.round(pts[idx])).T) + 0.15 * np.abs(idx - k) / window
            k = int(idx[err.argmin()])
        s = _edge_node(pts[k], box)
        if s in (a, b):
            k = (i + j) // 2
            s = _edge_node(pts[k], box)
        return solve(i, k, a, s, depth + 1) + solve(k, j, s, b, depth + 1)

    anchors = [(0, start)]
    for k in _edge_touches(pts, box):
        node = _edge_node(pts[k], box)
        if k - anchors[-1][0] >= 4 and len(pts) - 1 - k >= 4 and node not in (anchors[-1][1], end):
            anchors.append((k, node))
    anchors.append((len(pts) - 1, end))
    pieces = []
    for (i, a), (j, b) in zip(anchors, anchors[1:]):
        pieces += solve(i, j, a, b, 0)
    return [p[:6] for p in pieces if p[1] != p[2]], worst


# -- keyshape frame ----------------------------------------------------------

def _raw_points(data):
    """Every centerline point that can set the drawing's extent."""
    from icon_set.model.primitives import Arc, Point
    from icon_set.validation.envelope import arc_geometry

    nodes = {n["id"]: (float(n["x"]), float(n["y"])) for n in data["nodes"]}
    pts = list(nodes.values())
    for e in data["elements"]:
        k = e["kind"]
        if k == "dot":
            pts.append((e["x"], e["y"]))
        elif k == "circle":
            pts += [(e["cx"] - e["r"], e["cy"]), (e["cx"] + e["r"], e["cy"]),
                    (e["cx"], e["cy"] - e["r"]), (e["cx"], e["cy"] + e["r"])]
        elif k == "arc":
            a, b = (nodes[n] for n in e["nodes"])
            try:
                g = arc_geometry(Arc("x", Point(*a), Point(*b), e.get("rx", e["r"]), e.get("ry", e["r"]),
                                     bool(e.get("large_arc")), bool(e.get("sweep", 1))))
                pts += [g.point(g.start_angle + g.delta_angle * i / 90) for i in range(91)]
            except Exception:
                pass
        elif k in ("bezier", "polyline"):
            pts += _curve_samples(nodes[e["nodes"][0]], e, 24)
    return pts


def to_keyshape_frame(data):
    """Map the JSON drawing (drawn edge to edge) onto its SOLO48 centerline box.

    Rectangular keyshapes stretch each axis independently, as the JSON
    pipeline's own "stretch all icons" fit did; CIRCLE scales uniformly so
    circles stay round. Returns a transformed deep copy and the two scales.
    """
    import copy

    keyshape = KEYSHAPES[data["pipeline"]["keyshape_fit"]["keyshape"]]
    pts = _raw_points(data)
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    left, top, right, bottom = min(xs), min(ys), max(xs), max(ys)
    if keyshape == "CIRCLE":
        cx, cy = (left + right) / 2, (top + bottom) / 2
        reach = max(math.dist((cx, cy), p) for p in pts) or 1.0
        sx = sy = CIRCLE_RADIUS / reach
        fx = lambda x: 24 + (x - cx) * sx  # noqa: E731
        fy = lambda y: 24 + (y - cy) * sy  # noqa: E731
    else:
        tl, tt, tr, tb = TARGET_BOX[keyshape]
        sx = (tr - tl) / (right - left) if right - left >= 1 else None
        sy = (tb - tt) / (bottom - top) if bottom - top >= 1 else None
        sx, sy = sx or sy or 1.0, sy or sx or 1.0
        ox = tl if right - left >= 1 else (tl + tr) / 2 - (right + left) / 2 * sx + left * sx
        oy = tt if bottom - top >= 1 else (tt + tb) / 2 - (bottom + top) / 2 * sy + top * sy
        fx = lambda x: ox + (x - left) * sx  # noqa: E731
        fy = lambda y: oy + (y - top) * sy  # noqa: E731

    out = copy.deepcopy(data)
    pt = lambda p: [fx(p[0]), fy(p[1])]  # noqa: E731
    for n in out["nodes"]:
        n["x"], n["y"] = fx(n["x"]), fy(n["y"])
    for e in out["elements"]:
        k = e["kind"]
        if k == "dot":
            e["x"], e["y"] = fx(e["x"]), fy(e["y"])
        elif k == "circle":
            e["cx"], e["cy"] = fx(e["cx"]), fy(e["cy"])
            e["rx"], e["ry"] = e["r"] * sx, e["r"] * sy
        elif k == "arc":
            rx, ry = e.get("rx", e["r"]), e.get("ry", e["r"])
            e["rx"], e["ry"] = rx * sx, ry * sy
        elif k in ("bezier", "polyline"):
            if e.get("cubics"):
                e["cubics"] = [[pt(c1), pt(c2), pt(p3)] for c1, c2, p3 in e["cubics"]]
            if e.get("points"):
                e["points"] = [pt(p) for p in e["points"]]
    return out, (sx, sy)


# -- bezier seating ----------------------------------------------------------

def _split_cubic(p0, c1, c2, p3, t):
    lerp = lambda u, v: [u[0] + (v[0] - u[0]) * t, u[1] + (v[1] - u[1]) * t]  # noqa: E731
    a, b, c = lerp(p0, c1), lerp(c1, c2), lerp(c2, p3)
    d, e = lerp(a, b), lerp(b, c)
    f = lerp(d, e)
    return [a, d, f], [e, c, list(p3)]


def seat_beziers(chains, box, reached):
    """Keep every cubic inside the keyshape limit and touching it where it must.

    ``chains`` maps element id -> ``(start, segments)`` with mutable segments.
    Controls are clamped into the limit (a cubic lies in the convex hull of its
    points, so it can no longer overshoot). For every rectangle side that no
    straight geometry reaches, the curve that comes closest is split at its
    apex, and that knot and both neighbouring controls are placed on the side:
    the apex then sits exactly on the envelope.
    """
    if box[0] == "circle":
        for start, segments in chains.values():
            for segment in segments:
                for point in segment[:2] + ([segment[2]] if segment is not segments[-1] else []):
                    d = math.dist(point, (24, 24))
                    if d > CIRCLE_RADIUS:
                        point[0] = 24 + (point[0] - 24) * CIRCLE_RADIUS / d
                        point[1] = 24 + (point[1] - 24) * CIRCLE_RADIUS / d
        return
    l, t, r, b = box
    for start, segments in chains.values():
        for index, segment in enumerate(segments):
            movable = segment[:2] if index == len(segments) - 1 else segment
            for point in movable:
                point[0] = min(max(point[0], l), r)
                point[1] = min(max(point[1], t), b)
    for axis, edge, sign in ((0, l, -1), (0, r, 1), (1, t, -1), (1, b, 1)):
        if reached[(axis, edge)]:
            continue
        best = None
        for eid, (start, segments) in chains.items():
            p0 = list(start)
            for index, (c1, c2, p3) in enumerate(segments):
                for step in range(1, 64):
                    tt = step / 64
                    value = _cubic(p0, c1, c2, p3, tt)[axis] * sign
                    if best is None or value > best[0]:
                        best = (value, eid, index, tt, list(p0))
                p0 = p3
        if best is None or abs(best[0] * sign - edge) > 1.5:
            continue
        _, eid, index, tt, p0 = best
        segments = chains[eid][1]
        c1, c2, p3 = segments[index]
        first, second = _split_cubic(p0, c1, c2, p3, tt)
        first[1][axis] = first[2][axis] = second[0][axis] = edge
        segments[index:index + 1] = [first, second]


# -- conversion ------------------------------------------------------------

def _pt(x, y):
    return (int(round(x)), int(round(y)))


def _fmt(v):
    v = round(float(v), 3)
    return str(int(v)) if v.is_integer() else repr(v)


def _fmt_pt(p):
    return f"({_fmt(p[0])}, {_fmt(p[1])})"


def _slug(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "icon"
    # icon_id must start with a letter ("3g" -> "icon-3g").
    return slug if slug[0].isalpha() else f"icon-{slug}"


def convert(data, mode):
    """Return ``(body_lines, stats)`` for one JSON graph."""
    keyshape = KEYSHAPES[data["pipeline"]["keyshape_fit"]["keyshape"]]
    box = ("circle",) if keyshape == "CIRCLE" else TARGET_BOX[keyshape]
    chains: dict[str, tuple] = {}
    nodes = {n["id"]: n for n in data["nodes"]}
    if box[0] == "circle":
        # Round inward: a node on the CIRCLE limit must not land outside it.
        node_pt = {k: _edge_node((float(n["x"]), float(n["y"])), box) for k, n in nodes.items()}
    else:
        node_pt = {k: _pt(n["x"], n["y"]) for k, n in nodes.items()}
    rounded = sum(1 for n in data["nodes"] if not (float(n["x"]).is_integer() and float(n["y"]).is_integer()))
    elements = {e["id"]: e for e in data["elements"]}
    lines: list[str] = []
    stats = {"rounded_nodes": rounded, "fit_max": 0.0, "curves": 0, "primitives": 0}
    # element id -> ordered primitive ids it became (for contour expansion)
    expanded: dict[str, list[str]] = {}
    self_contained: set[str] = set()  # elements emitted as their own contour

    def emit_pieces(eid, pieces):
        ids = []
        many = len(pieces) > 1
        for index, piece in enumerate(pieces, 1):
            pid = f"{eid}-{index}" if many else eid
            if piece[0] == "line":
                lines.append(f"self.add_line({pid!r}, {_fmt_pt(piece[1])}, {_fmt_pt(piece[2])})")
            else:
                _, a, b, r, large, sweep = piece
                flags = (", large_arc=True" if large else "") + ("" if sweep else ", sweep=False")
                lines.append(f"self.add_arc({pid!r}, {_fmt_pt(a)}, {_fmt_pt(b)}, radius_x={r}{flags})")
            ids.append(pid)
        stats["primitives"] += len(ids)
        return ids

    for element in data["elements"]:
        eid, kind = element["id"], element["kind"]
        if kind == "dot":
            lines.append(f"self.add_dot({eid!r}, {_fmt_pt(_pt(element['x'], element['y']))})")
            expanded[eid] = [eid]
            stats["primitives"] += 1
        elif kind == "circle":
            cx, cy = _pt(element["cx"], element["cy"])
            rx = max(1, int(round(element.get("rx", element["r"]))))
            ry = max(1, int(round(element.get("ry", element["r"]))))
            ry_arg = f", radius_y={ry}" if ry != rx else ""
            lines.append(f"self.add_arc({eid + '-top'!r}, ({cx - rx}, {cy}), ({cx + rx}, {cy}), radius_x={rx}{ry_arg})")
            lines.append(f"self.add_arc({eid + '-bottom'!r}, ({cx + rx}, {cy}), ({cx - rx}, {cy}), radius_x={rx}{ry_arg})")
            expanded[eid] = [eid + "-top", eid + "-bottom"]
            self_contained.add(eid)
            stats["primitives"] += 2
        elif kind == "line":
            a, b = (node_pt[n] for n in element["nodes"])
            lines.append(f"self.add_line({eid!r}, {_fmt_pt(a)}, {_fmt_pt(b)})")
            expanded[eid] = [eid]
            stats["primitives"] += 1
        elif kind == "arc":
            a, b = (node_pt[n] for n in element["nodes"])
            rx = max(1, int(round(element.get("rx", element["r"]))))
            ry = max(1, int(round(element.get("ry", element["r"]))))
            ry_arg = f", radius_y={ry}" if ry != rx else ""
            flags = (", large_arc=True" if element.get("large_arc") else "") + ("" if element.get("sweep", 1) else ", sweep=False")
            lines.append(f"self.add_arc({eid!r}, {_fmt_pt(a)}, {_fmt_pt(b)}, radius_x={rx}{ry_arg}{flags})")
            expanded[eid] = [eid]
            stats["primitives"] += 1
        elif kind in ("bezier", "polyline"):
            stats["curves"] += 1
            na, nb = element["nodes"]
            a, b = node_pt[na], node_pt[nb]
            raw_start = (float(nodes[na]["x"]), float(nodes[na]["y"]))
            if mode == "bezier" and element.get("cubics"):
                cubics = [[list(map(float, c1)), list(map(float, c2)), list(map(float, p3))] for c1, c2, p3 in element["cubics"]]
                # Snap the outer knots to the integer nodes and carry the same
                # offset into the adjacent controls so the tangents survive.
                dsx, dsy = a[0] - raw_start[0], a[1] - raw_start[1]
                cubics[0][0] = [cubics[0][0][0] + dsx, cubics[0][0][1] + dsy]
                dex, dey = b[0] - cubics[-1][2][0], b[1] - cubics[-1][2][1]
                cubics[-1][1] = [cubics[-1][1][0] + dex, cubics[-1][1][1] + dey]
                cubics[-1][2] = list(b)
                chains[eid] = (a, cubics)
                lines.append(eid)  # placeholder, emitted after seating
                expanded[eid] = [eid]
                stats["primitives"] += 1
            else:
                pieces, worst = fit_curve(_curve_samples(raw_start, element), a, b, box)
                stats["fit_max"] = max(stats["fit_max"], worst)
                if not pieces:
                    pieces = [("line", a, b)] if a != b else []
                if not pieces:
                    expanded[eid] = []
                    continue
                ids = emit_pieces(eid, pieces)
                expanded[eid] = ids
                if len(ids) > 1:
                    self_contained.add(eid)
        else:
            raise ValueError(f"unknown element kind {kind!r}")

    if chains:
        if box[0] == "circle":
            reached = {}
        else:
            straight = [node_pt[n] for e in data["elements"] if e["kind"] not in ("bezier", "polyline")
                        for n in e.get("nodes", [])]
            straight += [node_pt[n] for e in data["elements"] if e["kind"] in ("bezier", "polyline") for n in e["nodes"]]
            l, t, r, b = box
            reached = {(0, l): any(p[0] == l for p in straight), (0, r): any(p[0] == r for p in straight),
                       (1, t): any(p[1] == t for p in straight), (1, b): any(p[1] == b for p in straight)}
        seat_beziers(chains, box, reached)
        for index, line in enumerate(lines):
            if line in chains:
                start, cubics = chains[line]
                segs = ", ".join(f"({_fmt_pt(c1)}, {_fmt_pt(c2)}, {_fmt_pt(p3)})" for c1, c2, p3 in cubics)
                lines[index] = f"self.add_bezier({line!r}, {_fmt_pt(start)}, {segs})"

    in_contour: dict[str, str] = {}
    contour_lines = []
    for contour in data["contours"]:
        members = [pid for m in contour["members"] for pid in expanded.get(m, [])]
        if not members:
            continue
        for m in contour["members"]:
            in_contour[m] = contour["id"]
        only_circle = len(contour["members"]) == 1 and elements[contour["members"][0]]["kind"] == "circle"
        closed = bool(contour["closed"]) or only_circle
        args = ", ".join(repr(m) for m in members)
        contour_lines.append(f"self.add_contour({contour['id']!r}, {args}{', closed=True' if closed else ''})")
    # Orphan elements that became several primitives need their own contour,
    # emitted in element order so regenerated modules are byte-stable.
    for eid in (e["id"] for e in data["elements"] if e["id"] in self_contained):
        if eid not in in_contour:
            closed = elements[eid]["kind"] == "circle"
            args = ", ".join(repr(m) for m in expanded[eid])
            contour_lines.append(f"self.add_contour({eid!r}, {args}{', closed=True' if closed else ''})")
            in_contour[eid] = eid

    def member_name(m):
        # A relation may name a contour, or an element that survived as one
        # primitive; an element split into pieces is named by its contour.
        if expanded.get(m) == [m]:
            return m
        return in_contour.get(m, m)

    valid_ids = {pid for ids in expanded.values() for pid in ids} | set(in_contour.values())
    relation_lines = []
    for relation in data["relations"]:
        names = []
        for m in relation["members"]:
            name = member_name(m)
            if name in valid_ids and name not in names:
                names.append(name)
        if len(names) >= 2:
            relation_lines.append(f"self.relate({relation['kind']!r}, {', '.join(repr(n) for n in names)})")
    return lines + contour_lines + relation_lines, stats


def module_source(data, mode, icon_id, class_name, uuid, rel_json):
    body, stats = convert(data, mode)
    keyshape = KEYSHAPES[data["pipeline"]["keyshape_fit"]["keyshape"]]
    words = [w for w in re.split(r"[^a-z0-9]+", data["name"].lower()) if w and not w.isdigit()]
    keywords = tuple(dict.fromkeys(words + [data["category"].lower()]))
    doc = (
        f"{data['name'].strip().capitalize()} ({data['category']}), converted from the icons-json "
        f"construction graph by json_to_solo --mode {mode}. {keyshape} keyshape; "
        + ("curves kept as cubic beziers." if mode == "bezier" else "curves fitted to integer lines and arcs.")
    )
    text = [
        f'"""{doc}"""',
        "from ...keyshapes import Keyshape",
        "from ._base import Solo48",
        "",
        f"SOURCE_ICON_ID = {uuid!r}",
        f"SOURCE_PATH = {('icons-json/' + rel_json)!r}",
        "AUTHOR = 'json_to_solo'",
        "",
        f"class {class_name}(Solo48):",
        f"    icon_id = {icon_id!r}",
        f"    keyshape = Keyshape.{keyshape}",
        "    semantic_role = 'MAIN'",
        "    semantic_kind = 'noun'",
        f"    category = {data['category']!r}",
        "    aliases = ()",
        f"    keywords = {keywords!r}",
        "",
        "    def build(self):",
    ]
    text += [f"        {line}" for line in body] or ["        pass"]
    return "\n".join(text) + "\n", stats


# -- reference rendering -----------------------------------------------------

def reference_svg(data):
    """The JSON geometry itself, unrounded, as the fidelity reference."""
    nodes = {n["id"]: (float(n["x"]), float(n["y"])) for n in data["nodes"]}
    paths = []
    for e in data["elements"]:
        k = e["kind"]
        if k == "dot":
            paths.append(f"M{e['x']} {e['y']}L{e['x']} {e['y']}")
        elif k == "circle":
            cx, cy, rx, ry = e["cx"], e["cy"], e.get("rx", e["r"]), e.get("ry", e["r"])
            paths.append(f"M{_fmt(cx - rx)} {_fmt(cy)}A{_fmt(rx)} {_fmt(ry)} 0 0 1 {_fmt(cx + rx)} {_fmt(cy)}"
                         f"A{_fmt(rx)} {_fmt(ry)} 0 0 1 {_fmt(cx - rx)} {_fmt(cy)}Z")
        else:
            a, b = (nodes[n] for n in e["nodes"])
            d = f"M{_fmt(a[0])} {_fmt(a[1])}"
            if k == "line":
                d += f"L{_fmt(b[0])} {_fmt(b[1])}"
            elif k == "arc":
                d += f"A{_fmt(e.get('rx', e['r']))} {_fmt(e.get('ry', e['r']))} 0 {int(e.get('large_arc', 0))} {int(e.get('sweep', 1))} {_fmt(b[0])} {_fmt(b[1])}"
            elif e.get("cubics"):
                d += "".join(f"C{_fmt(c1[0])} {_fmt(c1[1])} {_fmt(c2[0])} {_fmt(c2[1])} {_fmt(p3[0])} {_fmt(p3[1])}" for c1, c2, p3 in e["cubics"])
            else:
                d += "".join(f"L{_fmt(x)} {_fmt(y)}" for x, y in e["points"][1:])
            paths.append(d)
    return paths


def _svg_doc(paths):
    body = "".join(f'<path d="{d}"/>' for d in paths)
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none" '
            f'stroke="#000" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">{body}</svg>')


def _mask(svg_text, size=144):
    import cairosvg
    import numpy as np
    from PIL import Image
    png = cairosvg.svg2png(bytestring=svg_text.encode(), output_width=size, output_height=size, background_color="#ffffff")
    return np.asarray(Image.open(io.BytesIO(png)).convert("L")) < 128


# -- worker ------------------------------------------------------------------

_PACKAGE = "icon_set.model.icons.json_staging"


def _init_worker(mode, out_dir):
    sys.path.insert(0, str(ENGINE[mode]))
    importlib.import_module("icon_set.model.icons.solo._base")
    package = types.ModuleType(_PACKAGE)
    package.__path__ = [str(out_dir)]
    sys.modules[_PACKAGE] = package


def _check(job):
    stem, ref_paths = job
    result = {"stem": stem}
    try:
        module = importlib.import_module(f"{_PACKAGE}.{stem}")
        from icon_set.model.icons.solo._base import Solo48
        cls = next(v for v in vars(module).values()
                   if isinstance(v, type) and issubclass(v, Solo48) and v is not Solo48)
        icon = cls()
        report = icon.validate_icon()
        result["status"] = report.status
        result["errors"] = list(report.errors[:6])
        result["warnings"] = len(report.warnings)
        svg = icon.to_svg()
        result["paths"] = re.findall(r' d="([^"]+)"', svg)
        a = _mask(svg.replace("currentColor", "#000"))
        b = _mask(_svg_doc(ref_paths))
        union = (a | b).sum()
        result["iou"] = round(float((a & b).sum() / union), 3) if union else 0.0
    except Exception as error:  # a broken module is a result, not a crash
        result["status"] = "error"
        result["errors"] = [f"{type(error).__name__}: {error}"]
        result.setdefault("paths", [])
        result["iou"] = 0.0
    return result


# -- driver --------------------------------------------------------------------

def _existing_main():
    ids, uuids = set(), set()
    for path in MAIN_SOLO.glob("*.py"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"icon_id = '([^']+)'", text)
        if m:
            ids.add(m.group(1))
        tail = path.stem[-36:].replace("_", "-")
        uuids.add(tail)
    return ids, uuids


def plan(limit=None):
    files = sorted(glob.glob(str(JSON_ROOT / "**" / "*.json"), recursive=True))
    main_ids, main_uuids = _existing_main()
    taken = set(main_ids)
    entries = []
    for path in files[:limit] if limit else files:
        rel = os.path.relpath(path, JSON_ROOT)
        stem = Path(path).stem
        m = UUID.search(stem)
        uuid = m.group(1) if m else ""
        name_part = UUID.sub("", stem)
        data = json.loads(Path(path).read_text())
        base = _slug(data["name"] if data.get("name") else name_part)
        icon_id = base
        for candidate in (base, f"{base}-{_slug(data['category'])}", f"{base}-{uuid[:8]}"):
            if candidate not in taken:
                icon_id = candidate
                break
        taken.add(icon_id)
        module = re.sub(r"[^a-z0-9]+", "_", f"{_slug(name_part)}_{uuid}".lower()).strip("_")
        if module[0].isdigit():
            module = "icon_" + module
        class_name = "".join(w.capitalize() for w in re.split(r"[^a-zA-Z0-9]+", icon_id) if w)
        if class_name[0].isdigit() or keyword.iskeyword(class_name) or class_name in dir(__builtins__):
            class_name = "Icon" + class_name
        entries.append({
            "json": rel, "data": data, "uuid": uuid, "icon_id": icon_id, "module": module,
            "class": class_name, "exists_in_main": uuid in main_uuids,
            "renamed": icon_id != base,
        })
    return entries


def cmd_run(args):
    mode = args.mode
    out_dir = HERE / mode / "solo"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "_base.py").write_text(
        '"""Staging shim: generated modules import Solo48 exactly as they will in solo/."""\n'
        "from ..solo._base import CANVAS, CENTER, PROFILE, Solo48  # noqa: F401\n"
    )
    started = time.time()
    entries = plan(args.limit)
    sys.path.insert(0, str(ENGINE[mode]))  # fit mode reads arc geometry from the engine
    jobs, meta = [], {}
    for entry in entries:
        data, scale = to_keyshape_frame(entry["data"])
        source, stats = module_source(data, mode, entry["icon_id"], entry["class"], entry["uuid"], entry["json"])
        (out_dir / f"{entry['module']}.py").write_text(source)
        kinds = {e["kind"] for e in data["elements"]}
        meta[entry["module"]] = {
            "icon_id": entry["icon_id"], "name": data["name"], "category": data["category"],
            "json": entry["json"], "uuid": entry["uuid"], "keyshape": KEYSHAPES[data["pipeline"]["keyshape_fit"]["keyshape"]],
            "direct": not (kinds & {"bezier", "polyline"}), "json_status": data["pipeline"]["part4"]["valid"],
            "exists_in_main": entry["exists_in_main"], "renamed": entry["renamed"],
            "scale": [round(scale[0], 3), round(scale[1], 3)], **stats,
        }
        jobs.append((entry["module"], reference_svg(data)))
    generated = time.time()
    results = {}
    with ProcessPoolExecutor(max_workers=args.workers, initializer=_init_worker, initargs=(mode, out_dir)) as pool:
        for done, result in enumerate(pool.map(_check, jobs, chunksize=8), 1):
            stem = result.pop("stem")
            results[stem] = {**meta[stem], **result}
            if done % 250 == 0:
                print(f"  {mode}: {done}/{len(jobs)} checked", flush=True)
    refs = {stem: paths for stem, paths in jobs}
    (HERE / mode / "results.json").write_text(json.dumps({"mode": mode, "icons": results}, indent=1))
    (HERE / "reference.json").write_text(json.dumps(refs))
    counts = {}
    for r in results.values():
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print(f"{mode}: {len(results)} icons | generate {generated - started:.1f}s | validate {time.time() - generated:.1f}s | {counts}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run", help="generate modules, validate, and score fidelity")
    run.add_argument("--mode", choices=("fit", "bezier"), required=True)
    run.add_argument("--limit", type=int, default=None)
    run.add_argument("--workers", type=int, default=os.cpu_count())
    args = parser.parse_args(argv)
    return {"run": cmd_run}[args.command](args)


if __name__ == "__main__":
    raise SystemExit(main())
