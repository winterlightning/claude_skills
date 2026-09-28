from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "04dc2fcf-0f0c-4e8b-b40b-5ae745f490db"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__rounded-server-connected-to-hexagonal-hub/20260927T172638Z-thuan-mac-1/reference/elemental live 1_04dc2fcf-0f0c-4e8b-b40b-5ae745f490db.svg"
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


class RoundedServerConnectedToHexagonalHub(Solo48):
    """A rounded server box linked by a cable to a hexagonal hub with three outgoing links.

    Plan: VRECT_L. Box (8..40, 4..20) with r4 corners, its walls standalone lines so the
    status dot (16,12) and the drive slot (24..32, y12) sit exactly 8 inside. A stem drops
    from the box floor to a pointy-top hexagon (24,28)-(24,40), 8 below the box; links run
    from the hex side midpoints to the frame edges x=8/x=40 and from the bottom vertex to
    y=44, as in the reference. The old hex was squashed and the links stubby.
    """
    icon_id = "rounded-server-connected-to-hexagonal-hub"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/network"
    aliases = ("server hub", "elemental live", "server network")
    keywords = ("server", "network", "hub", "node", "cloud", "hexagon", "connection", "infrastructure")

    def build(self) -> None:
        self.add_arc("corner-tl", (8, 8), (12, 4), radius_x=4, radius_y=4, sweep=True)
        self.add_line("top", (12, 4), (36, 4))
        self.add_arc("corner-tr", (36, 4), (40, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_line("right", (40, 8), (40, 16))
        self.add_arc("corner-br", (40, 16), (36, 20), radius_x=4, radius_y=4, sweep=True)
        self.add_line("bottom-r", (36, 20), (24, 20))
        self.add_line("bottom-l", (24, 20), (12, 20))
        self.add_arc("corner-bl", (12, 20), (8, 16), radius_x=4, radius_y=4, sweep=True)
        self.add_line("left", (8, 16), (8, 8))
        ring = ["corner-tl", "top", "corner-tr", "right", "corner-br", "bottom-r", "bottom-l", "corner-bl", "left", "corner-tl"]
        for a, b in zip(ring, ring[1:]):
            self.relate("connect", a, b)
        self.add_dot("status", (16, 12))
        self.add_line("slot", (24, 12), (32, 12))
        self.add_line("stem", (24, 20), (24, 28))
        self.relate("connect", "stem", "bottom-r")
        self.relate("connect", "stem", "bottom-l")
        _path(self, "hub", (24, 28), [
            ("L", (29, 31)), ("L", (29, 34)), ("L", (29, 37)), ("L", (24, 40)),
            ("L", (19, 37)), ("L", (19, 34)), ("L", (19, 31)), ("L", (24, 28)),
        ], closed=True)
        self.relate("connect", "stem", "hub")
        self.add_line("link-left", (19, 34), (8, 34))
        self.add_line("link-right", (29, 34), (40, 34))
        self.add_line("link-down", (24, 40), (24, 44))
        for l in ("link-left", "link-right", "link-down"):
            self.relate("connect", "hub", l)
