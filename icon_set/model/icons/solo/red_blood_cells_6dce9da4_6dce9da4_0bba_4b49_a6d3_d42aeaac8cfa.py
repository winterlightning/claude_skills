from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "6dce9da4-0bba-4b49-a6d3-d42aeaac8cfa"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__red-blood-cells-6dce9da4/20260927T170824Z-thuan-mac-1/reference/pregnancy eggs_6dce9da4-0bba-4b49-a6d3-d42aeaac8cfa.svg"
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

import math


def _ell_pts(c, rx, ry, angles):
    return [(round(c[0] + rx * math.cos(a)), round(c[1] + ry * math.sin(a))) for a in angles]


def _ell_path(icon, name, c, rx, ry, angles, closed):
    """Cubics through integer knots on an axis-aligned ellipse at the given parameter angles
    (increasing = clockwise on screen); handles follow the ellipse tangent (elliptic-arc alpha)."""
    pts = _ell_pts(c, rx, ry, angles)
    n = len(angles)
    steps = []
    for i in range(n if closed else n - 1):
        a0, a1 = angles[i], angles[(i + 1) % n]
        if closed and i == n - 1:
            a1 += 2 * math.pi
        d = a1 - a0
        al = math.sin(d) * (math.sqrt(4 + 3 * math.tan(d / 2) ** 2) - 1) / 3
        p0, p1 = pts[i], pts[(i + 1) % n]
        t0 = (-rx * math.sin(a0), ry * math.cos(a0))
        t1 = (-rx * math.sin(a1), ry * math.cos(a1))
        steps.append(("C", (p0[0] + al * t0[0], p0[1] + al * t0[1]),
                      (p1[0] - al * t1[0], p1[1] - al * t1[1]), p1))
    _path(icon, name, pts[0], steps, closed)


class RedBloodCells(Solo48):
    """Two red blood cells: flattened discs, each with the curled inner line of its dimple.

    Plan: SQUARE. Front cell: ellipse rx15/ry12 about (27,30) (sets x42/y42); back cell: the
    same ellipse about (21,18) (sets x6/y6) peeking out behind it, its visible arc ending on
    knots it shares with the front outline (the rounded ideal crossings (12,28), (36,20)).
    The front cell carries the reference's curled dimple: a three-quarter inner ellipse
    rx6/ry3, 9 clear of its rim. Outlines are cubics through integer knots.
    """
    icon_id = "red-blood-cells-6dce9da4-solo"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science/medical"
    aliases = ("red blood cells", "erythrocytes", "blood cells", "cells")
    keywords = ("blood", "cell", "red", "erythrocyte", "medical", "hematology", "biology")

    def build(self) -> None:
        r = math.radians
        # back cell: visible from the lower-left crossing (12,28), round the top, to (36,20)
        _ell_path(self, "cell-back", (21, 18), 15, 12, [r(a) for a in (125.7, 150, 180, 225, 270, 315, 360, 370.8)], False)
        # front cell, full; knots include both crossings
        _ell_path(self, "cell-front", (27, 30), 15, 12,
                  [r(a) for a in (-169.2, -135, -90, -54.4, 0, 45, 90, 135, 180)], True)
        self.relate("connect", "cell-back", "cell-front")
        # the front cell's dimple: a three-quarter inner ellipse, open to the upper left
        _path(self, "dimple", (27, 27), [("A", (21, 30), 6, 3, True, True)])
