from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3778c097-0bd8-40c7-9e69-1cc141e803e8"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__makeup-brush-beside-six-well-palette/20260927T164509Z-thuan-mac-1/reference/make up brush set_3778c097-0bd8-40c7-9e69-1cc141e803e8.svg"
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


class MakeupBrushBesideSixWellPalette(Solo48):
    """Makeup brush standing beside an eyeshadow palette with six pans.

    Plan: HRECT_L (4,8)-(44,40). Brush on the left: fan bristle head (shallow r5 dome
    (4,10)-(12,10), top 8) with straight flanks tapering to a point at (8,24), handle stroke down to 40.
    Palette on the right: rounded case (20,8)-(44,40) built from standalone edges and r4
    corners joined in a ring, holding a 2x3 grid of pans (dots at x 28/36, y 16/24/32),
    8 from the walls and from each other.
    """
    icon_id = "makeup-brush-beside-six-well-palette"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "beauty"
    categories = ("primitives", "beauty")
    aliases = ("make up brush set", "eyeshadow palette")
    keywords = ("makeup", "brush", "palette", "eyeshadow", "cosmetics", "beauty")

    def build(self) -> None:
        _path(self, "brush-head", (8, 24), [("L", (4, 10)), ("A", (12, 10), 5, True),
                                            ("L", (8, 24))], closed=True)
        self.add_line("handle", (8, 24), (8, 40))
        self.relate("connect", "brush-head", "handle")
        L, T, R, B, r = 20, 8, 44, 40, 4
        segs = [("case-top", "L", (L + r, T), (R - r, T)), ("case-tr", "A", (R - r, T), (R, T + r)),
                ("case-right", "L", (R, T + r), (R, B - r)), ("case-br", "A", (R, B - r), (R - r, B)),
                ("case-bottom", "L", (R - r, B), (L + r, B)), ("case-bl", "A", (L + r, B), (L, B - r)),
                ("case-left", "L", (L, B - r), (L, T + r)), ("case-tl", "A", (L, T + r), (L + r, T))]
        for name, kind, a, b in segs:
            if kind == "L":
                self.add_line(name, a, b)
            else:
                self.add_arc(name, a, b, radius_x=r, radius_y=r, sweep=True)
        for (n1, *_), (n2, *_) in zip(segs, segs[1:] + segs[:1]):
            self.relate("connect", n1, n2)
        for x in (28, 36):
            for y in (16, 24, 32):
                self.add_dot(f"pan-{x}-{y}", (x, y))
