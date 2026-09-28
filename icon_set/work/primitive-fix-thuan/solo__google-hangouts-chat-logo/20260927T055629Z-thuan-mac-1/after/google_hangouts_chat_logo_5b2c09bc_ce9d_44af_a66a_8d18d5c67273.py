from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5b2c09bc-ce9d-44af-a66a-8d18d5c67273'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-hangouts-chat-logo/20260927T055629Z-thuan-mac-1/reference/google hangouts chat logo_5b2c09bc-ce9d-44af-a66a-8d18d5c67273.svg'
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
    icon_id = 'google-hangouts-chat-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google-chat', 'hangouts', 'google', 'chat', 'at-sign', 'logo', 'brand')

    def build(self) -> None:
        # Bubble: the r20 keyshape circle, its lower-left sweeping in to a
        # short tail whose vertical edge stands at x=24 (as in the reference).
        _path(self, 'bubble', (8, 36), [((4, 24), 20, 20, True), ((44, 24), 20, 20, True),
                                        ((24, 44), 20, 20, True), (24, 40),
                                        ('c', (18, 40), (11, 40), (8, 36))], True)
        # @ about (24,24): open r3 counter (6-diameter ring), hook from its
        # east point to the east point of the r11 outer curl (9 inside the
        # bubble); the curl runs over the top and ends low on the left,
        # clear of the tail.
        _circle(self, 'counter', 24, 24, 3)
        _path(self, 'curl', (27, 24), [('c', (27, 31), (35, 31), (35, 24)), ((13, 24), 11, 11, False),
                                       ('c', (13, 27), (13, 28), (14, 30))])
        self.relate('connect', 'counter', 'curl')
