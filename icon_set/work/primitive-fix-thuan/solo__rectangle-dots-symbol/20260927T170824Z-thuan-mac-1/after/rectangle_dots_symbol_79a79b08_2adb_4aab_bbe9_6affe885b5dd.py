from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "79a79b08-2adb-4aab-bbe9-6affe885b5dd"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__rectangle-dots-symbol/20260927T170824Z-thuan-mac-1/reference/rectangle dots_79a79b08-2adb-4aab-bbe9-6affe885b5dd.svg"
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

class RectangleDotsSymbol(Solo48):
    """A tall dashed rectangle (a placeholder frame) with two small dots on its centre line.

    Plan: VRECT_M, matching the reference's portrait proportions. Four rounded corner
    brackets (r4) with short arms, one dash in the middle of each long side (y20-28) and a
    gap in the middle of the top and bottom, as in the reference; two dots at (24,14) and
    (24,34). Leg-to-dash gaps are 9 so every straight gap certifies.
    """
    icon_id = "rectangle-dots-symbol"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/shapes"
    aliases = ("dashed rectangle", "placeholder", "selection frame", "rectangle dots")
    keywords = ("rectangle", "dashed", "dots", "frame", "placeholder", "selection", "crop", "portrait")

    def build(self) -> None:
        _path(self, "corner-tl", (10, 11), [("L", (10, 8)), ("A", (14, 4), 4, True), ("L", (18, 4))])
        _path(self, "corner-tr", (30, 4), [("L", (34, 4)), ("A", (38, 8), 4, True), ("L", (38, 11))])
        _path(self, "corner-br", (38, 37), [("L", (38, 40)), ("A", (34, 44), 4, True), ("L", (30, 44))])
        _path(self, "corner-bl", (18, 44), [("L", (14, 44)), ("A", (10, 40), 4, True), ("L", (10, 37))])
        self.add_line("side-left", (10, 20), (10, 28))
        self.add_line("side-right", (38, 20), (38, 28))
        self.add_dot("dot-top", (24, 14))
        self.add_dot("dot-bottom", (24, 34))
