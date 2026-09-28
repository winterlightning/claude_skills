from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '47fb874d-74a6-4cd9-9941-61fa6301ee2a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seed-spreader-with-two-wheels/20260927T072849Z-thuan-mac-1/reference/seeder_47fb874d-74a6-4cd9-9941-61fa6301ee2a.svg'
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
    icon_id = 'seed-spreader-with-two-wheels'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'farming'
    categories = ('farming', 'primitives')
    aliases = ()
    keywords = ('agricultural', 'seeder', 'machine')

    def build(self) -> None:
        # Seed spreader (reference, simplified): hopper trapezoid on a wide
        # spreader plate that spans the canvas, two box wheels below.
        _path(self, 'hopper', (18, 8), [(30, 8), (34, 24), (14, 24), (18, 8)], True)
        _path(self, 'plate', (4, 24), [(14, 24), (34, 24), (44, 24), (44, 32), (36, 32), (28, 32), (20, 32),
                                       (12, 32), (4, 32), (4, 24)], True)
        _path(self, 'wheel-left', (12, 32), [(12, 40), (20, 40), (20, 32)])
        _path(self, 'wheel-right', (28, 32), [(28, 40), (36, 40), (36, 32)])
        for n in ('hopper', 'wheel-left', 'wheel-right'):
            self.relate('connect', n, 'plate')
