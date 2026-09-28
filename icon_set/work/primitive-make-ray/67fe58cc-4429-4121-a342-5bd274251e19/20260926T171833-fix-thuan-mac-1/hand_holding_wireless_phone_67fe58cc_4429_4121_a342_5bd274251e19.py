from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '67fe58cc-4429-4121-a342-5bd274251e19'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-wireless-phone/20260926T171707Z-thuan-mac-1/reference/wifi transfer hand_67fe58cc-4429-4121-a342-5bd274251e19.svg'
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
    icon_id = 'hand-holding-wireless-phone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'phones'
    categories = ('phones', 'primitives')
    aliases = ()
    keywords = ('hand', 'phone', 'wireless', 'signal', 'holding', 'mobile')

    def build(self) -> None:
        # Phone 14..34 x 14..42 with r4 corners (centres (18,18), (30,18), (18,38)); its lower-right
        # corner is hidden by the hand. Signal: one r13 arc per top corner, concentric with it.
        _path(self, 'phone', (34, 32), [(34, 20), (34, 18), ((30, 14), 4, 4, False), (18, 14),
                                         ((14, 18), 4, 4, False), (14, 38), ((18, 42), 4, 4, False), (30, 42)])
        self.add_arc('signal-left', (6, 13), (13, 6), radius_x=13, sweep=True)
        self.add_arc('signal-right', (35, 6), (42, 13), radius_x=13, sweep=True)
        # Hand from the lower right: the back of the hand (r8 about (34,28)) leaves the phone's
        # edge; the thumb (r5 3-4-5 tip about (28,33)) lies across the screen at 45 degrees, its
        # upper edge (x - y = 2) running through the phone edge to the wrist line.
        self.add_arc('hand-back', (34, 20), (42, 28), radius_x=8, sweep=True)
        self.add_line('wrist-upper', (42, 28), (42, 40))
        self.add_line('wrist-lower', (42, 40), (42, 42))
        self.add_contour('hand', 'hand-back', 'wrist-upper', 'wrist-lower')
        self.relate('connect', 'hand', 'phone')
        _path(self, 'thumb', (42, 40), [(34, 32), (32, 30), ((25, 37), 5, 5, False, True), (30, 42)])
        self.relate('connect', 'thumb', 'phone')
        self.relate('connect', 'thumb', 'hand')
