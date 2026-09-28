from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9b7034f3-b252-42d2-bb8e-54655473701c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__narrow-tower-with-arched-window/20260927T164821Z-thuan-mac-1/reference/campanile_9b7034f3-b252-42d2-bb8e-54655473701c.svg"
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



class NarrowTowerWithArchedWindow(Solo48):
    """Campanile: a tall narrow tower with a pointed roof, an arched window high in the wall and a
    base line.

    Plan: VRECT_M (10..38 x 4..44). Walls x12/x36 from the eave line y16 to the base y44 (base
    line 10..38); roof triangle from the eave ends to the apex (24,4). Window: 8-wide arch with
    an r4 top about (24,26), sides down to y32 and a sill; every window edge is 8+ from the walls,
    eave and base (walls are standalone lines so the exact 8 certifies).
    """
    icon_id = "narrow-tower-with-arched-window"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/building"
    aliases = ("campanile", "bell tower", "tower")
    keywords = ("tower", "campanile", "bell tower", "building", "arched window", "church", "landmark")

    def build(self) -> None:
        self.add_line("wall-left", (12, 44), (12, 16))
        self.add_line("wall-right", (36, 16), (36, 44))
        _path(self, "roof", (12, 16), [("L", (24, 4)), ("L", (36, 16))])
        self.add_line("base", (10, 44), (38, 44))
        self.relate("connect", "wall-left", "roof")
        self.relate("connect", "wall-right", "roof")
        self.relate("connect", "wall-left", "base")
        self.relate("connect", "wall-right", "base")
        _path(self, "window", (20, 32), [("L", (20, 26)), ("A", (28, 26), 4, True), ("L", (28, 32)), ("L", (20, 32))],
              closed=True)
