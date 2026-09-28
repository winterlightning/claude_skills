from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7a2f7f35-8325-4934-a0d0-3dfb23a3f835"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__raised-closed-fist/20260927T170824Z-thuan-mac-1/reference/grip_7a2f7f35-8325-4934-a0d0-3dfb23a3f835.svg"
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

class RaisedClosedFist(Solo48):
    """Raised closed fist seen from the front: four knuckles, a thumb folded straight across.

    Plan: VRECT_L. Four r4 knuckle arcs across the top (x 8..40, top y4); finger splits run
    from the valleys down to the thumb's top edge (y20); the thumb is a band from the left
    wall to an r4 tip at x31 (9 clear of the right wall); the hand narrows into a wrist
    that ends on a flat base at y44.
    """
    icon_id = "raised-closed-fist"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/hands"
    aliases = ("fist", "raised fist", "power fist", "solidarity")
    keywords = ("fist", "hand", "power", "protest", "grip", "punch", "solidarity")

    def build(self) -> None:
        _path(self, "hand", (12, 44), [
            ("L", (12, 36)), ("L", (8, 30)), ("L", (8, 28)), ("L", (8, 20)), ("L", (8, 8)),
            ("A", (16, 8), 4, True), ("A", (24, 8), 4, True), ("A", (32, 8), 4, True), ("A", (40, 8), 4, True),
            ("L", (40, 30)), ("L", (36, 36)), ("L", (36, 44)), ("L", (12, 44)),
        ], closed=True)
        _path(self, "thumb", (8, 20), [
            ("L", (16, 20)), ("L", (24, 20)), ("L", (27, 20)), ("A", (27, 28), 4, True), ("L", (8, 28)),
        ])
        self.add_line("split-1", (16, 8), (16, 20))
        self.add_line("split-2", (24, 8), (24, 20))
        self.add_line("split-3", (32, 8), (32, 12))
        for p in ("thumb", "split-1", "split-2", "split-3"):
            self.relate("connect", "hand", p)
        self.relate("connect", "thumb", "split-1")
        self.relate("connect", "thumb", "split-2")
