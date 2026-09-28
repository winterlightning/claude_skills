from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ff31f3e6-1eff-4fd3-a286-ad5ef7b18e15"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__lipstick-beside-round-powder-compact/20260927T164509Z-thuan-mac-1/reference/makeup_ff31f3e6-1eff-4fd3-a286-ad5ef7b18e15.svg"
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


class LipstickBesideRoundPowderCompact(Solo48):
    """A lipstick standing beside a round powder compact.

    Plan: HRECT_L (4,8)-(44,40). Lipstick: slanted bullet (6,22)->(6,14)->(14,8)->(14,22)
    on a wider tube (4,22)-(16,22) down to a rounded base at 40, with a collar line at
    y=30. Compact seen slightly from above: rx10/ry5 elliptical lid about (34,22) (right 44) on a
    case band whose rim curves down to y=37, 8 from the tube.
    """
    icon_id = "lipstick-beside-round-powder-compact"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "beauty"
    categories = ("primitives", "beauty")
    aliases = ("makeup", "lipstick and compact")
    keywords = ("lipstick", "compact", "powder", "makeup", "cosmetics", "beauty")

    def build(self) -> None:
        _path(self, "bullet", (6, 22), [("L", (6, 14)), ("L", (14, 8)), ("L", (14, 22))])
        _path(self, "tube", (6, 22), [("L", (4, 22)), ("L", (4, 30)), ("L", (4, 37)), ("A", (7, 40), 3, False), ("L", (13, 40)),
                                      ("A", (16, 37), 3, False), ("L", (16, 30)), ("L", (16, 22)), ("L", (14, 22)), ("L", (6, 22))],
              closed=True)
        self.relate("connect", "bullet", "tube")
        self.add_line("collar", (4, 30), (16, 30))
        self.relate("connect", "tube", "collar")
        # Compact seen slightly from above: an elliptical lid on a shallow case band.
        _path(self, "lid", (24, 22), [("A", (44, 22), 10, 5, True), ("A", (24, 22), 10, 5, True)], closed=True)
        _path(self, "case", (24, 22), [("L", (24, 32)), ("A", (44, 32), 10, 5, False), ("L", (44, 22))])
        self.relate("connect", "lid", "case")
