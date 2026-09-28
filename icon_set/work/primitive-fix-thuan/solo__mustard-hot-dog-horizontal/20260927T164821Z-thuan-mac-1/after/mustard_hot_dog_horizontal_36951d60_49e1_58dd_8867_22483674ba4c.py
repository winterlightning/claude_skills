from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "36951d60-49e1-58dd-8867-22483674ba4c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__mustard-hot-dog-horizontal/20260927T164821Z-thuan-mac-1/reference/hot dog_36951d60-49e1-58dd-8867-22483674ba4c.svg"
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



class MustardHotDogHorizontal(Solo48):
    """Horizontal hot dog: a top bun loaf, the sausage shown by its wavy mustard line, and a
    bottom bun loaf stacked like the original.

    Plan: SQUARE. Top bun = open arch shell (r5 corners, legs to y16); bottom bun = open bowl shell (legs from
    y32); the shells' leg ends are 8.5 from the wave ends.
    Mustard = three cubic wave segments from (9,24) to (39,24), knots every 10, controls +-2
    (extremes 1.5, so 8.5 clear of both loaf walls); mirror-symmetric about x24.
    """
    icon_id = "mustard-hot-dog-horizontal"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("hot dog", "hotdog with mustard", "frankfurter")
    keywords = ("hot dog", "mustard", "sausage", "bun", "food", "fast food", "snack")

    def build(self) -> None:
        # top bun: an open arch shell (legs down to y16) over the sausage
        _path(self, "bun-top", (6, 16), [("L", (6, 11)), ("A", (11, 6), 5, True), ("L", (37, 6)),
                                         ("A", (42, 11), 5, True), ("L", (42, 16))])
        # bottom bun: an open bowl shell (legs up to y32) under the sausage
        _path(self, "bun-bottom", (6, 32), [("L", (6, 37)), ("A", (11, 42), 5, False), ("L", (37, 42)),
                                            ("A", (42, 37), 5, False), ("L", (42, 32))])
        steps = []
        for i in range(3):
            x0, x1 = 9 + 10 * i, 19 + 10 * i
            h = 22 if i % 2 == 0 else 26
            steps.append(("C", (x0 + 3, h), (x1 - 3, h), (x1, 24)))
        _path(self, "mustard", (9, 24), steps)
