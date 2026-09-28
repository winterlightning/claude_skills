from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9e5f3201-71ac-4e37-97ac-b3416198d4da'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-9e5f3201/20260926T182452Z-thuan-mac-1/reference/car_9e5f3201-71ac-4e37-97ac-b3416198d4da.svg'
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
    icon_id = 'car-9e5f3201'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('solo-ai-cars-refine', 'solo-ai-next100', 'car-9e5f3201')

    def build(self) -> None:
        # Side-view car (reference): one closed outline - slanted cabin on a long
        # body with r4 rounded ends - and two r5 ring wheels hung from floor nodes.
        _path(self, 'body', (13, 18), [(18, 8), (30, 8), (35, 18), (40, 18),
                                       ((44, 22), 4, 4, True), (44, 26),
                                       ((40, 30), 4, 4, True), (34, 30), (14, 30), (8, 30),
                                       ((4, 26), 4, 4, True), (4, 22),
                                       ((8, 18), 4, 4, True), (13, 18)], True)
        for name, cx in (('wheel-rear', 14), ('wheel-front', 34)):
            _circle(self, name, cx, 35, 5)
            self.relate('connect', 'body', name)
