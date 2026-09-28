from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "cc968864-9cbe-47b2-9f43-09b6e22ddf54"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__meteor-in-a-pointed-flame-tail/20260927T164821Z-thuan-mac-1/reference/astronomy comet 2_cc968864-9cbe-47b2-9f43-09b6e22ddf54.svg"
AUTHOR = "claude-fable-5-1"


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



class MeteorInAPointedFlameTail(Solo48):
    """Meteor: a round head at the lower right with a crater dot, trailing a pointed three-spike
    flame tail to the upper left.

    Plan: SQUARE. Head r10 about (32,32) (right/bottom 42). One closed silhouette: the head's
    3/4 arc from the top cardinal (32,22) round the right and bottom to the left cardinal (22,32),
    then the tail polyline: spike C (6,30), notch (16,22), main spike (6,6), notch (22,16),
    spike A (30,6), back to (32,22). Symmetric about the diagonal y=x.
    """
    icon_id = "meteor-in-a-pointed-flame-tail"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science/astronomy"
    aliases = ("comet", "shooting star", "fireball")
    keywords = ("meteor", "comet", "astronomy", "space", "flame", "tail", "fireball")

    def build(self) -> None:
        _path(self, "meteor", (32, 22), [
            ("A", (42, 32), 10, True), ("A", (32, 42), 10, True), ("A", (22, 32), 10, True),
            ("L", (6, 30)), ("L", (16, 22)), ("L", (6, 6)), ("L", (22, 16)), ("L", (30, 6)), ("L", (32, 22)),
        ], closed=True)
        self.add_dot("crater", (32, 32))
