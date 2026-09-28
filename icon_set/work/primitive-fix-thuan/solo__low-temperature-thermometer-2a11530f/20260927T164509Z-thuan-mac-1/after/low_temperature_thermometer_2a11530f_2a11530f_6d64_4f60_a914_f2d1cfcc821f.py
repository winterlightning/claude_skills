from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2a11530f-6d64-4f60-a914-f2d1cfcc821f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__low-temperature-thermometer-2a11530f/20260927T164509Z-thuan-mac-1/reference/temperature thermometer low_2a11530f-6d64-4f60-a914-f2d1cfcc821f.svg"
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


class LowTemperatureThermometerScale(Solo48):
    """Thermometer reading low with a scale of three tick marks beside the tube.

    Plan: VRECT_L (8,4)-(40,44). Tube half-width 6 (x 12..24) with an r6 cap about (18,10)
    (top 4) into an r10 bulb about (18,34) (left 8, bottom 44) at the 6-8-10 points
    (12,26)/(24,26). Mercury is a dot in the bulb only (low). Ticks x 32..40 at y 6/14/22,
    each 8+ from the tube wall and the bulb.
    """
    icon_id = "low-temperature-thermometer-2a11530f"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    categories = ("primitives", "weather")
    aliases = ("cold", "temperature low", "thermometer scale")
    keywords = ("low", "temperature", "thermometer", "cold", "scale", "weather")

    def build(self) -> None:
        # The right tube wall is a standalone line so the ticks' exact 8 certifies straight-vs-straight.
        _path(self, "thermometer", (24, 26), [("A", (12, 26), 10, True, True), ("L", (12, 10)),
                                              ("A", (24, 10), 6, True)])
        self.add_line("tube-right", (24, 10), (24, 26))
        self.relate("connect", "thermometer", "tube-right")
        self.add_dot("mercury", (18, 34))
        for y in (6, 14, 22):
            self.add_line(f"tick-{y}", (32, y), (40, y))
