from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e6d7e2d5-6eab-4182-9a4c-2d666181696c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__open-hand-supporting-a-sprout/20260927T174444Z-thuan-mac-1/reference/aquascaping plant_e6d7e2d5-6eab-4182-9a4c-2d666181696c.svg"
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
        elif st[0] == "R":
            c1, c2 = _rarc(here, st[1], st[2], st[3] if len(st) > 3 else None)
            icon.add_bezier(m, here, (c1, c2, st[1])); here = st[1]
        else:
            icon.add_bezier(m, here, (st[1], st[2], st[3])); here = st[3]
        members.append(m)
    icon.add_contour(name, *members, closed=closed)


def _rarc(p0, p1, c, cw=None):
    """cubic approximating a circular arc about c (possibly fractional) from p0 to p1 (short way)."""
    import math
    a0 = math.atan2(p0[1] - c[1], p0[0] - c[0]); a1 = math.atan2(p1[1] - c[1], p1[0] - c[0])
    d = a1 - a0
    while d <= -math.pi: d += 2 * math.pi
    while d > math.pi: d -= 2 * math.pi
    if cw is True and d < 0: d += 2 * math.pi
    if cw is False and d > 0: d -= 2 * math.pi
    r0 = math.dist(p0, c); r1 = math.dist(p1, c)
    k = 4 / 3 * math.tan(d / 4)
    c1 = (p0[0] - k * r0 * math.sin(a0), p0[1] + k * r0 * math.cos(a0))
    c2 = (p1[0] + k * r1 * math.sin(a1), p1[1] - k * r1 * math.cos(a1))
    return c1, c2


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


class OpenHandSupportingASprout(Solo48):
    """An open palm-up hand supporting a young sprout with two leaves (aquascaping plant,
    growth, care).

    Plan: SQUARE. Palm-up hand after hand-holding-heart: palm arc (6,30)->(22,26), flat thumb
    top to (30,26), r4 thumb tip, underside back to (20,34); fingers from the thumb tip to r6
    fingertips at the exact right 42, palm base y 42, wrist to (6,40). The sprout's stem
    rises from the thumb top node (26,26) to (26,18); two lens leaves (two cubics each, sharing
    both ends) spread from there, the left one to the tip (8,6) and the larger right one to
    (42,6), setting the exact top.
    """
    icon_id = "open-hand-supporting-a-sprout"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/plants"
    aliases = ("aquascaping plant", "hand with sprout", "growth", "seedling in hand")
    keywords = ("sprout", "seedling", "plant", "hand", "growth", "care", "ecology", "nature", "sustainability")

    def build(self) -> None:
        self.add_arc("palm-upper", (6, 30), (22, 26), radius_x=16, radius_y=8)
        self.add_line("thumb-top-a", (22, 26), (26, 26))
        self.add_line("thumb-top-b", (26, 26), (30, 26))
        self.add_arc("thumb-tip-upper", (30, 26), (34, 30), radius_x=4)
        self.add_arc("thumb-tip-lower", (34, 30), (30, 34), radius_x=4)
        self.add_line("thumb-bottom", (30, 34), (20, 34))
        self.add_contour("thumb", "palm-upper", "thumb-top-a", "thumb-top-b", "thumb-tip-upper",
                         "thumb-tip-lower", "thumb-bottom")
        self.add_arc("fingertips", (34, 30), (42, 36), radius_x=8, radius_y=6)
        self.add_line("fingers-lower", (42, 36), (40, 42))
        self.add_line("palm-base", (40, 42), (12, 42))
        self.add_line("wrist-lower", (12, 42), (6, 40))
        self.add_contour("hand", "fingertips", "fingers-lower", "palm-base", "wrist-lower")
        self.relate("connect", "thumb", "hand")
        self.add_line("stem", (26, 26), (26, 18))
        self.relate("connect", "thumb", "stem")
        _path(self, "leaf-left", (26, 18), [
            ("C", (24, 11), (16, 6), (8, 6)),
            ("C", (10, 13), (18, 18), (26, 18)),
        ], closed=True)
        _path(self, "leaf-right", (26, 18), [
            ("C", (28, 10), (34, 6), (42, 6)),
            ("C", (41, 13), (34, 18), (26, 18)),
        ], closed=True)
        for n in ("leaf-left", "leaf-right"):
            self.relate("connect", "stem", n)
        self.relate("connect", "leaf-left", "leaf-right")
