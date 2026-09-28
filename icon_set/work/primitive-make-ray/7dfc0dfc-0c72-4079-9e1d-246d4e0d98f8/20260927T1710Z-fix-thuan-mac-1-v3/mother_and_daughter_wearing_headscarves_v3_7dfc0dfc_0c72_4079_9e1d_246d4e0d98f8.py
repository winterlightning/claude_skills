from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7dfc0dfc-0c72-4079-9e1d-246d4e0d98f8"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__mother-and-daughter-wearing-headscarves-v3/20260927T164821Z-thuan-mac-1/reference/muslim mom daughter_7dfc0dfc-0c72-4079-9e1d-246d4e0d98f8.svg"
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



class MotherAndDaughterWearingHeadscarvesV3(Solo48):
    """Mother and daughter in headscarves: two hooded busts, the taller mother behind and the
    small daughter in front, each face inside its scarf arch.

    Plan: HRECT_L. Mirrored open busts: mother (r12 scarf arch, r3 face ring) at the left, daughter (r10 arch, dot face) in front at the right; the mother's near side ends on the daughter's arch at (28,23).
    Scarf arches flow straight down into the bodies; faces sit at the arch centres (>= 9 clear).
    """
    icon_id = "mother-and-daughter-wearing-headscarves-v3"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("muslim mom and daughter", "hijab mother and child")
    keywords = ("mother", "daughter", "muslim", "headscarf", "hijab", "family", "people", "portrait", "islam")

    def build(self) -> None:
        self.add_arc("mother-arch", (28, 20), (4, 20), radius_x=12, sweep=False)
        self.add_line("mother-side-far", (4, 20), (4, 40))
        self.add_line("mother-side-near", (28, 20), (28, 23))
        self.relate("connect", "mother-arch", "mother-side-far")
        self.relate("connect", "mother-arch", "mother-side-near")
        _circle(self, "mother-face", 16, 20, 3)
        self.add_arc("daughter-arch-near", (24, 31), (28, 23), radius_x=10, sweep=True)
        self.add_arc("daughter-arch-top", (28, 23), (44, 31), radius_x=10, sweep=True)
        self.add_contour("daughter-arch", "daughter-arch-near", "daughter-arch-top")
        self.relate("connect", "mother-side-near", "daughter-arch")
        self.add_line("daughter-side-near", (24, 31), (24, 40))
        self.add_line("daughter-side-far", (44, 31), (44, 40))
        self.relate("connect", "daughter-arch", "daughter-side-near")
        self.relate("connect", "daughter-arch", "daughter-side-far")
        self.add_dot("daughter-face", (34, 31))
