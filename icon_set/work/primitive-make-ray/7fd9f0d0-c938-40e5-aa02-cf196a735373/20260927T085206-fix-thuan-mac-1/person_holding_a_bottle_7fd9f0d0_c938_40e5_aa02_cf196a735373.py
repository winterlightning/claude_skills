from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7fd9f0d0-c938-40e5-aa02-cf196a735373'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-holding-a-bottle/20260927T084830Z-thuan-mac-1/reference/drinking bottle_7fd9f0d0-c938-40e5-aa02-cf196a735373.svg'
AUTHOR = "claude-opus-5-5"


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
    icon_id = 'person-holding-a-bottle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'recreation'
    categories = ('primitives', 'recreation')
    aliases = ()
    keywords = ('person', 'holding', 'a', 'bottle')

    def build(self) -> None:
        # person holding out a bottle (reference): head over a rounded shoulder, the arm running
        # forward to the foot of an upright bottle with a long neck. Before had a small ring head
        # and a zigzag arm.
        _circle(self, "head", 12, 16, 6)
        _path(self, "bust", (4, 40), [((12, 31), 8, 9, True), ((20, 37), 8, 6, True), (30, 37)])
        self.add_line("wall-left-low", (30, 37), (30, 40))
        _path(self, "bottle", (30, 37), [(30, 26), ('c', (30, 23), (33, 22), (33, 19)), (33, 8), (41, 8),
                                         (41, 19), ('c', (41, 22), (44, 23), (44, 26)), (44, 40), (30, 40)])
        self.relate("connect", "bust", "bottle"); self.relate("connect", "bust", "wall-left-low")
        self.relate("connect", "bottle", "wall-left-low")
