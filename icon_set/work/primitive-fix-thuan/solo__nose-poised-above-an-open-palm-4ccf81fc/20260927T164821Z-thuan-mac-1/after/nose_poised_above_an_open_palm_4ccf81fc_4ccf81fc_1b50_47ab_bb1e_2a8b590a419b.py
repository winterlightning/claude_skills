from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4ccf81fc-1b50-47ab-bb1e-2a8b590a419b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__nose-poised-above-an-open-palm-4ccf81fc/20260927T164821Z-thuan-mac-1/reference/baby family slime play dough 2_4ccf81fc-1b50-47ab-bb1e-2a8b590a419b.svg"
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



class NosePoisedAboveAnOpenPalm(Solo48):
    """Smelling gesture: a profile nose with two scent wisps rising beside it, poised above an
    open palm-up hand.

    Plan: SQUARE. Hand = the library's palm-up hand compressed to 36 wide (palm arc, flat thumb
    top at y26 with an r4 tip, r6 fingertips to x42, wrist to x6, base y42). Nose = bridge line
    (33,6)-(28,14) into a cubic tip curl to (35,16) whose lowest point is 8.8 above the thumb top
    and whose end leaves a 7-unit opening to the bridge. Wisps = two in-phase S cubics 9 apart at
    x18 and x9, from y15 up to the top extreme y6.
    """
    icon_id = "nose-poised-above-an-open-palm-4ccf81fc"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/gesture"
    aliases = ("smelling", "sniff", "scent in hand")
    keywords = ("nose", "smell", "sniff", "scent", "palm", "hand", "gesture", "aroma", "play dough")

    def build(self) -> None:
        self.add_arc("palm-upper", (6, 30), (22, 26), radius_x=16, radius_y=8)
        self.add_line("thumb-top", (22, 26), (30, 26))
        self.add_arc("thumb-tip-upper", (30, 26), (34, 30), radius_x=4)
        self.add_arc("thumb-tip-lower", (34, 30), (30, 34), radius_x=4)
        self.add_line("thumb-bottom", (30, 34), (20, 34))
        self.add_contour("thumb", "palm-upper", "thumb-top", "thumb-tip-upper", "thumb-tip-lower", "thumb-bottom")
        self.add_line("fingers-upper", (34, 30), (36, 30))
        self.add_arc("fingertips", (36, 30), (42, 36), radius_x=6)
        self.add_line("fingers-lower", (42, 36), (34, 42))
        self.add_line("palm-base", (34, 42), (12, 42))
        self.add_line("wrist-lower", (12, 42), (6, 40))
        self.add_contour("hand", "fingers-upper", "fingertips", "fingers-lower", "palm-base", "wrist-lower")
        self.relate("connect", "thumb", "hand")
        self.add_line("nose-bridge", (33, 6), (28, 14))
        self.add_bezier("nose-tip", (28, 14), ((27, 18), (32, 18), (35, 16)))
        self.add_contour("nose", "nose-bridge", "nose-tip")
        self.add_bezier("wisp-near", (18, 15), ((20, 12), (16, 9), (18, 6)))
        self.add_bezier("wisp-far", (9, 15), ((11, 12), (7, 9), (9, 6)))
