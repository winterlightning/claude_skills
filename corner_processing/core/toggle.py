#!/usr/bin/env python3
"""core/toggle.py — turn every corner core/detect.py detects into ROUND or into SHARP.

  round  every corner ends up round with a WHOLE-NUMBER radius (the icons sit on the 48 grid):
           1. every straight-sided round corner is first sharpened, so the icon's radii come
              from one rule (round corners with a curved side are kept as drawn)
           2. the icon's corner angles are grouped (an angle joins a group while within
              --group-tol of the group's running mean: 88 and 92 always match)
           3. each group's mean angle picks its radius from --bands
              (default "60:1,75:2,105:4,180:6" = 1/4, 1/2, 1, 1.5 x the stroke width 4,
               the 1024 pipeline's grouped bands 12.8/25.6/51.2/76.8 rescaled)
           4. a corner between two CURVES (a lens shape's point) is part of the curve and is
              kept as drawn; corners with at least one straight side are rounded
           5. a corner whose sides can't hold its band radius gets the largest whole number
              that fits (--fallback reduce) or stays sharp (--fallback skip); below 1 it
              stays sharp
  sharp  every ROUND corner whose two sides are straight lines is replaced by two straight
         lines meeting at its apex (the point where its arms' tangent lines cross). A round
         corner with a curved side is part of a curve and is kept (--sharpen all to change).
         Sharp corners are kept. Drawn with mitre joins and FLAT caps (no round shape at all);
         butt_joints() rebuilds every meeting point so flat ends neither bite in nor poke out.
         --miter sets how far a narrow corner's point may reach (see MITER_MODES).

A sharp corner with a CURVED arm is rounded too: the fillet centre is where the two arms'
inward offset curves (distance r) first meet, and each arm is split where the circle touches it.
Junctions (3+ arms), kinks and curves are never touched.

Writes <out>/round/*.svg and <out>/sharp/*.svg (48x48, solo style) and <out>/toggle.json with
what was changed per icon, plus a re-detection check of every output.

  python3 -m core.toggle --sample 100 --seed 48            # same sample as the report
  python3 -m core.toggle --files t-shirt.svg --bands "75:2,105:4,180:6" --fallback skip
"""

import argparse
import cmath
import copy
import json
import math
import os
import random
import shutil
import sys
import tempfile
import xml.etree.ElementTree as ET
from concurrent.futures import ProcessPoolExecutor

import numpy as np
from shapely.geometry import LineString, Point, Polygon
from svgpathtools import Arc, CubicBezier, Line, QuadraticBezier, parse_path

from . import keyshape_fit
from . import locks
from .progress import Progress
from .detect import (CORNER_MAX_R, CONTACT_TOL, CORNER_MIN_TURN, EPS, NODE_TOL, find_nodes, fmt, line_hit, seg_turn, nearest_on_stroke, SMOOTH_TOL, Stroke, _n, angle_between, clean_subpath,
                      detect, tangent,
                      unit)
from .paths import OUT_DIR
from .svg_io import DEFAULT_INPUT, element_to_path, iter_skeleton_shapes, localname

SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)
DEFAULT_BANDS = "60:1,75:2,105:4,180:6"   # group-mean angle upper bound : whole-number radius
GROUP_TOL = 8.0        # deg — an angle joins a group while within this of its running mean
MIN_RADIUS = 1         # u — smallest radius drawn; a corner that can't hold it stays sharp
SNAP = 0.01            # u — a trim leaving less straight than this takes the whole straight
                       #     (neighbouring fillets then meet exactly instead of leaving a sliver)
GEOM_ATTRS = ("d", "x", "y", "width", "height", "rx", "ry", "cx", "cy", "r",
              "x1", "y1", "x2", "y2", "points")
SHARP_STYLE = {"stroke-linecap": "butt", "stroke-linejoin": "miter", "stroke-miterlimit": "2"}
MITER_MODES = ("keyshape", "slice", "shift", "mixed", "2", "4")
KS_MODES = ("keyshape", "slice", "shift")   # --miter modes that measure points against the keyshape
# --miter: a mitre point reaches 2/sin(angle/2) u past its corner (2.8 u at 90 deg, 6.8 u at 34 deg;
# a round cap reached 2 u). Past the limit the point is cut flat (bevel).
#   2      every corner narrower than 60 deg is cut flat
#   4      points kept down to 29 deg
#   mixed  a corner that was ALREADY SHARP in the input (a triangle's tips) keeps its point
#          (limit 4); one that was round and got sharpened, or a joint built from strokes that
#          met with round caps, is cut flat below 60 deg (limit 2). The limit is per path, so a
#          path holding both kinds stays at 2 and each sharp-born tip gets a short limit-4
#          copy of its two arms drawn on top (flat ends inside the stroke: invisible)
#   keyshape  points kept down to 29 deg (limit 4) unless the point
#          reaches more than TIP_OK past the keyshape (beyond what the input reaches there):
#          then it is cut flat along the keyshape edge (a clip path), the rest of the point stays
#   slice  (default; manager's pick, 2026-10-06) like keyshape with no tolerance: every point
#          is cut flat where the keyshape ends
#   shift  a point past the keyshape has its corner moved inward along its bisector until the
#          full point just touches the keyshape edge (it stays a true point); where it can't
#          move (a curved arm, an arm too short, another stroke at the corner) it is sliced
MITER_LOW, MITER_HIGH = 2.0, 4.0
SHIFT_NEAR = 2 * 2.0    # u — another stroke this close to a corner holds it in place (shift)
SHIFT_HOLD = 1.0        # u — an arm's far end this close to another stroke is a junction: held
TIP_OK = 2.5           # u — --miter keyshape: a point reaching this far past the keyshape is
                       #     fine (a bookmark ribbon's 51 deg tips reach 2.2 u); further is cut
MITER_TIP_ARM = 3.0    # u — length of each arm of a tip copy (cut to its segment)
MITER_MATCH = 0.25     # u — an output join this close to an input sharp corner is sharp-born
# sharp output: mitred JOINS draw corners as true points and FLAT caps end strokes square — no
# round shape anywhere. A flat cap no longer hides where strokes meet, so butt_joints() rebuilds
# every meeting point (snap, split, join) before the SVG is written.
ROOT_ATTRS = {"width": "48", "height": "48", "viewBox": "0 0 48 48", "fill": "none",
              "stroke": "currentColor", "stroke-width": "4",
              "stroke-linecap": "round", "stroke-linejoin": "round"}


def close(a, b, tol=NODE_TOL):
    return abs(a - b) <= tol


# ---------------------------------------------------------------------------
# editable icon model: elements -> strokes (same filtering as corner48.load_strokes)
# ---------------------------------------------------------------------------
class Icon:
    def __init__(self, path):
        self.root = ET.parse(path).getroot()
        self.title = next((el.text for el in self.root.iter()
                           if localname(el.tag) == "title" and el.text), None)
        self.items = []        # [(element, [Stroke] or None)]  None = copy element as is
        self.dots = set()      # id() of elements that are dots (zero-length paths)
        self.dot_at = {}       # id() -> centre: tiny loops drawn as dots (sharp output)
        sid = 0
        for el in iter_skeleton_shapes(self.root):
            name = localname(el.tag)
            p = None if name in ("circle", "ellipse") else element_to_path(el)
            strokes = []
            if p is not None:
                for sub in p.continuous_subpaths():
                    segs, closed = clean_subpath(sub)
                    if not segs:
                        continue
                    strokes.append(Stroke(sid, el.get("id") or name, segs, closed))
                    sid += 1
            keep_raw = p is None or not strokes or len(strokes) < len(p.continuous_subpaths())
            if p is not None and not strokes:
                self.dots.add(id(el))      # a zero-length path (M18 25L18 25): drawn by its cap
            self.items.append((el, strokes, keep_raw))
        self.extra = []        # new standalone strokes (between-stroke fillets)
        self.corner_pts = []   # corners being rounded (a shared side is split half and half)
        self.stop_pts = []     # junctions: a fillet never trims past one
        self.el_attrs = {}     # id(el) or ("extra", i) -> extra attributes (per-path mitre limit)
        self.tips = []         # (element id, d) limit-4 tip copies drawn on top (--miter mixed)
        self.fit = None        # keyshape_fit.Fit: keep the ink inside the keyshape
        self.clip = None       # clip path d: mitre tips cut where they cross the keyshape

    def strokes(self):
        return [s for _, ss, _ in self.items for s in ss] + self.extra

    def svg(self, style=None):
        out = ET.Element(f"{{{SVG_NS}}}svg", {**ROOT_ATTRS, **(style or {})})
        if self.title:
            ET.SubElement(out, f"{{{SVG_NS}}}title").text = self.title
        root = out
        if self.clip:                              # mitre tips cut at the keyshape
            cp = ET.SubElement(ET.SubElement(out, f"{{{SVG_NS}}}defs"), f"{{{SVG_NS}}}clipPath",
                               {"id": "keyshape-cut"})
            ET.SubElement(cp, f"{{{SVG_NS}}}path", {"d": self.clip, "clip-rule": "evenodd"})
            out = ET.SubElement(out, f"{{{SVG_NS}}}g", {"clip-path": "url(#keyshape-cut)"})
        for el, strokes, keep_raw in self.items:
            if id(el) in self.dot_at:              # a tiny loop drawn as a square dot
                c = self.dot_at[id(el)]
                attrs = {"id": el.get("id")} if el.get("id") else {}
                attrs["d"] = f"M{_n(c.real)} {_n(c.imag)}L{_n(c.real)} {_n(c.imag)}"
                attrs["stroke-linecap"] = "square"
                ET.SubElement(out, f"{{{SVG_NS}}}path", attrs)
                continue
            if keep_raw and not strokes:
                attrs = {a: el.get(a) for a in ("id",) + GEOM_ATTRS if el.get(a) is not None}
                if id(el) in self.dots and (style or {}).get("stroke-linecap") == "butt":
                    # a dot is only its cap: a flat cap draws nothing, a square cap draws the
                    # 4 x 4 square the round dot was (sharp output: no round shapes)
                    attrs["stroke-linecap"] = "square"
                ET.SubElement(out, f"{{{SVG_NS}}}{localname(el.tag)}", attrs)
                continue
            if not strokes:                        # all its strokes merged into another path
                continue
            d = "".join(stroke_d(s) for s in strokes)
            attrs = {"id": el.get("id")} if el.get("id") else {}
            attrs["d"] = d
            attrs.update(self.el_attrs.get(id(el), {}))
            ET.SubElement(out, f"{{{SVG_NS}}}path", attrs)
        for i, s in enumerate(self.extra):
            ET.SubElement(out, f"{{{SVG_NS}}}path", {"id": f"corner-fillet-{i}", "d": stroke_d(s),
                                                     **self.el_attrs.get(("extra", i), {})})
        for k, (eid, d) in enumerate(self.tips):
            ET.SubElement(out, f"{{{SVG_NS}}}path", {"id": f"{eid}-tip-{k}", "d": d,
                                                     "stroke-miterlimit": _n(MITER_HIGH)})
        ET.indent(root, space="  ")
        return ET.tostring(root, encoding="unicode") + "\n"


def stroke_d(st):
    p = lambda z: f"{_n(z.real)} {_n(z.imag)}"
    segs = st.segs
    out = [f"M{p(segs[0].start)}"]
    for i, s in enumerate(segs):
        last = i == len(segs) - 1
        if isinstance(s, Line):
            if not (st.closed and last):
                out.append(f"L{p(s.end)}")
        elif isinstance(s, Arc):
            out.append(f"A{_n(s.radius.real)} {_n(s.radius.imag)} {_n(s.rotation)} "
                       f"{int(s.large_arc)} {int(s.sweep)} {p(s.end)}")
        elif isinstance(s, CubicBezier):
            out.append(f"C{p(s.control1)} {p(s.control2)} {p(s.end)}")
        elif isinstance(s, QuadraticBezier):
            out.append(f"Q{p(s.control)} {p(s.end)}")
    if st.closed:
        out.append("Z")
    return "".join(out)


def _continues(a, b):
    if not (isinstance(a, Line) and isinstance(b, Line)):
        return False
    ua, ub = unit(a.end - a.start), unit(b.end - b.start)
    return ua is not None and ub is not None and angle_between(ua, ub) < SMOOTH_TOL


