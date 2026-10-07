#!/usr/bin/env python3
"""core/detect.py — corner detector for the 48x48 icon set, read straight from the SVG segments.

The 48 icons are authored primitives (Line / Arc / Cubic on an integer grid), so a corner does
not have to be inferred from resampled turning (as the earlier 1024 pipeline did): the path
says it. Every corner is reported in one of two STATES so it can later be toggled either way:

  SHARP corner  — two arms meet at a point with a tangent jump: a join between two segments of
                  one path (L38 6 L42 10), or two stroke ends meeting at one node.
  ROUND corner  — one curved run (arc / cubic, possibly several smooth segments) bridging two
                  arms: L38 6 A4 4 0 0 1 42 10 L42 38. Its APEX is where the arms' tangent lines
                  meet (the point the sharp version would have), its RADIUS is fitted from the
                  legs (exact for arcs), and `circle_dev` says how far it is from a true circle.

and everything else is classified so nothing is silently dropped:

  curve         — a curved run that is part of the SHAPE (circle, smile, neck opening, S-bend,
                  a 180deg cap): never a corner, whatever it turns.
  junction      — 3+ arms meet (T contact, Y, crossing): structural, not toggleable.
  kink          — a 2-arm join turning only SMOOTH_TOL..CORNER_MIN_TURN deg (a near-straight bend).

A curved run is a ROUND corner only when ALL hold:
  1. it turns CORNER_MIN_TURN..ROUND_MAX_TURN deg in one direction (no inflection),
  2. neither end is a free stroke end,
  3. at least one end flows smoothly (G1) into a straight Line,
  4. its end tangents meet at an apex AHEAD of both ends,
  5. the corner is not a spike (angle >= MIN_ANGLE) and its apex lies on the canvas
     (its SHARP version must stay inside the icon).

Geometry for toggling (every corner): angle (between the arms), apex, per-arm straight reach
from the apex and `r_max` — the largest fillet radius whose trim t = r / tan(angle/2) fits both
arms (an arm whose far end is another corner only gets half of the shared straight).

Usage:
  python3 -m core.detect                              # all icons -> corner48_outputs/corners48.json
  python3 -m core.detect --sample 100 --seed 7        # random sample
  python3 -m core.detect --files t-shirt.svg triangle.svg
"""

import argparse
import cmath
import json
import math
import os
import random
import sys
import xml.etree.ElementTree as ET

import numpy as np
from concurrent.futures import ProcessPoolExecutor

from svgpathtools import Arc, CubicBezier, Line, QuadraticBezier

from .progress import Progress
from .paths import OUT_DIR
from .svg_io import DEFAULT_INPUT, element_to_path, iter_skeleton_shapes, localname

SMOOTH_TOL = 2.0         # deg — a join turning less than this is tangent-continuous (G1)
CORNER_MIN_TURN = 25.0   # deg — a turn below this is a kink, not a corner (= 1024 pipeline
                         #       ANGLE_THRESHOLD; interior angle > 155 deg)
MIN_ANGLE = 30.0         # deg — a round corner sharper than this would toggle into a spike
                         #       (= 1024 pipeline MIN_ANGLE): it is a curve
CANVAS = 48.0            # u   — a round corner's apex must lie on the canvas
ROUND_MAX_TURN = 170.0   # deg — a curved run turning more is a cap / loop (a stadium's 180deg
                         #       end), not one corner
INFLECT_TOL = 0.5        # deg — per-sample opposite turning below this is ignored as noise
INFLECT_MIN = 10.0       # deg — a curve is an S-bend only when it turns back by more than this
INFLECT_SHARE = 0.25     #       AND by more than this share of its total turn: a hand-drawn
                         #       rounded tip whose control points wobble back 4 deg out of 38
                         #       (arrow badges, tabs) is still one bend, i.e. a round corner
NODE_TOL = 0.28          # u   — ends this close are one node (= 1024 pipeline CLUSTER_TOL)
ON_STROKE_TOL = 0.375    # u   — a JOIN (a V's point) this close to another stroke's interior is on it
CONTACT_TOL = 1.0        # u   — a stroke END this close to another node or stroke touches it: with
                         #       a 4-wide stroke the inks overlap completely, and traced icons miss
                         #       by up to ~0.9 (a shaft stopping 0.87 short of its arrowhead tip).
                         #       Erring wide only keeps a corner from being rounded; missing a
                         #       contact lets a fillet pull the touched point away.
ARM_MERGE = 3.0          # deg — arms leaving a node this close in direction are one arm
CROSS_STEP = 0.1         # u   — flattening step for crossing detection
CIRCLE_TOL = 0.05        # u   — max deviation from the fitted circle for a 'circular' round corner
EPS = 1e-9


# ---------------------------------------------------------------------------
# geometry helpers (points / directions are complex numbers)
# ---------------------------------------------------------------------------
def unit(z):
    a = abs(z)
    return z / a if a > EPS else None


