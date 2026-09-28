from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '42841092-ec74-56d4-aedd-b98302173838'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__descending-lunar-node-symbol/20260927T091421Z-thuan-mac-1/reference/astrology tail node_42841092-ec74-56d4-aedd-b98302173838.svg'
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
    icon_id = 'descending-lunar-node-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('lunar node', 'astrology', 'descending', 'south node', 'symbol', 'horoscope', 'glyph', 'moon')

    def build(self) -> None:
        # Descending node (☋): two r5 rings about (11,11)/(37,11) touch the SQUARE top and sides; legs
        # leave each ring at its inner 3-4-5 point (15,14)/(33,14) and flare outward into an r12 bowl
        # about (24,30) whose bottom is the SQUARE bottom. Mirrored about x = 24.
        r = 5
        _path(self, "ring-left", (15, 14), [((11, 16), r, r, True), ((6, 11), r, r, True), ((11, 6), r, r, True),
                                            ((16, 11), r, r, True), ((15, 14), r, r, True)], True)
        _path(self, "ring-right", (33, 14), [((32, 11), r, r, True), ((37, 6), r, r, True), ((42, 11), r, r, True),
                                             ((37, 16), r, r, True), ((33, 14), r, r, True)], True)
        _path(self, "bowl", (15, 14), [(12, 30), ((24, 42), 12, 12, False), ((36, 30), 12, 12, False), (33, 14)])
        self.relate("connect", "bowl", "ring-left")
        self.relate("connect", "bowl", "ring-right")
