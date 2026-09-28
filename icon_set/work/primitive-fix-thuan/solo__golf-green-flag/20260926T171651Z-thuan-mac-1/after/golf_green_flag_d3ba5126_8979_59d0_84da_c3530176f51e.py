from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd3ba5126-8979-59d0-84da-c3530176f51e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__golf-green-flag/20260926T171651Z-thuan-mac-1/reference/golf hole_d3ba5126-8979-59d0-84da-c3530176f51e.svg'
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
    icon_id = 'golf-green-flag'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('golf', 'green', 'flag', 'course', 'hole', 'putting')

    def build(self) -> None:
        # Plan: the reference's golf flag planted in the green, on HRECT_L
        # (x 4..44, y 8..40). A straight pole with a triangular pennant
        # (12 wide, 12 tall, sharing the pole's top and a node on it) and the
        # green as one smooth open outline of cubics (left extreme, bottom,
        # right extreme and the raised right lobe on the frame edges), left
        # open around the pole where it stands in the grass, as drawn.
        self.add_line('pole-top', (16, 8), (16, 20))
        self.add_line('pole', (16, 20), (16, 31))
        _path(self, 'pennant', (16, 8), [(28, 14), (16, 20)])
        self.relate('connect', 'pole-top', 'pole')
        self.relate('connect', 'pole-top', 'pennant')
        self.relate('connect', 'pole', 'pennant')
        _path(self, 'green', (7, 27), [('c', (5, 28), (4, 30), (4, 33)),
                                       ('c', (4, 37), (12, 40), (20, 40)),
                                       ('c', (32, 40), (44, 37), (44, 30)),
                                       ('c', (44, 25), (40, 22), (36, 22)),
                                       ('c', (31, 22), (28, 24), (26, 26))])
