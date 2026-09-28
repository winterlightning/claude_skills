from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8cf6c1e6-b45e-5c2b-92da-343cbb689ad3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-holding-spoon-fork/20260926T162509Z-thuan-mac/reference/fork and spoon 1_8cf6c1e6-b45e-5c2b-92da-343cbb689ad3.svg'
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
    icon_id = 'hands-holding-spoon-fork'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('hands', 'holding', 'spoon', 'fork')

    def build(self) -> None:
        # Plan: two raised fists, spoon in the left and fork in the right, as in
        # the reference, on HRECT_L (x 4..44, y 8..40). Each fist (16 wide, top
        # y=28, r4 top corners) tapers toward the wrist on the side facing the
        # other fist, where one finger line (y=36) curls in from the edge like
        # the reference's knuckle lines. Spoon: an oval bowl (rx5, ry6) on a handle
        # down to the fist top. Fork: three tines 8 apart whose outer pair closes
        # in an r8 U; the centre tine continues as the handle.
        _path(self, 'left-fist', (4, 40), [
            (4, 32), ((8, 28), 4, 4, True), (12, 28), (16, 28), ((20, 32), 4, 4, True), (20, 36), (17, 40),
        ])
        self.add_line('left-finger', (20, 36), (12, 36))
        self.relate('connect', 'left-fist', 'left-finger')
        _path(self, 'right-fist', (44, 40), [
            (44, 32), ((40, 28), 4, 4, False), (36, 28), (32, 28), ((28, 32), 4, 4, False), (28, 36), (31, 40),
        ])
        self.add_line('right-finger', (28, 36), (36, 36))
        self.relate('connect', 'right-fist', 'right-finger')
        _path(self, 'bowl', (12, 8), [
            ((17, 14), 5, 6, True), ((12, 20), 5, 6, True), ((7, 14), 5, 6, True), ((12, 8), 5, 6, True),
        ], closed=True)
        self.add_line('spoon-handle', (12, 20), (12, 28))
        self.relate('connect', 'bowl', 'spoon-handle')
        self.relate('connect', 'left-fist', 'spoon-handle')
        _path(self, 'fork', (28, 8), [(28, 10), ((36, 18), 8, 8, False), ((44, 10), 8, 8, False), (44, 8)])
        _path(self, 'fork-shaft', (36, 8), [(36, 18), (36, 28)])
        self.relate('connect', 'fork', 'fork-shaft')
        self.relate('connect', 'fork-shaft', 'right-fist')
