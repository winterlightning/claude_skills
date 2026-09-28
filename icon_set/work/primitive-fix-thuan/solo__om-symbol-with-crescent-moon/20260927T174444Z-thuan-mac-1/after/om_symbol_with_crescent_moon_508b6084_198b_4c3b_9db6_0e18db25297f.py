from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "508b6084-198b-4c3b-9db6-0e18db25297f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__om-symbol-with-crescent-moon/20260927T174444Z-thuan-mac-1/reference/maha shivaratri om_508b6084-198b-4c3b-9db6-0e18db25297f.svg"
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


class OmSymbolWithCrescentMoon(Solo48):
    """Maha Shivaratri Om: a crescent moon at the upper left, the chandrabindu (dot over a
    small cup) at the upper right, and the Om sign across the bottom.

    Plan: SQUARE. Moon = a tilted crescent of two cubics sharing both horn tips
    (21,8)/(16,19) (exempt pair), its horns turned to the upper and lower right like the
    reference. The bindu dot sets the exact top; the Om lobe ends set the exact left 6. Chandrabindu = dot (36,6) over an rx6/ry3 cup. Om = the 3-shaped pair of
    lobes on the left joined at the waist (16,34) and a bridge that rises into the right loop
    (r8, exact right 42 and bottom 42) curling back in.
    """
    icon_id = "om-symbol-with-crescent-moon"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/religion"
    aliases = ("maha shivaratri om", "om with moon", "shiva", "om")
    keywords = ("om", "aum", "shivaratri", "shiva", "moon", "crescent", "hindu", "festival", "religion")

    def build(self) -> None:
        self.add_bezier("moon-outer", (21, 8), ((5, 1), (1, 19), (16, 19)))
        self.add_bezier("moon-inner", (16, 19), ((10, 15), (13, 9), (21, 8)))
        self.add_contour("moon", "moon-outer", "moon-inner", closed=True)
        self.add_dot("bindu", (36, 6))
        self.add_arc("cup", (30, 12), (42, 12), radius_x=6, radius_y=3, sweep=False)
        self.add_bezier("upper-lobe", (6, 31), ((18, 23), (25, 30), (16, 34)))
        self.add_bezier("lower-lobe", (16, 34), ((26, 34), (20, 46), (6, 40)))
        self.add_contour("left-lobes", "upper-lobe", "lower-lobe")
        self.add_bezier("bridge", (16, 34), ((28, 36), (26, 26), (34, 26)))
        self.add_arc("right-upper", (34, 26), (42, 34), radius_x=8)
        self.add_arc("right-lower", (42, 34), (34, 42), radius_x=8)
        self.add_bezier("right-tip", (34, 42), ((32, 42), (30, 40), (30, 38)))
        self.add_contour("right-lobe", "bridge", "right-upper", "right-lower", "right-tip")
        self.relate("connect", "left-lobes", "right-lobe")
