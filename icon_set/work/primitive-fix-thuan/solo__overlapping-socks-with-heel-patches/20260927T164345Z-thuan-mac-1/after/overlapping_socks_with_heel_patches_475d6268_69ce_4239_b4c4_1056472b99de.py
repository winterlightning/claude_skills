from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "475d6268-69ce-4239-b4c4-1056472b99de"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__overlapping-socks-with-heel-patches/20260927T164345Z-thuan-mac-1/reference/socks_475d6268-69ce-4239-b4c4-1056472b99de.svg"
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


class OverlappingSocksWithHeelPatches(Solo48):
    """A pair of socks, the right one in front and set lower, as in the reference: each
    has a cuff band, a straight leg and a 45-degree foot ending in a round toe. The front
    sock's left edge doubles as the back sock's heel edge, and its instep line doubles as
    the back sock's sole, so the pair shares those strokes instead of running parallel.

    Plan (SQUARE, 6..42): back leg x 16..30 (top 6, cuff 14), front leg x 30..42 (top 10,
    cuff 18). Foot lines x+y=37 (back instep), 53 (shared), 69 (front sole). Toes are
    three-cubic caps about (12,33) and (25,36) with knots on the cardinal points, which set
    the left (x=6) and bottom (y=42) extremes; the back toe tucks into the front toe's left
    knot J(19,36).
    """
    icon_id = "overlapping-socks-with-heel-patches"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "clothing"
    categories = ("primitives", "clothing")
    aliases = ("socks", "pair of socks")
    keywords = ("socks", "clothing", "footwear", "heel", "cuff", "pair", "laundry")

    def build(self) -> None:
        J, N = (19, 36), (21, 32)
        _path(self, "sock-front", (30, 10), [
            ("L", (42, 10)), ("L", (42, 18)), ("L", (42, 24)),
            ("C", (42, 26), (40, 29), (39, 30)),              # rounded heel
            ("L", (29, 40)),                                    # sole x+y=69
            ("C", (27, 42), (27, 42), (25, 42)),
            ("C", (22, 42), (19, 39), J),
            ("C", (19, 34), (20, 33), N),
            ("L", (30, 23)),                                    # instep x+y=53
            ("L", (30, 18)), ("L", (30, 14)), ("L", (30, 10))], True)
        _path(self, "sock-back", (30, 10), [
            ("L", (30, 6)), ("L", (16, 6)), ("L", (16, 14)), ("L", (16, 18)),
            ("C", (16, 20), (15, 22), (14, 23)),                # ankle
            ("L", (8, 29)),                                     # instep x+y=37
            ("C", (7, 30), (6, 31), (6, 33)),
            ("C", (6, 36), (9, 39), (12, 39)),
            ("C", (15, 39), (18, 37), J)])
        self.add_line("cuff-back", (16, 14), (30, 14))
        self.add_line("cuff-front", (30, 18), (42, 18))
        self.relate("connect", "sock-front", "sock-back")
        for cuff in ("cuff-back", "cuff-front"):
            self.relate("connect", cuff, "sock-front")
        self.relate("connect", "cuff-back", "sock-back")