def tangent(seg, t):
    """Unit tangent of seg at t. Where a control point sits on its end point the derivative
    vanishes and svgpathtools falls back to one that can point BACKWARDS (a curl drawn
    ...C19.8 23 18 19.5 18 19.5); the direction the curve actually travels near t wins."""
    h = 1e-3
    a, b = (t, t + h) if t < 1 - h else (t - h, t)
    fd = unit(seg.point(b) - seg.point(a))
    try:
        u = seg.unit_tangent(t)
        if math.isfinite(u.real) and math.isfinite(u.imag) and abs(u) > 0.5:
            if fd is None or (u * fd.conjugate()).real > 0:
                return u
            return fd
    except (ValueError, ZeroDivisionError):
        pass
    if fd is not None:
        return fd
    h = 1e-4
    a, b = (t, t + h) if t < 1 - h else (t - h, t)
    return unit(seg.point(b) - seg.point(a))


def turn_deg(u, v):
    """Signed direction change (deg) going from direction u to direction v."""
    return math.degrees(cmath.phase(v / u))


def angle_between(u, v):
    return abs(turn_deg(u, v))


def seg_turn(seg, n=32):
    """(signed total turn deg, has_inflection) of one segment, by tangent sampling."""
    if isinstance(seg, Line):
        return 0.0, False
    tans = [tangent(seg, k / n) for k in range(n + 1)]
    tans = [t for t in tans if t is not None]
    steps = [turn_deg(a, b) for a, b in zip(tans, tans[1:])]
    total = sum(steps)
    sign = 1 if total >= 0 else -1
    back = sum(-s * sign for s in steps if s * sign < -INFLECT_TOL)
    inflect = back > INFLECT_MIN and back > INFLECT_SHARE * abs(total)
    return total, inflect


def line_hit(p, u, q, v):
    """Solve p + a*u = q - b*v  ->  (a, b, point) or None if parallel."""
    den = u.real * v.imag - u.imag * v.real
    if abs(den) < 1e-12:
        return None
    d = q - p
    a = (d.real * v.imag - d.imag * v.real) / den
    b = (u.real * d.imag - u.imag * d.real) / den
    return a, b, p + a * u


def fmt(x):
    return round(float(x), 3)


def _n(x):
    s = f"{x:.3f}".rstrip("0").rstrip(".")
    return "0" if s in ("", "-0") else s


def seg_d(seg):
    """One segment as an absolute SVG path command string (starting with its own M)."""
    p = lambda z: f"{_n(z.real)} {_n(z.imag)}"
    head = f"M{p(seg.start)}"
    if isinstance(seg, Line):
        return f"{head}L{p(seg.end)}"
    if isinstance(seg, Arc):
        return (f"{head}A{_n(seg.radius.real)} {_n(seg.radius.imag)} {_n(seg.rotation)} "
                f"{int(seg.large_arc)} {int(seg.sweep)} {p(seg.end)}")
    if isinstance(seg, CubicBezier):
        return f"{head}C{p(seg.control1)} {p(seg.control2)} {p(seg.end)}"
    if isinstance(seg, QuadraticBezier):
        return f"{head}Q{p(seg.control)} {p(seg.end)}"
    return f"{head}L{p(seg.end)}"


def pt(z):
    return [fmt(z.real), fmt(z.imag)]


# ---------------------------------------------------------------------------
# stroke model
# ---------------------------------------------------------------------------
class Stroke:
    """One continuous subpath of a stroked element."""

    def __init__(self, sid, elem_id, segs, closed):
        self.sid, self.elem_id, self.segs, self.closed = sid, elem_id, segs, closed

    def n(self):
        return len(self.segs)

    def prev(self, i):
        if i > 0:
            return i - 1
        return self.n() - 1 if self.closed else None

    def next(self, i):
        if i < self.n() - 1:
            return i + 1
        return 0 if self.closed else None


SLIVER = 0.01            # u — segments shorter than this are precision slivers (a closing
                         #     Z after 4-decimal coordinates); a path ending this close to its
                         #     start is closed


def clean_subpath(sub):
    """Drop sliver segments and decide closure with SLIVER tolerance. -> (segs, closed)."""
    segs = [s for s in sub if s.length() > SLIVER]
    if not segs:
        return [], False
    closed = len(segs) > 1 and abs(segs[-1].end - segs[0].start) <= SLIVER
    if closed and segs[-1].end != segs[0].start:          # close it exactly: move the last
        last, s0 = segs[-1], segs[0].start                 # segment's end onto the start
        if isinstance(last, Line):
            segs[-1] = Line(last.start, s0)
        elif isinstance(last, CubicBezier):
            segs[-1] = CubicBezier(last.start, last.control1, last.control2, s0)
        elif isinstance(last, QuadraticBezier):
            segs[-1] = QuadraticBezier(last.start, last.control, s0)
        elif isinstance(last, Arc):
            segs[-1] = Arc(last.start, last.radius, last.rotation, last.large_arc, last.sweep, s0)
    return segs, closed


