from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f3554d59-4ee9-5ba8-bc14-5b1324691503"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__overlapping-chain-rings-batch-015-01/20260927T164345Z-thuan-mac-1/reference/attachment_f3554d59-4ee9-5ba8-bc14-5b1324691503.svg"
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


class OverlappingChainRings(Solo48):
    """Two chain links overlapping along a 45-degree diagonal, drawn as in the reference:
    one long outer link outline, with the two inner link ends crossing in the middle as a
    lens (the lower link's rounded end and the upper link's rounded end).

    Plan (SQUARE, 6..42): axis x+y=48. Outer caps are r10 arcs about (16,32) and (32,16)
    whose cardinal points set all four keyshape extremes; the straight sides x+y=34 and
    x+y=62 join the caps at the 6-8-10 lattice points (about an 8 degree kink, accepted).
    The inner ends are two r13 arcs sharing the side nodes P(17,17) and Q(31,31), one
    bulging down-left, one up-right, meeting the sides at about 40 degrees.
    """
    icon_id = "overlapping-chain-rings-batch-015-01"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "state")
    aliases = ("chain link", "link", "attachment")
    keywords = ("chain", "rings", "link", "attachment", "connection", "diagonal", "url")

    def build(self) -> None:
        P, Q = (17, 17), (31, 31)
        _path(self, "outline", (10, 24), [
            ("A", (24, 38), 10, 10, False, True), ("L", Q), ("L", (38, 24)),
            ("A", (24, 10), 10, 10, False, True), ("L", P), ("L", (10, 24))], True)
        self.add_arc("end-lower-link", P, Q, radius_x=13, radius_y=13, sweep=LOWER_SWEEP)
        self.add_arc("end-upper-link", P, Q, radius_x=13, radius_y=13, sweep=not LOWER_SWEEP)
        self.relate("connect", "outline", "end-lower-link")
        self.relate("connect", "outline", "end-upper-link")
        self.relate("connect", "end-lower-link", "end-upper-link")


LOWER_SWEEP = False