def merge_collinear(st):
    """Join consecutive Lines that continue straight (keeps the drawing, drops split points).
    A closed path is first rotated to start at a real join, so a seam in the middle of a
    straight edge doesn't leave that edge split in two."""
    if st.closed and len(st.segs) > 1 and _continues(st.segs[-1], st.segs[0]):
        k = next((i for i in range(1, len(st.segs)) if not _continues(st.segs[i - 1], st.segs[i])), None)
        if k is not None:
            st.segs = st.segs[k:] + st.segs[:k]
    segs = st.segs
    changed = True
    while changed and len(segs) > 1:
        changed = False
        n = len(segs)
        rng = range(n) if st.closed else range(1, n)
        for i in rng:
            j = (i - 1) % n
            a, b = segs[j], segs[i]
            if i == j or not (isinstance(a, Line) and isinstance(b, Line)):
                continue
            ua, ub = unit(a.end - a.start), unit(b.end - b.start)
            if ua is None or ub is None or angle_between(ua, ub) >= SMOOTH_TOL:
                continue
            if st.closed and i == 0:
                # wrap join: keep the start point (it is a node others may refer to)
                continue
            segs[j:i + 1] = [Line(a.start, b.end)]
            changed = True
            break
    st.segs = segs


def arc_between(p1, p2, r, u_in, u_out):
    cross = u_in.real * u_out.imag - u_in.imag * u_out.real
    return Arc(p1, complex(r, r), 0.0, False, cross > 0, p2)


FIT_SAMPLES = 800       # samples per arm segment for the general (curved-arm) fillet


def _arm_samples(seg, at_end, limit):
    """Dense samples of `seg` near the corner: (t, point, unit tangent in path direction),
    ordered from the corner outward, limited to `limit` arc length from the corner."""
    ts = np.linspace(0.0, 1.0, FIT_SAMPLES)
    pts = np.array([seg.point(x) for x in ts], dtype=complex)
    g = np.gradient(pts)
    g = np.where(np.abs(g) < 1e-12, 1e-12, g)
    u = g / np.abs(g)
    if at_end:                         # corner at t=1: walk back from the end
        ts, pts, u = ts[::-1], pts[::-1], u[::-1]
    s = np.concatenate([[0.0], np.cumsum(np.abs(np.diff(pts)))])
    keep = s <= limit
    return ts[keep], pts[keep], u[keep]


def fillet_general(A, B, r, limA, limB):
    """Fillet between segment A (ending at the corner) and segment B (starting there), either
    straight or curved. The centre C is the first point (from the corner outward) of A's inward
    offset curve that is exactly r from B; the arc runs from A's touch point to B's.
    Returns (A_cropped, arc, B_cropped) or None when r does not fit inside the limits."""
    tA, tB = tangent(A, 1.0), tangent(B, 0.0)
    if tA is None or tB is None:
        return None
    cross = tA.real * tB.imag - tA.imag * tB.real
    if abs(cross) < 1e-9:
        return None
    side = 1j if cross > 0 else -1j          # inward normal = tangent rotated toward the turn
    ta, pa, ua = _arm_samples(A, True, limA)
    tb, pb, _ = _arm_samples(B, False, limB)
    if len(ta) < 3 or len(tb) < 3:
        return None
    centres = pa + r * side * ua
    dist = np.abs(centres[:, None] - pb[None, :])          # centre -> every B sample
    f = dist.min(axis=1) - r
    if f[0] >= 0:
        return None
    k = int(np.argmax(f >= 0))
    if k == 0:                                           # never reaches r within the limits
        return None
    w = f[k - 1] / (f[k - 1] - f[k])                     # linear root between samples
    ta_star = ta[k - 1] + w * (ta[k] - ta[k - 1])
    q1 = A.point(ta_star)
    c = centres[k - 1] + w * (centres[k] - centres[k - 1])
    j = int(np.argmin(np.abs(pb - c)))
    if j == 0 or j >= len(tb) - 1:                       # touch point at the corner / at limit
        return None
    # refine B's touch parameter with a parabola through the three nearest samples
    d0, d1, d2 = (abs(pb[x] - c) for x in (j - 1, j, j + 1))
    den = d0 - 2 * d1 + d2
    off = 0.5 * (d0 - d2) / den if abs(den) > 1e-12 else 0.0
    tb_star = float(tb[j] + max(-1.0, min(1.0, off)) * (tb[j + 1] - tb[j]))
    q2 = B.point(tb_star)
    if abs(q1 - A.start) < 1e-6 or abs(q2 - B.end) < 1e-6:
        return None
    arc = Arc(q1, complex(r, r), 0.0, False, cross > 0, q2)
    return A.cropped(0.0, float(ta_star)), arc, B.cropped(tb_star, 1.0)


def _limit(seg, corner_at_end, corner_pts, stop_pts):
    """Arc length of `seg`, measured from the corner, that a fillet may use: up to the first
    junction lying on the segment (a stroke attached there must stay attached), half the
    segment when its far end is another corner that is also being rounded, else nearly all."""
    L = seg.length()
    far_end = seg.start if corner_at_end else seg.end
    corner = seg.end if corner_at_end else seg.start
    limit = L / 2.0 if any(close(far_end, q) for q in corner_pts) else L * 0.98
    n = max(16, int(L / 0.05))
    pts = [seg.point(k / n) for k in range(n + 1)]
    for q in stop_pts:
        if close(q, corner):
            continue
        d = [abs(p - q) for p in pts]
        k = min(range(len(d)), key=d.__getitem__)
        if d[k] <= NODE_TOL:
            s = seg.length(0, k / n) if not corner_at_end else seg.length(k / n, 1)
            limit = min(limit, s * 0.98)
    return limit


def fillet_fit(A, B, r, corner_pts, stop_pts):
    """General fillet of exactly radius r. -> (A', arc, B', r) or None if it does not fit."""
    limA, limB = _limit(A, True, corner_pts, stop_pts), _limit(B, False, corner_pts, stop_pts)
    got = fillet_general(A, B, r, limA, limB)
    return (*got, r) if got is not None else None


# ---------------------------------------------------------------------------
# sharp -> round
# ---------------------------------------------------------------------------
def round_in_path(icon, P, theta, r):
    """Fillet the in-path join at P (both neighbours Lines). True if applied."""
    t = r / math.tan(math.radians(theta) / 2.0)
    for st in icon.strokes():
        n = len(st.segs)
        for i in range(n):
            j = i - 1 if i > 0 else (n - 1 if st.closed else None)
            if j is None or j == i:
                continue
            a, b = st.segs[j], st.segs[i]
            if not (close(a.end, P) and close(b.start, P)):
                continue
            if not (isinstance(a, Line) and isinstance(b, Line)):
                got = fillet_fit(a, b, r, icon.corner_pts, icon.stop_pts)
                if got is None:
                    return False, r
                new_a, arc, new_b, r = got
                if j < i:
                    st.segs[j:i + 1] = [new_a, arc, new_b]
                else:
                    st.segs = [new_b] + st.segs[1:-1] + [new_a, arc]
                return "curved", r
            u_in, u_out = unit(a.end - a.start), unit(b.end - b.start)
            if min(a.length(), b.length()) < t - 1e-6:
                return False, r
            p1, p2 = P - t * u_in, P + t * u_out
            consumed = False
            if abs(p1 - a.start) <= SNAP:
                p1, consumed = a.start, True
            if abs(b.end - p2) <= SNAP:
                p2, consumed = b.end, True
            arc = arc_between(p1, p2, r, u_in, u_out)
            new_a = None if p1 == a.start else Line(a.start, p1)
            new_b = None if p2 == b.end else Line(p2, b.end)
            if j < i:
                st.segs[j:i + 1] = [s for s in (new_a, arc, new_b) if s is not None]
            else:            # closed wrap join: j is the last segment, i == 0
                st.segs = [s for s in (new_b,) if s] + st.segs[1:-1] + \
                          [s for s in (new_a, arc) if s]
            return ("consumed" if consumed else True), r
    return False, r


def round_between(icon, P, theta, r):
    """Fillet two stroke ENDS meeting at P."""
    ends = []
    for st in icon.strokes():
        if st.closed:
            continue
        if close(st.segs[-1].end, P):
            ends.append((st, "end"))
        if close(st.segs[0].start, P):
            ends.append((st, "start"))
    if len(ends) != 2:
        return False, r
    return fillet_ends(icon, P, theta, r, ends[0], ends[1])


def fillet_ends(icon, P, theta, r, end_a, end_b):
    """Fillet between two stroke ends at P (end = (stroke, "start"|"end")): trim both and
    attach the arc to stroke A."""
    t = r / math.tan(math.radians(theta) / 2.0)
    (sa, wa), (sb, wb) = end_a, end_b
    ends = [end_a, end_b]
    segs = [st.segs[-1] if w == "end" else st.segs[0] for st, w in ends]
    if not all(isinstance(s, Line) for s in segs):
        # orient: A runs INTO P, B runs OUT of P
        A = segs[0] if wa == "end" else segs[0].reversed()
        B = segs[1] if wb == "start" else segs[1].reversed()
        got = fillet_fit(A, B, r, icon.corner_pts, icon.stop_pts)
        if got is None:
            return False, r
        new_a, arc, new_b, r = got
        if wa == "end":
            sa.segs[-1] = new_a
            sa.segs.append(arc)
        else:
            sa.segs[0] = new_a.reversed()
            sa.segs.insert(0, arc.reversed())
        if wb == "start":
            sb.segs[0] = new_b
        else:
            sb.segs[-1] = new_b.reversed()
        return "curved", r
    if min(s.length() for s in segs) < t - 1e-6:
        return False, r
    # travel: along A INTO P, then out of P along B
    a_far = segs[0].start if wa == "end" else segs[0].end
    b_far = segs[1].end if wb == "start" else segs[1].start
    u_in, u_out = unit(P - a_far), unit(b_far - P)
    p1, p2 = P - t * u_in, P + t * u_out
    consumed = False
    if abs(p1 - a_far) <= SNAP:
        p1, consumed = a_far, True
    if abs(b_far - p2) <= SNAP:
        p2, consumed = b_far, True
    for (st, w), s, q in (((sa, wa), segs[0], p1), ((sb, wb), segs[1], p2)):
        if w == "end":
            st.segs[-1] = Line(s.start, q)
        else:
            st.segs[0] = Line(q, s.end)
    # attach the arc to stroke A so it continues A's line (line -> arc in ONE path, the way a
    # drawn round corner is authored), ending on B's trimmed end
    arc = arc_between(p1, p2, r, u_in, u_out)
    if wa == "end":
        sa.segs.append(arc)
    else:
        sa.segs.insert(0, Arc(p2, arc.radius, 0.0, False, not arc.sweep, p1))
    for st in (sa, sb):                       # a fully consumed end segment is dropped
        st.segs = [s for s in st.segs if s.length() > 1e-9] or st.segs
    return ("consumed" if consumed else True), r


def split_at(icon, P):
    """Split every stroke that passes through P at a join there, so all arms at P are ends."""
    for _, strokes, _ in icon.items:
        out = []
        for st in strokes:
            cut = [i for i in range(st.n()) if close(st.segs[i].start, P) and (st.closed or i > 0)]
            if not cut:
                out.append(st)
            elif st.closed:            # open the loop at P
                i = cut[0]
                out.append(Stroke(st.sid, st.elem_id, st.segs[i:] + st.segs[:i], False))
            else:
                i = cut[0]
                out += [Stroke(st.sid, st.elem_id, st.segs[:i], False),
                        Stroke(st.sid, st.elem_id, st.segs[i:], False)]
        strokes[:] = out


def _ends_at(icon, P, tol):
    """[(stroke, which, direction leaving P)] for every open stroke end within tol of P."""
    out = []
    for st in icon.strokes():
        if st.closed:
            continue
        if abs(st.segs[0].start - P) <= tol:
            out.append((st, "start", tangent(st.segs[0], 0.0)))
        if abs(st.segs[-1].end - P) <= tol:
            out.append((st, "end", -tangent(st.segs[-1], 1.0)))
    return [e for e in out if e[2] is not None]


