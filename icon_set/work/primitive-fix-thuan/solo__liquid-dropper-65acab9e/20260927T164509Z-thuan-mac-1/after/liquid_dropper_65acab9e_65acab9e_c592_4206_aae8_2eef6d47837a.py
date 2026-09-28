from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "65acab9e-c592-4206-aae8-2eef6d47837a"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__liquid-dropper-65acab9e/20260927T164509Z-thuan-mac-1/reference/instrument sampler_65acab9e-c592-4206-aae8-2eef6d47837a.svg"
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


class LiquidDropper(Solo48):
    """A liquid dropper (sampler pipette) held diagonally with a drop falling from its tip.

    Plan: SQUARE (6,6)-(42,42); the dropper is mirrored about the diagonal y=x. Bulb = r8
    circle about (14,14) (left 6, top 6) opened between its right and bottom cardinal
    points, which flare into a 45-degree tube (sides x-y=+-7) with an r5 cap about (26,26).
    Drop = upright teardrop: r4 lower half about (38,38) (right and bottom 42) with straight
    sides up to the point (38,32), about 9 from the tip.
    """
    icon_id = "liquid-dropper-65acab9e"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("primitives", "science")
    aliases = ("instrument sampler", "pipette", "eye dropper")
    keywords = ("dropper", "pipette", "sampler", "drop", "liquid", "lab", "science")

    def build(self) -> None:
        # Bulb r8 about (14,14) flaring from its right/bottom cardinal points into a
        # 45-degree tube (sides x-y=+-7) ending in an r5 3-4-5 cap about (26,26).
        _path(self, "dropper", (22, 14), [("A", (14, 22), 8, False, True), ("C", (16, 22), (17, 24), (19, 26)),
                                          ("L", (23, 30)), ("A", (30, 23), 5, False), ("L", (26, 19)),
                                          ("C", (24, 17), (22, 16), (22, 14))], closed=True)
        _path(self, "drop", (38, 32), [("L", (34, 38)), ("A", (42, 38), 4, False), ("L", (38, 32))], closed=True)