def load_strokes(path):
    root = ET.parse(path).getroot()
    strokes, extras = [], {"circles": 0, "dots": 0}
    for el in iter_skeleton_shapes(root):
        name = localname(el.tag)
        if name in ("circle", "ellipse"):
            extras["circles"] += 1
            continue
        p = element_to_path(el)
        if p is None:
            continue
        for sub in p.continuous_subpaths():
            segs, closed = clean_subpath(sub)
            if not segs:
                extras["dots"] += 1
                continue
            strokes.append(Stroke(len(strokes), el.get("id") or name, segs, closed))
    return strokes, extras


def join_turn(st, i):
    """Signed turn (deg) at the join INTO segment i (from segment prev(i)), or None."""
    j = st.prev(i)
    if j is None:
        return None
    a, b = tangent(st.segs[j], 1.0), tangent(st.segs[i], 0.0)
    if a is None or b is None:
        return None
    return turn_deg(a, b)


# ---------------------------------------------------------------------------
# curved runs -> round corners / curves
# ---------------------------------------------------------------------------
def curve_runs(st):
    """Maximal chains of curved segments joined smoothly and turning the same way.
    Returns [(seg_indices, total_turn, inflection)] in path order."""
    n = st.n()
    info = [seg_turn(s) for s in st.segs]
    curved = [not isinstance(s, Line) for s in st.segs]

    def links(i):              # does segment i continue the run of segment prev(i)?
        j = st.prev(i)
        if j is None or not (curved[i] and curved[j]):
            return False
        jt = join_turn(st, i)
        if jt is None or abs(jt) >= SMOOTH_TOL:
            return False
        si, sj = info[i][0], info[j][0]
        return si * sj >= 0 and not info[i][1] and not info[j][1]

    order = list(range(n))
    if st.closed:
        starts = [i for i in range(n) if not links(i)]
        if not starts:                       # smooth all-curve loop: one closed curve
            total = sum(t for t, _ in info)
            return [(order, total, any(f for _, f in info), True)]
        k = starts[0]
        order = order[k:] + order[:k]
    runs, cur = [], []
    for i in order:
        if curved[i] and cur and links(i):
            cur.append(i)
            continue
        if cur:
            runs.append(cur)
        cur = [i] if curved[i] else []
    if cur:
        runs.append(cur)
    out = []
    for r in runs:
        total = sum(info[i][0] for i in r) + sum(join_turn(st, i) or 0.0 for i in r[1:])
        out.append((r, total, any(info[i][1] for i in r), False))
    return out


def classify_run(st, run, total, inflect, attached_end):
    """Round-corner record (dict) or a curve record with the rule that failed."""
    i0, i1 = run[0], run[-1]
    s0, s1 = st.segs[i0], st.segs[i1]
    P0, P3 = s0.start, s1.end
    t0, t3 = tangent(s0, 0.0), tangent(s1, 1.0)
    rec = {"kind": "curve", "stroke": st.elem_id, "segs": [seg_d(st.segs[i]) for i in run],
           "turn": fmt(abs(total)), "start": pt(P0), "end": pt(P3)}
    turn = abs(total)
    if inflect:
        rec["why"] = "inflection"
        return rec
    if turn < CORNER_MIN_TURN:
        rec["why"] = "gentle"
        return rec
    if turn > ROUND_MAX_TURN:
        rec["why"] = "cap/loop"
        return rec
    jp, jn = st.prev(i0), st.next(i1)
    ends_free = [jp is None and not attached_end(st, "start"),
                 jn is None and not attached_end(st, "end")]
    if any(ends_free):
        rec["why"] = "free end"
        return rec
    exact, kinked = [], []
    for j, at in ((jp, i0), (jn, i1)):
        if j is None:
            exact.append(False)
            kinked.append(False)
            continue
        jt = join_turn(st, at if j == jp else j)
        is_line = isinstance(st.segs[j], Line) and jt is not None
        exact.append(is_line and abs(jt) < SMOOTH_TOL)
        kinked.append(is_line and abs(jt) < CORNER_MIN_TURN)
    # a rounding flows into a straight line at one end, or sits BETWEEN two lines that it meets
    # with small kinks: a hand-drawn fillet that is not quite tangent (a laptop screen's
    # `L41 11 A3 3 .. 39 8 L9 8`, off by 3 and 19 deg) is still that corner's rounding, while a
    # bulge that leaves a real corner and ends kinked on a line is not
    if not (any(exact) or all(kinked)):
        rec["why"] = "no straight arm"
        return rec
    smooth_line = kinked
    # the corner's arms: the straight LINES themselves where the curve meets one (their
    # crossing is the true sharp point even when the drawn curve is not tangent to them),
    # else the curve's own end tangent
    if smooth_line[0]:
        t0 = unit(st.segs[jp].end - st.segs[jp].start) or t0
    if smooth_line[1]:
        t3 = unit(st.segs[jn].end - st.segs[jn].start) or t3
    hit = line_hit(P0, t0, P3, t3)
    if hit is None or hit[0] <= EPS or hit[1] <= EPS:
        rec["why"] = "no apex"
        return rec
    a, b, apex = hit
    theta = 180.0 - angle_between(t0, t3)     # interior angle between the arms
    if theta < MIN_ANGLE:
        rec["why"] = "spike"
        return rec
    if not (0.0 <= apex.real <= CANVAS and 0.0 <= apex.imag <= CANVAS):
        rec["why"] = "apex off canvas"
        rec["apex"] = pt(apex)
        return rec
    half = math.radians(theta) / 2.0
    r_fit = 0.5 * (a + b) * math.tan(half)
    # circle tangent to both arm lines at distance r_fit: centre on the bisector
    bis = unit(unit(P0 - apex) + unit(P3 - apex))
    centre = apex + bis * (r_fit / math.sin(half)) if bis is not None else None
    dev = 0.0
    if centre is not None:
        for i in run:
            s = st.segs[i]
            for k in range(25):
                dev = max(dev, abs(abs(s.point(k / 24) - centre) - r_fit))
    drawn_r = None
    if len(run) == 1 and isinstance(s0, Arc) and abs(s0.radius.real - s0.radius.imag) < 1e-6:
        drawn_r = fmt(s0.radius.real)
    rec.update({
        "kind": "round", "apex": pt(apex), "angle": fmt(theta), "r": fmt(r_fit),
        "r_drawn": drawn_r, "legs": [fmt(a), fmt(b)], "circle_dev": fmt(dev),
        "circular": bool(dev <= CIRCLE_TOL), "centre": pt(centre) if centre is not None else None,
        "arms": ["line" if sl else "curve" for sl in smooth_line],
        "shape": "arc" if all(isinstance(st.segs[i], Arc) for i in run) else "bezier",
        "size": fmt(corner_size(r_fit, theta)),
    })
    rec.pop("why", None)
    return rec


