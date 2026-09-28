from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "38c7b142-9112-4996-82a7-8d6d958adc9f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__protective-hood-grille/20260927T170824Z-thuan-mac-1/reference/mask helmet_38c7b142-9112-4996-82a7-8d6d958adc9f.svg"
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

def _bump(p, q, h):
    import math
    dx, dy = q[0] - p[0], q[1] - p[1]
    L = math.hypot(dx, dy)
    k = h * 4 / 3
    nx, ny = dy / L * k, -dx / L * k          # bulge to the left of travel (down when moving left)
    return ("C", (p[0] + nx, p[1] + ny), (q[0] + nx, q[1] + ny), q)


class ProtectiveHoodGrille(Solo48):
    """A protective mask helmet (kendo men style): a domed hood around a barred face grille,
    flaring out into scalloped shoulder flaps.

    Plan: SQUARE. Grille: a rounded rectangle x18-30, y15-31 (r3 corners concentric with the
    hood's r12 top corners, so 9 clear) with a middle bar at y23, 8 from its straight top and
    bottom. Hood: top y6, sides x9/x39 that flare out to the edges x6/x42, and a hem of three
    scalloped flaps (the middle one a level bump down to the bottom edge y42).
    """
    icon_id = "protective-hood-grille"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ("mask helmet", "kendo mask", "men", "fencing mask", "protective hood")
    keywords = ("mask", "helmet", "kendo", "fencing", "grille", "protective", "hood", "martial arts")

    def build(self) -> None:
        _path(self, "hood", (9, 18), [
            ("A", (21, 6), 12, True), ("L", (27, 6)), ("A", (39, 18), 12, True), ("L", (39, 26)),
            ("C", (39, 32), (42, 33), (42, 38)),
            ("C", (42, 41.5), (35, 42), (31, 39)), _bump((31, 39), (17, 39), 3), ("C", (13, 42), (6, 41.5), (6, 38)),
            ("C", (6, 33), (9, 32), (9, 26)), ("L", (9, 18)),
        ], closed=True)
        g = [("g-top", (21, 15), ("L", (27, 15))), ("g-tr", (27, 15), ("A", (30, 18), 3, True)),
             ("g-r1", (30, 18), ("L", (30, 23))), ("g-r2", (30, 23), ("L", (30, 28))),
             ("g-br", (30, 28), ("A", (27, 31), 3, True)), ("g-bottom", (27, 31), ("L", (21, 31))),
             ("g-bl", (21, 31), ("A", (18, 28), 3, True)), ("g-l2", (18, 28), ("L", (18, 23))),
             ("g-l1", (18, 23), ("L", (18, 18))), ("g-tl", (18, 18), ("A", (21, 15), 3, True))]
        for i, (name, start, step) in enumerate(g):
            _path(self, name, start, [step])
            self.relate("connect", name, g[i - 1][0])
        self.add_line("bar", (18, 23), (30, 23))
        for p in ("g-l1", "g-l2", "g-r1", "g-r2"):
            self.relate("connect", "bar", p)
