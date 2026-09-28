from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '05f00c7f-9195-41aa-b8b1-c15ae7c59bd3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crossed-fingers-with-folded-thumb-batch-021-07/20260927T091424Z-thuan-mac-1/reference/finger crossed 1_05f00c7f-9195-41aa-b8b1-c15ae7c59bd3.svg'
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
    icon_id = 'crossed-fingers-with-folded-thumb-batch-021-07'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('crossed', 'fingers', 'with', 'folded', 'thumb')

    def build(self) -> None:
        # Plan: crossed index (front, lines 2x+y=49/69) and middle (back, lines
        # 2x-y=11/31) fingers on 1:2 bands (width 8.9, r5 tips about (25,9) and
        # (15,9)); the back finger is hidden where it passes behind the front one
        # (joins at (20,9), (15,19)) and ends behind the curled fingers, whose
        # knuckle line leaves the front finger at (25,19) and rounds down into the
        # palm side (r7 about (33,26)). Folded thumb = pill across the palm (top
        # y=27, r4 cap about (27,31), open bottom edge); palm = quarter ellipses
        # rx16/ry11 about (24,33).
        _path(self, 'front', (8, 33), [
            (11, 27), (15, 19), (20, 9), (22, 5), ((30, 9), 5, 5, True), (25, 19), (21, 27),
        ])
        _path(self, 'back-tip', (15, 19), [(10, 9), ((18, 5), 5, 5, True), (20, 9)])
        _path(self, 'thumb', (11, 27), [(21, 27), (27, 27), ((31, 31), 4, 4, True), ((27, 35), 4, 4, True), (20, 35)])
        _path(self, 'palm', (25, 19), [
            (33, 19), ((40, 26), 7, 7, True), (40, 33),
            ((24, 44), 16, 11, True), ((8, 33), 16, 11, True),
        ])
        for a, b in (('front', 'back-tip'), ('front', 'thumb'), ('front', 'palm')):
            self.relate('connect', a, b)
