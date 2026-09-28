from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "668b603c-496b-4647-8586-a295e215868b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__reclining-figure-beneath-a-beach-umbrella/20260927T170824Z-thuan-mac-1/reference/beach person water parasol_668b603c-496b-4647-8586-a295e215868b.svg"
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

class RecliningFigureBeneathABeachUmbrella(Solo48):
    """A person reclining on the beach beside a beach umbrella, with water waves below.

    Plan: HRECT_L. Umbrella: r8 dome canopy about (12,16) closed by a flat edge, and a pole
    from the canopy edge down to a wave knot. Water: a Lucide-style wave line (cubic knots
    every 8 at y38, extremes 36/40, troughs under the body). Person: r4 ring head 8 above a short vertical neck
    stub (the upper torso), then a zigzag body like the reference -- a propping arm down to
    the sand, torso to the hip, a raised knee and the foot at the right edge -- kept 8+
    above the wave crests.
    """
    icon_id = "reclining-figure-beneath-a-beach-umbrella"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel/beach"
    aliases = ("beach", "sunbathing", "beach umbrella", "parasol", "vacation")
    keywords = ("beach", "umbrella", "parasol", "sunbathe", "relax", "vacation", "sea", "person", "summer")

    def build(self) -> None:
        _path(self, "canopy", (4, 16), [("A", (20, 16), 8, True), ("L", (14, 16)), ("L", (4, 16))], closed=True)
        self.add_line("pole", (14, 16), (12, 38))
        k = 8 / 3
        steps, x = [], 4
        for i in range(5):
            s = 1 if i % 2 == 0 else -1          # trough, crest, trough, crest, trough
            steps.append(("C", (x + k, 38 + s * k), (x + 8 - k, 38 + s * k), (x + 8, 38)))
            x += 8
        _path(self, "water", (4, 38), steps)
        self.relate("connect", "canopy", "pole")
        self.relate("connect", "pole", "water")
        _circle(self, "head", 33, 12, 4)
        self.add_line("torso", (33, 24), (33, 26))
        self.add_polyline("body", (28, 28), (33, 26), (37, 27), (40, 22), (44, 28))
        self.relate("connect", "torso", "body")
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
