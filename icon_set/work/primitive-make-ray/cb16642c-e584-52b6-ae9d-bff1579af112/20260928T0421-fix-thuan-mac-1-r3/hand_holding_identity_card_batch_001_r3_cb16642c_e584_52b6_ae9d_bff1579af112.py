"""Hand from the bottom right presenting a portrait ID card, thumb over its
lower-right corner.

Plan: vertical counterpart of the r2 layout. Card = standalone edges + r3
corners in a ring (6..32 x 6..34); portrait = r3 ring head at (17,17) with
shoulders replacing part of the bottom edge (rx6 ry3, top 31). Thumb = 3-4-5
tube on the (3,4) axis, C=(32,27): upper side (36,24)-(42,32), lower side
(28,30)-(31,34)-(37,42), r5 tip split at the right-edge end (32,22). One
finger stroke behind the card bottom. SQUARE.
Human reference: icon_set/references/human_ref/user.svg.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "cb16642c-e584-52b6-ae9d-bff1579af112"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__hand-holding-identity-card-batch-001-r3/20260928T042124Z-thuan-mac-1/reference/digital policies data breach user_cb16642c-e584-52b6-ae9d-bff1579af112.svg"
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



class HandHoldingIdentityCardBatch001R3(Solo48):
    icon_id = "hand-holding-identity-card-batch-001-r3"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "apps"
    categories = ("apps", "primitives")
    aliases = ("digital-policies-data-breach-user", "present-id-card")
    keywords = ("hand", "identity", "card", "id", "badge", "user", "verification", "holding")

    def build(self) -> None:
        self.add_line("card-bottom", (31, 34), (23, 34))
        self.add_arc("shoulders", (23, 34), (11, 34), radius_x=6, radius_y=3, sweep=True)
        self.add_line("card-bottom-l", (11, 34), (9, 34))
        self.add_arc("card-bl", (9, 34), (6, 31), radius_x=3, sweep=True)
        self.add_line("card-left", (6, 31), (6, 9))
        self.add_arc("card-tl", (6, 9), (9, 6), radius_x=3, sweep=True)
        self.add_line("card-top", (9, 6), (29, 6))
        self.add_arc("card-tr", (29, 6), (32, 9), radius_x=3, sweep=True)
        self.add_line("card-right", (32, 9), (32, 22))
        ring = ["card-bottom", "shoulders", "card-bottom-l", "card-bl", "card-left", "card-tl",
                "card-top", "card-tr", "card-right"]
        for a, b in zip(ring, ring[1:]):
            self.relate("connect", a, b)
        _circle(self, "head", 17, 17, 3)
        self.mark_human_figure("portrait", head="head", torso="shoulders", torso_junction="end")
        # thumb over the bottom-right corner (mirror of r2 about y=24)
        self.add_line("thumb-lower-out", (37, 42), (31, 34))
        self.add_line("thumb-lower-in", (31, 34), (28, 30))
        self.add_arc("tip-left", (28, 30), (32, 22), radius_x=5, sweep=True)
        self.add_arc("tip-right", (32, 22), (36, 24), radius_x=5, sweep=True)
        self.add_line("thumb-upper", (36, 24), (42, 32))
        self.add_contour("thumb", "thumb-lower-out", "thumb-lower-in", "tip-left", "tip-right", "thumb-upper")
        self.relate("connect", "thumb", "card-bottom")
        self.relate("connect", "thumb", "card-right")
        self.add_line("finger", (17, 34), (23, 42))
        self.relate("connect", "finger", "card-bottom-l")
        self.relate("connect", "finger", "shoulders")
