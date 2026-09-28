from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a28d0f50-89ab-4114-8acd-5f487e570ca3"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__mammoth-with-long-trunk-and-curved-tusk/20260927T164509Z-thuan-mac-1/reference/mammoth_a28d0f50-89ab-4114-8acd-5f487e570ca3.svg"
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
        else:
            icon.add_bezier(m, here, (st[1], st[2], st[3])); here = st[3]
        members.append(m)
    icon.add_contour(name, *members, closed=closed)


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


class MammothWithLongTrunkAndCurvedTusk(Solo48):
    """Mammoth facing left: domed head with a hair notch, an eye, a long trunk hooking up at
    the tip, a curved tusk hooking forward from the mouth, a rounded back and two legs.

    Plan: HRECT_L (4,8)-(44,40). Head front H=(10,22); forehead domes to the top (18,8),
    dips at the hair notch (24,11) and the back rounds down to the rump side x=44. Legs:
    front 19..28 and rear 36..44 with an r4 arch between them. Trunk x=10 from H down to a
    J hook; the tusk leaves the trunk at the mouth node (10,30),
    dips forward and curves up to its tip (4,25).
    """
    icon_id = "mammoth-with-long-trunk-and-curved-tusk"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("primitives", "animals")
    aliases = ("mammoth", "woolly mammoth")
    keywords = ("mammoth", "tusk", "trunk", "prehistoric", "ice age", "animal")

    def build(self) -> None:
        H, X, C = (10, 22), (10, 32), (16, 28)
        self.add_line("front-leg", (19, 40), (19, 31))
        _path(self, "body", (19, 31), [("C", (19, 29), (18, 28), C), ("C", (14, 27), (11, 25), H),
                                       ("C", (10, 14), (13, 8), (18, 8)), ("C", (21, 8), (22, 11), (24, 11)),
                                       ("C", (34, 10), (44, 14), (44, 24))])
        self.relate("connect", "front-leg", "body")
        self.add_line("rear-leg", (44, 24), (44, 40))
        self.relate("connect", "body", "rear-leg")
        self.add_line("rear-leg-inner", (36, 40), (36, 34))
        self.add_arc("leg-arch", (36, 34), (28, 34), radius_x=4, radius_y=4, sweep=False)
        self.add_line("front-leg-inner", (28, 34), (28, 40))
        self.relate("connect", "rear-leg-inner", "leg-arch")
        self.relate("connect", "leg-arch", "front-leg-inner")
        _path(self, "trunk", H, [("L", X), ("L", (10, 37)), ("C", (10, 39), (11, 40), (13, 40))])
        self.add_bezier("tusk", X, ((6, 34), (4, 32), (4, 30)))
        self.add_bezier("tusk-tip", (4, 30), ((4, 28), (5, 27), (6, 26)))
        self.relate("connect", "tusk", "tusk-tip")
        self.relate("connect", "body", "trunk")
        self.relate("connect", "trunk", "tusk")
        self.add_dot("eye", (19, 18))
