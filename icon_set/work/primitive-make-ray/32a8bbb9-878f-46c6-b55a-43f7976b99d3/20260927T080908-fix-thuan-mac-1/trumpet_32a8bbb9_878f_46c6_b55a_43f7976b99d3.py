from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '32a8bbb9-878f-46c6-b55a-43f7976b99d3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__trumpet/20260927T080808Z-thuan-mac-1/reference/trumpet_32a8bbb9-878f-46c6-b55a-43f7976b99d3.svg'
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
    icon_id = 'trumpet'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'music'
    categories = ('primitives', 'music')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Trumpet (reference): straight leadpipe on y=22 into a cone bell
        # (vertex (36,22), mouth x=44 y12..32); the tube loop is a flat r8
        # stadium hanging from the leadpipe (centres (14,30)/(21,30));
        # three short valve pistons rise from the leadpipe, 8 apart.
        xs = (4, 10, 14, 18, 21, 26, 36)
        segs = []
        for i in range(len(xs) - 1):
            self.add_line(f'pipe-{i}', (xs[i], 22), (xs[i + 1], 22)); segs.append(f'pipe-{i}')
        self.add_contour('leadpipe', *segs)
        _path(self, 'loop', (21, 22), [((29, 30), 8, 8, True), ((21, 38), 8, 8, True), (14, 38),
                                       ((6, 30), 8, 8, True), ((14, 22), 8, 8, True)])
        _path(self, 'bell', (36, 22), [(44, 12), (44, 32), (36, 22)], True)
        for i, x in enumerate((10, 18, 26)):
            self.add_line(f'valve-{i}', (x, 10), (x, 22))
            self.relate('connect', f'valve-{i}', 'leadpipe')
        self.relate('connect', 'loop', 'leadpipe')
        self.relate('connect', 'bell', 'leadpipe')
