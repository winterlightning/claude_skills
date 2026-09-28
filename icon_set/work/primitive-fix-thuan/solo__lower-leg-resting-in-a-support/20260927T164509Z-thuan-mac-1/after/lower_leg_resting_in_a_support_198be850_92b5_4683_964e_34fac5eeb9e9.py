from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "198be850-92b5-4683-964e-34fac5eeb9e9"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__lower-leg-resting-in-a-support/20260927T164509Z-thuan-mac-1/reference/bandage leg hanging_198be850-92b5-4683-964e-34fac5eeb9e9.svg"
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


class LowerLegRestingInASupport(Solo48):
    """A lower leg hanging in a sling: shin and calf coming down from the top, the foot
    pointing left, a support strap meeting the shin from the left and an L-shaped tray
    (floor and back wall) under the heel.

    Plan: SQUARE (6,6)-(42,42). Leg outline: shin front x=20, ankle cubic into a steep instep,
    r4 toe cap about (12,29), sole y=33, r8 heel about (26,25), calf back bulging up to
    (32,6). Strap y=12 from x=6 to the shin. Tray: floor y=42 (9 under the sole), r4
    corner, back wall x=42 up to y=30, all standalone lines joined with `connect`.
    """
    icon_id = "lower-leg-resting-in-a-support"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "medical"
    categories = ("primitives", "medical")
    aliases = ("bandage leg hanging", "leg in sling", "leg traction")
    keywords = ("leg", "foot", "sling", "support", "injury", "medical", "traction")

    def build(self) -> None:
        _path(self, "leg", (18, 6), [("L", (18, 17)), ("C", (18, 21), (14, 24), (9, 27)),
                                     ("A", (9, 33), 3, False), ("L", (27, 33)),
                                     ("A", (33, 27), 6, False), ("C", (33, 22), (29, 21), (29, 16)),
                                     ("L", (29, 6))])
        self.add_line("floor", (6, 42), (38, 42))
        self.add_arc("tray-corner", (38, 42), (42, 38), radius_x=4, radius_y=4, sweep=False)
        self.add_line("wall", (42, 38), (42, 30))
        self.relate("connect", "floor", "tray-corner")
        self.relate("connect", "tray-corner", "wall")
