from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "09b060de-331e-4760-a299-7d321fd12cd5"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__potato-head-toy/20260927T170824Z-thuan-mac-1/reference/mr potato head_09b060de-331e-4760-a299-7d321fd12cd5.svg"
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

class PotatoHeadToy(Solo48):
    """Mr. Potato Head: a potato-shaped head with side ears, a bowler hat, eyes, nose and a
    wide smile.

    Plan: VRECT_L. Bowler hat: a crown (rx10/ry6 arc, top y4) on a brim line that runs the
    full width (x8-40) at y10 and caps the head. Head: straight sides at x11/x37 with r3
    ears bulging to the edges below the brim, then an rx13/ry12 rounded bottom (y44).
    Face: dot eyes 9 below the brim, a nose dot, and a cubic smile, all 8+ apart.
    """
    icon_id = "potato-head-toy"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/toys"
    aliases = ("mr potato head", "potato head", "toy")
    keywords = ("potato", "toy", "mr potato head", "hat", "face", "kids", "play")

    def build(self) -> None:
        brim = [((8, 10), (11, 10)), ((11, 10), (14, 10)), ((14, 10), (34, 10)), ((34, 10), (37, 10)), ((37, 10), (40, 10))]
        names = [f"brim-{k}" for k in range(len(brim))]
        for n, (a, b) in zip(names, brim):
            self.add_line(n, a, b)
        for a, b in zip(names, names[1:]):
            self.relate("connect", a, b)
        _path(self, "crown", (14, 10), [("A", (34, 10), 10, 6, True)])
        _path(self, "head", (11, 10), [
            ("L", (11, 20)), ("A", (11, 26), 3, False), ("L", (11, 32)), ("A", (37, 32), 13, 12, False),
            ("L", (37, 26)), ("A", (37, 20), 3, False), ("L", (37, 10)),
        ])
        for b in ("brim-1", "brim-2"):
            self.relate("connect", "crown", b)
        for b in ("brim-0", "brim-1", "brim-3", "brim-4"):
            self.relate("connect", "head", b)
        self.add_dot("eye-left", (20, 19))
        self.add_dot("eye-right", (28, 19))
        self.add_dot("nose", (24, 26))
        self.add_bezier("smile", (20, 33), ((21, 35), (27, 35), (28, 33)))
