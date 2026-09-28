from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7389d596-ba6d-4622-a96a-4308a96a11cd"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__night-hail/20260927T164821Z-thuan-mac-1/reference/weather night hail_7389d596-ba6d-4622-a96a-4308a96a11cd.svg"
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



class NightHail(Solo48):
    """Night hail: a crescent moon beside a cloud with hailstones falling below.

    Plan: SQUARE. Moon = r5 arc about (11,11) hitting the top and left extremes, open toward the
    cloud. Cloud = r10 arc about (32,20) (east point 42) into a base at y30, an r6 bump about
    (25,24) and a short neck; the moon stays 9+ from every cloud member. Precipitation hangs
    below the base with the bottom extreme at 42.
    """
    icon_id = "night-hail"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ("hail at night", "night hailstorm")
    keywords = ("weather", "night", "hail", "cloud", "moon", "storm", "forecast")

    def build(self) -> None:
        # crescent moon: r5 arc about (11,11) open toward the cloud (ends at the 3-4-5 points)
        self.add_arc("moon", (14, 7), (14, 15), radius_x=5, large_arc=True, sweep=False)
        # cloud: big r10 arc about (32,20), base, small r6 bump about (25,24), connector back up
        self.add_arc("cloud-big", (26, 12), (32, 30), radius_x=10, large_arc=True, sweep=True)
        self.add_line("cloud-base-right", (32, 30), (28, 30))
        self.add_line("cloud-base-left", (28, 30), (25, 30))
        self.add_arc("cloud-bump", (25, 30), (25, 18), radius_x=6, sweep=True)
        self.add_line("cloud-neck", (25, 18), (26, 12))
        self.add_contour("cloud", "cloud-big", "cloud-base-right", "cloud-base-left", "cloud-bump", "cloud-neck",
                         closed=True)
        self.add_dot("hail-1", (14, 42))
        self.add_dot("hail-2", (24, 42))
        self.add_dot("hail-3", (34, 42))
