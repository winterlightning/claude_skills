from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a668eb75-0801-43ec-9627-67abbe1f014e"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__macaron-with-thick-central-filling/20260927T164509Z-thuan-mac-1/reference/macaroon_a668eb75-0801-43ec-9627-67abbe1f014e.svg"
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


class MacaronWithThickCentralFilling(Solo48):
    """Macaron from the side: two domed shells around a thick filling whose edges bulge out
    past the shells.

    Plan: HRECT_M (4,10)-(44,38), mirrored about x=24 and y=24. Outline = top shell
    (two broad cubics (8,20)->(24,10)->(40,20), flat top 10), right filling bulge (r4 about (40,24),
    right 44), bottom shell (bottom 38), left bulge (left 4). Two seam lines y=20 and y=28
    across the shells, 8 apart, so the filling reads as a band.
    """
    icon_id = "macaron-with-thick-central-filling"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ("macaroon", "macaron")
    keywords = ("macaron", "macaroon", "cookie", "dessert", "sweet", "food")

    def build(self) -> None:
        _path(self, "macaron", (8, 20), [("C", (8, 12), (14, 10), (24, 10)), ("C", (34, 10), (40, 12), (40, 20)),
                                         ("A", (40, 28), 4, True),
                                         ("C", (40, 36), (34, 38), (24, 38)), ("C", (14, 38), (8, 36), (8, 28)),
                                         ("A", (8, 20), 4, True)], closed=True)
        self.add_line("seam-top", (8, 20), (40, 20))
        self.add_line("seam-bottom", (8, 28), (40, 28))
        self.relate("connect", "macaron", "seam-top")
        self.relate("connect", "macaron", "seam-bottom")
