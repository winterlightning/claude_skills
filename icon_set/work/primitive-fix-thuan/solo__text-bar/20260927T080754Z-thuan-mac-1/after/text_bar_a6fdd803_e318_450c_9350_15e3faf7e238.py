from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a6fdd803-e318-450c-9350-15e3faf7e238'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__text-bar/20260927T080754Z-thuan-mac-1/reference/text bar_a6fdd803-e318-450c-9350-15e3faf7e238.svg'
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
    icon_id = 'text-bar'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('text', 'bar', 'interface-essential')

    def build(self) -> None:
        # Lucide text-cursor at 2x: curled serifs top and bottom, stem with a short crossbar
        _path(self, "top-l", (10, 4), [(16, 4), ((24, 12), 8, 8, True)])
        _path(self, "top-r", (38, 4), [(32, 4), ((24, 12), 8, 8, False)])
        _path(self, "bot-l", (10, 44), [(16, 44), ((24, 36), 8, 8, False)])
        _path(self, "bot-r", (38, 44), [(32, 44), ((24, 36), 8, 8, True)])
        self.add_line("stem-a", (24, 12), (24, 28))
        self.add_line("stem-b", (24, 28), (24, 36))
        self.add_line("bar-l", (19, 28), (24, 28))
        self.add_line("bar-r", (24, 28), (29, 28))
        for a, b in (("top-l-2", "stem-a"), ("top-r-2", "stem-a"), ("top-l-2", "top-r-2"),
                     ("bot-l-2", "stem-b"), ("bot-r-2", "stem-b"), ("bot-l-2", "bot-r-2"),
                     ("stem-a", "stem-b"), ("bar-l", "bar-r"), ("bar-l", "stem-a"), ("bar-l", "stem-b"),
                     ("bar-r", "stem-a"), ("bar-r", "stem-b")):
            self.relate("connect", a, b)
