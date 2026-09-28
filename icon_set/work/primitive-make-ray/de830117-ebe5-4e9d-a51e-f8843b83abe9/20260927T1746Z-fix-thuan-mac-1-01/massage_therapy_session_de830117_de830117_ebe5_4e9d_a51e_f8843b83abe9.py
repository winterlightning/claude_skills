from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "de830117-ebe5-4e9d-a51e-f8843b83abe9"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__massage-therapy-session-de830117/20260927T174444Z-thuan-mac-1/reference/massage top_de830117-ebe5-4e9d-a51e-f8843b83abe9.svg"
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


class MassageTherapySession(Solo48):
    """A massage session: a therapist leans over and presses a hand onto the back of a client
    lying face down, whose head rests at the far end of the body.

    Plan: SQUARE. Therapist = r4 ring head (12,10) (top 6) over a bust silhouette: straight
    back x 6, r8 shoulder round to (14,22), then the arm straight down to the hand H (20,34).
    Client = a hump rising from the floor (15,42) through H to an r5 ring head about (33,28)
    and dropping from it to the canvas corner (42,42); a floor line closes it.
    """
    icon_id = "massage-therapy-session-de830117"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/health"
    aliases = ("massage", "massage therapy", "back massage", "spa")
    keywords = ("massage", "therapy", "therapist", "spa", "relax", "wellness", "back", "physiotherapy")

    def build(self) -> None:
        _circle(self, "therapist-head", 12, 10, 4)
        _path(self, "therapist", (6, 42), [
            ("L", (6, 30)),
            ("A", (14, 22), 8, True),
            ("L", (20, 34)),
        ])
        self.mark_human_figure("therapist", head="therapist-head", torso="therapist-2", torso_junction="end")
        _path(self, "client-body", (15, 42), [
            ("C", (15, 38), (17, 35), (20, 34)),
            ("C", (23, 33), (26, 31), (28, 28)),
        ])
        _circle(self, "client-head", 33, 28, 5)
        self.add_bezier("client-legs", (38, 28), ((41, 32), (42, 37), (42, 42)))
        self.add_line("floor", (15, 42), (42, 42))
        self.relate("connect", "therapist", "client-body")
        self.relate("connect", "client-body", "client-head")
        self.relate("connect", "client-head", "client-legs")
        self.relate("connect", "client-legs", "floor")
        self.relate("connect", "client-body", "floor")
