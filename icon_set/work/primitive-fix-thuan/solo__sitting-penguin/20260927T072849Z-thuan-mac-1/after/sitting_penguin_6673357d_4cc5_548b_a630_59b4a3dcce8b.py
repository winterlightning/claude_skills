from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6673357d-4cc5-548b-a630-59b4a3dcce8b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sitting-penguin/20260927T072849Z-thuan-mac-1/reference/tux_6673357d-4cc5-548b-a630-59b4a3dcce8b.svg'
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
    icon_id = 'sitting-penguin'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('penguin', 'sitting', 'tux', 'linux', 'mascot', 'bird', 'flippers', 'antarctic')

    def build(self) -> None:
        # Tux-style sitting penguin: r13 crown about (24,19) flowing into a
        # pear body; big r6 round feet at the base corners (as in the
        # reference), dot eyes and a small V beak.
        _path(self, 'penguin', (11, 19), [((24, 6), 13, 13, True), ((37, 19), 13, 13, True),
                                          ('c', (37, 24), (36, 27), (36, 30)), ((42, 36), 6, 6, True), ((36, 42), 6, 6, True),
                                          (12, 42), ((6, 36), 6, 6, True), ((12, 30), 6, 6, True),
                                          ('c', (12, 27), (11, 24), (11, 19))], True)
        _path(self, 'foot-right-inner', (36, 42), [((30, 36), 6, 6, True), ((36, 30), 6, 6, True)])
        _path(self, 'foot-left-inner', (12, 30), [((18, 36), 6, 6, True), ((12, 42), 6, 6, True)])
        self.relate('connect', 'foot-right-inner', 'penguin')
        self.relate('connect', 'foot-left-inner', 'penguin')
        self.add_dot('eye-left', (20, 17))
        self.add_dot('eye-right', (28, 17))
        _path(self, 'beak', (21, 25), [(24, 28), (27, 25)])
