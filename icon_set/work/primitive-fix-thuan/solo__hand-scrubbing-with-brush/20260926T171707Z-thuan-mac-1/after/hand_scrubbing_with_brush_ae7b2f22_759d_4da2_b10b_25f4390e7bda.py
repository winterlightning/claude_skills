from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ae7b2f22-759d-4da2-b10b-25f4390e7bda'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-scrubbing-with-brush/20260926T171707Z-thuan-mac-1/reference/hand brush bubble_ae7b2f22-759d-4da2-b10b-25f4390e7bda.svg'
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
    icon_id = 'hand-scrubbing-with-brush'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('hand', 'brush', 'scrubbing', 'cleaning', 'suds', 'washing')

    def build(self) -> None:
        # Scrubbing brush: a pill 6..42 x 14..22 (r4 ends); top and bottom edges are standalone
        # lines, split where the hand and the bristles meet them.
        self.add_line('brush-top-1', (10, 14), (34, 14))
        self.add_line('brush-top-2', (34, 14), (38, 14))
        self.add_arc('brush-right', (38, 14), (38, 22), radius_x=4, sweep=True)
        self.add_line('brush-bottom-1', (38, 22), (20, 22))
        self.add_line('brush-bottom-2', (20, 22), (12, 22))
        self.add_line('brush-bottom-3', (12, 22), (10, 22))
        self.add_arc('brush-left', (10, 22), (10, 14), radius_x=4, sweep=True)
        parts = ['brush-top-1', 'brush-top-2', 'brush-right', 'brush-bottom-1', 'brush-bottom-2',
                 'brush-bottom-3', 'brush-left']
        for a, b in zip(parts, parts[1:] + parts[:1]):
            self.relate('connect', a, b)
        # Bristles under the left half.
        for x in (12, 20):
            self.add_line(f'bristle-{x}', (x, 22), (x, 30))
        self.relate('connect', 'bristle-12', 'brush-bottom-2')
        self.relate('connect', 'bristle-12', 'brush-bottom-3')
        self.relate('connect', 'bristle-20', 'brush-bottom-1')
        self.relate('connect', 'bristle-20', 'brush-bottom-2')
        # Hand gripping it from the upper left: the arm's lower edge, the back of the hand and
        # r4 fingertips curling down onto the brush.
        self.add_line('arm', (6, 6), (10, 14))
        self.relate('connect', 'arm', 'brush-top-1')
        self.relate('connect', 'arm', 'brush-left')
        _path(self, 'hand', (16, 6), [(30, 6), ((34, 10), 4, 4, True), (34, 14)])
        self.relate('connect', 'hand', 'brush-top-1')
        self.relate('connect', 'hand', 'brush-top-2')
        # Foam: a three-lobed cloud (r4 lobes) at the lower right.
        _path(self, 'foam', (30, 42), [(38, 42), ((38, 34), 4, 4, False), ((30, 34), 4, 4, False),
                                        ((30, 42), 4, 4, False)], True)
