from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b65f68ff-83c3-5c4a-9b2d-bb76e66ff665'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__iot-pin-markers/20260926T164653Z-thuan-mac/reference/internet of thing analytics services_b65f68ff-83c3-5c4a-9b2d-bb76e66ff665.svg'
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
    icon_id = 'iot-pin-markers'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Plan: IoT hub linked to device pins as in the reference, on HRECT_L
        # (x 4..44, y 8..40): a large r5 hub ring on top (24,13), a stem down to
        # an r4 node ring (24,28), and two r4 device rings level with it at the
        # sides (8,28)/(40,28); each small ring stands 8 above its own short base
        # stroke on y=40. The reference's flat diamond bases become base strokes
        # (a diamond that small closes into a sliver hole). Mirrored about x=24.
        _circle(self, 'hub', 24, 13, 5)
        self.add_line('stem', (24, 18), (24, 24))
        _circle(self, 'node', 24, 28, 4)
        self.relate('connect', 'hub', 'stem')
        self.relate('connect', 'stem', 'node')
        self.add_line('node-base', (20, 40), (28, 40))
        for side, x in (('left', 8), ('right', 40)):
            _circle(self, f'{side}-pin', x, 28, 4)
            self.add_line(f'{side}-base', (x - 4, 40), (x + 4, 40))