# ---------------------------------------------------------------------------
# nodes: in-path sharp joins, stroke ends, T contacts, crossings
# ---------------------------------------------------------------------------
def nearest_on_stroke(st, p, tol):
    """(distance, tangent) of the closest point of stroke st to p within tol, else None."""
    best = None
    for s in st.segs:
        x0, x1, y0, y1 = s.bbox()
        if not (x0 - tol <= p.real <= x1 + tol and y0 - tol <= p.imag <= y1 + tol):
            continue
        n = max(8, int(s.length() / 0.05))
        for k in range(n + 1):
            q = s.point(k / n)
            d = abs(q - p)
            if d <= tol and (best is None or d < best[0]):
                best = (d, tangent(s, k / n))
    return best


def flatten(st, step=CROSS_STEP):
    pts = []
    for s in st.segs:
        n = max(1, int(s.length() / step)) if not isinstance(s, Line) else 1
        for k in range(n):
            pts.append((s.point(k / n), s, k / n))
    last = st.segs[-1]
    pts.append((last.end, last, 1.0))
    return pts


def _seg_poly(seg, step=CROSS_STEP):
    n = 1 if isinstance(seg, Line) else max(1, int(seg.length() / step))
    return [seg.point(k / n) for k in range(n + 1)]


def _polyline_hits(A, B):
    """Interior crossings of polylines A and B: [(point, dir_a, dir_b)], parallel overlaps and
    near-tangent touches excluded. The bounding-box test and the line solve run on every piece
    pair at once (numpy); the few real hits then go through the exact per-pair checks, in the
    same order as a plain double loop, so the result is identical."""
    if len(A) < 2 or len(B) < 2:
        return []
    PA, PB = np.asarray(A, dtype=complex), np.asarray(B, dtype=complex)
    a0, a1, b0, b1 = PA[:-1, None], PA[1:, None], PB[None, :-1], PB[None, 1:]
    box = ~((np.maximum(a0.real, a1.real) < np.minimum(b0.real, b1.real)) |
            (np.maximum(b0.real, b1.real) < np.minimum(a0.real, a1.real)) |
            (np.maximum(a0.imag, a1.imag) < np.minimum(b0.imag, b1.imag)) |
            (np.maximum(b0.imag, b1.imag) < np.minimum(a0.imag, a1.imag)))
    ks, ms = np.nonzero(box)
    if not len(ks):
        return []
    u = PA[ks + 1] - PA[ks]                      # line_hit(a0, A, b0, -B): a0 + a*A = b0 + b*B
    v = -(PB[ms + 1] - PB[ms])
    d = PB[ms] - PA[ks]
    den = u.real * v.imag - u.imag * v.real
    ok = np.abs(den) >= 1e-12
    with np.errstate(divide="ignore", invalid="ignore"):
        ta = (d.real * v.imag - d.imag * v.real) / den
        tb = (u.real * d.imag - u.imag * d.real) / den
    ok &= (ta >= 0) & (ta <= 1) & (tb >= 0) & (tb <= 1)
    out = []
    for k, m in zip(ks[ok].tolist(), ms[ok].tolist()):
        a0_, a1_, b0_, b1_ = A[k], A[k + 1], B[m], B[m + 1]
        h = line_hit(a0_, a1_ - a0_, b0_, -(b1_ - b0_))
        if h is None or not (0 <= h[0] <= 1 and 0 <= h[1] <= 1):
            continue
        ua, ub = unit(a1_ - a0_), unit(b1_ - b0_)
        if ua is None or ub is None or min(angle_between(ua, ub),
                                           180 - angle_between(ua, ub)) < SMOOTH_TOL:
            continue
        out.append((h[2], ua, ub))
    return out


