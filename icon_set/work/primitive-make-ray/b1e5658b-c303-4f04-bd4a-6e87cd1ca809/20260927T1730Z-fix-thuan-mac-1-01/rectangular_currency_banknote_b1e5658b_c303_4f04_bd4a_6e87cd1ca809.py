from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b1e5658b-c303-4f04-bd4a-6e87cd1ca809"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__rectangular-currency-banknote/20260927T170824Z-thuan-mac-1/reference/money bill_b1e5658b-c303-4f04-bd4a-6e87cd1ca809.svg"
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

class RectangularCurrencyBanknote(Solo48):
    """A banknote: a bill with concave notched corners and a round emblem in the middle.

    Plan: HRECT_M. The bill fills x4-44, y10-38; each corner is a concave r6 quarter-arc bite
    (centred on the corner), as on the reference's inner bill. The emblem is an r5 ring at
    the centre, 9 clear of the long edges. Edges are standalone members joined in a ring so
    the straight gaps certify.
    """
    icon_id = "rectangular-currency-banknote"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/money"
    aliases = ("banknote", "bill", "money", "cash", "currency")
    keywords = ("money", "banknote", "bill", "cash", "currency", "payment", "dollar", "finance")

    def build(self) -> None:
        ring = [("top", (10, 10), ("L", (38, 10))), ("bite-tr", (38, 10), ("A", (44, 16), 6, False)),
                ("right", (44, 16), ("L", (44, 32))), ("bite-br", (44, 32), ("A", (38, 38), 6, False)),
                ("bottom", (38, 38), ("L", (10, 38))), ("bite-bl", (10, 38), ("A", (4, 32), 6, False)),
                ("left", (4, 32), ("L", (4, 16))), ("bite-tl", (4, 16), ("A", (10, 10), 6, False))]
        for k, (name, start, step) in enumerate(ring):
            _path(self, name, start, [step])
            self.relate("connect", name, ring[k - 1][0])
        _circle(self, "emblem", 24, 24, 5)
