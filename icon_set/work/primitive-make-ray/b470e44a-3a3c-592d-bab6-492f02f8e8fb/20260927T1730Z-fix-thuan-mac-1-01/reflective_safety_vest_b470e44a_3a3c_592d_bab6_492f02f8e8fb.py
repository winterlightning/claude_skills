from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b470e44a-3a3c-592d-bab6-492f02f8e8fb"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__reflective-safety-vest/20260927T170824Z-thuan-mac-1/reference/safety vest_b470e44a-3a3c-592d-bab6-492f02f8e8fb.svg"
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

class ReflectiveSafetyVest(Solo48):
    """A reflective safety vest: shoulder straps, a V-neck, a centre zip and two reflective
    bands around the body.

    Plan: VRECT_L. Outline (mirrored about x24): 8-wide straps x12-20 / x28-36 at the top
    edge y4, curved armholes swinging out to the sides x8/x40 at y22, straight sides, r4
    bottom corners at y44. The V-neck runs from the straps' inner corners to (24,16); the zip
    runs from there to the hem; reflective bands at y28 and y36 (8 apart, 8 above the hem).
    """
    icon_id = "reflective-safety-vest"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/clothing"
    aliases = ("safety vest", "hi-vis vest", "reflective vest", "high visibility")
    keywords = ("vest", "safety", "reflective", "hi-vis", "construction", "worker", "clothing", "high visibility")

    def build(self) -> None:
        _path(self, "vest", (20, 4), [
            ("L", (12, 4)), ("L", (12, 10)), ("C", (8, 22), (12, 16), (8, 17)), ("L", (8, 28)), ("L", (8, 36)),
            ("L", (8, 40)), ("A", (12, 44), 4, False), ("L", (24, 44)), ("L", (36, 44)), ("A", (40, 40), 4, False),
            ("L", (40, 36)), ("L", (40, 28)), ("L", (40, 22)), ("C", (36, 10), (40, 17), (36, 16)), ("L", (36, 4)),
            ("L", (28, 4)), ("L", (24, 16)), ("L", (20, 4)),
        ], closed=True)
        self.add_line("zip-top", (24, 16), (24, 28))
        self.add_line("zip-mid", (24, 28), (24, 36))
        self.add_line("zip-bottom", (24, 36), (24, 44))
        for y in (28, 36):
            self.add_line(f"band-{y}-left", (8, y), (24, y))
            self.add_line(f"band-{y}-right", (24, y), (40, y))
        for p in ("zip-top", "zip-bottom", "band-28-left", "band-28-right", "band-36-left", "band-36-right"):
            self.relate("connect", "vest", p)
        for zip_part, y in (("zip-top", 28), ("zip-mid", 28), ("zip-mid", 36), ("zip-bottom", 36)):
            self.relate("connect", zip_part, f"band-{y}-left")
            self.relate("connect", zip_part, f"band-{y}-right")
        self.relate("connect", "zip-top", "zip-mid")
        self.relate("connect", "zip-mid", "zip-bottom")
