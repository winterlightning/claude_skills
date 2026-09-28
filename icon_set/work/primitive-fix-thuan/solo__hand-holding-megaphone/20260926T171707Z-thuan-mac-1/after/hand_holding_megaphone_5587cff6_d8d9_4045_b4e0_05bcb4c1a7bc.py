from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5587cff6-d8d9-4045-b4e0-05bcb4c1a7bc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-megaphone/20260926T171707Z-thuan-mac-1/reference/labor megaphone_5587cff6-d8d9-4045-b4e0-05bcb4c1a7bc.svg'
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
    icon_id = 'hand-holding-megaphone'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'work'
    categories = ('work', 'primitives')
    aliases = ()
    keywords = ('megaphone', 'hand', 'announcement', 'speaker', 'holding', 'labor')

    def build(self) -> None:
        # Megaphone: an r5 rounded rear (x 7..18, y 12..22), a seam, and a bell whose sides
        # stay level before flaring out to the mouth at x=44.
        _path(self, 'body', (13, 22), [(12, 22), ((12, 12), 5, 5, True), (18, 12),
                                        ('c', (30, 12), (40, 10), (44, 8)), (44, 28),
                                        ('c', (40, 24), (30, 22), (18, 22)), (13, 22)], True)
        self.add_line('seam', (18, 12), (18, 22))
        self.relate('connect', 'body', 'seam')
        # Handle down from the rear into a fist: cuff line, sleeve edges, round knuckle front.
        self.add_line('handle', (13, 22), (13, 30))
        self.relate('connect', 'body', 'handle')
        _path(self, 'fist', (13, 30), [(15, 30), ((15, 40), 5, 5, True), (8, 40), (8, 30), (13, 30)], True)
        self.relate('connect', 'fist', 'handle')
        self.add_line('sleeve-top', (4, 30), (8, 30))
        self.add_line('sleeve-bottom', (4, 40), (8, 40))
        self.relate('connect', 'fist', 'sleeve-top')
        self.relate('connect', 'fist', 'sleeve-bottom')
