"""Fire extinguisher: tall cylinder with a domed top, a label band, a neck, a horn nozzle to the right and a
hose looping down the left. VRECT_L (8,4)-(40,44).
Plan: body walls x16/x32 from y24 to a rounded floor at 44, dome r8 about (24,24), neck to y8, horn funnel
(40,4)-(32,8)-(40,12), hose (24,8)-(16,8) arc r8 to (8,16) then down to (8,32). Band at y33 (9 from the dome ends).
Construction reference: Lucide fire-extinguisher (cylinder + hose loop) proportions on this grid."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3f9582f0-2d09-40b4-9994-e281fa50f35f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__fire-extinguisher-with-horn-nozzle-batch-045/20260927T174430Z-thuan-mac-1/reference/fire extinguisher_3f9582f0-2d09-40b4-9994-e281fa50f35f.svg"
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



class FireExtinguisherWithHornNozzle(Solo48):
    icon_id = "fire-extinguisher-with-horn-nozzle-batch-045"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("fire-extinguisher",)
    keywords = ("fire", "extinguisher", "safety", "horn", "nozzle", "hose")

    def build(self) -> None:
        _path(self, "body", (16, 24), [
            ("A", (24, 16), 8, True),
            ("A", (32, 24), 8, True),
            ("L", (32, 33)),
            ("L", (32, 41)),
            ("A", (29, 44), 3, True),
            ("L", (19, 44)),
            ("A", (16, 41), 3, True),
            ("L", (16, 33)),
            ("L", (16, 24)),
        ], True)
        self.add_line("band", (16, 33), (32, 33))
        self.add_line("neck", (24, 16), (24, 8))
        self.add_line("horn-pipe", (24, 8), (32, 8))
        self.add_polyline("horn", (40, 4), (32, 8), (40, 12))
        _path(self, "hose", (24, 8), [
            ("L", (16, 8)),
            ("A", (8, 16), 8, False),
            ("L", (8, 32)),
        ])
        self.relate("connect", "band", "body")
        self.relate("connect", "neck", "body")
        self.relate("connect", "neck", "horn-pipe")
        self.relate("connect", "neck", "hose")
        self.relate("connect", "horn-pipe", "horn")
