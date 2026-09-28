from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "45a26188-cede-432f-ba35-4a8a0a60abee"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__masked-ninja-head-45a26188/20260927T174444Z-thuan-mac-1/reference/ninja_45a26188-cede-432f-ba35-4a8a0a60abee.svg"
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


class MaskedNinjaHead(Solo48):
    """A ninja's masked head: hood dome, a headband knotted at the side with two loose tails,
    the eye opening band with narrowed eyes, and the lower face covered.

    Plan: SQUARE. Head 28 wide (x 6..34): rx14/ry8 dome (top 6) and rx14/ry12 chin (bottom 42)
    on short straight sides. The headband (y 14) and the mask's upper edge (y 30) are standalone
    lines across the head, so the eye band is 16 tall and the two eye dashes at y 22 sit exactly
    8 from both lines and 8 apart. The knot at the head's right corner (34,14) sends two tails
    fanning to the canvas edge x 42.
    """
    icon_id = "masked-ninja-head-45a26188"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("ninja", "masked ninja", "shinobi")
    keywords = ("ninja", "mask", "headband", "warrior", "japan", "stealth", "martial arts", "avatar")

    def build(self) -> None:
        self.add_arc("dome", (6, 14), (34, 14), radius_x=14, radius_y=8, sweep=True)
        self.add_arc("chin", (34, 30), (6, 30), radius_x=14, radius_y=12, sweep=True)
        self.add_line("side-left", (6, 14), (6, 30))
        self.add_line("side-right", (34, 14), (34, 30))
        self.add_line("headband", (6, 14), (34, 14))
        self.add_line("mask-edge", (6, 30), (34, 30))
        ring = ("dome", "side-right", "chin", "side-left")
        for a, b in zip(ring, ring[1:] + ring[:1]):
            self.relate("connect", a, b)
        for a in ("dome", "side-left", "side-right"):
            self.relate("connect", a, "headband")
        for a in ("chin", "side-left", "side-right"):
            self.relate("connect", a, "mask-edge")
        self.add_line("eye-left", (14, 22), (16, 22))
        self.add_line("eye-right", (24, 22), (26, 22))
        self.add_bezier("tail-upper", (34, 14), ((37, 12), (40, 11), (42, 7)))
        self.add_bezier("tail-lower", (34, 14), ((37, 15), (40, 17), (42, 20)))
        for t in ("tail-upper", "tail-lower"):
            for a in ("dome", "side-right", "headband"):
                self.relate("connect", a, t)
        self.relate("connect", "tail-upper", "tail-lower")
