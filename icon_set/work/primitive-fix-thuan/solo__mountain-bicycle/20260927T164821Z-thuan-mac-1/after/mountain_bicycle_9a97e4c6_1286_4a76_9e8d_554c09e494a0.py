from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9a97e4c6-1286-4a76-9e8d-554c09e494a0"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__mountain-bicycle/20260927T164821Z-thuan-mac-1/reference/mountain bike_9a97e4c6-1286-4a76-9e8d-554c09e494a0.svg"
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



class MountainBicycle(Solo48):
    """Mountain bike: two ring wheels under a diamond frame with a seat on a post and a flat
    handlebar on a stem.

    Plan: HRECT_L (4..44 x 8..40). Wheels r7 four-arc circles about (11,33)/(37,33) (12 apart).
    Frame: seat point S(16,12), head H(32,12), bottom bracket B(24,25) (8.3 clear of both rims);
    top tube S-H, seat tube S-B, down tube H-B, seat stay S-(11,26) and fork H-(37,26) land on the
    rim tops. Seat post up to (16,8) with the saddle to the left; stem up to (32,8) with the bar
    to the right.
    """
    icon_id = "mountain-bicycle"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/vehicle"
    aliases = ("bike", "mtb", "mountain bike")
    keywords = ("bicycle", "bike", "mountain", "cycling", "sport", "vehicle", "ride")

    def build(self) -> None:
        _circle(self, "wheel-rear", 11, 33, 7)
        _circle(self, "wheel-front", 37, 33, 7)
        self.add_line("top-tube", (16, 14), (32, 10))
        self.add_line("seat-tube", (16, 14), (24, 25))
        self.add_line("down-tube", (32, 10), (24, 25))
        self.add_line("seat-stay", (16, 14), (11, 26))
        self.add_line("fork", (32, 10), (37, 26))
        self.add_line("seat-post", (16, 14), (16, 10))
        self.add_line("saddle", (10, 10), (16, 10))
        self.add_line("stem", (32, 10), (34, 8))
        self.add_line("handlebar", (34, 8), (40, 8))
        for a, b in (("top-tube", "seat-tube"), ("top-tube", "down-tube"), ("seat-tube", "down-tube"),
                     ("top-tube", "seat-stay"), ("seat-tube", "seat-stay"), ("top-tube", "fork"),
                     ("down-tube", "fork"), ("seat-stay", "wheel-rear"), ("fork", "wheel-front"),
                     ("seat-post", "top-tube"), ("seat-post", "seat-tube"), ("seat-post", "seat-stay"),
                     ("seat-post", "saddle"), ("stem", "top-tube"), ("stem", "down-tube"), ("stem", "fork"),
                     ("stem", "handlebar")):
            self.relate("connect", a, b)
