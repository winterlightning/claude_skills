from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8151d499-4365-4040-96c3-3b98701238fa"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__rear-air-conditioner/20260927T170824Z-thuan-mac-1/reference/air conditioner rear 1_8151d499-4365-4040-96c3-3b98701238fa.svg"
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

class RearAirConditioner(Solo48):
    """An air-conditioner unit with wavy airflow arrows rising up into it from below.

    Plan: HRECT_L. Unit: rounded rectangle x4-44, y8-28 (r4 corners), edges as standalone
    members joined in a ring. Two airflow arrows at x16/32: chevron tips at y16 inside the
    unit (arms +-4, 8 clear of the walls and of each other), straight shafts that cross the
    unit's bottom edge (split there, connected) and continue as S-waves to the bottom y40.
    """
    icon_id = "rear-air-conditioner"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/appliances"
    aliases = ("air conditioner", "ac unit", "air intake", "hvac")
    keywords = ("air", "conditioner", "ac", "hvac", "airflow", "cooling", "intake", "vent")

    def build(self) -> None:
        ring = [("corner-bl", (8, 28), ("A", (4, 24), 4, True)), ("side-l", (4, 24), ("L", (4, 12))),
                ("corner-tl", (4, 12), ("A", (8, 8), 4, True)), ("top", (8, 8), ("L", (40, 8))),
                ("corner-tr", (40, 8), ("A", (44, 12), 4, True)), ("side-r", (44, 12), ("L", (44, 24))),
                ("corner-br", (44, 24), ("A", (40, 28), 4, True)), ("bottom-r", (40, 28), ("L", (32, 28))),
                ("bottom-m", (32, 28), ("L", (16, 28))), ("bottom-l", (16, 28), ("L", (8, 28)))]
        for k, (name, start, step) in enumerate(ring):
            _path(self, name, start, [step])
            self.relate("connect", name, ring[k - 1][0])
        for x, edges in ((16, ("bottom-m", "bottom-l")), (32, ("bottom-r", "bottom-m"))):
            self.add_polyline(f"head-{x}", (x - 4, 20), (x, 16), (x + 4, 20))
            self.add_line(f"shaft-{x}", (x, 16), (x, 28))
            self.add_bezier(f"wave-{x}", (x, 28), ((x + 3, 32), (x - 3, 36), (x, 40)))
            self.relate("connect", f"shaft-{x}", f"head-{x}")
            self.relate("connect", f"shaft-{x}", f"wave-{x}")
            for e in edges:
                self.relate("connect", f"shaft-{x}", e)
                self.relate("connect", f"wave-{x}", e)
