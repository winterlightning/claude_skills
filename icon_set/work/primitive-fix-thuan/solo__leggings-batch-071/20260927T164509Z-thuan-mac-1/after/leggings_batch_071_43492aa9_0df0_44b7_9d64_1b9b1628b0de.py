from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "43492aa9-0df0-44b7-9d64-1b9b1628b0de"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__leggings-batch-071/20260927T164509Z-thuan-mac-1/reference/tights_43492aa9-0df0-44b7-9d64-1b9b1628b0de.svg"
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


class Leggings(Solo48):
    """Leggings (tights): a waistband over two long legs that taper to narrow ankle hems.

    Plan: VRECT_M (10,4)-(38,44), mirrored about x=24. Outline: waist top y=4 across
    10..38, straight waistband sides to y=12, outer leg sides as gentle cubics tapering to
    the ankles (12,44)/(36,44), hems 8 wide, inner legs straight up to the crotch (24,21).
    Waistband seam y=12 across, 9 above the crotch.
    """
    icon_id = "leggings-batch-071"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "clothing"
    categories = ("primitives", "clothing")
    aliases = ("tights", "leggings", "yoga pants")
    keywords = ("leggings", "tights", "pants", "yoga", "clothing", "fashion")

    def build(self) -> None:
        _path(self, "leggings", (10, 4), [("L", (38, 4)), ("L", (38, 12)), ("C", (38, 24), (36, 34), (36, 44)),
                                          ("L", (28, 44)), ("L", (24, 21)), ("L", (20, 44)), ("L", (12, 44)),
                                          ("C", (12, 34), (10, 24), (10, 12)), ("L", (10, 4))], closed=True)
        self.add_line("waistband", (10, 12), (38, 12))
        self.relate("connect", "leggings", "waistband")
