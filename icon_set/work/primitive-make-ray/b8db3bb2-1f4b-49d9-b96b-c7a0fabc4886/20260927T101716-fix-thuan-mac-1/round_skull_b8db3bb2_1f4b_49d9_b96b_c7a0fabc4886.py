from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b8db3bb2-1f4b-49d9-b96b-c7a0fabc4886'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-skull/20260927T101542Z-thuan-mac-1/reference/skull_b8db3bb2-1f4b-49d9-b96b-c7a0fabc4886.svg'
AUTHOR = 'claude-opus-5-5'


def _path(icon, name, start, steps, closed=False):
    """steps: (x, y) line | ((x, y), rx, ry, sweep[, large]) arc | ('c', c1, c2, end) cubic."""
    members, point = [], start
    for i, step in enumerate(steps):
        member = f"{name}-{i + 1}"
        if step[0] == 'c':
            icon.add_bezier(member, point, (step[1], step[2], step[3])); point = step[3]
        elif isinstance(step[0], (int, float)):
            icon.add_line(member, point, step); point = step
        else:
            end, rx, ry, sweep = step[:4]
            large = step[4] if len(step) > 4 else False
            icon.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep, large_arc=large); point = end
        members.append(member)
    icon.add_contour(name, *members, closed=closed)
    return members


def _circle(icon, name, cx, cy, r):
    """Full circle from four cardinal quarter arcs (certifiable spacing)."""
    return _path(icon, name, (cx, cy - r), [((cx + r, cy), r, r, True), ((cx, cy + r), r, r, True),
                                            ((cx - r, cy), r, r, True), ((cx, cy - r), r, r, True)], True)


class Drawing(Solo48):
    icon_id = 'round-skull'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('skull', 'head', 'bones', 'eyes', 'anatomy', 'skeleton')

    def build(self) -> None:
        # Cranium: r18 half circle about (24,24) (x 6..42, top 6) of two cardinal quarter arcs,
        # short standalone side walls, cheeks curving in to standalone jaw verticals at x=12/36
        # down to the bottom edge; two long teeth at x=20/28 (8 from the jaw and each other);
        # r3 ring eyes just below the centre line, 8 from the side walls.
        _path(self, "cranium", (6, 24), [((24, 6), 18, 18, True), ((42, 24), 18, 18, True)])
        for side, s in (("left", -1), ("right", 1)):
            x0, xj = 24 + s * 18, 24 + s * 12
            self.add_line(f"wall-{side}", (x0, 24), (x0, 28))
            self.add_bezier(f"cheek-{side}", (x0, 28), ((x0, 34), (xj, 33), (xj, 37)))
            self.add_line(f"jaw-{side}", (xj, 37), (xj, 42))
            self.relate("connect", "cranium", f"wall-{side}")
            self.relate("connect", f"wall-{side}", f"cheek-{side}")
            self.relate("connect", f"cheek-{side}", f"jaw-{side}")
            _circle(self, f"eye-{side}", 24 + s * 7, 25, 3)
            self.add_line(f"tooth-{side}", (24 + s * 4, 36), (24 + s * 4, 42))
