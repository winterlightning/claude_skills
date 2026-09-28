from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "153226c0-7d54-42d8-8fa9-2caf44b880cf"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__medusa-head-with-snake-hair-batch-086/20260927T164821Z-thuan-mac-1/reference/meduza gorgon_153226c0-7d54-42d8-8fa9-2caf44b880cf.svg"
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



class MedusaHeadWithSnakeHair(Solo48):
    """Medusa: a round-jawed face with a straight hairline, two eyes, a mouth, and four
    snakes rising from the hairline (outer pair flaring outward, inner pair wriggling up).

    Plan: VRECT_L. Head = hairline y18 from x11 to x37, sides down to y29, r13 jaw about (24,31)
    (bottom 44). Eyes are dots 8 below the hairline and 8 inside the sides; mouth 9 above the jaw.
    Snakes root at x 11/19/29/37 (>=8 apart) and end on the keyshape extremes 8/40 (x) and 4 (y).
    """
    icon_id = "medusa-head-with-snake-hair-batch-086"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "characters/myth"
    aliases = ("gorgon", "medusa")
    keywords = ("medusa", "gorgon", "snake", "hair", "myth", "greek", "head")

    def build(self) -> None:
        _path(self, "head", (11, 18), [("L", (19, 18)), ("L", (29, 18)), ("L", (37, 18)), ("L", (37, 31)),
                                       ("A", (11, 31), 13, True), ("L", (11, 18))], closed=True)
        self.add_dot("eye-left", (20, 27))
        self.add_dot("eye-right", (28, 27))
        self.add_line("mouth", (22, 35), (26, 35))
        # outer snakes: rise from the corners, bow outward to the keyshape side, then wriggle back up
        self.add_bezier("snake-outer-left-1", (11, 18), ((11, 14), (8, 15), (8, 11)))
        self.add_bezier("snake-outer-left-2", (8, 11), ((8, 7), (10, 7), (10, 4)))
        self.add_contour("snake-outer-left", "snake-outer-left-1", "snake-outer-left-2")
        self.add_bezier("snake-outer-right-1", (37, 18), ((37, 14), (40, 15), (40, 11)))
        self.add_bezier("snake-outer-right-2", (40, 11), ((40, 7), (38, 7), (38, 4)))
        self.add_contour("snake-outer-right", "snake-outer-right-1", "snake-outer-right-2")
        # inner snakes: S-curves that wriggle up and diverge
        self.add_bezier("snake-inner-left", (19, 18), ((18, 13), (21, 9), (19, 4)))
        self.add_bezier("snake-inner-right", (29, 18), ((30, 13), (27, 9), (29, 4)))
        for s in ("snake-outer-left", "snake-outer-right", "snake-inner-left", "snake-inner-right"):
            self.relate("connect", s, "head")
