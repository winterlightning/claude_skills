from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4729c204-6315-48af-8efc-68755e7cb075"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__raised-index-finger-hand-solo/20260927T170824Z-thuan-mac-1/reference/finger_4729c204-6315-48af-8efc-68755e7cb075.svg"
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

class RaisedIndexFingerHandSolo(Solo48):
    """A hand with the index finger raised, the other fingers curled, thumb out to the side.

    Plan: VRECT_L. Index finger x16-24 with an r4 tip at the top edge (y4); two curled-finger
    knuckles (r4) step down to the right edge x40; the palm rounds into the bottom (r12 about
    (28,32), bottom y44); the thumb is a 45-degree tube with an r5 3-4-5 tip about (13,30)
    that sets the left edge x8. Two short finger splits hang from the knuckle valleys.
    """
    icon_id = "raised-index-finger-hand-solo"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/hands"
    aliases = ("pointing up", "index finger", "one finger", "finger up")
    keywords = ("hand", "finger", "index", "point", "up", "one", "attention", "gesture")

    def build(self) -> None:
        _path(self, "hand", (16, 26), [
            ("L", (16, 8)), ("A", (24, 8), 4, True), ("L", (24, 22)), ("A", (32, 22), 4, True),
            ("L", (32, 24)), ("A", (40, 24), 4, True), ("L", (40, 32)), ("A", (28, 44), 12, True),
            ("L", (26, 44)), ("C", (22, 44), (17, 41), (15, 39)), ("L", (9, 33)), ("A", (16, 26), 5, True),
        ], closed=True)
        self.add_line("split-1", (24, 22), (24, 30))
        self.add_line("split-2", (32, 24), (32, 30))
        self.relate("connect", "hand", "split-1")
        self.relate("connect", "hand", "split-2")
