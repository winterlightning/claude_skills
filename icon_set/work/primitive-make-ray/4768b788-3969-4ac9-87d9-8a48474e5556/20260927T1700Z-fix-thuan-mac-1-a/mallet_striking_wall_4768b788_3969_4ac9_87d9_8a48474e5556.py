from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4768b788-3969-4ac9-87d9-8a48474e5556"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__mallet-striking-wall/20260927T164509Z-thuan-mac-1/reference/home improvement 7_4768b788-3969-4ac9-87d9-8a48474e5556.svg"
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


class MalletStrikingWall(Solo48):
    """A mallet striking a wall: an upright wall line at the left, three impact rays between
    the wall and the mallet face, and a mallet with a rounded head and a handle angled down.

    Plan: SQUARE (6,6)-(42,42). Wall x=6 full height. Mallet head rounded rectangle
    (26,13)-(42,23) r4 from standalone edges joined in a ring; handle from the head bottom
    node (34,23) down to (29,42). Impact rays fanning out, mirrored about y=18: (14,10)-(18,6),
    (14,18)-(18,18), (14,26)-(18,30), each 8+ from the wall, the head and each other.
    """
    icon_id = "mallet-striking-wall"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ("home improvement", "hammer on wall", "mallet")
    keywords = ("mallet", "hammer", "wall", "strike", "repair", "home improvement", "tool")

    def build(self) -> None:
        self.add_line("wall", (6, 6), (6, 42))
        L, T, R, B, r = 26, 13, 42, 23, 4
        segs = [("head-top", "L", (L + r, T), (R - r, T)), ("head-tr", "A", (R - r, T), (R, T + r)),
                ("head-right", "L", (R, T + r), (R, B - r)), ("head-br", "A", (R, B - r), (R - r, B)),
                ("head-bottom-r", "L", (R - r, B), (34, B)), ("head-bottom-l", "L", (34, B), (L + r, B)),
                ("head-bl", "A", (L + r, B), (L, B - r)),
                ("head-left", "L", (L, B - r), (L, T + r)), ("head-tl", "A", (L, T + r), (L + r, T))]
        for name, kind, a, b in segs:
            if kind == "L":
                self.add_line(name, a, b)
            else:
                self.add_arc(name, a, b, radius_x=r, radius_y=r, sweep=True)
        for (n1, *_), (n2, *_) in zip(segs, segs[1:] + segs[:1]):
            self.relate("connect", n1, n2)
        self.add_line("handle", (34, 23), (29, 42))
        self.relate("connect", "head-bottom-r", "handle")
        self.relate("connect", "head-bottom-l", "handle")
        self.add_line("ray-top", (14, 10), (18, 6))
        self.add_line("ray-mid", (14, 18), (18, 18))
        self.add_line("ray-bottom", (14, 26), (18, 30))
