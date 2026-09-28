from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c536046d-ba8c-4f3d-ab8e-72b88649c323"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__interlocking-female-and-male-symbols-batch-051/20260927T164345Z-thuan-mac-1/reference/gender gay_c536046d-ba8c-4f3d-ab8e-72b88649c323.svg"
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


class InterlockingFemaleAndMaleSymbols(Solo48):
    """Female and male gender symbols with their rings overlapping (interlocked): the
    female ring on the left with its cross below, the male ring on the right with its
    arrow pointing up-right.

    Plan (SQUARE, 6..42): two r10 rings 12 apart (centres (16,20) and (28,20)) cross at the
    lattice points (22,12) and (22,28), where both rings carry a shared knot. Female stem
    (16,30)-(16,42) with a crossbar at y=38 (8.4 clear of the ring). Male shaft leaves the
    right ring's knot (35,13) at 45 degrees to the tip (42,6), which sets the top and right
    extremes; the arrowhead arms run along the keyshape edges.
    """
    icon_id = "interlocking-female-and-male-symbols-batch-051"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols"
    categories = ("primitives", "symbols")
    aliases = ("gender heterosexual", "gender symbols", "venus and mars")
    keywords = ("gender", "female", "male", "symbols", "interlocking", "circles", "identity", "couple")

    def build(self) -> None:
        r = 10
        _path(self, "ring-female", (16, 10), [
            ("A", (22, 12), r, True), ("A", (26, 20), r, True), ("A", (22, 28), r, True),
            ("A", (16, 30), r, True), ("A", (6, 20), r, True), ("A", (16, 10), r, True)], True)
        _path(self, "ring-male", (28, 10), [
            ("A", (35, 13), r, True), ("A", (38, 20), r, True), ("A", (28, 30), r, True),
            ("A", (22, 28), r, True), ("A", (18, 20), r, True), ("A", (22, 12), r, True),
            ("A", (28, 10), r, True)], True)
        self.relate("connect", "ring-female", "ring-male")
        self.add_line("female-stem-upper", (16, 30), (16, 38))
        self.add_line("female-stem-lower", (16, 38), (16, 42))
        self.add_line("female-bar-left", (12, 38), (16, 38))
        self.add_line("female-bar-right", (16, 38), (20, 38))
        for a in ("female-stem-lower", "female-bar-left", "female-bar-right"):
            self.relate("connect", "female-stem-upper", a)
        self.relate("connect", "female-stem-upper", "ring-female")
        self.add_line("male-shaft", (35, 13), (42, 6))
        self.add_polyline("male-head", (36, 6), (42, 6), (42, 12))
        self.relate("connect", "male-shaft", "ring-male")
        self.relate("connect", "male-shaft", "male-head")