def find_nodes(strokes):
    """Cluster node candidates. Each candidate: (point, [(arm_dir, stroke_id, kind)])."""
    cands = []
    for st in strokes:
        for i in range(st.n()):
            j = st.prev(i)
            if j is None:
                continue
            a, b = tangent(st.segs[j], 1.0), tangent(st.segs[i], 0.0)
            if a is None or b is None or angle_between(a, b) < SMOOTH_TOL:
                continue
            cands.append((st.segs[i].start, [(-a, st.sid, st.segs[j]), (b, st.sid, st.segs[i])],
                          {"join": (st.sid, i)}))
        if not st.closed:
            s0, s1 = st.segs[0], st.segs[-1]
            cands.append((s0.start, [(tangent(s0, 0.0), st.sid, s0)], {"end": (st.sid, "start")}))
            cands.append((s1.end, [(-tangent(s1, 1.0), st.sid, s1)], {"end": (st.sid, "end")}))
    nodes = []
    for p, arms, tag in cands:
        for nd in nodes:
            if abs(nd["p"] - p) <= NODE_TOL:
                nd["arms"] += arms
                nd["tags"].append(tag)
                break
        else:
            nodes.append({"p": p, "arms": list(arms), "tags": [tag]})
    # snap: a node holding a stroke END within CONTACT_TOL of another node is that node
    # (keeps the other node's position when it is a join: the drawn corner point)
    has_end = lambda nd: any("end" in tg for tg in nd["tags"])
    merged = True
    while merged:
        merged = False
        for a in range(len(nodes)):
            for b in range(len(nodes)):
                if a == b or not has_end(nodes[b]):
                    continue
                if abs(nodes[a]["p"] - nodes[b]["p"]) > CONTACT_TOL:
                    continue
                # not a near-miss when the end's own stroke already runs through the other
                # node (a baseline's end 1u past a bar's T on it; a path's start next to its end)
                sids_b = {sid for _, sid, _ in nodes[b]["arms"]}
                sids_a = {sid for _, sid, _ in nodes[a]["arms"]}
                if any(nearest_on_stroke(strokes[s], nodes[a]["p"], NODE_TOL) for s in sids_b) or \
                        any(nearest_on_stroke(strokes[s], nodes[b]["p"], NODE_TOL) for s in sids_a):
                    continue
                if True:
                    nodes[a]["arms"] += nodes[b]["arms"]
                    nodes[a]["tags"] += nodes[b]["tags"]
                    del nodes[b]
                    merged = True
                    break
            if merged:
                break
    # T contacts: a node (a stroke END, or a sharp JOIN such as a V's point) lying on the
    # interior of another stroke that has no node there
    for nd in nodes:
        present = {sid for _, sid, _ in nd["arms"]}
        tol = CONTACT_TOL if has_end(nd) else ON_STROKE_TOL
        for st in strokes:
            if st.sid in present:
                # an end landing on its OWN path, away from that end (a path that runs back
                # along itself): check only segments that do not touch this node
                if not has_end(nd):
                    continue
                far = [s for s in st.segs if abs(s.start - nd["p"]) > CONTACT_TOL
                       and abs(s.end - nd["p"]) > CONTACT_TOL]
                hit = nearest_on_stroke(Stroke(st.sid, st.elem_id, far, False), nd["p"], tol) \
                    if far else None
                if hit is not None and hit[1] is not None:
                    nd["arms"] += [(hit[1], st.sid, None), (-hit[1], st.sid, None)]
                    nd["tags"].append({"on": st.sid})
                continue
            hit = nearest_on_stroke(st, nd["p"], tol)
            if hit is not None and hit[1] is not None:
                nd["arms"] += [(hit[1], st.sid, None), (-hit[1], st.sid, None)]
                nd["tags"].append({"on": st.sid})
    # crossings between different strokes — and between non-adjacent segments of one stroke
    # (a path can cross itself, e.g. after the sharp output joins two strokes at a corner) —
    # away from every existing node
    def add_crossing(x, ua, ub, ia, ib):
        if any(abs(x - nd["p"]) <= NODE_TOL for nd in nodes):
            return
        nodes.append({"p": x, "arms": [(ua, ia, None), (-ua, ia, None),
                                       (ub, ib, None), (-ub, ib, None)],
                      "tags": [{"cross": (ia, ib)}]})

    flat = [flatten(st) for st in strokes]
    for ia in range(len(strokes)):
        for ib in range(ia + 1, len(strokes)):
            for x, ua, ub in _polyline_hits([p for p, _, _ in flat[ia]], [p for p, _, _ in flat[ib]]):
                add_crossing(x, ua, ub, ia, ib)
    for st in strokes:
        n = st.n()
        polys = [_seg_poly(s) for s in st.segs]
        for i in range(n):
            for j in range(i + 2, n):
                if st.closed and i == 0 and j == n - 1:
                    continue                   # adjacent across the closing seam
                for x, ua, ub in _polyline_hits(polys[i], polys[j]):
                    add_crossing(x, ua, ub, st.sid, st.sid)
    for nd in nodes:                           # distinct arms
        nd["raw"] = sum(1 for d, _, _ in nd["arms"] if d is not None)
        uniq = []
        for d, sid, seg in nd["arms"]:
            if d is None:
                continue
            if all(angle_between(d, e) > ARM_MERGE for e, _, _ in uniq):
                uniq.append((d, sid, seg))
        nd["arms"] = uniq
    return nodes


