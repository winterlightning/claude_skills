from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "aee9af45-4408-44bc-855b-a22fd716f1e5"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__low-oval-bread-loaf/20260927T164509Z-thuan-mac-1/reference/bakery_aee9af45-4408-44bc-855b-a22fd716f1e5.svg"
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


class LowOvalBreadLoaf(Solo48):
    """Low oval bread loaf seen from the side: a broad dome over a flat base with three
    diagonal scoring cuts leaving the crust.

    Plan: HRECT_M (4,10)-(44,38). Crust = flat base (12,38)-(36,38), r8 heel corners,
    vertical heel walls to y28, then a Hermite dome through (11,13),(20,10),(29,10),(37,13).
    Scores are three parallel cuts hanging from the dome knots, slanting down-right.
    """
    icon_id = "low-oval-bread-loaf"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ("bread loaf", "bakery")
    keywords = ("bread", "loaf", "bakery", "baguette", "food")

    def build(self) -> None:
        K = 1.1
        # Long low loaf on CIRCLE: only the heel tips (4,24)/(44,24) reach radius 20.
        _path(self, "base", (4, 24), [("C", (4, 30), (7, 34), (13, 34)), ("L", (35, 34)),
                                     ("C", (41, 34), (44, 30), (44, 24))])
        _herm(self, "dome", [((44, 24), (0, -1)), ((33, 14), (-1, -0.2)), ((24, 13), (-1, 0)),
                             ((15, 14), (-1, 0.2)), ((4, 24), (0, 1))], closed=False, k=K)
        self.relate("connect", "base", "dome")
        for i, (x, y) in enumerate(((15, 14), (24, 13), (33, 14))):
            n = f"score-{i + 1}"
            self.add_bezier(n, (x, y), ((x + 1, y + 3), (x + 2, y + 5), (x + 2, y + 8)))
            self.relate("connect", "dome", n)
