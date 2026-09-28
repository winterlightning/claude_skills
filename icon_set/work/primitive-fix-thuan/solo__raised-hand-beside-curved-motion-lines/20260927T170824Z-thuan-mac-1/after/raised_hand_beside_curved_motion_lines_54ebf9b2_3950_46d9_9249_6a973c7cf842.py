from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "54ebf9b2-3950-46d9-9249-6a973c7cf842"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__raised-hand-beside-curved-motion-lines/20260927T170824Z-thuan-mac-1/reference/massage point_54ebf9b2-3950-46d9-9249-6a973c7cf842.svg"
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

class RaisedHandBesideCurvedMotionLines(Solo48):
    """A raised hand with its index finger up and two curved motion lines beside it.

    Plan: HRECT_L. Motion lines are two concentric quarter arcs about (17,22) (r4 and r13)
    in the corner above a 45-degree thumb (r5 tip about (22,32)), 9 clear of the index finger's wall at
    x26. Index finger x26-34 (top y8), middle finger x34-42, the palm's pinky side bulging
    to x44, and a palm narrowing into an open wrist at y40.
    """
    icon_id = "raised-hand-beside-curved-motion-lines"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/hands"
    aliases = ("massage point", "hand wave", "pressure point")
    keywords = ("hand", "finger", "press", "massage", "point", "motion", "wave", "touch")

    def build(self) -> None:
        # motion lines: concentric quarter arcs (r4, r13) about (17,22), in the corner above the thumb
        _path(self, "motion-outer", (17, 9), [("A", (4, 22), 13, False)])
        _path(self, "motion-inner", (17, 18), [("A", (13, 22), 4, False)])
        # thumb: 45-degree tube with an r5 3-4-5 tip about (22,32), pointing into the arcs' corner
        _path(self, "hand", (23, 40), [
            ("L", (18, 35)), ("A", (25, 28), 5, True), ("L", (26, 29)),
            ("L", (26, 12)), ("A", (34, 12), 4, True), ("L", (34, 16)), ("A", (42, 16), 4, True),
            ("L", (42, 20)), ("C", (44, 28), (42, 24), (44, 25)), ("L", (44, 32)), ("C", (40, 40), (44, 36), (40, 37)),
        ])
        self.add_line("split", (34, 16), (34, 28))
        self.relate("connect", "hand", "split")