# ---------------------------------------------------------------------------
# arm reach (straight length from the apex) and room for a fillet
# ---------------------------------------------------------------------------
INNER_MIN_ANGLE = 30.0   # deg — a corner-with-inner-stroke must be at least this open...
INNER_MAX_ANGLE = 155.0  # deg — ...and a real corner (outer arms in line = a T, not a corner)
INNER_MARGIN = 5.0       # deg — the inner arm must sit at least this far inside the corner
INNER_BISECTOR = 15.0    # deg — ...and run within this of the corner's bisector: an arrow shaft
                         #       (0-4 deg off) vs. a stroke meeting a corner from the side (a
                         #       pistol grip under the slide's corner: 22 deg off) = a junction


def _inner_corner(arms):
    """For 3 distinct arms: if one lies strictly INSIDE the angle the other two make, and that
    angle is a real corner, return (outer_a, outer_b, inner) — else None. A T (outer arms in a
    line) and a Y (no arm inside another pair's angle) return None."""
    for i in range(3):
        a, b = [arms[k] for k in range(3) if k != i]
        x = arms[i]
        ab = angle_between(a[0], b[0])
        if not INNER_MIN_ANGLE <= ab <= INNER_MAX_ANGLE:
            continue
        ax, xb = angle_between(a[0], x[0]), angle_between(x[0], b[0])
        bis = a[0] / abs(a[0]) + b[0] / abs(b[0])
        if abs(ax + xb - ab) < 1.0 and min(ax, xb) > INNER_MARGIN and abs(bis) > 1e-9 \
                and angle_between(bis, x[0]) <= INNER_BISECTOR:
            return a, b, x
    return None


def straight_reach(strokes, sid, start_pt, direction, stops=()):
    """Walk stroke `sid` from start_pt along `direction` over collinear Lines; return
    (length, far_end_point). 0 when the arm leaves on a curve. The walk stops at the first
    node in `stops` lying on the straight (a T contact or another corner): a fillet can never
    trim past it."""
    L, far = _straight_reach(strokes, sid, start_pt, direction)
    best = None
    for q in stops:
        rel = (q - start_pt) / direction          # along / across the arm
        if NODE_TOL < rel.real < L - 1e-9 and abs(rel.imag) <= NODE_TOL:
            if best is None or rel.real < best:
                best = rel.real
    if best is not None:
        return best, start_pt + best * direction
    return L, far


def _straight_reach(strokes, sid, start_pt, direction):
    st = strokes[sid]
    for i, s in enumerate(st.segs):
        for fwd in (True, False):
            p0, p1 = (s.start, s.end) if fwd else (s.end, s.start)
            if abs(p0 - start_pt) > NODE_TOL or not isinstance(s, Line):
                continue
            if angle_between(unit(p1 - p0) or direction, direction) > ARM_MERGE:
                continue
            length, cur, k = abs(p1 - p0), p1, i
            while True:
                k = st.next(k) if fwd else st.prev(k)
                if k is None or k == i:
                    break
                nx = st.segs[k]
                if not isinstance(nx, Line):
                    break
                q0, q1 = (nx.start, nx.end) if fwd else (nx.end, nx.start)
                d = unit(q1 - q0)
                if d is None or angle_between(d, direction) > ARM_MERGE:
                    break
                length += abs(q1 - q0)
                cur = q1
            return length, cur
    return 0.0, start_pt


def corner_size(r, angle):
    """How big a round corner looks: its radius, or for a corner narrower than 90 deg the
    longer reach along its sides (r / tan(angle / 2)). A 34 deg corner with r 4.2 runs 13.6u
    along each side and its sharp point would land 10u out: a designed curve, not a corner."""
    t = math.tan(math.radians(max(angle, 1.0)) / 2.0)
    return max(r, r / t) if t > 1e-9 else r


CORNER_MAX_R = 8.0     # u — a round corner bigger than this (corner_size) is a designed curve:
                       #     detection reports it as a curve and the ROUND output keeps it as
                       #     drawn (the sharp output has its own, lower limit: BIG_ROUND_R 5.5)


