from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f1a7fb9a-6746-4814-855a-9b30ee60ae0b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__open-hand-digital-blocks/20260927T174444Z-thuan-mac-1/reference/technology robot hand ai logic_f1a7fb9a-6746-4814-855a-9b30ee60ae0b.svg"
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


class OpenHandDigitalBlocks(Solo48):
    """An open hand, palm up, presenting digital pixel blocks (AI / robot logic).

    Plan: SQUARE. Palm-up hand after hand-holding-heart: short palm arc (6,30)->(14,26), long
    flat thumb top to (32,26), r4 thumb tip, thumb underside back to (20,34); the fingers run from the
    thumb tip to r6 fingertips at the exact right 42, palm base y 42, wrist to (6,40). Three
    9x10 pixel blocks share edges in a stair: two stand side by side on the thumb (their floor
    is the thumb top) and one is stacked on the right one, reaching the exact top 6.
    """
    icon_id = "open-hand-digital-blocks"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/ai"
    aliases = ("technology robot hand", "ai logic", "hand with blocks", "digital blocks")
    keywords = ("ai", "artificial intelligence", "logic", "blocks", "pixels", "digital", "hand", "technology", "data")

    def build(self) -> None:
        self.add_arc("palm-upper", (6, 30), (14, 26), radius_x=8, radius_y=4)
        self.add_line("thumb-top-a", (14, 26), (23, 26))
        self.add_line("thumb-top-b", (23, 26), (32, 26))
        self.add_arc("thumb-tip-upper", (32, 26), (36, 30), radius_x=4)
        self.add_arc("thumb-tip-lower", (36, 30), (32, 34), radius_x=4)
        self.add_line("thumb-bottom", (32, 34), (20, 34))
        self.add_contour("thumb", "palm-upper", "thumb-top-a", "thumb-top-b", "thumb-tip-upper", "thumb-tip-lower", "thumb-bottom")
        self.add_arc("fingertips", (36, 30), (42, 36), radius_x=6)
        self.add_line("fingers-lower", (42, 36), (40, 42))
        self.add_line("palm-base", (40, 42), (12, 42))
        self.add_line("wrist-lower", (12, 42), (6, 40))
        self.add_contour("hand", "fingertips", "fingers-lower", "palm-base", "wrist-lower")
        self.relate("connect", "thumb", "hand")
        edges = {
            "block-top": ((23, 6), (32, 6)), "block-right-a": ((32, 6), (32, 16)),
            "block-right-b": ((32, 16), (32, 26)), "block-left": ((23, 6), (23, 16)),
            "block-divider": ((23, 16), (23, 26)), "block-mid-a": ((14, 16), (23, 16)),
            "block-mid-b": ((23, 16), (32, 16)), "block-outer": ((14, 16), (14, 26)),
        }
        for n, (a, b) in edges.items():
            self.add_line(n, a, b)
        names = list(edges)
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                if set(edges[a]) & set(edges[b]):
                    self.relate("connect", a, b)
        self.relate("connect", "block-outer", "thumb")
        self.relate("connect", "block-divider", "thumb")
        self.relate("connect", "block-right-b", "thumb")
