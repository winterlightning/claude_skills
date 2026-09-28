from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd4d3043e-d77b-492a-b270-ae78ce436bd5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__golf-club-beside-ball/20260926T160438Z-thuan-mac-2/reference/golf equipment_d4d3043e-d77b-492a-b270-ae78ce436bd5.svg'
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
    icon_id = 'golf-club-beside-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('golf', 'club', 'beside', 'ball')

    def build(self) -> None:
        # Plan: golf club and ball on SQUARE (naturally asymmetric). The club head is
        # a rounded blob at the bottom left (leftmost x=6, sole y=42) whose heel
        # rises into the hosel J (21,34); the long shaft continues from J to the top
        # edge. The ball is an r6 ring in the bottom-right corner, 9+ from the club.
        J = (21, 34)
        _path(self, 'club-head', J, [
            ('c', (17, 32), (14, 31), (11, 31)),
            ('c', (8, 31), (6, 33), (6, 36)),
            ('c', (6, 40), (9, 42), (12, 42)),
            (16, 42),
            ('c', (19, 42), (20, 38), J),
        ], closed=True)
        self.add_line('shaft', J, (34, 6))
        self.relate('connect', 'club-head', 'shaft')
        _circle(self, 'ball', 36, 36, 6)