def detect(path, max_r=None):
    """Corners, junctions, kinks and curves of one icon. max_r: a round corner wider than this
    is reported as a curve ("too large for a corner"), not as a round corner."""
    strokes, extras = load_strokes(path)
    nodes = find_nodes(strokes)

    def attached_end(st, which):
        for nd in nodes:                       # by tag: a snapped node may sit up to CONTACT_TOL away
            if {"end": (st.sid, which)} in nd["tags"]:
                return len(nd["arms"]) >= 2
        return False

    rounds, curves = [], []
    for st in strokes:
        for run, total, inflect, loop in curve_runs(st):
            if loop:
                curves.append({"kind": "curve", "stroke": st.elem_id, "why": "closed loop",
                               "segs": [seg_d(st.segs[i]) for i in run], "turn": fmt(abs(total)),
                               "start": pt(st.segs[run[0]].start), "end": pt(st.segs[run[-1]].end)})
                continue
            rec = classify_run(st, run, total, inflect, attached_end)
            rec["_run"] = (st.sid, run)
            (rounds if rec["kind"] == "round" else curves).append(rec)

    sharps, junctions, kinks = [], [], []
    for nd in nodes:
        arms = nd["arms"]
        if len(arms) <= 1:
            continue
        rec = {"p": pt(nd["p"]), "degree": len(arms)}
        # 3+ stroke arms meet here even when two leave in the same direction (a stroke that
        # starts tangent to a corner's side): rounding that corner would detach it
        inner = _inner_corner(arms) if len(arms) == 3 and nd["raw"] == 3 and \
            not any("cross" in tg for tg in nd["tags"]) else None
        if inner is not None:
            # a corner with a stroke ending at its point from INSIDE the corner (an arrow tip:
            # two head arms + the shaft) — a corner of the outer two arms, not a junction
            (d1, sid1, seg1), (d2, sid2, seg2), (dc, sidc, segc) = inner
            theta = angle_between(d1, d2)
            rec.update(kind="sharp", angle=fmt(theta), turn=fmt(180.0 - theta),
                       arms=["line" if isinstance(s, Line) else "curve" for s in (seg1, seg2)],
                       strokes=sorted({strokes[sid1].elem_id, strokes[sid2].elem_id}),
                       where="with inner stroke",
                       inner={"stroke": strokes[sidc].elem_id,
                              "dir": fmt(math.degrees(cmath.phase(dc)))},
                       arm_dirs=[fmt(math.degrees(cmath.phase(d))) for d in (d1, d2)])
            rec["_arms"] = [(d1, sid1), (d2, sid2)]
            sharps.append(rec)
            continue
        if len(arms) >= 3 or nd["raw"] >= 3:
            rec.update(kind="junction",
                       type="crossing" if any("cross" in t for t in nd["tags"])
                       # a V (a path's own corner) whose point lies on a line running through it
                       else "K" if any("on" in t for t in nd["tags"])
                       and any("join" in t for t in nd["tags"])
                       else "T" if any("on" in t for t in nd["tags"]) else "meeting")
            junctions.append(rec)
            continue
        (d1, sid1, seg1), (d2, sid2, seg2) = arms
        theta = angle_between(d1, d2)
        turn = 180.0 - theta
        if turn < SMOOTH_TOL:
            continue
        rec.update(angle=fmt(theta), turn=fmt(turn),
                   arms=["line" if isinstance(s, Line) else "curve" for s in (seg1, seg2)],
                   strokes=sorted({strokes[sid1].elem_id, strokes[sid2].elem_id}),
                   where="in-path" if any("join" in t for t in nd["tags"]) else "between strokes")
        rec["_arms"] = [(d1, sid1), (d2, sid2)]
        rec["arm_dirs"] = [fmt(math.degrees(cmath.phase(d))) for d in (d1, d2)]
        (kinks if turn < CORNER_MIN_TURN else sharps).append(rec)

    # room: straight reach of each arm from the apex; half of it if the far end is a corner too
    corner_pts = [complex(*c["p"]) for c in sharps]
    stops = [nd["p"] for nd in nodes if len(nd["arms"]) >= 2]
    tangent_pts = []
    for r in rounds:
        tangent_pts.append((complex(*r["start"]), r["legs"][0]))
        tangent_pts.append((complex(*r["end"]), r["legs"][1]))

    def available(reach, far):
        if any(abs(far - q) <= NODE_TOL for q in corner_pts):
            return reach / 2.0
        for q, leg in tangent_pts:
            if abs(far - q) <= NODE_TOL:
                return (reach + leg) / 2.0
        return reach

    for c in sharps:
        P = complex(*c["p"])
        reach, avail = [], []
        for d, sid in c.pop("_arms"):
            L, far = straight_reach(strokes, sid, P, d, stops)
            reach.append(fmt(L))
            avail.append(available(L, far) if L > 0 else 0.0)
        c["reach"] = reach
        c["r_max"] = fmt(min(avail) * math.tan(math.radians(c["angle"]) / 2.0))
    for r in rounds:
        sid, run = r.pop("_run")
        st = strokes[sid]
        apex = complex(*r["apex"])
        avail, reach = [], []
        for end, leg, d in ((r["start"], r["legs"][0], -tangent(st.segs[run[0]], 0.0)),
                            (r["end"], r["legs"][1], tangent(st.segs[run[-1]], 1.0))):
            L, far = straight_reach(strokes, sid, complex(*end), d, stops)
            reach.append(fmt(leg + L))
            avail.append(available(leg + L, far) if L > 0 else leg)
        r["reach"] = reach
        r["r_max"] = fmt(min(avail) * math.tan(math.radians(r["angle"]) / 2.0))
    if max_r is not None:                  # too wide to be a corner: a designed curve
        big = [r for r in rounds if r["size"] > max_r + 1e-6]
        rounds = [r for r in rounds if r["size"] <= max_r + 1e-6]
        for r in big:
            r.update(kind="curve", why=f"too large for a corner (size {fmt(r['size'])} > {fmt(max_r)})", big=True)
            curves.append(r)
        ends = [complex(*r[e]) for r in big for e in ("start", "end")]
        kinks = [k for k in kinks if not any(abs(complex(*k["p"]) - q) <= NODE_TOL for q in ends)]
    for c in curves:
        c.pop("_run", None)
    for k in kinks:
        k.pop("_arms", None)
    # a kink where a round corner's curve meets its line is part of that round corner
    ends = [complex(*r[e]) for r in rounds for e in ("start", "end")]
    kinks = [k for k in kinks if not any(abs(complex(*k["p"]) - q) <= NODE_TOL for q in ends)]
    return {"sharp": sharps, "round": rounds, "junction": junctions, "kink": kinks,
            "curve": curves, "circles": extras["circles"], "dots": extras["dots"]}


