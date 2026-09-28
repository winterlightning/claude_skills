from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2b81b158-1000-5c01-96ea-05c64a806041"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__mustard-hot-dog-diagonal/20260927T164821Z-thuan-mac-1/reference/hot dog grilled_2b81b158-1000-5c01-96ea-05c64a806041.svg"
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



class MustardHotDogDiagonal(Solo48):
    """Hot dog on the diagonal: a rounded bun split lengthwise by the wavy mustard line on the
    sausage, so both bun halves show.

    Plan: CIRCLE. Bun = pill on the 3:4 diagonal with r10 caps about (18,32)/(30,16) whose apexes
    (12,40)/(36,8) sit exactly at r20; walls (10,26)-(22,10) and (26,38)-(38,22) are 10 from the
    axis. Mustard = four cubic wave segments along the axis, knots every 10, crests 1.65 across,
    joined to the bun at both apexes.
    """
    icon_id = "mustard-hot-dog-diagonal"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("hot dog", "hotdog with mustard", "frankfurter")
    keywords = ("hot dog", "mustard", "sausage", "bun", "food", "fast food", "snack")

    def build(self) -> None:
        _path(self, "bun", (12, 40), [("A", (26, 38), 10, False), ("L", (38, 22)), ("A", (36, 8), 10, False),
                                      ("A", (22, 10), 10, False), ("L", (10, 26)), ("A", (12, 40), 10, False)],
              closed=True)
        knots = [(12, 40), (18, 32), (24, 24), (30, 16), (36, 8)]
        along, across = (1.2, -1.6), (1.76, 1.32)
        steps = []
        for i in range(4):
            p0, p1 = knots[i], knots[i + 1]
            s = 1 if i % 2 == 0 else -1
            c1 = (p0[0] + along[0] + s * across[0], p0[1] + along[1] + s * across[1])
            c2 = (p1[0] - along[0] + s * across[0], p1[1] - along[1] + s * across[1])
            steps.append(("C", c1, c2, p1))
        _path(self, "mustard", knots[0], steps)
        self.relate("connect", "mustard", "bun")
