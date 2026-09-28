from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6da646a1-34eb-51f2-af2d-b08aed786a57'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__simple-computer-keyboard/20260927T072849Z-thuan-mac-1/reference/keyboard_6da646a1-34eb-51f2-af2d-b08aed786a57.svg'
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
    icon_id = 'simple-computer-keyboard'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'computers'
    categories = ('computers', 'primitives')
    aliases = ()
    keywords = ('keyboard', 'typing', 'input', 'keys', 'peripheral', 'computer', 'hardware', 'text')

    def build(self) -> None:
        # Keyboard body: square-cornered frame (4,8)-(44,40).
        _path(self, 'frame', (4, 8), [(44, 8), (44, 40), (4, 40), (4, 8)], True)
        # Two rows of four keys, 8 apart, and a space bar.
        for y in (16, 24):
            for x in (12, 20, 28, 36):
                self.add_dot(f'key-{x}-{y}', (x, y))
        self.add_line('space', (16, 32), (32, 32))
