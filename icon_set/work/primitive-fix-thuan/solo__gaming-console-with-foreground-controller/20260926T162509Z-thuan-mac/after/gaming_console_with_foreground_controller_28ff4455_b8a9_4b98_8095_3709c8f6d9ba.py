from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '28ff4455-b8a9-4b98-8095-3709c8f6d9ba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gaming-console-with-foreground-controller/20260926T162509Z-thuan-mac/reference/playstation four controller_28ff4455-b8a9-4b98-8095-3709c8f6d9ba.svg'
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
    icon_id = 'gaming-console-with-foreground-controller'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('gaming', 'console', 'with', 'foreground', 'controller')

    def build(self) -> None:
        # Plan: upright slim console behind a wide gamepad, as in the reference,
        # on SQUARE (6..42). The gamepad spans the full width (y 22..42): r6
        # shoulders, sides flaring out to r4 grips, and a shallow r10 arch
        # between the grips; two thumbstick dots sit 9 from the top edge and
        # 8+ from the sides and the arch. The console stands on the gamepad's top
        # edge: a narrow front slab (x 16..24, rounded top-left) and its side
        # panel, whose 1:3 top slope rounds into a short right edge that stops 9
        # above the pad.
        _path(self, 'pad', (16, 22), [
            (24, 22), (32, 22), ((38, 28), 6, 6, True), (42, 38), ((38, 42), 4, 4, True), (32, 42),
            ((16, 42), 10, 10, False), (10, 42), ((6, 38), 4, 4, True), (10, 28), ((16, 22), 6, 6, True),
        ], closed=True)
        self.add_dot('stick-left', (18, 31))
        self.add_dot('stick-right', (30, 31))
        _path(self, 'console', (16, 22), [
            (16, 9), ((19, 6), 3, 3, True), (24, 6), (36, 10), ('c', (38, 10.6667), (39, 11.5), (39, 13)),
        ])
        self.add_line('slab-edge', (24, 6), (24, 22))
        self.relate('connect', 'pad', 'console')
        self.relate('connect', 'pad', 'slab-edge')
        self.relate('connect', 'console', 'slab-edge')
