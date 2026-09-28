from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "324706d7-2d66-4a91-bead-c314dc987a3f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__red-blood-cell-strem/20260927T170824Z-thuan-mac-1/reference/red blood cell strem_324706d7-2d66-4a91-bead-c314dc987a3f.svg"
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

class RedBloodCellStrem(Solo48):
    """A single red blood cell seen face-on: a softly wavy rim with two curved dimple marks.

    Plan: CIRCLE. The rim is a closed Catmull-Rom curve through 8 lobe peaks and 8 valleys:
    cardinal peaks on the r20 lattice points (their neighbouring valleys share x or y, so the
    curve's extreme is the knot itself), diagonal peaks just inside r20, valleys near r17.
    Two dimple marks are arcs of r13 circles (5-12-13 lattice ends), point-symmetric about
    the centre, bulging toward the upper left and lower right as in the reference.
    """
    icon_id = "red-blood-cell-strem"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science/medical"
    aliases = ("red blood cell", "erythrocyte", "blood cell", "cell")
    keywords = ("blood", "cell", "red", "erythrocyte", "medical", "hematology", "biology")

    def build(self) -> None:
        import math
        pts = []
        for k in range(16):
            a = math.radians(k * 22.5)
            r = 20 if k % 4 == 0 else (19.8 if k % 2 == 0 else 18)
            pts.append((round(24 + r * math.cos(a)), round(24 + r * math.sin(a))))
        _smooth(self, "rim", pts, closed=True)
        _path(self, "dimple-a", (15, 22), [("A", (22, 15), 13, True)])
        _path(self, "dimple-b", (33, 26), [("A", (26, 33), 13, True)])
