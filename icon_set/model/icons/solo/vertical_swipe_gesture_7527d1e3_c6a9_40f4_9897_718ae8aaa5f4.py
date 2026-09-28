from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7527d1e3-c6a9-40f4-9897-718ae8aaa5f4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vertical-swipe-gesture-solo/20260926T164653Z-thuan-mac/reference/gesture tap all direction 1_7527d1e3-c6a9-40f4-9897-718ae8aaa5f4.svg'
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
    icon_id = 'vertical-swipe-gesture-solo'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('finger', 'nail', 'up', 'down')

    def build(self) -> None:
        # Plan: up/down swipe gesture as in the reference, on VRECT_M
        # (x 10..38, y 4..44): a fingertip arch (r14 about (24,30), top y=16,
        # legs down to y=38) with a D-shaped nail inside (r4 top, 8 wide,
        # y 25..32), an up arrowhead above it (tip (24,4)) and a down arrowhead
        # below it (tip (24,44)). The arrows are heads only: shafts plus the
        # nail and 8-unit clearances need more than 40 units. The nail's
        # straight parts and the arrowheads are standalone lines so the exact 8
        # gaps certify. Mirrored about x=24.
        _path(self, 'up-arrow', (20, 8), [(24, 4), (28, 8)])
        _path(self, 'down-arrow', (20, 40), [(24, 44), (28, 40)])
        _path(self, 'finger', (10, 38), [(10, 30), ((24, 16), 14, 14, True), ((38, 30), 14, 14, True), (38, 38)])
        _path(self, 'nail-top', (20, 29), [((24, 25), 4, 4, True), ((28, 29), 4, 4, True)])
        self.add_line('nail-right', (28, 29), (28, 32))
        self.add_line('nail-bottom', (28, 32), (20, 32))
        self.add_line('nail-left', (20, 32), (20, 29))
        for a, b in (('nail-top', 'nail-right'), ('nail-right', 'nail-bottom'), ('nail-bottom', 'nail-left'),
                     ('nail-left', 'nail-top')):
            self.relate('connect', a, b)
