from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '576d9617-a85f-5cb2-ab16-dc7c3b638fe0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dog-lying-down/20260927T032037Z-thuan-mac-1/reference/dog lying down_576d9617-a85f-5cb2-ab16-dc7c3b638fe0.svg'
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
    icon_id = 'dog-lying-down'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'pets'
    categories = ('pets', 'primitives')
    aliases = ()
    keywords = ('dog', 'lying', 'resting', 'sleep', 'down', 'pet', 'relax')

    def build(self) -> None:
        # Plan: side view facing right. One closed outline: leaf tail (tip 4,8),
        # rump, flat belly on y40, paw curl, snout, head, sagging back so the
        # head sits higher. The floppy ear is a U hung between head nodes
        # (28,20) and (36,20); the haunch curve lands on belly node (18,40).
        _path(self, 'body', (8, 24), [
            ('c', (14, 18), (12, 10), (4, 8)),
            ('c', (7, 16), (4, 24), (4, 32)),
            ((12, 40), 8, 8, False),
            (18, 40), (40, 40),
            ((44, 36), 4, 4, False),
            (44, 29),
            ('c', (44, 27), (42, 26), (40, 25)),
            ('c', (39, 21), (38, 20), (36, 20)),
            (28, 20),
            ('c', (20, 21), (13, 21), (8, 24)),
        ], True)
        _path(self, 'ear', (28, 20), [(28, 28), ((36, 28), 4, 4, False), (36, 20)])
        _path(self, 'haunch', (14, 30), [('c', (19, 30), (21, 35), (18, 40))])
        self.relate('connect', 'ear', 'body')
        self.relate('connect', 'haunch', 'body')
