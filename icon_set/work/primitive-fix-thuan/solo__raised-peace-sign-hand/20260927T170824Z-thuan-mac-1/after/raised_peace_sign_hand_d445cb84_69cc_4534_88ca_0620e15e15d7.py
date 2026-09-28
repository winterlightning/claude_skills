from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d445cb84-69cc-4534-88ca-0620e15e15d7"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__raised-peace-sign-hand/20260927T170824Z-thuan-mac-1/reference/peace sign_d445cb84-69cc-4534-88ca-0620e15e15d7.svg"
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

class RaisedPeaceSignHand(Solo48):
    """A raised hand making the peace (victory) sign: index and middle fingers in a V.

    Plan: VRECT_L. The V fingers are mirrored 1:2 tubes whose r5 tips (about (13,9) and
    (35,9)) set the top edge y4; their inner walls meet at the crotch (24,21). The folded
    thumb is the reference's "7" crease: a top edge at y29 from the right wall, an r4 turn
    and a short drop; the
    curled ring and little fingers are two r4 knuckle bumps on the left wall that set x8.
    """
    icon_id = "raised-peace-sign-hand"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/hands"
    aliases = ("peace sign", "victory hand", "v sign", "two fingers")
    keywords = ("peace", "victory", "hand", "v", "two", "fingers", "gesture")

    def build(self) -> None:
        _path(self, "hand", (12, 34), [
            ("A", (12, 26), 4, True), ("A", (12, 18), 4, True), ("L", (12, 17)), ("L", (8, 9)),
            ("A", (16, 5), 5, True), ("L", (24, 21)), ("L", (32, 5)), ("A", (40, 9), 5, True),
            ("L", (36, 17)), ("L", (36, 29)), ("L", (36, 34)),
            ("A", (26, 44), 10, True), ("L", (22, 44)), ("A", (12, 34), 10, True),
        ], closed=True)
        # folded thumb: its top edge crosses the palm from the right wall, then turns down (a "7")
        _path(self, "thumb", (36, 29), [("L", (27, 29)), ("A", (23, 33), 4, False), ("L", (23, 35))])
        self.relate("connect", "hand", "thumb")
