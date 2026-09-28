from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2d45d97b-981f-4f97-9c20-497b6332e1a3"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__littleneck-clam-shell/20260927T164509Z-thuan-mac-1/reference/littleneck_2d45d97b-981f-4f97-9c20-497b6332e1a3.svg"
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


class LittleneckClamShell(Solo48):
    """Littleneck clam: a broad rounded shell rising to the umbo at the top centre, with two
    concentric growth lines following the lower edge.

    Plan: HRECT_M (4,10)-(44,38), mirrored about x=24. Shell = Hermite loop through the umbo
    (24,10), shoulders (10,15)/(38,15), sides (4,26)/(44,26) and the bottom (24,38).
    Growth lines hang between the side knots and between the shoulder knots, sagging to
    y=29 and y=20 (9 apart, 10 below the umbo).
    """
    icon_id = "littleneck-clam-shell"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ("littleneck", "clam", "shellfish")
    keywords = ("clam", "littleneck", "shell", "seafood", "shellfish", "beach")

    def build(self) -> None:
        # Right half as cubics, the left half mirrored exactly about x=24.
        right = [((24, 10), (29, 12.5), (35, 12.5), (38, 15)), ((38, 15), (42, 18.5), (44, 21), (44, 26)),
                 ((44, 26), (44, 33), (35, 38), (24, 38))]
        m = lambda p: (48 - p[0], p[1])
        left = [(m(d), m(c), m(b), m(a)) for a, b, c, d in reversed(right)]
        segs = [("C", b, c, d) for a, b, c, d in right + left]
        _path(self, "shell", (24, 10), segs, closed=True)
        self.add_bezier("growth-1", (4, 26), ((10, 30), (16, 29), (24, 29)))
        self.add_bezier("growth-1b", (24, 29), ((32, 29), (38, 30), (44, 26)))
        self.add_bezier("growth-2", (10, 15), ((14, 19), (18, 20), (24, 20)))
        self.add_bezier("growth-2b", (24, 20), ((30, 20), (34, 19), (38, 15)))
        for a, b in (("growth-1", "growth-1b"), ("growth-2", "growth-2b")):
            self.relate("connect", a, b)
        for n in ("growth-1", "growth-1b", "growth-2", "growth-2b"):
            self.relate("connect", "shell", n)