def round_inner(icon, P, theta, r, rec):
    """Round a corner with an INNER stroke ending at its point (an arrow tip: the two head
    arms are filleted, and the shaft is shortened so it ends ON the new arc instead of poking
    out past the rounded tip)."""
    split_at(icon, P)
    ends = _ends_at(icon, P, CONTACT_TOL)
    want = [cmath.rect(1.0, math.radians(d)) for d in rec["arm_dirs"]] + \
           [cmath.rect(1.0, math.radians(rec["inner"]["dir"]))]
    picked = []
    for w in want:
        cand = [e for e in ends if e not in picked]
        if not cand:
            return False, r
        best = min(cand, key=lambda e: angle_between(e[2], w))
        if angle_between(best[2], w) > 10.0:
            return False, r
        picked.append(best)
    (sa, wa, ua), (sb, wb, ub), (sc, wc, _) = picked
    if not (close(sa.segs[0].start if wa == "start" else sa.segs[-1].end, P) and
            close(sb.segs[0].start if wb == "start" else sb.segs[-1].end, P)):
        return False, r
    ok, r = fillet_ends(icon, P, theta, r, (sa, wa), (sb, wb))
    if not ok:
        return False, r
    # shorten the inner stroke to where it meets the fillet circle
    half = math.radians(theta) / 2.0
    bis = unit(ua + ub)
    seg = sc.segs[0] if wc == "start" else sc.segs[-1]
    if bis is None:
        return ok, r
    centre = P + bis * (r / math.sin(half))
    if not isinstance(seg, Line):              # curved inner stroke: cut where it meets the circle
        f = lambda x: abs(seg.point(x) - centre) - r
        t_end = 0.0 if wc == "start" else 1.0
        steps = [t_end + (k / 200.0) * (1.0 if wc == "start" else -1.0) for k in range(201)]
        if f(t_end) <= 0:
            return ok, r
        for x0, x1 in zip(steps, steps[1:]):
            if f(x1) <= 0:
                for _ in range(40):            # bisection
                    xm = 0.5 * (x0 + x1)
                    x0, x1 = (xm, x1) if f(xm) > 0 else (x0, xm)
                cut = 0.5 * (x0 + x1)
                if wc == "start":
                    sc.segs[0] = seg.cropped(cut, 1.0)
                else:
                    sc.segs[-1] = seg.cropped(0.0, cut)
                break
        return ok, r
    E, far = (seg.start, seg.end) if wc == "start" else (seg.end, seg.start)
    u = unit(far - E)
    w = E - centre
    wu = (w.conjugate() * u).real
    disc = wu * wu - (abs(w) ** 2 - r * r)
    if u is None or disc < 0:
        return ok, r
    s = -wu - math.sqrt(disc)
    if 0 < s < seg.length() - 1e-6:
        q = E + s * u
        if wc == "start":
            sc.segs[0] = Line(q, seg.end)
        else:
            sc.segs[-1] = Line(seg.start, q)
    return ok, r


# ---------------------------------------------------------------------------
# sharp output: flat caps — rebuild every meeting point so nothing pokes out or bites in
# ---------------------------------------------------------------------------
# With round caps a stroke end hid whatever happened where strokes meet. A flat cap shows it:
# two ends that miss each other by 1 u draw two offset rectangles (a stair step), two ends that
# meet at an angle leave a wedge cut out of the outside of the corner, and a path bending at a
# junction pushes its mitre point through the stroke beside it. butt_joints() first closes
# near-loops and trims 1 u stubs (see those functions), then fixes the geometry at every
# meeting point, repeating until nothing changes:
#   1. snap   an end that misses its meeting point by up to CONTACT_TOL is moved onto it (onto
#             the bend it touches, onto the centreline it lands on, or onto the crossing of
#             the ends' own directions) — a flat end ON a centreline is always inside that ink
#   2. split  a path that bends where another stroke leaves through the OUTSIDE of the bend
#             is cut there: its mitre point would stick out past that stroke
#   3. join   two ends that bound an empty outside gap (> 180 deg) become one path through
#             the point, so the mitre fills the corner instead of leaving a wedge
OUTER_MARGIN = 3.0     # deg — an arm counts as outside a bend only when this far past its sides
HAIRPIN = 15.0         # deg — two ends this close in direction (a flag's cloth along its pole)
                       #       are not joined: the turn would be a hairpin, not a corner
BUTT_PASSES = 40       # passes before giving up (a pass snaps a whole icon, or splits / joins
                       # one meeting point, then the meeting points are found again)


def _angle(u):
    return math.degrees(cmath.phase(u)) % 360.0


def _inside(x, a, b):
    """Is direction x inside the smaller angle between directions a and b (sides excluded)?"""
    th = angle_between(a, b)
    return (angle_between(a, x) > OUTER_MARGIN and angle_between(x, b) > OUTER_MARGIN
            and abs(angle_between(a, x) + angle_between(x, b) - th) < 0.5)


def _outside(x, a, b):
    return (not _inside(x, a, b) and angle_between(x, a) > OUTER_MARGIN
            and angle_between(x, b) > OUTER_MARGIN)


def _end_dir(st, which):
    """Direction leaving the end point along the stroke."""
    return tangent(st.segs[0], 0.0) if which == "start" else -tangent(st.segs[-1], 1.0)


def _end_pt(st, which):
    return st.segs[0].start if which == "start" else st.segs[-1].end


def _moved(seg, which, P):
    """seg with its start or end moved onto P, keeping its kind (and, for a curve, the tangent
    at that end). None when a straight would shrink to nothing."""
    E = seg.start if which == "start" else seg.end
    d = P - E
    if isinstance(seg, Line):
        new = Line(P, seg.end) if which == "start" else Line(seg.start, P)
        return new if new.length() >= 0.25 else None
    if isinstance(seg, CubicBezier):
        return (CubicBezier(P, seg.control1 + d, seg.control2, seg.end) if which == "start"
                else CubicBezier(seg.start, seg.control1, seg.control2 + d, P))
    if isinstance(seg, QuadraticBezier):
        return (QuadraticBezier(P, seg.control + d, seg.end) if which == "start"
                else QuadraticBezier(seg.start, seg.control + d, P))
    if isinstance(seg, Arc):
        return (Arc(P, seg.radius, seg.rotation, seg.large_arc, seg.sweep, seg.end)
                if which == "start" else
                Arc(seg.start, seg.radius, seg.rotation, seg.large_arc, seg.sweep, P))
    return None


def _move_end(st, which, P):
    """Move one open end of st onto P. Returns True when something moved."""
    i = 0 if which == "start" else -1
    if abs(_end_pt(st, which) - P) < 1e-6:
        return False
    new = _moved(st.segs[i], which, P)
    if new is None:
        return False
    st.segs[i] = new
    return True


def _move_bend(st, i, P):
    """Move the bend of st at the join into segment i onto P (both segments follow)."""
    j = st.prev(i)
    if abs(st.segs[i].start - P) < 1e-6:
        return False
    a, b = _moved(st.segs[j], "end", P), _moved(st.segs[i], "start", P)
    if a is None or b is None:
        return False
    st.segs[j], st.segs[i] = a, b
    return True


def _landing(st, E, d, tol):
    """Where an end at E heading d (into the other stroke) lands on the INTERIOR of stroke st,
    moving along its own line only (sliding sideways would tilt the end's segment). None when
    its line misses st within tol, or meets st only within CONTACT_TOL of st's own ends (st is
    ending there too: that pair is two ends meeting, not an end landing on a line)."""
    best = None
    ends = () if st.closed else (st.segs[0].start, st.segs[-1].end)
    for s in st.segs:
        x0, x1, y0, y1 = s.bbox()
        if not (x0 - tol <= E.real <= x1 + tol and y0 - tol <= E.imag <= y1 + tol):
            continue
        if isinstance(s, Line):                 # a straight: where the two lines cross, exactly
            u = unit(s.end - s.start)
            hit = line_hit(E, d, s.start, -u) if u is not None else None
            if hit is not None and -1e-9 <= hit[1] <= s.length() + 1e-9:
                q = hit[2]
                if abs(q - E) <= tol and not any(abs(q - e) <= CONTACT_TOL for e in ends) \
                        and (best is None or abs(q - E) < best[0]):
                    best = (abs(q - E), q)
            continue
        n = max(8, int(s.length() / 0.02))
        for k in range(n + 1):
            q = s.point(k / n)
            r = abs(q - E)
            if r > tol or any(abs(q - e) <= CONTACT_TOL for e in ends):
                continue
            off = abs((q - E).real * d.imag - (q - E).imag * d.real)   # distance to E's line
            if off < 0.03 and (best is None or r < best[0]):
                best = (r, q)
    if best is None:
        return None
    return E + d * ((best[1] - E) * d.conjugate()).real   # exactly on E's own line


def _passes(st, P):
    """Does stroke st run THROUGH P (not merely end next to it)? -> its tangent there or None."""
    hit = nearest_on_stroke(st, P, CONTACT_TOL)
    if hit is None or hit[1] is None:
        return None
    if not st.closed and any(abs(e - P) <= hit[0] + CONTACT_TOL
                             for e in (st.segs[0].start, st.segs[-1].end)):
        return None                            # it ends right there: not passing through
    return hit[1]


def _ends_meet(ends, reach):
    """Meeting point for several ends [(point, direction)]: the candidate (an end point, or
    where two ends' lines cross) that the ends reach by moving ALONG their own lines as far as
    possible — sliding an end sideways would tilt its whole segment (an envelope's top edge).
    Ties go to the smallest total move. None when no candidate is within reach of every end."""
    cands = [E for E, _ in ends]
    for i in range(len(ends)):
        for j in range(i + 1, len(ends)):
            (E1, d1), (E2, d2) = ends[i], ends[j]
            hit = line_hit(E1, d1, E2, -d2)
            if hit is not None:
                cands.append(hit[2])
    best = None
    for P in cands:
        if any(abs(P - E) > reach for E, _ in ends):
            continue
        side = sum(abs((P - E).real * d.imag - (P - E).imag * d.real) for E, d in ends)
        key = (round(side, 3), sum(abs(P - E) for E, _ in ends))
        if best is None or key < best[0]:
            best = (key, P)
    return best[1] if best else None


def _node_arms(strokes, nd):
    """[(direction, kind, ref)] of every arm at a node. kind: 'end' (ref (stroke, which)),
    'bend' (ref (stroke, i)), 'pass' / 'cross' (ref stroke)."""
    arms = []
    for tg in nd["tags"]:
        if "end" in tg:
            sid, which = tg["end"]
            st = strokes[sid]
            d = _end_dir(st, which)
            if d is not None:
                arms.append((d, "end", (st, which)))
        elif "join" in tg:
            sid, i = tg["join"]
            st = strokes[sid]
            a, b = -tangent(st.segs[st.prev(i)], 1.0), tangent(st.segs[i], 0.0)
            arms += [(a, "bend", (st, i)), (b, "bend", (st, i))]
        elif "on" in tg:
            st = strokes[tg["on"]]
            u = _passes(st, nd["p"])
            if u is not None:
                arms += [(u, "pass", st), (-u, "pass", st)]
        elif "cross" in tg:
            pass                                   # crossings carry their arms in nd["arms"]
    if any("cross" in tg for tg in nd["tags"]):
        arms += [(d, "cross", None) for d, _, _ in nd["arms"]]
    return [a for a in arms if a[0] is not None]


def _snap(strokes, nd):
    tags = nd["tags"]
    ends = [(strokes[tg["end"][0]], tg["end"][1]) for tg in tags if "end" in tg]
    if not ends or len(_node_arms(strokes, nd)) < 2:
        return False
    moved = False
    joins = [tg["join"] for tg in tags if "join" in tg]
    passing = [strokes[tg["on"]] for tg in tags if "on" in tg
               and _passes(strokes[tg["on"]], nd["p"]) is not None]
    corners = []
    for sid, i in joins:
        st = strokes[sid]
        a, b = -tangent(st.segs[st.prev(i)], 1.0), tangent(st.segs[i], 0.0)
        if a is not None and b is not None and angle_between(a, b) <= 180.0 - CORNER_MIN_TURN:
            corners.append((st, i, a, b))
        else:
            passing.append(st)                 # a seam or slight kink: the path runs through
    if corners:
        # ends meeting a corner: pick the point the ends AND the corner's two sides reach along
        # their own lines (an envelope's top edge ending 1 u above the frame's corner moves the
        # corner up onto the top edge's line, instead of tilting the top edge down to it). Only
        # a corner between two straights can move: moving one on a curve would redraw the curve.
        lines = [(_end_pt(st, w), _end_dir(st, w)) for st, w in ends]
        fixed = []
        for st, i, a, b in corners:
            V = st.segs[i].start
            lines += [(V, a), (V, b)]
            if not (isinstance(st.segs[st.prev(i)], Line) and isinstance(st.segs[i], Line)):
                fixed.append(V)
        lines = [(E, d) for E, d in lines if d is not None]
        P = fixed[0] if fixed else _ends_meet(lines, CONTACT_TOL + 0.5)
        if P is None:
            P = corners[0][0].segs[corners[0][1]].start
        for st, i, _, _ in corners:
            moved |= _move_bend(st, i, P)
        for st, which in ends:
            moved |= _move_end(st, which, P)
    else:
        landed = False
        for st, which in ends:                 # onto the centreline the end runs into
            E, d = _end_pt(st, which), _end_dir(st, which)
            for o in passing:
                P = _landing(o, E, -d, CONTACT_TOL + 0.5) if d is not None else None
                if P is not None:
                    moved |= _move_end(st, which, P)
                    landed = True
                    break
        if not landed and len(ends) >= 2:      # ends only: where their directions cross
            pts = [(_end_pt(st, w), _end_dir(st, w)) for st, w in ends]
            P = _ends_meet([(E, d) for E, d in pts if d is not None], CONTACT_TOL + 0.5)
            if P is not None:                  # none: they can't meet without tilting; leave
                for st, which in ends:
                    moved |= _move_end(st, which, P)
    return moved


