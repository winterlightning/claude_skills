from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ef1c856a-063a-4941-92f0-78189ee7aba9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-patting-dog/20260926T171707Z-thuan-mac-1/reference/dog side patting good_ef1c856a-063a-4941-92f0-78189ee7aba9.svg'
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
    icon_id = 'hand-patting-dog'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'pets'
    categories = ('pets', 'primitives')
    aliases = ()
    keywords = ('dog', 'pat', 'hand', 'good-dog', 'praise', 'petting', 'pet')

    def build(self) -> None:
        # Hand lying on the dog's neck at 45 degrees, fingers pointing down-left: edges on
        # x+y = 54 (upper), 66 (between the fingers) and 78 (lower); r5 fingertips, staggered.
        _path(self, 'hand', (42, 12), [(30, 24), (22, 32), (18, 36), ((24, 42), 5, 5, False),
                                        (30, 36), (36, 30)])
        _path(self, 'finger-2', (30, 36), [((36, 42), 5, 5, False), (42, 36)])
        self.relate('connect', 'hand', 'finger-2')
        # Dog head in profile facing left: pointed ear, r5 round muzzle about (11,21), jaw and
        # the front and back of the neck running under the hand.
        _path(self, 'dog', (30, 24), [(24, 6), (18, 12), (11, 16), ((11, 26), 5, 5, False),
                                       (16, 27), (22, 32)])
        self.relate('connect', 'dog', 'hand')
