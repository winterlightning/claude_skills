from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "002b9a57-99f7-4dfa-ae32-31d2caa18e3f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__open-hands-beneath-hexagonal-pendant/20260927T174444Z-thuan-mac-1/reference/crafts necklace_002b9a57-99f7-4dfa-ae32-31d2caa18e3f.svg"
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
        elif st[0] == "R":
            c1, c2 = _rarc(here, st[1], st[2], st[3] if len(st) > 3 else None)
            icon.add_bezier(m, here, (c1, c2, st[1])); here = st[1]
        else:
            icon.add_bezier(m, here, (st[1], st[2], st[3])); here = st[3]
        members.append(m)
    icon.add_contour(name, *members, closed=closed)


def _rarc(p0, p1, c, cw=None):
    """cubic approximating a circular arc about c (possibly fractional) from p0 to p1 (short way)."""
    import math
    a0 = math.atan2(p0[1] - c[1], p0[0] - c[0]); a1 = math.atan2(p1[1] - c[1], p1[0] - c[0])
    d = a1 - a0
    while d <= -math.pi: d += 2 * math.pi
    while d > math.pi: d -= 2 * math.pi
    if cw is True and d < 0: d += 2 * math.pi
    if cw is False and d > 0: d -= 2 * math.pi
    r0 = math.dist(p0, c); r1 = math.dist(p1, c)
    k = 4 / 3 * math.tan(d / 4)
    c1 = (p0[0] - k * r0 * math.sin(a0), p0[1] + k * r0 * math.cos(a0))
    c2 = (p1[0] + k * r1 * math.sin(a1), p1[1] - k * r1 * math.cos(a1))
    return c1, c2


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


class OpenHandsBeneathHexagonalPendant(Solo48):
    """An open palm-up hand beneath a hexagonal pendant hanging on its necklace (crafts,
    handmade jewellery).

    Plan: SQUARE. One palm-up hand (two upright hands cannot flank a pendant in 36 units at
    8 spacing): short palm arc (6,30)->(14,26), long flat thumb top to (32,26), r4 thumb tip,
    underside back to (20,34); fingers to r6 fingertips at the exact right 42, palm base y 42,
    wrist to (6,40). The pointy-top hexagon pendant (17..27, 14..26) is set down on the thumb:
    its bottom vertex is a node of the thumb top. The necklace hangs as a wide, shallow
    swag from the top corners (6,6)/(38,6) into its top vertex.
    """
    icon_id = "open-hands-beneath-hexagonal-pendant"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/jewelry"
    aliases = ("crafts necklace", "handmade jewelry", "pendant in hand", "necklace")
    keywords = ("necklace", "pendant", "hexagon", "hand", "crafts", "handmade", "jewelry", "gift")

    def build(self) -> None:
        self.add_arc("palm-upper", (6, 30), (14, 26), radius_x=8, radius_y=4)
        self.add_line("thumb-top-a", (14, 26), (22, 26))
        self.add_line("thumb-top-b", (22, 26), (32, 26))
        self.add_arc("thumb-tip-upper", (32, 26), (36, 30), radius_x=4)
        self.add_arc("thumb-tip-lower", (36, 30), (32, 34), radius_x=4)
        self.add_line("thumb-bottom", (32, 34), (20, 34))
        self.add_contour("thumb", "palm-upper", "thumb-top-a", "thumb-top-b", "thumb-tip-upper",
                         "thumb-tip-lower", "thumb-bottom")
        self.add_arc("fingertips", (36, 30), (42, 36), radius_x=6)
        self.add_line("fingers-lower", (42, 36), (40, 42))
        self.add_line("palm-base", (40, 42), (12, 42))
        self.add_line("wrist-lower", (12, 42), (6, 40))
        self.add_contour("hand", "fingertips", "fingers-lower", "palm-base", "wrist-lower")
        self.relate("connect", "thumb", "hand")
        _path(self, "pendant", (22, 14), [
            ("L", (27, 17)), ("L", (27, 23)), ("L", (22, 26)), ("L", (17, 23)), ("L", (17, 17)), ("L", (22, 14)),
        ], closed=True)
        self.relate("connect", "pendant", "thumb")
        self.add_bezier("chain-left", (6, 6), ((10, 11), (16, 14), (22, 14)))
        self.add_bezier("chain-right", (38, 6), ((34, 11), (28, 14), (22, 14)))
        for n in ("chain-left", "chain-right"):
            self.relate("connect", n, "pendant")
        self.relate("connect", "chain-left", "chain-right")
