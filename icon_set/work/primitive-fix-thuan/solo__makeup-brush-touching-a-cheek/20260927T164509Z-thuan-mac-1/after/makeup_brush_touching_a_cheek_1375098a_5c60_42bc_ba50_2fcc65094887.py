from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1375098a-5c60-42bc-ba50-2fcc65094887"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__makeup-brush-touching-a-cheek/20260927T164509Z-thuan-mac-1/reference/beauty massage spread_1375098a-5c60-42bc-ba50-2fcc65094887.svg"
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


class MakeupBrushTouchingACheek(Solo48):
    """Close-up of a face with a makeup brush sweeping the cheek: a large jaw/cheek curve at
    the lower right, a closed eye at the left and a fan brush on the 45-degree axis whose
    bristle dome rests on the cheek.

    Plan: SQUARE (6,6)-(42,42). Jaw = r25 arc about (17,17) from (10,41) through the
    bottom (17,42) to (41,24). Brush axis x+y=48: handle (42,6)->(34,14),
    fan flanks from the ferrule node (34,14) to the 3-4-5 dome ends (22,19)/(29,26) of an
    r5 dome about (26,22). Closed eye: r5 arc (6,24)->(13,24).
    """
    icon_id = "makeup-brush-touching-a-cheek"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "beauty"
    categories = ("primitives", "beauty")
    aliases = ("beauty massage spread", "blush brush", "applying makeup")
    keywords = ("makeup", "brush", "cheek", "blush", "face", "beauty", "cosmetics")

    def build(self) -> None:
        _path(self, "jaw", (10, 41), [("A", (17, 42), 25, False), ("A", (41, 24), 25, False)])
        _path(self, "brush-head", (34, 14), [("L", (22, 19)), ("A", (29, 26), 5, False), ("L", (34, 14))], closed=True)
        self.add_line("handle", (34, 14), (42, 6))
        self.relate("connect", "brush-head", "handle")
        self.add_arc("eye", (6, 24), (13, 24), radius_x=5, radius_y=5, sweep=False)
