from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ff21c89d-bd7b-4a37-8d27-89d2bc3b02dd"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__macaw-profile-with-large-hooked-bill/20260927T164509Z-thuan-mac-1/reference/macaw_ff21c89d-bd7b-4a37-8d27-89d2bc3b02dd.svg"
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


class MacawProfileWithLargeHookedBill(Solo48):
    """Macaw perched in profile facing right: round head with a large hooked bill, chest
    curving down into a long tail at the lower left, a wing curve on the body and an eye dot.

    Plan: VRECT_L (8,4)-(40,44). Head = r10 arc about (26,14) (top 4) from the back (16,14)
    to (32,6); bill = cubic out to the rightmost (40,12) and down to a hooked tip (37,20),
    chin notch back to (32,18); chest bulges down to (28,34) and the tail underside runs to
    the tail tip (8,44); back from the tip up to the head. Wing leaves the back at the
    neck and sweeps round to rejoin the back above the tail.
    """
    icon_id = "macaw-profile-with-large-hooked-bill"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("primitives", "animals")
    aliases = ("macaw", "parrot")
    keywords = ("macaw", "parrot", "bird", "beak", "tropical", "animal")

    def build(self) -> None:
        _path(self, "bird", (8, 44), [("L", (12, 32)), ("C", (13, 28), (15, 24), (15, 20)), ("C", (15, 18), (15, 16), (16, 14)),
                                      ("A", (32, 6), 10, True),
                                      ("C", (36, 5), (40, 8), (40, 12)), ("C", (40, 16), (39, 18), (37, 20)),
                                      ("L", (32, 18)),
                                      ("C", (34, 22), (34, 29), (28, 34)), ("C", (22, 39), (14, 40), (8, 44))])
        self.add_bezier("wing", (15, 20), ((25, 20), (28, 30), (12, 32)))
        self.relate("connect", "bird", "wing")
        self.add_dot("eye", (25, 13))