def _cut(icon, st, i):
    """Split stroke st at the join into segment i (open a closed loop there)."""
    for _, strokes, _ in icon.items:
        if st in strokes:
            k = strokes.index(st)
            if st.closed:
                strokes[k] = Stroke(st.sid, st.elem_id, st.segs[i:] + st.segs[:i], False)
            else:
                strokes[k:k + 1] = [Stroke(st.sid, st.elem_id, st.segs[:i], False),
                                    Stroke(st.sid, st.elem_id, st.segs[i:], False)]
            return True
    if st in icon.extra:
        k = icon.extra.index(st)
        if st.closed:
            icon.extra[k] = Stroke(st.sid, st.elem_id, st.segs[i:] + st.segs[:i], False)
        else:
            icon.extra[k:k + 1] = [Stroke(st.sid, st.elem_id, st.segs[:i], False),
                                   Stroke(st.sid, st.elem_id, st.segs[i:], False)]
        return True
    return False


def _split(icon, strokes, nd):
    arms = _node_arms(strokes, nd)
    for tg in nd["tags"]:
        if "join" not in tg:
            continue
        sid, i = tg["join"]
        st = strokes[sid]
        a, b = -tangent(st.segs[st.prev(i)], 1.0), tangent(st.segs[i], 0.0)
        if a is None or b is None or angle_between(a, b) > 180.0 - CORNER_MIN_TURN:
            continue                         # a near-straight pass: its mitre barely shows
        others = [d for d, kind, ref in arms if not (kind == "bend" and ref == (st, i))]
        if any(_outside(x, a, b) for x in others):
            return _cut(icon, st, i)
    return False


def _join(icon, strokes, nd):
    arms = sorted(_node_arms(strokes, nd), key=lambda a: _angle(a[0]))
    if len(arms) < 2:
        return False
    pairs = []
    for k in range(len(arms)):
        x, y = arms[k], arms[(k + 1) % len(arms)]
        gap = (_angle(y[0]) - _angle(x[0])) % 360.0 or 360.0
        if x[1] != "end" or y[1] != "end" or x[2] == y[2]:
            continue
        if gap >= 180.0 - SMOOTH_TOL and 360.0 - gap >= HAIRPIN:
            pairs.append((gap, x[2], y[2]))
    for _, (sa, wa), (sb, wb) in sorted(pairs, key=lambda p: -p[0]):   # widest gap first
        if abs(_end_pt(sa, wa) - _end_pt(sb, wb)) > NODE_TOL:
            continue                         # not snapped onto one point (yet)
        a_in = sa.segs if wa == "end" else [s.reversed() for s in reversed(sa.segs)]
        b_out = sb.segs if wb == "start" else [s.reversed() for s in reversed(sb.segs)]
        if sa is sb:
            sa.segs, sa.closed = a_in, True
            if abs(sa.segs[-1].end - sa.segs[0].start) > 1e-6:
                _move_end(sa, "end", sa.segs[0].start)
            return True
        gap_v = b_out[0].start - a_in[-1].end
        bridge = [Line(a_in[-1].end, b_out[0].start)] if abs(gap_v) > 1e-6 else []
        sa.segs = a_in + bridge + b_out
        for _, ss, _ in icon.items:
            if sb in ss:
                ss.remove(sb)
        if sb in icon.extra:
            icon.extra.remove(sb)
        return True                          # one join per pass: the node list is now stale
    return False


def _close_near_loops(icon):
    """A path whose own two ends nearly meet (an envelope frame drawn M4 9 ... L4 8) is a loop
    left open by 1 u: close it at the point both ends reach along their own lines. (The node
    finder keeps a path's start and end apart, so the snap step never sees this pair.)"""
    for st in icon.strokes():
        if st.closed or st.n() < 2:
            continue
        a, b = st.segs[0].start, st.segs[-1].end
        if abs(a - b) > CONTACT_TOL + 0.5:
            continue
        da, db = _end_dir(st, "start"), _end_dir(st, "end")
        if da is None or db is None or angle_between(da, db) < HAIRPIN:
            continue
        P = _ends_meet([(a, da), (b, db)], CONTACT_TOL + 0.5)
        if P is None:
            continue
        _move_end(st, "start", P)
        _move_end(st, "end", P)
        if abs(st.segs[-1].end - st.segs[0].start) <= 1e-6:
            st.closed = True


def _trim_overshoots(icon):
    """An end that runs up to CONTACT_TOL past the point where another stroke's END lands on
    it (a baseline 1 u past the bar standing on it) is cut back to that point: with flat caps
    the 1 u stub shows as a step beside the bar, not as an overhang. The two ends then meet
    and the join step makes them one corner."""
    strokes = icon.strokes()
    for st in strokes:
        if st.closed:
            continue
        for which in ("start", "end"):
            i = 0 if which == "start" else -1
            seg = st.segs[i]
            if not isinstance(seg, Line):
                continue
            E, d = _end_pt(st, which), _end_dir(st, which)
            if d is None:
                continue
            if any(o is not st and nearest_on_stroke(o, E, NODE_TOL) is not None
                   for o in strokes):
                continue                 # the end already meets something: not a stub
            best = None
            for o in strokes:
                if o is st or o.closed:
                    continue
                for ow in ("start", "end"):
                    F, fd = _end_pt(o, ow), _end_dir(o, ow)
                    t = ((F - E) * d.conjugate()).real          # how far along st from E
                    off = abs(((F - E) * d.conjugate()).imag)   # how far off st's line
                    if not (NODE_TOL < t <= CONTACT_TOL + 1e-6 and off <= NODE_TOL):
                        continue
                    if fd is None or angle_between(fd, d) < CORNER_MIN_TURN \
                            or angle_between(fd, -d) < CORNER_MIN_TURN:
                        continue                                 # not a corner: in line
                    if best is None or t < best[0]:
                        best = (t, E + d * t)
            if best is not None:
                _move_end(st, which, best[1])


BIG_ROUND_R = float(os.environ.get("CORNER48_BIG_ROUND_R", 6.0))   # u (--big-round-r) — (user, 2026-10-06: was 5.5; r 6 rounds are corners) a round corner bigger than this (corner48.corner_size: its radius, or
                          #     its reach along the sides when narrower than 90 deg) is a designed curve, not a softened
                          #     corner: it stays as drawn in the sharp output (a boot's r 7-8
                          #     instep and heel). Small ones (r 1-6) are sharpened
SHARP_EVERY_CORNER = {    # icons whose sharp output sharpens every round corner, big ones too
    "add-tab.svg",        # (user, 2026-10-06): all 5 corners sharp, the r 7 tab shoulders too
}
SHARP_THESE_CORNERS = {   # icon -> apexes of big round corners its sharp output sharpens anyway
}
SOFT_GAP = float(os.environ.get("CORNER48_SOFT_GAP", 1.0))   # u (--soft-gap; user, 2026-10-06) — a round corner over
                          #     BIG_ROUND_R (up to CORNER_MAX_R) is still sharpened when its sharp
                          #     point sits no further than this from the drawn curve: a wide,
                          #     gentle corner (a badge's r 7 shoulders at 128 deg: 0.8 u). 0: off
JOINED_MAX_R = BIG_ROUND_R  # u — a rounded corner drawn as separate strokes (straight, arc in its
                          #     own path, straight) is sharpened once butt_joints() makes it one
                          #     path, if it is no larger than this and than its straight sides


def _probe_rounds(icon, res, tmp_dir):
    """Round corners in the current sharp drawing that the INPUT's detection did not have."""
    probe = os.path.join(tmp_dir, "butt-probe.svg")
    with open(probe, "w", encoding="utf-8") as fh:
        fh.write(icon.svg(SHARP_STYLE))
    seen = [complex(*c["apex"]) for c in res["round"]]
    return [c for c in detect(probe)["round"]
            if not any(abs(complex(*c["apex"]) - q) <= JUNCTION_MATCH for q in seen)]


def sharpen_joined_rounds(icon, log, res, tmp_dir, max_r=None):
    """Small fillets between two straights that only became one path in butt_joints() are
    corners like any other: sharpen them (see JOINED_MAX_R). Returns True if any changed."""
    changed = False
    for c in _probe_rounds(icon, res, tmp_dir):
        straight = [rc - lg for rc, lg in zip(c["reach"], c["legs"])]
        r_corner = min(c["r"], c.get("r_drawn") or c["r"])
        if c["arms"] != ["line", "line"] or r_corner > (JOINED_MAX_R if max_r is None else max_r) \
                or r_corner > min(straight) + 1e-6:
            continue
        ok = sharpen(icon, c)
        changed |= ok
        log.append({"p": c["apex"], "angle": c["angle"], "r": c["r"],
                    "status": "sharpened" if ok else "skipped", "why": "drawn as separate strokes"})
    if changed:
        for st in icon.strokes():
            merge_collinear(st)
    return changed


def log_joined_rounds(icon, log, res, tmp_dir):
    """Round corners butt_joints() made visible stay round. A rounded corner drawn as separate
    strokes (a straight, then an arc in its own path) was never a corner to the detector, so
    the sharp output never sharpened it; joining the strokes only removes the seam between
    them (a hairline with flat caps). Sharpening them would redraw shoulders, domes and backs
    that are part of the design, so they are logged as kept round instead (small ones were
    already sharpened by sharpen_joined_rounds)."""
    for c in _probe_rounds(icon, res, tmp_dir):
        log.append({"p": c["apex"], "angle": c["angle"], "r": c["r"],
                    "status": "kept round", "why": "drawn as separate strokes"})


HALF_W = 2.0            # u — half the stroke width
FREE_END_EXTEND = 2.0   # u — a free end (touching nothing) is extended this far along its own
                        #     direction: a round cap reached 2 u past the end, and a flat end
                        #     would leave short strokes (a cross, a doorway) visibly shorter


def _end_box(E, d, e):
    """Ink a flat end adds when it grows by e beyond E (d points into the stroke)."""
    n = d * 1j * HALF_W
    a, b = E + n, E - n
    if e <= 1e-9:
        return LineString([(a.real, a.imag), (b.real, b.imag)])
    c, f = b - d * e, a - d * e
    return Polygon([(z.real, z.imag) for z in (a, b, c, f)])


def _circle_strokes(icon):
    """<circle>/<ellipse> elements as closed strokes of two half arcs (they carry no strokes in
    the icon model, but a stroke ending on a wheel touches it)."""
    out = []
    for el, _, _ in icon.items:
        if localname(el.tag) not in ("circle", "ellipse"):
            continue
        try:
            r0 = float(el.get("r") or 0)
            cx, cy = float(el.get("cx", 0)), float(el.get("cy", 0))
            rx, ry = float(el.get("rx") or r0), float(el.get("ry") or r0)
        except ValueError:
            continue
        if rx <= 0 or ry <= 0:
            continue
        a, b = complex(cx + rx, cy), complex(cx - rx, cy)
        out.append(Stroke(-1, "circle", [Arc(a, complex(rx, ry), 0, False, True, b),
                                         Arc(b, complex(rx, ry), 0, False, True, a)], True))
    return out


