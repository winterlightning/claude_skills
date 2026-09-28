from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4d6b18c3-9c28-4f4a-8e22-8679e1c298f6"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__merlion-statue/20260927T164821Z-thuan-mac-1/reference/merlion statue_4d6b18c3-9c28-4f4a-8e22-8679e1c298f6.svg"
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



class MerlionStatue(Solo48):
    """Merlion: a left-facing lion head with a scalloped mane and open mouth spouting water,
    on a rounded fish body with a wavy scale line.

    Plan: VRECT_L (8..40 x 4..44). One closed silhouette: crown (24,4) -> cubic snout to the
    upper lip (8,14) -> mouth notch to (18,18) -> lower lip (12,24) -> chest (18,32) -> belly
    (18,36) -> elliptical bottom rx11/ry8 (bottom 44) -> right side up to (40,20) -> mane scallops
    (r5 3-4-5 ends on the extremes, r8 middle) back to the crown. Jet branches from the lower lip;
    the scale wave crosses from the chest node (15,28) to (40,28); eye dot at (26,16).
    """
    icon_id = "merlion-statue"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmark"
    aliases = ("merlion", "singapore merlion")
    keywords = ("merlion", "singapore", "statue", "lion", "fish", "landmark", "fountain")

    def build(self) -> None:
        _path(self, "body", (24, 4), [
            ("C", (16, 4), (8, 8), (8, 14)),
            ("L", (18, 18)), ("L", (12, 24)), ("L", (18, 32)), ("L", (18, 36)),
            ("A", (40, 36), 11, 8, False),
            ("L", (40, 30)), ("L", (40, 20)),
            ("A", (38, 16), 5, False), ("A", (28, 6), 8, False), ("A", (24, 4), 5, False),
        ], closed=True)
        self.add_bezier("jet", (12, 24), ((10, 27), (8, 30), (8, 33)))
        self.add_bezier("wave-1", (18, 32), ((21, 29), (25, 29), (28, 32)))
        self.add_bezier("wave-2", (28, 32), ((31, 34), (35, 33), (40, 30)))
        self.add_contour("wave", "wave-1", "wave-2")
        self.add_dot("eye", (26, 16))
        self.relate("connect", "jet", "body")
        self.relate("connect", "wave", "body")
