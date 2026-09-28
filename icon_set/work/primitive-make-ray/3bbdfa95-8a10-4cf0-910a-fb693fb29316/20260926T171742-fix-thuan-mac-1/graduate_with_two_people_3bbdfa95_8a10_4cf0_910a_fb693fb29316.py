from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3bbdfa95-8a10-4cf0-910a-fb693fb29316'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__graduate-with-two-people/20260926T171651Z-thuan-mac-1/reference/study virtual classroom_3bbdfa95-8a10-4cf0-910a-fb693fb29316.svg'
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
    icon_id = 'graduate-with-two-people'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'school-learning'
    categories = ('school-learning', 'primitives')
    aliases = ()
    keywords = ('graduate', 'people', 'group', 'education', 'mortarboard', 'classroom')

    def build(self) -> None:
        # Attempt (reported cannot-fix): the reference's graduate between two
        # classmates on HRECT_L (x 4..44, y 8..40), mirrored about x = 24: a
        # 20x10 mortarboard on a U head (r4), r4 ring heads for the
        # classmates, and one contour of three shoulder humps on the bottom
        # edge. Valid, but at 8-unit clearance the humps are only 3-5 tall
        # and the two side heads sit beside the cap like eyes, so the group
        # reads as a frowning face wearing a hat.
        _path(self, 'cap', (24, 8), [(34, 13), (28, 16), (24, 18), (20, 16), (14, 13), (24, 8)], True)
        _path(self, 'head', (20, 16), [(20, 22), ((28, 22), 4, 4, False, True), (28, 16)])
        self.relate('connect', 'cap', 'head')
        _circle(self, 'head-left', 8, 24, 4)
        _circle(self, 'head-right', 40, 24, 4)
        _path(self, 'shoulders', (4, 40), [('c', (4, 38), (6, 37), (8, 37)), ('c', (10, 37), (12, 38), (12, 40)),
                                           ('c', (12, 37), (18, 35), (24, 35)), ('c', (30, 35), (36, 37), (36, 40)),
                                           ('c', (36, 38), (38, 37), (40, 37)), ('c', (42, 37), (44, 38), (44, 40))])