def extend_free_ends(icon, ext=FREE_END_EXTEND, fit=None):
    """SHARP output: give every free stroke end back the length its round cap used to add. A
    straight end is lengthened; a curved end gets a short straight continuing its tangent. Ends
    that touch another stroke (or a dot, or a circle) are left flush, and an end stops before its centreline
    runs within half a stroke of another stroke's. Two free ends that FACE each other (the other
    lies ahead, within 45 deg) grow together and keep the gap their round caps left: a dashed
    line keeps its dashes and gaps, the open top of a hexagon keeps its gap instead of closing
    to a crack. Every end is planned on the drawing as it is, then all are applied.
    fit (default icon.fit): the extension stops exactly where the flat end's corners would leave
    the keyshape (beyond what the input reached there), solved to 0.01 u."""
    fit = fit or icon.fit
    strokes = icon.strokes()
    dots = [Stroke(-1, "dot", [Line(c, c + 1e-6)], False) for c in icon.dot_at.values()] + \
        _circle_strokes(icon)                   # an end on a wheel touches it: stays flush
    free = []
    for st in strokes:
        if st.closed:
            continue
        for which in ("start", "end"):
            rest = st.segs[1:] if which == "start" else st.segs[:-1]
            others = [o for o in strokes if o is not st] + dots + \
                ([Stroke(st.sid, st.elem_id, rest, False)] if rest else [])
            E, d = _end_pt(st, which), _end_dir(st, which)
            if d is None or any(nearest_on_stroke(o, E, CONTACT_TOL) is not None for o in others):
                continue
            free.append((st, which, E, d, others))
    plans = []
    for st, which, E, d, others in free:
        # facing free ends, of other strokes or the other end of this one
        mates = [(F, dF) for o, w, F, dF, _ in free
                 if not (o is st and w == which) and 1e-9 < abs(F - E) <= 2 * HALF_W + 2 * ext
                 and angle_between(-d, F - E) <= 45.0]
        reach = 0.0
        for k in range(1, int(round(ext / 0.1)) + 1):
            e = k * 0.1
            Q = E - d * e                       # d points into the stroke: go the other way
            if any(nearest_on_stroke(o, Q, HALF_W) is not None for o in others):
                break                           # would run into another stroke's centreline
            if any(_end_box(E, d, e).distance(_end_box(F, dF, e))
                   < max(0.0, abs(F - E) - 2 * HALF_W) - 0.05 for F, dF in mates):
                break                           # would close the gap the round caps left
            reach = e
        n = d * 1j * HALF_W
        inside = lambda e: fit is None or \
            fit.past_near([E - d * e + n, E - d * e - n], E) <= keyshape_fit.KS_TOL   # noqa: E731
        if reach > 0 and not inside(reach):     # its flat corners would leave the keyshape:
            lo, hi = 0.0, reach                 # stop exactly at the keyshape edge
            if not inside(0.0):
                hi = 0.0
            for _ in range(20):
                if hi - lo < 0.005:
                    break
                mid = (lo + hi) / 2
                lo, hi = (mid, hi) if inside(mid) else (lo, mid)
            reach = round(lo, 2)
        if reach >= 0.01:
            plans.append((st, which, E, E - d * reach))
    for st, which, E, P in plans:
        i = 0 if which == "start" else -1
        seg = st.segs[i]
        if isinstance(seg, Line):
            st.segs[i] = Line(P, seg.end) if which == "start" else Line(seg.start, P)
        elif which == "start":
            st.segs.insert(0, Line(P, E))
        else:
            st.segs.append(Line(E, P))


TINY_LOOP = 3.0           # u — a closed loop that fits in this box (a pram's 2 u wheel drawn as
                          #     a lens of two arcs) is a dot: in the sharp output its pointed
                          #     ends would mitre into long spikes, so it becomes a square dot


TINY_DOT = 0.5            # u — an open stroke this short (M23.9998 17H24.0226) is a dot drawn
                          #     by its round caps: a flat cap would make it vanish


def dot_tiny_loops(icon):
    """SHARP output: elements made only of tiny closed loops, or of near-zero open strokes, are
    drawn as square dots at their centre (like zero-length dot paths)."""
    for el, strokes, _ in icon.items:
        if not strokes:
            continue
        boxes = [s.bbox() for st in strokes for s in st.segs]
        x0, x1 = min(b[0] for b in boxes), max(b[1] for b in boxes)
        y0, y1 = min(b[2] for b in boxes), max(b[3] for b in boxes)
        if all(st.closed for st in strokes):
            if x1 - x0 > TINY_LOOP or y1 - y0 > TINY_LOOP:
                continue
        elif any(st.closed for st in strokes) or x1 - x0 > TINY_DOT or y1 - y0 > TINY_DOT:
            continue
        icon.dot_at[id(el)] = complex((x0 + x1) / 2, (y0 + y1) / 2)
        strokes[:] = []


def butt_joints(icon):
    """Rebuild every meeting point for flat caps (see the block comment above)."""
    _close_near_loops(icon)
    _trim_overshoots(icon)
    for _ in range(BUTT_PASSES):
        strokes = icon.strokes()
        for k, st in enumerate(strokes):
            st.sid = k                       # find_nodes indexes strokes by sid
        nodes = find_nodes(strokes)
        changed = False
        for nd in nodes:
            changed |= _snap(strokes, nd)
        if changed:
            continue
        if any(_split(icon, strokes, nd) for nd in nodes):
            continue
        if any(_join(icon, strokes, nd) for nd in nodes):
            continue
        break
    for st in icon.strokes():
        merge_collinear(st)


def round_corner(icon, c, r):
    """Dispatch one detected sharp corner to the right fillet routine."""
    P = complex(*c["p"])
    if c["where"] == "with inner stroke":
        return round_inner(icon, P, c["angle"], r, c)
    fn = round_in_path if c["where"] == "in-path" else round_between
    return fn(icon, P, c["angle"], r)


# ---------------------------------------------------------------------------
# round -> sharp
# ---------------------------------------------------------------------------
def sharpen(icon, rec):
    start, end, apex = (complex(*rec[k]) for k in ("start", "end", "apex"))
    for st in icon.strokes():
        n = len(st.segs)
        for i0 in range(n):
            if not close(st.segs[i0].start, start, 1e-3):
                continue
            k, idx = i0, []
            for _ in range(n):
                idx.append(k)
                if close(st.segs[k].end, end, 1e-3):
                    break
                k = (k + 1) % n if st.closed else k + 1
                if k >= n:
                    idx = None
                    break
            else:
                idx = None
            if not idx or any(isinstance(st.segs[x], Line) for x in idx):
                continue
            old = [st.segs[x] for x in idx]
            new = [Line(start, apex), Line(apex, end)]
            if idx == sorted(idx) and idx[-1] - idx[0] == len(idx) - 1:
                st.segs[idx[0]:idx[-1] + 1] = new
            else:            # run wraps the closed seam: rotate so it is contiguous
                st.segs = st.segs[idx[0]:] + st.segs[:idx[0]]
                st.segs[0:len(idx)] = new
            _extend_to_apex(icon, st, old, apex)
            return True
    return False


def _extend_to_apex(icon, owner, old_segs, apex):
    """A stroke that ENDED on the removed arc (a shaft meeting a rounded arrow tip) would be
    left hanging inside the new sharp tip: extend it to the apex when it points there."""
    pts = [s.point(k / 24) for s in old_segs for k in range(25)]
    ends0 = (old_segs[0].start, old_segs[-1].end)
    for st in icon.strokes():
        if st is owner or st.closed:
            continue
        for which in ("start", "end"):
            seg = st.segs[0] if which == "start" else st.segs[-1]
            E, far = (seg.start, seg.end) if which == "start" else (seg.end, seg.start)
            if not isinstance(seg, Line) or any(close(E, q) for q in ends0):
                continue
            if min(abs(E - q) for q in pts) > CONTACT_TOL:
                continue
            d_in, d_apex = unit(E - far), unit(apex - E)
            if d_in is None or d_apex is None or angle_between(d_in, d_apex) > 30.0:
                continue
            if which == "start":
                st.segs[0] = Line(apex, seg.end)
            else:
                st.segs[-1] = Line(seg.start, apex)


# ---------------------------------------------------------------------------
JUNCTION_MATCH = 0.5   # u — an output junction this close to an input one is the same junction


def _still_meets(strokes, p, after):
    """SHARP output: an input junction the detector no longer reports is still connected when
    butt_joints() moved it (an end snapped onto the centreline it stopped short of) or snapped
    it into a corner (a bar's T 1 u from its baseline's end is now the corner of one path), or
    when two separate segments still meet there (an ear arc crossing
    the cheek it was joined to: the detector skips crossings of neighbouring segments)."""
    P = complex(*p)
    if any(abs(P - complex(*c["p"])) <= CONTACT_TOL + 0.5
           for c in after["sharp"] + after["junction"]):
        return True
    hits = sum(1 for st in strokes for seg in st.segs
               if nearest_on_stroke(Stroke(0, "", [seg], False), P, 0.3) is not None)
    if hits >= 2:
        return True
    # a tiny loop drawn as a square dot: a stroke meeting it still meets it (pram wheel + leg)
    dots = [st.segs[0].start for st in strokes if st.elem_id == "dot"]
    return any(abs(P - c) <= HALF_W + 0.5 for c in dots) and hits >= 1


def check_output(before, after, mode, log, strokes=None):
    """Compare re-detection of an output with the input's detection.
    fail     — an input junction disappeared (a stroke came loose), a NEW crossing appeared
               (an arc cuts through a stroke), or corners are left in the wrong state
    contact  — a new T / meeting appeared (a sharpened leg now runs along another stroke)
    ok       — neither
    strokes  — the SHARP output's strokes: a junction butt_joints() turned into a corner, or
               one the detector can't see inside a single path, is not lost"""
    near = lambda p, L: any(abs(complex(*p) - complex(*q["p"])) <= JUNCTION_MATCH for q in L)
    lost = [j["p"] for j in before["junction"] if not near(j["p"], after["junction"])]
    if strokes is not None:
        lost = [p for p in lost if not _still_meets(strokes, p, after)]
    new = [j for j in after["junction"] if not near(j["p"], before["junction"])]
    crossings = [j["p"] for j in new if j["type"] == "crossing"]
    # an inner stroke cut back onto its corner's new arc (an arrow shaft) is an expected T
    expected = [(complex(*e["p"]), 2.0 * e["r"]) for e in log
                if e.get("inner") and e["status"] == "rounded"]
    contacts = [j["p"] for j in new if j["type"] != "crossing"
                and not any(abs(complex(*j["p"]) - q) <= d for q, d in expected)]
    if mode == "round":
        wrong = len(after["sharp"]) - sum(e["status"] in ("skipped", "kept sharp") for e in log)
    else:
        wrong = len(after["round"]) - sum(e["status"] == "kept round" for e in log)
    status = "fail" if lost or crossings or wrong > 0 else ("contact" if contacts else "ok")
    return {"status": status, "lost": lost, "crossings": crossings, "contacts": contacts,
            "wrong_state": max(0, wrong)}


def parse_bands(spec):
    """'60:1,75:2,105:4,180:6' -> [(60.0, 1), (75.0, 2), (105.0, 4), (180.0, 6)]"""
    out = []
    for part in spec.split(","):
        bound, r = part.split(":")
        out.append((float(bound), int(r)))
    return sorted(out)


def band_radius(angle, bands):
    """First bound inclusive, later bounds exclusive (as the 1024 pipeline's radius_for: 60 -> first
    band, 75 -> third... a grid-snapped 90 sits mid-band either way)."""
    for i, (bound, r) in enumerate(bands):
        if (angle <= bound) if i == 0 else (angle < bound):
            return r
    return bands[-1][1]


def group_angles(angles, tol=GROUP_TOL):
    """Sorted greedy walk; an angle joins the current group while within `tol` of the group's
    running mean. Returns {corner_index: group_mean}."""
    order = sorted(range(len(angles)), key=lambda i: angles[i])
    groups = []
    for i in order:
        if groups and abs(angles[i] - sum(angles[j] for j in groups[-1]) / len(groups[-1])) <= tol:
            groups[-1].append(i)
        else:
            groups.append([i])
    return {i: sum(angles[j] for j in g) / len(g) for g in groups for i in g}


CURVED_SIDE_MAX_R = 5.0   # u — a round corner with ONE curved side is still a corner (and is
                          #     sharpened) when it is a small fillet: a laptop base's r 2 corner
                          #     on a barely curved side, a battery nub's r 4 corner, a bow's
                          #     wing tip. Larger ones (a shoulder flowing out of a curved neck,
                          #     a shield's flank, r 8-23) are part of the curve and stay.


