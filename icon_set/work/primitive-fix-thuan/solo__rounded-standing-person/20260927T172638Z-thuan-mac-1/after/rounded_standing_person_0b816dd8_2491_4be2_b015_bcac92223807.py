from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0b816dd8-2491-4be2-b015-bcac92223807"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__rounded-standing-person/20260927T172638Z-thuan-mac-1/reference/body_0b816dd8-2491-4be2-b015-bcac92223807.svg"
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


class RoundedStandingPerson(Solo48):
    """A standing person drawn as an outlined figure: round head over a body with arms and legs.

    Plan: VRECT_L. r5 head about (24,9), exactly 8 above the flat shoulder line y=22. The body
    outline has rx8/ry6 shoulders out to x=8/x=40, arms down to hands at y=36, then steps in to
    the legs x=16/x=32 which run open to the base y=44. Inner arm lines x=16/x=32 rise from the
    hands to the shoulder line, and a leg split x=24 rises from the base to y=34; all 8 apart.
    The old stick figure did not match the outlined body of the reference.
    """
    icon_id = "rounded-standing-person"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/figures"
    aliases = ("person", "body", "human", "standing person")
    keywords = ("person", "body", "human", "figure", "user", "standing", "people")

    def build(self) -> None:
        _circle(self, "head", 24, 9, 5)
        parts = {}
        for side, sx in (("left", 1), ("right", -1)):
            X = lambda x: 24 + sx * (x - 24)
            parts[f"shoulder-{side}"] = ("A", (X(8), 28), (X(16), 22))
            parts[f"side-{side}"] = ("L", (X(8), 28), (X(8), 36))
            parts[f"hand-{side}"] = ("L", (X(8), 36), (X(16), 36))
            parts[f"leg-{side}"] = ("L", (X(16), 36), (X(16), 44))
            parts[f"arm-{side}"] = ("L", (X(16), 22), (X(16), 36))
        for name, (kind, a, b) in parts.items():
            if kind == "A":
                self.add_arc(name, a, b, radius_x=8, radius_y=6, sweep=name.endswith("left"))
            else:
                self.add_line(name, a, b)
        self.add_line("shoulder-line", (16, 22), (32, 22))
        self.add_line("legs", (24, 34), (24, 44))
        for side in ("left", "right"):
            for a, b in (("shoulder", "side"), ("side", "hand"), ("hand", "leg"), ("hand", "arm"), ("leg", "arm"), ("arm", "shoulder")):
                self.relate("connect", f"{a}-{side}", f"{b}-{side}")
            self.relate("connect", "shoulder-line", f"shoulder-{side}")
            self.relate("connect", "shoulder-line", f"arm-{side}")
