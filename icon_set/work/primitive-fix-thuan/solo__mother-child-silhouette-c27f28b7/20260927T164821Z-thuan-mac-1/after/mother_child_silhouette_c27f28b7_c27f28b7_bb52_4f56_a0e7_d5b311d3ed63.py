from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c27f28b7-bb52-4f56-a0e7-d5b311d3ed63"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__mother-child-silhouette-c27f28b7/20260927T164821Z-thuan-mac-1/reference/primitive symbols mother_c27f28b7-bb52-4f56-a0e7-d5b311d3ed63.svg"
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



class MotherChildSilhouette(Solo48):
    """Mother with child: a round head above an A-line dress body, with a small child figure
    (dot head, T-shaped arms and body) standing inside the dress.

    Plan: VRECT_L (8..40 x 4..44). Head = r4 four-arc circle about (24,8); body top is a standalone
    line at y20 (exactly 8 below the head, split at x24 for the neck junction), sides slant to the
    base (8,44)-(40,44). Child: dot (24,28), arm bar (21,36)-(27,36), stick (24,36)-(24,44) on the
    base; every child part keeps 8 from the dress walls.
    """
    icon_id = "mother-child-silhouette-c27f28b7"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people"
    aliases = ("mother", "mother and child", "pregnant mother")
    keywords = ("mother", "child", "family", "parent", "woman", "dress", "silhouette", "baby")

    def build(self) -> None:
        _circle(self, "head", 24, 8, 4)
        self.add_line("body-top-left", (18, 20), (24, 20))
        self.add_line("body-top-right", (24, 20), (30, 20))
        _path(self, "dress", (30, 20), [("L", (40, 44)), ("L", (24, 44)), ("L", (8, 44)), ("L", (18, 20))])
        self.relate("connect", "body-top-left", "body-top-right")
        self.relate("connect", "body-top-left", "dress")
        self.relate("connect", "body-top-right", "dress")
        self.mark_human_figure("mother", head="head", torso="body-top-left", torso_junction="end")
        self.add_dot("child-head", (24, 28))
        self.add_line("child-arms", (21, 36), (27, 36))
        self.add_line("child-body", (24, 36), (24, 44))
        self.relate("connect", "child-arms", "child-body")
        self.relate("connect", "child-body", "dress")
        self.mark_human_figure("child", head="child-head", torso="child-body", torso_junction="start")
