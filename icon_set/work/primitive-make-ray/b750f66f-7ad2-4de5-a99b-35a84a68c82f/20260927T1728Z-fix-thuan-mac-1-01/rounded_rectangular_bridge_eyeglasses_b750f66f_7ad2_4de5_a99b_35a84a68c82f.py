from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b750f66f-7ad2-4de5-a99b-35a84a68c82f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__rounded-rectangular-bridge-eyeglasses/20260927T172638Z-thuan-mac-1/reference/sunglasses_b750f66f-7ad2-4de5-a99b-35a84a68c82f.svg"
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


def _mx(p):
    return (48 - p[0], p[1])


class RoundedRectangularBridgeEyeglasses(Solo48):
    """Glasses with rounded-rectangle lenses and an arched bridge, seen from the front.

    Plan: CIRCLE, so the flat frame keeps its proportions; only the outer lens sides reach r20
    at (4,24)/(44,24). Each lens: flat top at y=16, soft top-outer corner, big rounded lower
    outer corner, small rounded lower inner corner, straight inner side. Inner sides at x=19
    and x=29; a shallow r13 bridge arches between the top corners. Mirrored about x=24 (the old
    drawing was tilted and broken apart).
    """
    icon_id = "rounded-rectangular-bridge-eyeglasses"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ("sunglasses", "glasses", "eyeglasses")
    keywords = ("sunglasses", "glasses", "eyeglasses", "shades", "lens", "summer", "vision")

    def build(self) -> None:
        lens = [
            ("L", (9, 16)),
            ("C", (6, 16), (4, 19), (4, 24)),
            ("C", (4, 29), (7, 32), (12, 32)),
            ("L", (14, 32)),
            ("C", (17, 32), (19, 30), (19, 27)),
            ("L", (19, 16)),
        ]
        _path(self, "lens-left", (19, 16), lens, closed=True)
        rl = []
        for st in lens:
            rl.append(("L", _mx(st[1])) if st[0] == "L" else ("C", _mx(st[1]), _mx(st[2]), _mx(st[3])))
        _path(self, "lens-right", (29, 16), rl, closed=True)
        self.add_arc("bridge", (19, 16), (29, 16), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.relate("connect", "lens-left", "bridge")
        self.relate("connect", "lens-right", "bridge")