def _radius_at(seg, t):
    if isinstance(seg, Line):
        return float("inf")
    try:
        k = seg.curvature(t)
    except (ValueError, ZeroDivisionError):
        return None
    return float("inf") if k < 1e-9 else 1.0 / k


FILLET_MAX_TURN = 120.0   # deg — ...and is a corner, not a hook: a helmet's ear guard curling
                          #     back 135 deg into its brim stays a curve
FILLET_MIN_TURN = 60.0    # deg — a small fillet makes the corner by itself: one r 4 arc turning
                          #     90 deg (a bow's wing tip) is a corner; a bracket corner drawn as an
                          #     r 5 arc then an r 4 arc (about 40 + 50 deg) is one rounded corner


def sharpen_fillet_arc(icon, c):
    """A round corner with a curved side whose rounding is ONE small curve segment (an arc or a
    Bezier, radius <= CURVED_SIDE_MAX_R, turning >= FILLET_MIN_TURN by itself, one way) with a
    straight on at least one side: replace just that segment by its two tangent lines meeting
    at a point (a laptop base's corner, a battery nub, a bow's wing tip). The curve beside it is
    kept. Returns the new point or None."""
    run = []                                # the corner's own segments (start, end)
    for d in c["segs"]:
        try:
            ps = parse_path(d)
            run.append((ps[0].start, ps[-1].end))
        except Exception:
            pass
    for st in icon.strokes():
        for i, seg in enumerate(st.segs):
            if isinstance(seg, Line):
                continue
            if not any(close(seg.start, a, 1e-3) and close(seg.end, b, 1e-3) for a, b in run):
                continue                    # not one of this corner's own segments
            j, k = st.prev(i), st.next(i)
            if j is None or k is None:
                continue
            if not (isinstance(st.segs[j], Line) or isinstance(st.segs[k], Line)):
                continue
            radii = [_radius_at(seg, t / 16) for t in range(17)]
            if any(rr is None for rr in radii) or min(radii) > CURVED_SIDE_MAX_R:
                continue
            total, inflect = seg_turn(seg)
            if inflect or not FILLET_MIN_TURN <= abs(total) <= FILLET_MAX_TURN:
                continue
            u0, u1 = tangent(seg, 0.0), tangent(seg, 1.0)
            hit = line_hit(seg.start, u0, seg.end, u1) if u0 is not None and u1 is not None else None
            if hit is None or hit[0] <= 1e-6 or hit[1] <= 1e-6 or \
                    abs(hit[2] - seg.start) > 3 * CURVED_SIDE_MAX_R:
                continue
            X = hit[2]
            st.segs[i:i + 1] = [Line(seg.start, X), Line(X, seg.end)]
            return X
    return None


def _point_past_keyshape(fit, c, limit):
    """Would sharpening round corner c put its point (mitre tip, or bevel corners) past the
    keyshape, further than the drawn round corner reached?"""
    if fit is None:
        return False
    start, end, apex = (complex(*c[k]) for k in ("start", "end", "apex"))
    u_in, u_out = unit(apex - start), unit(end - apex)
    if u_in is None or u_out is None:
        return False
    tip = keyshape_fit.mitre_tip(apex, u_in, u_out, limit)
    if tip is None:
        return False
    reach = abs(apex - (start + end) / 2) + keyshape_fit.NEAR      # the drawn arc is in here
    return fit.past(tip[0], apex, reach)


def _soft(c):
    """A big round corner gentle enough to sharpen (SOFT_GAP): its point sits close to the curve."""
    if SOFT_GAP <= 0 or c["size"] > CORNER_MAX_R:
        return False
    gap = c["r"] * (1 / math.sin(math.radians(max(c["angle"], 1.0)) / 2) - 1)
    return gap <= SOFT_GAP


def make_sharp(path, sharpen_curved=False, keep_big=True, fit=None, limit=MITER_LOW, keep=(), max_r=None,
               force=(), crossed=()):
    """Round corners whose two sides are straight lines -> their apex; so is a small fillet
    (r <= CURVED_SIDE_MAX_R) with one curved side. A round corner wider than BIG_ROUND_R, or a
    larger one with a curved side, is a designed curve and stays as drawn unless sharpen_curved.
    With fit (keyshape_fit.Fit), a round corner whose point would poke past the keyshape stays
    round as drawn. max_r: a round corner wider than this is not a corner (detect() calls it a
    curve) and stays as drawn. Returns (icon, log, detection)."""
    res = detect(path, max_r)
    icon = Icon(path)
    icon.corner_pts = [complex(*c["p"]) for c in res["sharp"]]
    for st in icon.strokes():
        merge_collinear(st)
    log = []
    for c in res["round"]:
        if keep_big and not sharpen_curved and max_r is None and c["size"] > BIG_ROUND_R and \
                not _soft(c) and \
                not any(close(complex(*c["apex"]), complex(*k), 0.05) for k in force):
            log.append({"p": c["apex"], "angle": c["angle"], "r": c["r"],
                        "status": "kept round", "why": "too large for a corner"})
            continue
        if any(close(complex(*c["apex"]), complex(*k), 0.05) for k in crossed):
            log.append({"p": c["apex"], "angle": c["angle"], "r": c["r"],
                        "status": "kept round", "why": "sharp point would cross a stroke"})
            continue
        if any(close(complex(*c["apex"]), complex(*k), 0.05) for k in keep):
            log.append({"p": c["apex"], "angle": c["angle"], "r": c["r"],
                        "status": "kept round", "why": "rounding past keyshape"})
            continue
        if _point_past_keyshape(fit, c, limit):
            log.append({"p": c["apex"], "angle": c["angle"], "r": c["r"],
                        "status": "kept round", "why": "point past keyshape"})
            continue
        if not sharpen_curved and c["arms"] != ["line", "line"]:
            P = sharpen_fillet_arc(icon, c)
            if P is not None:
                log.append({"p": [fmt(P.real), fmt(P.imag)], "angle": c["angle"], "r": c["r"],
                            "status": "sharpened", "why": "small fillet beside a curve"})
            else:
                log.append({"p": c["apex"], "angle": c["angle"], "r": c["r"],
                            "status": "kept round", "why": "curved side"})
            continue
        ok = sharpen(icon, c)
        log.append({"p": c["apex"], "angle": c["angle"], "r": c["r"],
                    "status": "sharpened" if ok else "skipped"})
    for c in res["sharp"]:
        log.append({"p": c["p"], "angle": c["angle"], "status": "kept sharp"})
    for c in res["curve"]:                 # too wide for a corner: kept as drawn
        if c.get("big"):
            log.append({"p": c["apex"], "angle": c["angle"], "r": c["r"], "status": "kept round",
                        "why": "too large for a corner", "big": True})
    for st in icon.strokes():
        merge_collinear(st)
    return icon, log, res


def _fits(icon, c, r):
    """Dry run: does a radius-r fillet fit corner c of `icon` (a fresh copy is modified)?"""
    if "curve" not in c["arms"] and r > c["r_max"] + 1e-6:
        return False
    # dry run even on straight sides: r_max splits a side shared with a ROUND neighbour half and
    # half, but a kept round corner keeps its whole drawn arc
    trial = copy.deepcopy(icon)
    ok, _ = round_corner(trial, c, r)
    return bool(ok)


def _samples_near(icon, P, reach, n=24):
    return [q for st in icon.strokes() for sg in st.segs for q in (sg.point(k / n) for k in range(n + 1))
            if abs(q - P) <= reach]


def _band_past_keyshape(icon, c, r, was):
    """Round output: does re-rounding corner c with band radius r (smaller than the drawn
    radius `was`) poke past the keyshape, further than the drawn corner reached?"""
    if icon.fit is None or was is None or r >= was - 1e-6:
        return False
    trial = copy.deepcopy(icon)
    ok, _ = round_corner(trial, c, r)
    if not ok:
        return False
    P = complex(*c["p"])
    reach = was / math.sin(math.radians(max(c["angle"], 1.0)) / 2) + 1.0
    return icon.fit.round_ink_past(_samples_near(trial, P, reach), P, reach)


CROSS_NEAR = 1.0          # u — a new crossing this close to a sharpened corner's reach is that
                          #     corner's doing (a vr headset's band runs down through the visor's
                          #     r 6 top corners: the sharp point pokes through the band)


def _sharp_output(src, name, sharpen_all, fit, limit, miter, tmp_dir, crossed=(), tip_fit=None, shift=True):
    """SHARP output of one icon -> (icon, log, res, svg, out_strokes, after, check)."""
    icon, log, res = make_sharp(src, sharpen_all, fit=fit, limit=limit,
                                keep_big=name not in SHARP_EVERY_CORNER,
                                force=SHARP_THESE_CORNERS.get(name, ()), crossed=crossed)
    icon.fit = fit
    dot_tiny_loops(icon)
    butt_joints(icon)
    sharpen_joined_rounds(icon, log, res, tmp_dir)
    extend_free_ends(icon, fit=tip_fit)
    log_joined_rounds(icon, log, res, tmp_dir)
    apply_miter(icon, res, miter)
    if miter == "shift" and shift:
        shift_tips(icon, log, limit, tip_fit)
    cut_tips(icon, log, limit, tip_fit, TIP_OK if miter == "keyshape" else 0.0, ends=miter in KS_MODES)
    svg = icon.svg({**SHARP_STYLE, "stroke-miterlimit": "4" if miter in ("4",) + KS_MODES else "2"})
    out_strokes = icon.strokes() + [Stroke(-1, "dot", [Line(c, c + 1e-6)], False)
                                    for c in icon.dot_at.values()]
    icon.tips = []                         # tip copies overlap their own path: check the
    check_src = os.path.join(tmp_dir, "sharp-check.svg")   # drawing without them
    with open(check_src, "w", encoding="utf-8") as fh:
        fh.write(icon.svg(SHARP_STYLE))
    after = detect(check_src)
    return icon, log, res, svg, out_strokes, after, check_output(res, after, "sharp", log, out_strokes)


def _crossed_corners(log, check):
    """Apexes of sharpened round corners a new crossing in the sharp output sits on."""
    out = []
    for e in log:
        if e.get("status") != "sharpened" or not e.get("r"):
            continue
        P = complex(*e["p"])
        reach = e["r"] / math.tan(math.radians(max(e["angle"], 1.0)) / 2) + CROSS_NEAR
        if any(abs(complex(*q) - P) <= reach for q in check.get("crossings", [])):
            out.append(tuple(e["p"]))
    return out


