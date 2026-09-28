from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "351711c6-091c-4ad6-9359-49de85c21a85"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__masked-person-bust-batch-051/20260927T174444Z-thuan-mac-1/reference/fraudster_351711c6-091c-4ad6-9359-49de85c21a85.svg"
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


class MaskedPersonBustBatch051(Solo48):
    """A fraudster: a bald head wearing a mask band across the eyes, over rounded shoulders.

    Plan: SQUARE. Head = capsule: rx10/ry8 crown about (24,14) (top 6), straight sides x 14/34 from
    y 14 to 22, r10 jaw about (24,22) (chin 32). The mask band fills the straight part between
    two standalone lines y 14 and y 22, like the reference's band across the eyes. The chin
    rests 4 above an rx18/ry6 shoulder arch (bust contact on the shared axis x 24).
    """
    icon_id = "masked-person-bust-batch-051"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    human_construction = "bust"
    aliases = ("fraudster", "masked person", "thief", "robber", "burglar")
    keywords = ("fraud", "fraudster", "thief", "mask", "robber", "criminal", "scam", "burglar", "avatar")

    def build(self) -> None:
        self.add_arc("crown", (14, 14), (34, 14), radius_x=10, radius_y=8, sweep=True)
        self.add_line("side-right", (34, 14), (34, 22))
        self.add_arc("jaw", (34, 22), (14, 22), radius_x=10, sweep=True)
        self.add_line("side-left", (14, 22), (14, 14))
        self.add_line("mask-top", (14, 14), (34, 14))
        self.add_line("mask-bottom", (14, 22), (34, 22))
        ring = ("crown", "side-right", "jaw", "side-left")
        for a, b in zip(ring, ring[1:] + ring[:1]):
            self.relate("connect", a, b)
        for a in ("crown", "side-left", "side-right"):
            self.relate("connect", a, "mask-top")
        for a in ("jaw", "side-left", "side-right"):
            self.relate("connect", a, "mask-bottom")
        self.add_arc("shoulders", (6, 42), (42, 42), radius_x=18, radius_y=6, sweep=True)
        self.relate("connect", "jaw", "shoulders")
