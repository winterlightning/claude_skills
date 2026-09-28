from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d90fb3c8-645e-4603-bbc3-4fad85460ae4"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__rectangular-faceted-gem/20260927T170824Z-thuan-mac-1/reference/jade_d90fb3c8-645e-4603-bbc3-4fad85460ae4.svg"
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

class RectangularFacetedGem(Solo48):
    """A step-cut (octagon) gemstone seen from above: an outer girdle, an inner table and
    eight facet lines joining their corners.

    Plan: SQUARE. Outer octagon with 45-degree corners (x/y 6..42, corner cut 7); inner table
    inset 8 on the straight sides with small corner cuts of 3 (diagonals 6*sqrt2 apart), so every facet band
    is at least 8 wide; eight facet lines join matching corners.
    """
    icon_id = "rectangular-faceted-gem"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/jewelry"
    aliases = ("jade", "gem", "emerald cut", "gemstone", "jewel")
    keywords = ("gem", "jewel", "jade", "emerald", "stone", "crystal", "precious", "facet")

    def build(self) -> None:
        outer = [(13, 6), (35, 6), (42, 13), (42, 35), (35, 42), (13, 42), (6, 35), (6, 13)]
        inner = [(17, 14), (31, 14), (34, 17), (34, 31), (31, 34), (17, 34), (14, 31), (14, 17)]
        _path(self, "girdle", outer[0], [("L", p) for p in outer[1:] + outer[:1]], closed=True)
        _path(self, "table", inner[0], [("L", p) for p in inner[1:] + inner[:1]], closed=True)
        for i, (a, b) in enumerate(zip(outer, inner)):
            self.add_line(f"facet-{i}", a, b)
            self.relate("connect", f"facet-{i}", "girdle")
            self.relate("connect", f"facet-{i}", "table")
