from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7c962d05-9c47-401c-91bd-8dc4600a8dc0"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__mustard-squeeze-bottle-7c962d05/20260927T164821Z-thuan-mac-1/reference/mustard_7c962d05-9c47-401c-91bd-8dc4600a8dc0.svg"
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



class MustardSqueezeBottle(Solo48):
    """Mustard squeeze bottle: a tall rounded body, a cap band on its shoulders and a tapered
    nozzle tip.

    Plan: VRECT_M (10..38 x 4..44). Body outline with r4 corners from y20 to y44, its top closed
    by the cap band's bottom edge (14..34, y20); cap band 20x8 (y12..20); nozzle trapezoid
    (18,12)-(20,4)-(28,4)-(30,12) whose sides stay 8 apart at the tip.
    """
    icon_id = "mustard-squeeze-bottle-7c962d05"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("mustard bottle", "squeeze bottle", "condiment bottle")
    keywords = ("mustard", "bottle", "squeeze", "condiment", "sauce", "ketchup", "food")

    def build(self) -> None:
        _path(self, "body", (14, 20), [("A", (10, 24), 4, False), ("L", (10, 40)), ("A", (14, 44), 4, False),
                                       ("L", (34, 44)), ("A", (38, 40), 4, False), ("L", (38, 24)),
                                       ("A", (34, 20), 4, False)])
        _path(self, "cap", (14, 20), [("L", (14, 12)), ("L", (18, 12)), ("L", (30, 12)), ("L", (34, 12)),
                                      ("L", (34, 20)), ("L", (14, 20))], closed=True)
        _path(self, "nozzle", (18, 12), [("L", (20, 4)), ("L", (28, 4)), ("L", (30, 12))])
        self.relate("connect", "body", "cap")
        self.relate("connect", "nozzle", "cap")
