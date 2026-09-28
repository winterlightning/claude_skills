from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a7f76942-5429-5bfb-a03f-aa82345155cf"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__mammoth-in-profile/20260927T164509Z-thuan-mac-1/reference/fantasy behemoth_a7f76942-5429-5bfb-a03f-aa82345155cf.svg"
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


class MammothInProfile(Solo48):
    """Woolly mammoth in profile facing left: high shoulder hump, back sloping to the rump,
    two leg columns, a trunk hanging at the front and a tusk sweeping up.

    Plan: HRECT_L (4,8)-(44,40). The trunk hangs straight down x=10 from the head front
    (10,20) and curls forward at the foot line; the tusk leaves the trunk at (10,24) and
    sweeps forward and up to (4,16). Forehead domes up to the hump top (22,8); the back
    slopes down to the rump and the rear leg (44,40). Throat y=28 into the front leg
    x=18; legs front 18..27, rear 35..44, joined by an r4 arch instead of a belly bar.
    """
    icon_id = "mammoth-in-profile"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("primitives", "animals")
    aliases = ("fantasy behemoth", "woolly mammoth")
    keywords = ("mammoth", "behemoth", "prehistoric", "tusk", "trunk", "animal")

    def build(self) -> None:
        H = (10, 20)
        self.add_line("front-leg", (18, 40), (18, 28))
        _path(self, "body", (18, 28), [("C", (15, 28), (12, 27), (10, 24)), ("L", H), ("C", (13, 15), (16, 8), (23, 8)),
                                       ("C", (32, 8), (40, 14), (44, 22)), ("L", (44, 40))])
        self.relate("connect", "front-leg", "body")
        # Legs: the gap between the leg columns is an r4 arch, so there is no belly bar.
        _path(self, "legs", (35, 40), [("L", (35, 34)), ("A", (27, 34), 4, False), ("L", (27, 40))])
        _path(self, "trunk", (10, 24), [("L", (10, 34)), ("C", (10, 38), (8, 40), (5, 40))])
        self.add_bezier("tusk", (10, 24), ((6, 26), (4, 21), (4, 16)))
        self.relate("connect", "body", "trunk")
        self.relate("connect", "body", "tusk")
        self.add_dot("eye", (21, 19))
