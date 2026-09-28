"""Index finger from the top right pressing on a house's roof.

Plan: Lucide `house` outline (apex (17,8), 45-degree eaves, r3 floor corners,
SQUARE). Finger = 3-4-5 tube on the (3,-4) axis, centre C=(32,16): sides
x+y=41 (28,19)->(35,6)... upper side (29,12)->(35,6), lower side (36,19)->(42,13),
r5 tip split at the roof contact (28,19) and the wall start (32,21) so the roof
ends on the tip and the right wall starts under it.
Reduction: the curled second finger is dropped.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1f58e0b9-2d9d-4e01-88b6-5e110128d93c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__finger-touching-house-outline/20260928T042124Z-thuan-mac-1/reference/ginger bread house_1f58e0b9-2d9d-4e01-88b6-5e110128d93c.svg"
AUTHOR = "claude-fable-5-1"


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


def _H(p1, t1, p2, t2, k=1.0):
    """One Hermite cubic step for _path: controls at chord/3*k along unit tangents."""
    import math
    def unit(v):
        n = math.hypot(*v)
        return (v[0] / n, v[1] / n)
    L = math.hypot(p2[0] - p1[0], p2[1] - p1[1]) / 3 * k
    u1, u2 = unit(t1), unit(t2)
    return ("C", (p1[0] + u1[0] * L, p1[1] + u1[1] * L), (p2[0] - u2[0] * L, p2[1] - u2[1] * L), p2)



class FingerTouchingHouseOutline(Solo48):
    icon_id = "finger-touching-house-outline"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("tap-house", "select-home")
    keywords = ("finger", "house", "touch", "tap", "home", "select", "point")

    def build(self) -> None:
        # house (traversed clockwise from the wall start under the finger tip)
        self.add_line("wall-right", (32, 21), (32, 39))
        self.add_arc("corner-br", (32, 39), (29, 42), radius_x=3, sweep=True)
        self.add_line("floor", (29, 42), (9, 42))
        self.add_arc("corner-bl", (9, 42), (6, 39), radius_x=3, sweep=True)
        self.add_line("wall-left", (6, 39), (6, 19))
        self.add_line("roof-left", (6, 19), (17, 8))
        self.add_line("roof-right", (17, 8), (28, 19))
        self.add_contour("house", "wall-right", "corner-br", "floor", "corner-bl", "wall-left",
                         "roof-left", "roof-right")
        # finger
        self.add_line("finger-upper", (35, 6), (29, 12))
        self.add_arc("tip-left", (29, 12), (28, 19), radius_x=5, sweep=False)
        self.add_arc("tip-bottom", (28, 19), (32, 21), radius_x=5, sweep=False)
        self.add_arc("tip-right", (32, 21), (36, 19), radius_x=5, sweep=False)
        self.add_line("finger-lower", (36, 19), (42, 13))
        self.add_contour("finger", "finger-upper", "tip-left", "tip-bottom", "tip-right", "finger-lower")
        self.relate("connect", "house", "finger")