def make_round(path, bands, group_tol, fallback, tmp_dir, sharpen_curved=False, fit=None, keep=(), max_r=None,
               no_room=()):
    """Sharpen every straight-sided corner, then round every sharp corner with a whole-number
    band radius. Round corners with a curved side are kept as drawn. With fit, a corner whose band
    radius would poke past the keyshape is not re-rounded: it keeps the corner as drawn (a
    second pass with those apexes in `keep`, which make_sharp leaves round). So does a corner
    drawn round that has no room for even r 1 once sharpened (`no_room`: a vr headset's band
    runs down through the visor's top corners) — it would otherwise come out square."""
    # every straight-sided corner, big ones too: the round output re-rounds them all with the
    # band radii (BIG_ROUND_R only keeps big rounds in the SHARP output)
    sharp_icon, _, res0 = make_sharp(path, sharpen_curved, keep_big=False, keep=keep, max_r=max_r)
    tmp = os.path.join(tmp_dir, os.path.basename(path))
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(sharp_icon.svg())
    res = detect(tmp, max_r)                # every corner is sharp here, with true r_max
    icon = Icon(tmp)
    icon.fit = fit
    icon.corner_pts = [complex(*c["p"]) for c in res["sharp"]]
    icon.stop_pts = [complex(*j["p"]) for j in res["junction"]]
    for st in icon.strokes():
        merge_collinear(st)
    drawn = {tuple(c["apex"]): c["r"] for c in res0["round"]}
    corners = res["sharp"]
    gmean = group_angles([c["angle"] for c in corners], group_tol)
    plan = []
    for i, c in enumerate(corners):
        if c["arms"] == ["curve", "curve"]:
            plan.append((c, None, 0, 0, gmean[i]))   # between two curves: part of the curve
            continue
        band = band_radius(gmean[i], bands)
        fit = next((k for k in range(band, MIN_RADIUS - 1, -1) if _fits(icon, c, k)), 0)
        r = fit if fallback == "reduce" else (band if fit == band else 0)
        plan.append((c, band, fit, r, gmean[i]))
    if icon.fit is not None and not keep:     # band radius pokes past the keyshape: keep as drawn
        out = [tuple(c["p"]) for c, band, _, r, _ in plan if band is not None and r >= MIN_RADIUS and
               _band_past_keyshape(icon, c, r, next((v for k, v in drawn.items()
                                                     if close(complex(*k), complex(*c["p"]))), None))]
        if out:
            return make_round(path, bands, group_tol, fallback, tmp_dir, sharpen_curved, fit, keep=out,
                              max_r=max_r)
    stuck = [tuple(c["p"]) for c, band, _, r, _ in plan if band is not None and r < MIN_RADIUS and
             any(close(complex(*k), complex(*c["p"])) for k in drawn) and tuple(c["p"]) not in keep]
    if stuck:                               # drawn round, no room to re-round: keep as drawn
        return make_round(path, bands, group_tol, fallback, tmp_dir, sharpen_curved, fit,
                          keep=tuple(keep) + tuple(stuck), max_r=max_r, no_room=tuple(no_room) + tuple(stuck))
    log = []
    for c, band, fit, r, gm in plan:
        P = complex(*c["p"])
        was = next((v for k, v in drawn.items() if close(complex(*k), P)), None)
        entry = {"p": c["p"], "angle": c["angle"], "group": round(gm, 1), "band": band,
                 "curved": "curve" in c["arms"], "was_round": was,
                 "inner": c["where"] == "with inner stroke"}
        if band is None:
            entry.update(status="kept sharp", why="curve + curve")
        elif r < MIN_RADIUS:
            entry.update(status="skipped", why=f"band r {band} doesn't fit" if fit else "no room for r 1")
        else:
            ok, _ = round_corner(icon, c, r)
            entry.update(status="rounded" if ok else "skipped", r=r, reduced=r < band,
                         consumed=ok == "consumed")
            if not ok:
                entry["why"] = "geometry"
        log.append(entry)
    for c in res["round"]:                  # curved-side round corners, kept as drawn
        nr = any(close(complex(*c["apex"]), complex(*k), 0.6) for k in no_room)
        ks = not nr and any(close(complex(*c["apex"]), complex(*k), 0.6) for k in keep)
        log.append({"p": c["apex"], "angle": c["angle"], "group": None, "band": None,
                    "curved": not (ks or nr), "was_round": c["r"], "status": "kept round", "r": c["r"],
                    "why": "no room to re-round" if nr else "band radius past keyshape" if ks else "curved side",
                    **({"keyshape": True} if ks else {})})
    for c in res0["curve"]:                 # too wide for a corner: kept as drawn
        if c.get("big"):
            log.append({"p": c["apex"], "angle": c["angle"], "group": None, "band": None,
                        "curved": False, "was_round": c["r"], "status": "kept round", "r": c["r"],
                        "why": "too large for a corner", "big": True})
    for st in icon.strokes():
        merge_collinear(st)
    return icon.svg(), log, res0


def _acute_joins(st):
    """[(i, vertex)] joins of a stroke where the mitre limit matters: interior angle between
    the two limits (wider: always a point; narrower than limit 4: always cut)."""
    lo = math.degrees(2 * math.asin(1 / MITER_HIGH))       # 28.96
    hi = math.degrees(2 * math.asin(1 / MITER_LOW))        # 60
    out = []
    for i in range(st.n()):
        j = st.prev(i)
        if j is None:
            continue
        a, b = tangent(st.segs[j], 1.0), tangent(st.segs[i], 0.0)
        if a is None or b is None:
            continue
        inner = 180.0 - angle_between(a, b)
        if lo - 1e-6 <= inner < hi:
            out.append((j, i))
    return out


def _tip_d(st, j, i):
    """d of a short copy of the corner between segments j and i (MITER_TIP_ARM each way)."""
    a, b = st.segs[j], st.segs[i]
    pa = a.point(max(0.0, 1 - MITER_TIP_ARM / a.length())) if a.length() > 0 else a.end
    pb = b.point(min(1.0, MITER_TIP_ARM / b.length())) if b.length() > 0 else b.start
    p = lambda z: f"{_n(z.real)} {_n(z.imag)}"
    return f"M{p(pa)}L{p(a.end)}L{p(pb)}"


def apply_miter(icon, res, mode):
    """Set the mitre limit for --miter mode: the root's for 2 / 4, per path for mixed."""
    if mode != "mixed":
        return
    sharp_born = [complex(*c["p"]) for c in res["sharp"]]
    born = lambda P: any(abs(P - q) <= MITER_MATCH for q in sharp_born)
    groups = [(id(el), el.get("id") or "path", ss) for el, ss, _ in icon.items if ss]
    groups += [(("extra", k), f"corner-fillet-{k}", [s]) for k, s in enumerate(icon.extra)]
    for key, eid, ss in groups:
        joins = [(st, j, i, born(st.segs[i].start)) for st in ss for j, i in _acute_joins(st)]
        if not joins or not any(b for *_, b in joins):
            continue                                   # nothing sharp-born to keep: limit 2
        if all(b for *_, b in joins):
            icon.el_attrs[key] = {"stroke-miterlimit": _n(MITER_HIGH)}
        else:
            icon.tips += [(eid, _tip_d(st, j, i)) for st, j, i, b in joins if b]


def _cross(a, b):
    return a.real * b.imag - a.imag * b.real


def _meet(P, u, Q, v):
    """Intersection of the line through P along u with the line through Q along v (None: parallel)."""
    den = _cross(u, v)
    if abs(den) < 1e-6:
        return None
    return P + u * (_cross(Q - P, v) / den)


def shift_tips(icon, log, limit, fit):
    """SHARP output (--miter shift): a corner whose mitre point pokes past the keyshape is moved
    inward just far enough for the full point to touch the keyshape edge, KEEPING ITS ANGLE: both
    arms keep their direction and slide parallel, each arm's far end sliding along the straight
    segment beyond it (so that segment keeps its direction too). An arm that can't slide (it ends
    on a free end or another stroke, or the segment beyond runs straight on) stays on its line and
    the corner moves back along it; with both arms held, the corner stays and cut_tips slices it."""
    if fit is None:
        return
    strokes = icon.strokes()
    for st in strokes:
        others = [q for o in strokes if o is not st for sg in o.segs
                  for q in (sg.point(k / 24) for k in range(25))]
        held = lambda P, r=SHIFT_HOLD: any(abs(q - P) < r for q in others)   # noqa: E731
        for i in range(st.n()):
            j = st.prev(i)
            if j is None or j == i or not isinstance(st.segs[j], Line) or not isinstance(st.segs[i], Line):
                continue
            A, V, B = st.segs[j].start, st.segs[i].start, st.segs[i].end
            u_in, u_out = keyshape_fit.unit(V - A), keyshape_fit.unit(B - V)
            if u_in is None or u_out is None or held(V, SHIFT_NEAR):
                continue
            tip = keyshape_fit.mitre_tip(V, u_in, u_out, limit)
            if tip is None:
                continue
            allow = fit.allowance(V)
            past = lambda D: max(fit.excess(q + D) for q in tip[0]) - allow   # noqa: E731
            by = past(0)
            if by <= keyshape_fit.KS_TOL:
                continue
            # which arms can slide: the segment beyond is a straight line at an angle to the arm
            k, m = st.prev(j), st.next(i)
            slide_in = (k is not None and k not in (i, j) and isinstance(st.segs[k], Line) and not held(A)
                        and keyshape_fit.unit(st.segs[k].end - st.segs[k].start) is not None
                        and abs(_cross(u_in, keyshape_fit.unit(st.segs[k].end - st.segs[k].start))) > 0.05)
            slide_out = (m is not None and m not in (i, j) and isinstance(st.segs[m], Line) and not held(B)
                         and keyshape_fit.unit(st.segs[m].end - st.segs[m].start) is not None
                         and abs(_cross(u_out, keyshape_fit.unit(st.segs[m].end - st.segs[m].start))) > 0.05)
            if slide_in and slide_out:
                d = -keyshape_fit.unit(u_in - u_out)        # straight inward, along the bisector
            elif slide_out:
                d = -u_in                                    # back along the held incoming arm
            elif slide_in:
                d = u_out                                    # back along the held outgoing arm
            else:
                continue

            def build(t):
                W = V + d * t
                A2 = _meet(W, u_in, st.segs[k].start, st.segs[k].end - st.segs[k].start) if slide_in else A
                B2 = _meet(W, u_out, st.segs[m].start, st.segs[m].end - st.segs[m].start) if slide_out else B
                if A2 is None or B2 is None:
                    return None
                # every touched segment keeps its direction and some length
                if ((W - A2).real * u_in.real + (W - A2).imag * u_in.imag) < 0.5 or \
                        ((B2 - W).real * u_out.real + (B2 - W).imag * u_out.imag) < 0.5:
                    return None
                if slide_in:
                    ks = st.segs[k].start
                    if abs(A2 - ks) < 0.5 or ((A2 - ks) * (st.segs[k].end - ks).conjugate()).real <= 0:
                        return None
                if slide_out:
                    me = st.segs[m].end
                    if abs(me - B2) < 0.5 or ((me - B2) * (me - st.segs[m].start).conjugate()).real <= 0:
                        return None
                return W, A2, B2

            hi = 0.5
            while past(d * hi) > keyshape_fit.KS_TOL and hi < 48:
                hi *= 1.5
            lo = 0.0
            for _ in range(30):
                mid = (lo + hi) / 2
                if past(d * mid) > keyshape_fit.KS_TOL:
                    lo = mid
                else:
                    hi = mid
            got = build(hi)
            if got is None:
                continue                                     # no room to move that far: slice
            W, A2, B2 = got
            if slide_in:
                st.segs[k] = Line(st.segs[k].start, A2)
            st.segs[j] = Line(A2, W)
            st.segs[i] = Line(W, B2)
            if slide_out:
                st.segs[m] = Line(B2, st.segs[m].end)
            log.append({"p": [fmt(V.real), fmt(V.imag)], "status": "tip shifted", "by": round(hi, 2),
                        "to": [fmt(W.real), fmt(W.imag)], "past": round(by, 2),
                        "arms": "both" if slide_in and slide_out else "one"})


CUT_BLEED = 0.05         # u — a cut grows this far past the ink it removes: a clip hole whose
                         #     sides lie exactly on the stroke's edges leaves anti-aliased
                         #     hairlines in browsers (the keyshape-side edge stays exact)


def cut_tips(icon, log, limit, fit=None, ok=0.0, ends=False):
    """SHARP output: a join whose ink pokes past the keyshape (further than the input reached
    there, by more than `ok` u) is cut flat along the keyshape edge, by a clip path: all ink
    around the join outside the keyshape goes, the rest of the point stays. fit: the keyshape to cut against (default: icon.fit). ends: also slice
    flat stroke ends whose corners leave the keyshape (no tolerance)."""
    fit = fit or icon.fit
    if fit is None:
        return
    groups = [(icon.el_attrs.get(id(el), {}), ss) for el, ss, _ in icon.items if ss]
    groups += [(icon.el_attrs.get(("extra", k), {}), [s]) for k, s in enumerate(icon.extra)]
    cuts = []
    for attrs, ss in groups:
        lim = float(attrs.get("stroke-miterlimit", limit))
        for st in ss:
            for i in range(st.n()):
                j = st.prev(i)
                if j is None:
                    continue
                u_in, u_out = tangent(st.segs[j], 1.0), tangent(st.segs[i], 0.0)
                if u_in is None or u_out is None:
                    continue
                V = st.segs[i].start
                tip = keyshape_fit.mitre_tip(V, u_in, u_out, lim)
                if tip is None:
                    continue
                # the join's outer ink: the mitre point, or the two bevel corners, and the arms'
                # outer corners at the join (a corner sharpened onto the keyshape edge pokes out
                # with its whole stroke width, not only its point)
                pts = list(tip[0]) + ([complex(x, y) for x, y in tip[1].exterior.coords] if tip[1] else [])
                by = fit.past_near(pts, V)
                if by <= max(ok, keyshape_fit.KS_TOL):   # within reach: keep the point
                    continue
                reach = max(abs(q - V) for q in pts) + CUT_BLEED
                cut = Point(V.real, V.imag).buffer(reach, quad_segs=32).difference(fit.region_near(V))
                if cut.area > 1e-3:
                    cuts.append(cut)
                    log.append({"p": [fmt(V.real), fmt(V.imag)], "status": "tip cut",
                                "by": round(by, 2),
                                "angle": round(180 - math.degrees(math.acos(max(-1, min(1, (u_in.conjugate() * u_out).real)))), 1)})
    if ends:                                    # flat ends: their corners never leave the
        for st in (st for _, ss in groups for st in ss if not st.closed):   # keyshape
            for which in ("start", "end"):
                E, d = _end_pt(st, which), _end_dir(st, which)
                if d is None:
                    continue
                n = d * 1j * HALF_W
                if fit.past_near([E + n, E - n], E) <= keyshape_fit.KS_TOL:
                    continue
                sq = Polygon([(z.real, z.imag) for z in (E + n, E - n, E - n + d * 2 * HALF_W,
                                                         E + n + d * 2 * HALF_W)])
                cut = sq.buffer(CUT_BLEED, join_style="mitre").difference(fit.region_near(E))
                if cut.area > 1e-3:
                    cuts.append(cut)
                    log.append({"p": [fmt(E.real), fmt(E.imag)], "status": "end cut",
                                "by": round(fit.past_near([E + n, E - n], E), 2)})
    if cuts:
        icon.clip = keyshape_fit.clip_d(cuts)


