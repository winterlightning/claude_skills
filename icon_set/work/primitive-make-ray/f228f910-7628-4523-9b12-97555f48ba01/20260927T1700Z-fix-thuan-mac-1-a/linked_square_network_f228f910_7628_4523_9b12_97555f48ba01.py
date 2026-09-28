from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f228f910-7628-4523-9b12-97555f48ba01"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__linked-square-network/20260927T164509Z-thuan-mac-1/reference/block chain_f228f910-7628-4523-9b12-97555f48ba01.svg"
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


class LinkedSquareNetwork(Solo48):
    """A chain of linked blocks snaking across two rows (a block chain).

    Plan: HRECT_L (4,8)-(44,40). Four 12x12 rounded blocks (r3 corners) on two staggered
    rows like the reference: top row B1 (12,8) and C1 (32,8), bottom row A2 (4,28) and
    B2 (24,28). Links (8 long): B1-C1 across the top, C1 down to B2, B2-A2 across the
    bottom, so the chain zigzags. Link ends are nodes split into the block sides.
    """
    icon_id = "linked-square-network"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology"
    categories = ("primitives", "technology")
    aliases = ("block chain", "blockchain", "linked blocks")
    keywords = ("blockchain", "block", "chain", "network", "linked", "crypto", "ledger")

    def build(self) -> None:
        r, w = 3, 12
        blocks = {"b1": (12, 8), "c1": (32, 8), "b2": (24, 28), "a2": (4, 28)}
        nodes = {"b1": [("R", 14)], "c1": [("L", 14), ("B", 34)], "b2": [("T", 34), ("L", 34)], "a2": [("R", 34)]}
        # Each block is a rounded square; link nodes are split into its sides.
        for name, (x, y) in blocks.items():
            L, T, R, B = x, y, x + w, y + w
            extra = dict(nodes[name])
            top = [("L", (extra["T"], T))] if "T" in extra else []
            right = [("L", (R, extra["R"]))] if "R" in extra else []
            bottom = [("L", (extra["B"], B))] if "B" in extra else []
            left = [("L", (L, extra["L"]))] if "L" in extra else []
            _path(self, name, (L + r, T), top + [("L", (R - r, T)), ("A", (R, T + r), r, True)] + right +
                  [("L", (R, B - r)), ("A", (R - r, B), r, True)] + bottom +
                  [("L", (L + r, B)), ("A", (L, B - r), r, True)] + left +
                  [("L", (L, T + r)), ("A", (L + r, T), r, True)], closed=True)
        links = [("link-b1c1", "b1", (24, 14), "c1", (32, 14)), ("link-c1b2", "c1", (34, 20), "b2", (34, 28)),
                 ("link-b2a2", "b2", (24, 34), "a2", (16, 34))]
        for name, a, pa, b, pb in links:
            self.add_line(name, pa, pb)
            self.relate("connect", a, name)
            self.relate("connect", b, name)