def _detect_one(args):
    """Worker: (input_dir, name, max_r) -> (name, result, error)."""
    folder, name, max_r = args
    try:
        return name, detect(os.path.join(folder, name), max_r), None
    except Exception as e:  # keep going; report at the end
        return name, None, f"{type(e).__name__}: {e}"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Segment-based corner detector for 48x48 icons.")
    ap.add_argument("--input", default=DEFAULT_INPUT)
    ap.add_argument("--out", default=OUT_DIR)
    ap.add_argument("--files", nargs="*")
    ap.add_argument("--sample", type=int, default=0, help="random sample of N icons")
    ap.add_argument("--seed", type=int, default=48)
    ap.add_argument("--jobs", type=int, default=os.cpu_count() or 1,
                    help="parallel worker processes (default: all CPU cores; 1 = no pool)")
    ap.add_argument("--ready", action="store_true",
                    help="only icons NOT in locks.json (not reviewed yet): locked and pending "
                         "icons keep the results they were reviewed on")
    ap.add_argument("--reviewed", action="store_true", help="only icons in locks.json")
    ap.add_argument("--corner-max-r", type=float, default=CORNER_MAX_R,
                    help="a round corner wider than this (u) is a designed curve, not a corner")
    cfg = ap.parse_args(argv)

    names = cfg.files or sorted(n for n in os.listdir(cfg.input) if n.lower().endswith(".svg"))
    if cfg.ready or cfg.reviewed:
        from . import locks
        reviewed = set(locks.load())
        names = [n for n in names if (n in reviewed) == cfg.reviewed]
    if cfg.sample:
        names = sorted(random.Random(cfg.seed).sample(names, min(cfg.sample, len(names))))
    os.makedirs(cfg.out, exist_ok=True)
    result, fails = {}, []
    prog = Progress("corner48", len(names))
    jobs = [(cfg.input, n, cfg.corner_max_r) for n in names]
    if cfg.jobs > 1 and len(names) > 1:
        with ProcessPoolExecutor(max_workers=cfg.jobs) as pool:
            done = pool.map(_detect_one, jobs, chunksize=8)
            for n, res, err in done:
                prog.step(n)
                (fails.append((n, err)) if err else result.__setitem__(n, res))
    else:
        for job in jobs:
            n, res, err = _detect_one(job)
            prog.step(n)
            (fails.append((n, err)) if err else result.__setitem__(n, res))
    prog.done()
    path = os.path.join(cfg.out, "corners48.json")
    partial = bool(cfg.files or cfg.sample or cfg.ready or cfg.reviewed)
    if partial and os.path.exists(path):        # a partial run updates only its own icons
        with open(path, encoding="utf-8") as f:
            merged = json.load(f)
        merged.update(result)
        result_out = dict(sorted(merged.items()))
    else:
        result_out = result
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result_out, f, indent=1)
    tot = {k: sum(len(v[k]) for v in result.values())
           for k in ("sharp", "round", "junction", "kink", "curve")}
    print(f"processed {len(names)} icons | {tot} | {len(fails)} failures")
    for n, e in fails[:20]:
        print(f"  FAIL {n}: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
