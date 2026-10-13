#!/usr/bin/env python3
"""core/keyshape_fit.py — keep the outputs' ink inside the icon's keyshape.

The keyshape (core/keyshape.py: detected from the input's ink) is the envelope the icon is drawn
to. The input's round caps and joins stay inside it; the outputs can poke out:

  round output   a corner re-rounded with a SMALLER band radius than it was drawn with
                 reaches further out along its bisector
  sharp output   a sharpened corner's point, a mitre tip, a flat end's square corners

Every check allows what the input itself already reaches at that place ("allowance"): an
icon whose input is off-centre (a rainbow drawn in the top half) is not cut back to the
keyshape, its outputs just may not reach further than the input did there.

Used by core/toggle.py (rules in its README section "Keyshape fit").
"""

import json
import math
import os

import numpy as np
from shapely.geometry import Point, Polygon, box
from shapely.ops import unary_union

HALF_W = 2.0           # u — half the stroke width (a round cap / join reaches this far)
KS_TOL = 0.1           # u — ink this little past the keyshape (or the input) is on it
NEAR = 2.5             # u — input ink this close to a point counts as "the input there"
NEAR_SIDE = 6.0        # u — region_near: input ink within this far along a side sets that side
SAMPLES = 24           # samples per segment
CANVAS = box(-16, -16, 64, 64)   # clip region outside the cuts (generous: never clips by itself)


def load(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return {}


class Fit:
    """One icon's keyshape plus the input's centreline samples."""

    def __init__(self, rec, input_strokes, input_circles=()):
        l, t, r, b = rec["bounds"]
        self.l, self.t, self.r, self.b = l, t, r, b
        self.R = rec.get("r")
        self.c = complex((l + r) / 2, (t + b) / 2)
        self.shape = Point(self.c.real, self.c.imag).buffer(self.R, quad_segs=64) if self.R else box(l, t, r, b)
        pts = [s.point(k / SAMPLES) for st in input_strokes for s in st.segs for k in range(SAMPLES + 1)]
        for cx, cy, rx, ry in input_circles:
            pts += [complex(cx + rx * math.cos(a), cy + ry * math.sin(a))
                    for a in (2 * math.pi * k / 48 for k in range(48))]
        self.inp = np.array(pts, dtype=complex) if pts else np.zeros(0, dtype=complex)
        self.inp_ex = np.array([self.excess(p) for p in pts]) if pts else np.zeros(0)

    def excess(self, p):
        """How far point p lies past the keyshape (u; <= 0 inside)."""
        if self.R:
            return abs(p - self.c) - self.R
        return max(self.l - p.real, self.t - p.imag, p.real - self.r, p.imag - self.b)

    def allowance(self, P, reach=NEAR):
        """How far past the keyshape the INPUT's ink already reaches near P (>= 0)."""
        if not len(self.inp):
            return 0.0
        near = np.abs(self.inp - P) <= reach
        return max(0.0, float(self.inp_ex[near].max()) + HALF_W) if near.any() else 0.0

    def past(self, pts, P, reach=NEAR):
        """Ink points pts poke out further than the keyshape and the input near P allow."""
        return max(self.excess(q) for q in pts) > self.allowance(P, reach) + KS_TOL

    def round_ink_past(self, samples, P, reach):
        """Round-capped centreline samples (a re-rounded corner) poke out past the allowance."""
        return max(self.excess(q) + HALF_W for q in samples) > self.allowance(P, reach) + KS_TOL

    def region_near(self, P, window=NEAR_SIDE):
        """What ink may cover near P: the keyshape with each side pushed out as far as the
        input's own ink reaches past THAT side within `window` u along it (a frame drawn with
        its stroke centred on the keyshape edge may keep its square corner: it reaches no further
        than the frame's own sides). A round keyshape grows by the input's reach within window."""
        if not len(self.inp):
            return self.shape
        if self.R:
            a = self.allowance(P, window)
            return self.shape.buffer(a, quad_segs=64) if a > 0 else self.shape
        x, y = self.inp.real, self.inp.imag
        near_y, near_x = np.abs(y - P.imag) <= window, np.abs(x - P.real) <= window
        side = lambda over, sel: max(0.0, float(over[sel].max()) + HALF_W) if sel.any() else 0.0   # noqa: E731
        aL, aR = side(self.l - x, near_y), side(x - self.r, near_y)
        aT, aB = side(self.t - y, near_x), side(y - self.b, near_x)
        return box(self.l - aL, self.t - aT, self.r + aR, self.b + aB)

    def past_near(self, pts, P):
        """How far the farthest of pts lies outside region_near(P) (u; 0 when all inside)."""
        reg = self.region_near(P)
        return max((reg.exterior.distance(Point(q.real, q.imag)) for q in pts
                    if not reg.covers(Point(q.real, q.imag))), default=0.0)

    def region(self, P):
        """The keyshape grown by the input's own reach near P: ink may go this far."""
        a = self.allowance(P)
        return self.shape.buffer(a, join_style="mitre") if a > 0 else self.shape


def unit(z):
    return z / abs(z) if abs(z) > 1e-12 else None


def mitre_tip(V, u_in, u_out, limit):
    """Outer extreme points of a join at V (u_in: direction arriving, u_out: leaving), drawn
    with a mitre join of this limit: [tip] when mitred, the two bevel corners when cut, and the
    wedge polygon beyond the bevel (None when bevelled)."""
    turn = math.acos(max(-1.0, min(1.0, (u_in.conjugate() * u_out).real)))
    if turn < math.radians(2):
        return None
    inner = math.pi - turn
    bis = unit(u_in - u_out)                  # points out of the corner
    if bis is None or inner < 1e-6:
        return None
    n_a = u_in * 1j if ((u_in * 1j).conjugate() * bis).real > 0 else -u_in * 1j
    n_b = u_out * 1j if ((u_out * 1j).conjugate() * bis).real > 0 else -u_out * 1j
    a, b = V + n_a * HALF_W, V + n_b * HALF_W
    if 1 / math.sin(inner / 2) > limit:
        return [a, b], None
    T = V + bis * HALF_W / math.sin(inner / 2)
    return [T], Polygon([(a.real, a.imag), (T.real, T.imag), (b.real, b.imag)])


def clip_d(cuts):
    """SVG path d of CANVAS minus the cuts (holes), for a clipPath with clip-rule evenodd."""
    keep = CANVAS.difference(unary_union(cuts))
    polys = [keep] if keep.geom_type == "Polygon" else list(keep.geoms)
    out = []
    for poly in polys:
        for ring in [poly.exterior, *poly.interiors]:
            xy = list(ring.coords)[:-1]
            out.append("M" + "L".join(f"{_n(x)} {_n(y)}" for x, y in xy) + "Z")
    return "".join(out)


def _n(v):
    s = f"{v:.3f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def keyshapes_path():
    from .paths import OUT_DIR
    return os.path.join(OUT_DIR, "keyshapes.json")
