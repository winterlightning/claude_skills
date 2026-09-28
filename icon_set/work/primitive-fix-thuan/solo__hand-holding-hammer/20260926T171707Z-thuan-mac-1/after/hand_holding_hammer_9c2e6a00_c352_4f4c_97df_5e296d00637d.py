from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9c2e6a00-c352-4f4c-97df-5e296d00637d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-hammer/20260926T171707Z-thuan-mac-1/reference/tools hammer hold_9c2e6a00-c352-4f4c-97df-5e296d00637d.svg'
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
    icon_id = 'hand-holding-hammer'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'tools'
    categories = ('primitives', 'tools')
    aliases = ()
    keywords = ('hammer', 'hand', 'holding', 'grip', 'construction', 'carpentry', 'build', 'tool')

    def build(self) -> None:
        # Axis frame: the handle runs along a (up-right), b is across it; integer a,b -> grid points.
        ab = lambda a, b: (24 + a + b, 24 - a + b)
        # Hammer head: block a 6..12, b -6..4, with an r10 claw (centre (32,22)) curling down
        # from its striking corner; the handle leaves the head's lower face at b=0.
        _path(self, 'head', ab(6, 0), [ab(6, -6), ab(12, -6), ab(12, 4), ab(6, 4), ab(6, 0)], True)
        self.add_arc('claw', ab(12, 4), (38, 30), radius_x=10, sweep=True)
        self.relate('connect', 'head', 'claw')
        self.add_line('handle', ab(6, 0), ab(0, 0))
        self.relate('connect', 'head', 'handle')
        # Fist across the handle (a -12..0, b -5..5): two curled fingers (r5 knuckles) on the
        # upper-left side, a crease between them; the handle end shows below it.
        _path(self, 'fist', ab(0, 0), [ab(0, 5), ab(-12, 5), ab(-12, 0), ab(-12, -5),
                                        (ab(-6, -5), 5, 5, True), (ab(0, -5), 5, 5, True), ab(0, 0)], True)
        self.relate('connect', 'fist', 'handle')
        self.add_line('finger-crease', ab(-6, -5), ab(-6, -1))
        self.relate('connect', 'fist', 'finger-crease')
        self.add_line('handle-end', ab(-12, 0), ab(-18, 0))
        self.relate('connect', 'fist', 'handle-end')
