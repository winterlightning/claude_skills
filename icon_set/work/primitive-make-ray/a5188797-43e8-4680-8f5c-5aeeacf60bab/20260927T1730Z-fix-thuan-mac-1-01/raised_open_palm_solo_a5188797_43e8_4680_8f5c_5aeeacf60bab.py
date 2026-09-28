from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a5188797-43e8-4680-8f5c-5aeeacf60bab"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__raised-open-palm-solo/20260927T170824Z-thuan-mac-1/reference/handful_a5188797-43e8-4680-8f5c-5aeeacf60bab.svg"
AUTHOR = "claude-opus-5-5"


def _path(icon, name, start, steps, closed=False):
    """steps: ('L', end) | ('A', end, r[, ry], sweep[, large]) | ('C', c1, c2, end)"""
    here, members = start, []
    for i, st in enumerate(steps):
        m = f"{name}-{i + 1}"
        if st[0] == "L":
            icon.add_line(m, here, st[1]); here = st[1]
        elif st[0] == "A":
            end, r = st[1], st[2]
            rest = list(st[3:])
            ry = r
            if rest and not isinstance(rest[0], bool):
                ry = rest.pop(0)
            sweep = rest[0] if rest else True
            large = rest[1] if len(rest) > 1 else False
            icon.add_arc(m, here, end, radius_x=r, radius_y=ry, large_arc=large, sweep=sweep); here = end
        else:
            icon.add_bezier(m, here, (st[1], st[2], st[3])); here = st[3]
        members.append(m)
    icon.add_contour(name, *members, closed=closed)


def _circle(icon, name, cx, cy, r):
    _path(icon, name, (cx, cy - r), [("A", (cx + r, cy), r, True), ("A", (cx, cy + r), r, True),
                                      ("A", (cx - r, cy), r, True), ("A", (cx, cy - r), r, True)], True)


def _smooth(icon, name, pts, closed=True, t=1/3):
    """Catmull-Rom cubics through integer knots."""
    n = len(pts); segs = []
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p0 = pts[(i - 1) % n] if (closed or i > 0) else pts[i]
        p1 = pts[i]; p2 = pts[(i + 1) % n]
        p3 = pts[(i + 2) % n] if (closed or i + 2 < n) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 2, p1[1] + (p2[1] - p0[1]) * t / 2)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 2, p2[1] - (p3[1] - p1[1]) * t / 2)
        segs.append(("C", c1, c2, p2))
    _path(icon, name, pts[0], segs, closed)


def _herm(icon, name, knots, closed=True, k=1.0):
    """knots: [(point, tangent_dir)]; controls at chord/3*k along the unit tangents."""
    import math
    def unit(v):
        n = math.hypot(*v)
        return (v[0] / n, v[1] / n)
    segs = []
    n = len(knots)
    for i in range(n if closed else n - 1):
        (p1, t1), (p2, t2) = knots[i], knots[(i + 1) % n]
        L = math.hypot(p2[0] - p1[0], p2[1] - p1[1]) / 3 * k
        u1, u2 = unit(t1), unit(t2)
        segs.append(("C", (p1[0] + u1[0] * L, p1[1] + u1[1] * L), (p2[0] - u2[0] * L, p2[1] - u2[1] * L), p2))
    _path(icon, name, knots[0][0], segs, closed)

def _w(p, q):
    """Hand frame: p steps across the fingers by (3,1), q steps along them by (1,-3)."""
    return (12 + 3 * p + q, 28 + p - 3 * q)


class RaisedOpenPalmSolo(Solo48):
    """An open hand raised and leaning to the right: thumb, index, middle and ring fingers.

    Plan: HRECT_L. Fingers are 1:3-slanted tubes that share walls (Lucide `hand` style) on
    the lattice frame _w(p, q); each tip is an r5 arc about L+(4,3) from the left wall point
    L to R=L+(9,3), so the arc's top is an exact integer. Middle finger sets the top (y8),
    the ring tip the right edge (x44), the 1:2 thumb tip the left edge (x4); the palm narrows
    into an open wrist at the bottom edge y40.
    """
    icon_id = "raised-open-palm-solo"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/hands"
    aliases = ("handful", "open hand", "raised hand", "waving hand")
    keywords = ("hand", "palm", "open", "raised", "wave", "hello", "handful", "fingers")

    def build(self) -> None:
        # thumb: a 1:2 tube pointing up-left, r5 tip about (9,27) from A=(4,27) to B=(12,23),
        # its upper side meeting the index wall at the notch (13,25)
        steps = [("L", (4, 27)), ("A", (12, 23), 5, True), ("L", (13, 25))]
        for p, q in ((0, 5), (3, 7), (6, 5)):
            steps.append(("L", _w(p, q)))
            steps.append(("A", _w(p + 3, q), 5, True))
        steps.append(("L", _w(9, 0)))
        steps.append(("L", (38, 40)))
        _path(self, "hand", (10, 39), steps)
        for p, top in ((3, 5), (6, 5)):
            self.add_line(f"split-{p}", _w(p, top), _w(p, 0))
            self.relate("connect", "hand", f"split-{p}")
