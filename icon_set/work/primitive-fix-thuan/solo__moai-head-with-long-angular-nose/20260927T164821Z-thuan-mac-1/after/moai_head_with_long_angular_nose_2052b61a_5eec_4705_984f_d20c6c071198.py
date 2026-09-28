from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2052b61a-5eec-4705-984f-d20c6c071198"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__moai-head-with-long-angular-nose/20260927T164821Z-thuan-mac-1/reference/moai_2052b61a-5eec-4705-984f-d20c6c071198.svg"
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



class MoaiHeadWithLongAngularNose(Solo48):
    """Moai: a tall rounded-top head with a heavy brow ridge and long straight nose (one T stroke),
    deep-set eye dots, a pursed mouth and a chin that narrows to a flat base.

    Plan: VRECT_L (8..40 x 4..44). Sides are standalone lines so the eye dots certify at exactly
    8 from them; crown = r6 corner arcs + flat top at y4; jaw = two slants into a base at y44.
    Brow (16,16)-(32,16) split at the nose root; nose (24,16)-(24,28); eyes (16,25)/(32,25);
    mouth (20,36)-(28,36), 8 above the base and 8 below the nose tip.
    """
    icon_id = "moai-head-with-long-angular-nose"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmark"
    aliases = ("easter island head", "moai statue")
    keywords = ("moai", "easter island", "statue", "head", "stone", "monolith", "rapa nui")

    def build(self) -> None:
        self.add_line("side-left", (8, 34), (8, 10))
        _path(self, "crown", (8, 10), [("A", (14, 4), 6, True), ("L", (34, 4)), ("A", (40, 10), 6, True)])
        self.add_line("side-right", (40, 10), (40, 34))
        _path(self, "jaw", (40, 34), [("L", (36, 44)), ("L", (12, 44)), ("L", (8, 34))])
        self.relate("connect", "side-left", "crown")
        self.relate("connect", "crown", "side-right")
        self.relate("connect", "side-right", "jaw")
        self.relate("connect", "jaw", "side-left")
        self.add_line("brow-left", (16, 16), (24, 16))
        self.add_line("brow-right", (24, 16), (32, 16))
        self.add_line("nose", (24, 16), (24, 28))
        self.relate("connect", "brow-left", "brow-right")
        self.relate("connect", "brow-left", "nose")
        self.relate("connect", "brow-right", "nose")
        self.add_dot("eye-left", (16, 25))
        self.add_dot("eye-right", (32, 25))
        self.add_line("mouth", (20, 36), (28, 36))
