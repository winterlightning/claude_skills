from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d55eccac-fdd8-49ae-b39b-078588112508"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__loop-handle-leash/20260927T164345Z-thuan-mac-1/reference/leash_d55eccac-fdd8-49ae-b39b-078588112508.svg"
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


class LoopHandleLeash(Solo48):
    """A leash laid on the diagonal: a teardrop loop handle at the upper right, a short
    cord, and the tilted capsule-shaped clip at the lower left, as in the reference.

    Plan (SQUARE, 6..42): loop = r8 arc (270 degrees) about (34,14) closed by two tangent
    strands meeting at the tip T(26,22); its cardinal points set the top and right extremes.
    Clip = 45-degree capsule with r5 caps about (11,37) and (16,32) (3-4-5 side joins on
    x+y=41 and x+y=55); its cap cardinals set the left and bottom extremes. The cord runs
    from the clip's cap knot (20,29) to T, about 4 degrees off the diagonal.
    """
    icon_id = "loop-handle-leash"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("primitives", "animals")
    aliases = ("leash", "dog leash", "lead")
    keywords = ("loop", "handle", "leash", "lead", "dog", "pet", "clip")

    def build(self) -> None:
        tip = (26, 22)
        _path(self, "loop", tip, [
            ("L", (26, 14)), ("A", (34, 22), 8, 8, True, True), ("L", tip)], True)
        _path(self, "clip", (8, 33), [
            ("A", (15, 40), 5, 5, False, True), ("L", (19, 36)),
            ("A", (20, 29), 5, 5, False), ("A", (12, 29), 5, 5, False), ("L", (8, 33))], True)
        self.add_line("cord", (20, 29), tip)
        self.relate("connect", "cord", "loop")
        self.relate("connect", "cord", "clip")
