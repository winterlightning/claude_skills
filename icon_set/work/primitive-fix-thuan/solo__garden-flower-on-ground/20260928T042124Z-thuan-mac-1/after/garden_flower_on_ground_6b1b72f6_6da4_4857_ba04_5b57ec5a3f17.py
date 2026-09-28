"""Garden flower: quatrefoil bloom (four r5 semicircle petals, lattice notches) on a
stem with two curved leaves rising from the ground line.

Plan: ring r5 at (24,19); petal arcs r5 (large) from 3-4-5 points on the ring,
centres 8 from the ring centre: top (24,11) -> apex 6, sides 11/37, bottom 32.
Stem (24,32)-(24,42); ground (6,42)-(42,42); leaves = cubics from the stem foot
to (6,32)/(42,32) with the tip control level so x=6/42 are exact. SQUARE.
Reduction: five petals become four (Lucide construction).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6b1b72f6-6da4-4857-ba04-5b57ec5a3f17"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__garden-flower-on-ground/20260928T042124Z-thuan-mac-1/reference/garden_6b1b72f6-6da4-4857-ba04-5b57ec5a3f17.svg"
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



class GardenFlowerOnGround(Solo48):
    icon_id = "garden-flower-on-ground"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("garden", "flower-bed")
    keywords = ("flower", "garden", "plant", "bloom", "petals", "leaves", "ground")

    def build(self) -> None:
        # quatrefoil bloom: four r5 semicircle petals about (24,18), lattice notches
        cx, cy, r = 24, 16, 5
        _path(self, "bloom", (cx - r, cy - r), [
            ("A", (cx + r, cy - r), r, True),   # top petal, apex (24,6)
            ("A", (cx + r, cy + r), r, True),   # right petal
            ("A", (cx - r, cy + r), r, True),   # bottom petal, apex (24,30)
            ("A", (cx - r, cy - r), r, True),   # left petal
        ], True)
        self.add_line("stem", (24, 26), (24, 42))
        self.relate("connect", "bloom", "stem")
        self.add_line("ground", (6, 42), (42, 42))
        self.relate("connect", "stem", "ground")
        self.add_bezier("leaf-left", (24, 42), ((22, 33), (14, 31), (6, 30)))
        self.add_bezier("leaf-right", (24, 42), ((26, 33), (34, 31), (42, 30)))
        for m in ("leaf-left", "leaf-right"):
            self.relate("connect", "stem", m)
            self.relate("connect", "ground", m)
