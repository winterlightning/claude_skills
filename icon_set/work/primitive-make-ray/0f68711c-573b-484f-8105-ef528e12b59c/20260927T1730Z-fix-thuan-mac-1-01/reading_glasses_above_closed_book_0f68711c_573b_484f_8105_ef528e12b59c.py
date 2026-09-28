from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0f68711c-573b-484f-8105-ef528e12b59c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__reading-glasses-above-closed-book/20260927T170824Z-thuan-mac-1/reference/read glasses_0f68711c-573b-484f-8105-ef528e12b59c.svg"
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

class ReadingGlassesAboveClosedBook(Solo48):
    """Round reading glasses resting above a closed book seen from its side.

    Plan: SQUARE. Glasses: two r6 ring lenses about (14,12) and (34,12) joined by an r5
    bridge arc that rises between them, with short temple stubs out to the edges x6/x42.
    Book (8 below the lenses): top cover y26, bottom cover y42, a flat spine at x6 with r4
    corners on the left and one page line at y34, all standalone members joined at nodes so
    the 8-unit page gaps certify.
    """
    icon_id = "reading-glasses-above-closed-book"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/education"
    aliases = ("reading", "study", "glasses and book", "read")
    keywords = ("glasses", "book", "read", "reading", "study", "library", "literature", "spectacles")

    def build(self) -> None:
        _circle(self, "lens-left", 14, 12, 6)
        _circle(self, "lens-right", 34, 12, 6)
        _path(self, "bridge", (20, 12), [("A", (28, 12), 5, True)])
        self.add_line("temple-left", (6, 12), (8, 12))
        self.add_line("temple-right", (40, 12), (42, 12))
        for p, lens in (("bridge", "lens-left"), ("bridge", "lens-right"),
                        ("temple-left", "lens-left"), ("temple-right", "lens-right")):
            self.relate("connect", p, lens)
        self.add_line("cover-top", (10, 26), (42, 26))
        self.add_line("cover-bottom", (10, 42), (42, 42))
        _path(self, "spine", (10, 42), [("A", (6, 38), 4, True), ("L", (6, 30)), ("A", (10, 26), 4, True)])
        self.add_line("pages", (15, 34), (42, 34))
        self.relate("connect", "spine", "cover-top")
        self.relate("connect", "spine", "cover-bottom")