def input_fit(src, rec):
    """keyshape_fit.Fit for the input at src and its keyshape record (None: no keyshape)."""
    if not rec or not rec.get("keyshape"):
        return None
    inp = Icon(src)
    circles = []
    for el, ss, _ in inp.items:
        if localname(el.tag) in ("circle", "ellipse"):
            try:
                r0 = float(el.get("r") or 0)
                circles.append((float(el.get("cx", 0)), float(el.get("cy", 0)),
                                float(el.get("rx") or r0), float(el.get("ry") or r0)))
            except ValueError:
                pass
    return keyshape_fit.Fit(rec, inp.strokes(), circles)


def process_icon(args):
    """Worker: build both outputs of one icon and check them. -> (name, entry, error)."""
    src, name, out, bands, group_tol, fallback, sharpen_all, modes, miter, ks, max_r, ks_tip = args
    tmp_dir = tempfile.mkdtemp(prefix="corner48_")     # per icon: workers never share files
    try:
        entry = {}
        fit = input_fit(src, ks)
        limit = MITER_HIGH if miter in ("4",) + KS_MODES else MITER_LOW
        tip_fit = (fit or input_fit(src, ks_tip)) if miter in KS_MODES else None
        for mode in modes:
            if mode == "round":
                svg, log, res = make_round(src, bands, group_tol, fallback, tmp_dir, sharpen_all, fit,
                                           max_r=max_r)
            else:
                # the sharp output keeps rounds wider than BIG_ROUND_R (6) as drawn: lower
                # than max_r, which only the round output uses
                icon, log, res, svg, out_strokes, after, check = _sharp_output(
                    src, name, sharpen_all, fit, limit, miter, tmp_dir, tip_fit=tip_fit)
                crossed = _crossed_corners(log, check)
                if crossed:                        # a sharpened point another stroke crosses
                    icon, log, res, svg, out_strokes, after, check = _sharp_output(  # stays round
                        src, name, sharpen_all, fit, limit, miter, tmp_dir, crossed, tip_fit)
                if miter == "shift" and check["status"] == "fail" and \
                        any(e["status"] == "tip shifted" for e in log):
                    # a moved corner tilts its arms into another stroke: slice this icon instead
                    icon, log, res, svg, out_strokes, after, check = _sharp_output(
                        src, name, sharpen_all, fit, limit, miter, tmp_dir, crossed, tip_fit, shift=False)
                    log.append({"status": "shift undone", "why": "moving a corner broke the drawing"})
                with open(os.path.join(out, mode, name), "w", encoding="utf-8") as fh:
                    fh.write(svg)
                entry[mode] = {"log": log, "after": {k: len(after[k]) for k in
                                                     ("sharp", "round", "junction", "kink", "curve")},
                               "check": check}
                continue
            dst = os.path.join(out, mode, name)
            with open(dst, "w", encoding="utf-8") as fh:
                fh.write(svg)
            after = detect(dst)           # re-detection check of the output
            entry[mode] = {"log": log, "after": {k: len(after[k]) for k in
                                                 ("sharp", "round", "junction", "kink", "curve")},
                           "check": check_output(res, after, mode, log)}
        entry["before"] = {k: len(res[k]) for k in ("sharp", "round", "junction", "kink", "curve")}
        return name, entry, None
    except Exception as e:
        return name, None, f"{type(e).__name__}: {e}"
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def main(argv=None):
    global BIG_ROUND_R, JOINED_MAX_R, SOFT_GAP
    ap = argparse.ArgumentParser(description="Make every detected corner round, or every one sharp.")
    ap.add_argument("--input", default=DEFAULT_INPUT)
    ap.add_argument("--out", default=OUT_DIR)
    ap.add_argument("--files", nargs="*")
    ap.add_argument("--sample", type=int, default=0)
    ap.add_argument("--seed", type=int, default=48)
    ap.add_argument("--bands", default=DEFAULT_BANDS,
                    help="angle:radius bands by group-mean angle, whole-number radii")
    ap.add_argument("--group-tol", type=float, default=GROUP_TOL)
    ap.add_argument("--sharpen", choices=("straight", "all"), default="straight",
                    help="which round corners are sharpened: only those whose two sides are "
                         "straight lines (default), or also those with a curved side")
    ap.add_argument("--fallback", choices=("reduce", "skip"), default="reduce",
                    help="corner that can't hold its band radius: largest whole radius that "
                         "fits (reduce) or leave it sharp (skip)")
    ap.add_argument("--jobs", type=int, default=os.cpu_count() or 1,
                    help="parallel worker processes (default: all CPU cores; 1 = no pool)")
    ap.add_argument("--mode", choices=("both", "round", "sharp"), default="both",
                    help="build only one output (quick checks into a scratch --out; the review "
                         "page needs both)")
    ap.add_argument("--reviewed", action="store_true",
                    help="only the icons in locks.json (locked + pending): a quick check that "
                         "a change keeps every reviewed icon as approved")
    ap.add_argument("--ready", action="store_true",
                    help="only icons NOT in locks.json (not reviewed yet): locked and pending "
                         "icons keep the outputs they were reviewed on")
    ap.add_argument("--miter", choices=MITER_MODES, default="slice",
                    help="sharp output: keep points down to 29 deg unless one reaches more than "
                         f"{TIP_OK:g} u past the keyshape, then cut it flat there (keyshape); cut "
                         "every point flat where the keyshape ends (slice); move a point's corner "
                         "inward until it touches the keyshape (shift); cut "
                         "corners narrower than 60 deg flat (2); keep points down to 29 deg (4); "
                         "or keep points only where the input was already sharp (mixed); "
                         "default slice (manager's pick, 2026-10-06)")
    ap.add_argument("--keyshapes", default=None,
                    help="keyshapes.json from core/keyshape.py (default: <out>/keyshapes.json): "
                         "outputs keep their ink inside the keyshape (README: Keyshape fit)")
    ap.add_argument("--keyshape-fit", action="store_true",
                    help="keep the outputs' ink inside the keyshape (off by default for now)")
    ap.add_argument("--corner-max-r", type=float, default=CORNER_MAX_R,
                    help="ROUND output: a round corner wider than this (u) is a designed curve, "
                         "not a corner, and keeps its drawn shape instead of a band radius "
                         f"(default {CORNER_MAX_R:g}; the sharp output keeps rounds wider than "
                         f"{BIG_ROUND_R:g})")
    ap.add_argument("--big-round-r", type=float, default=None,
                    help=f"sharp output: round corners up to this size are sharpened (default {BIG_ROUND_R:g})")
    ap.add_argument("--soft-gap", type=float, default=None,
                    help="sharp output: also sharpen bigger corners (up to the corner limit) whose point "
                         f"sits within this many u of the drawn curve (default {SOFT_GAP:g}; 0: off)")
    cfg = ap.parse_args(argv)
    if cfg.big_round_r is not None:              # workers read them from the environment
        os.environ["CORNER48_BIG_ROUND_R"] = str(cfg.big_round_r)
        BIG_ROUND_R = JOINED_MAX_R = cfg.big_round_r
    if cfg.soft_gap is not None:
        os.environ["CORNER48_SOFT_GAP"] = str(cfg.soft_gap)
        SOFT_GAP = cfg.soft_gap
    modes = ("round", "sharp") if cfg.mode == "both" else (cfg.mode,)

    names = cfg.files or sorted(n for n in os.listdir(cfg.input) if n.lower().endswith(".svg"))
    if cfg.reviewed or cfg.ready:
        reviewed = set(locks.load())
        names = [n for n in names if (n in reviewed) == cfg.reviewed]
    if cfg.sample:
        names = sorted(random.Random(cfg.seed).sample(names, min(cfg.sample, len(names))))
    for m in ("round", "sharp"):
        os.makedirs(os.path.join(cfg.out, m), exist_ok=True)
    bands = parse_bands(cfg.bands)
    kss = keyshape_fit.load(cfg.keyshapes or os.path.join(cfg.out, "keyshapes.json")) if cfg.keyshape_fit else {}
    if cfg.keyshape_fit and not kss:
        print("  note: no keyshapes.json (run core/keyshape.py --input-only first): no keyshape fit")
    kss_tip = keyshape_fit.load(cfg.keyshapes or os.path.join(cfg.out, "keyshapes.json")) \
        if cfg.miter in KS_MODES else {}
    if cfg.miter in KS_MODES and not kss_tip:
        print("  note: no keyshapes.json (run core/keyshape.py --input-only first): no tip is cut")
    report, fails = {}, []
    prog = Progress("corner48_toggle", len(names))
    jobs = [(os.path.join(cfg.input, n), n, cfg.out, bands, cfg.group_tol, cfg.fallback,
             cfg.sharpen == "all", modes, cfg.miter, kss.get(n), cfg.corner_max_r, kss_tip.get(n))
            for n in names]
    if cfg.jobs > 1 and len(names) > 1:
        with ProcessPoolExecutor(max_workers=cfg.jobs) as pool:
            for name, entry, err in pool.map(process_icon, jobs, chunksize=4):
                prog.step(name)
                (fails.append((name, err)) if err else report.__setitem__(name, entry))
    else:
        for job in jobs:
            name, entry, err = process_icon(job)
            prog.step(name)
            (fails.append((name, err)) if err else report.__setitem__(name, entry))
    prog.done()
    path = os.path.join(cfg.out, "toggle.json")
    icons = report
    partial = bool(cfg.files or cfg.sample or cfg.ready or cfg.reviewed) or cfg.mode != "both"
    if partial and os.path.exists(path):        # a partial run updates only its own icons and
        with open(path, encoding="utf-8") as f:  # outputs (a --mode sharp run keeps round)
            icons = json.load(f).get("icons", {})
        for n, entry in report.items():
            icons[n] = {**icons.get(n, {}), **entry}
        icons = dict(sorted(icons.items()))
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"bands": cfg.bands, "group_tol": cfg.group_tol, "fallback": cfg.fallback,
                   "sharpen": cfg.sharpen, "miter": cfg.miter, "keyshape_fit": bool(kss),
                   "corner_max_r": cfg.corner_max_r,
                   "icons": icons}, f, indent=1)
    tot = lambda mode, st: sum(1 for v in report.values() for e in v.get(mode, {"log": []})["log"]
                               if e["status"] == st)
    print(f"processed {len(names)} icons | round: {tot('round', 'rounded')} rounded, "
          f"{tot('round', 'skipped')} skipped | sharp: {tot('sharp', 'sharpened')} sharpened, "
          f"{tot('sharp', 'skipped')} skipped | {len(fails)} failures")
    for n, e in fails[:20]:
        print(f"  FAIL {n}: {e}")
    for mode in modes:
        st = [v[mode]["check"]["status"] for v in report.values()]
        print(f"  check {mode}: {st.count('ok')} ok, {st.count('contact')} new contact, "
              f"{st.count('fail')} fail" + (" -> " + ", ".join(n for n, v in report.items()
                                                             if v[mode]["check"]["status"] == "fail")[:400]
                                            if st.count("fail") else ""))
    # icons a reviewer locked in as good (locks.json) must not change silently
    changed = locks.changed_locks(names=set(report), input_dir=cfg.input, out_dir=cfg.out,
                                  parts=("input",) + modes)
    locks.warn(changed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
