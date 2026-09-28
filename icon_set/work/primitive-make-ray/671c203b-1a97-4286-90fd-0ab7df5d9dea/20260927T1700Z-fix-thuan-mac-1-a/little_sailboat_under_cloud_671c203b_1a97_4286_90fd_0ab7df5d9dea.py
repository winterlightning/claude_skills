from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "671c203b-1a97-4286-90fd-0ab7df5d9dea"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__little-sailboat-under-cloud/20260927T164509Z-thuan-mac-1/reference/business boat success_671c203b-1a97-4286-90fd-0ab7df5d9dea.svg"
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


class LittleSailboatUnderCloud(Solo48):
    """A little paper sailboat on a wave under a small cloud.

    Plan: SQUARE (6,6)-(42,42). Hull = trapezoid (6,24)-(29,24) over (11,32)-(24,32);
    triangular sail on the hull top from (8,24)/(22,24) up to (14,10). Cloud at the top
    right: bottom (30,16)-(38,16), r4 end lobes about (30,12)/(38,12) (right 42) and an r5
    crown arc (38,8)->(30,8) peaking at y=6. Wave: cubic line across the bottom, knots at
    y=41, crests 40.25 and troughs exactly 42.
    """
    icon_id = "little-sailboat-under-cloud"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport"
    categories = ("primitives", "transport")
    aliases = ("business boat success", "paper boat", "sailboat")
    keywords = ("sailboat", "boat", "paper boat", "cloud", "sea", "wave", "sail")

    def build(self) -> None:
        _path(self, "hull", (6, 24), [("L", (8, 24)), ("L", (22, 24)), ("L", (29, 24)), ("L", (24, 32)),
                                      ("L", (11, 32)), ("L", (6, 24))], closed=True)
        _path(self, "sail", (8, 24), [("L", (14, 10)), ("L", (22, 24))])
        self.relate("connect", "hull", "sail")
        self.add_line("cloud-bottom", (30, 16), (38, 16))
        _path(self, "cloud", (38, 16), [("A", (38, 8), 4, False), ("A", (30, 8), 5, False), ("A", (30, 16), 4, False)])
        self.relate("connect", "cloud-bottom", "cloud")
        # Wave: knots on y=41, crests at 40.25 and troughs exactly at 42 (equal controls).
        segs, x = [], 6
        for i in range(6):
            y = 40 if i % 2 == 0 else 41 + 4 / 3
            segs.append(("C", (x + 2, y), (x + 4, y), (x + 6, 41)))
            x += 6
        _path(self, "wave", (6, 41), segs)
