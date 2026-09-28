from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '727add99-ce34-4828-932a-d2567ed13149'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ice-skate-boot/20260926T164653Z-thuan-mac/reference/skate ice_727add99-ce34-4828-932a-d2567ed13149.svg'
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
    icon_id = 'ice-skate-boot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('ice-skate', 'skating', 'winter', 'sport', 'blade', 'rink', 'boot', 'figure-skating')

    def build(self) -> None:
        # Plan: ice-skate boot as in the reference, on SQUARE (6..42). Boot: a
        # big r6 rounded heel, straight back (x=6), a collar sloping up to the
        # front (6,10)->(24,6), a straight shaft front, a sloping instep (two
        # tangent cubics) that rounds over the toe down to the flat sole (y=32).
        # Two single posts (x 14/30) carry a flat blade (y=42) whose front curls
        # up in an r6 quarter arc, 8 clear of the toe.
        _path(self, 'boot', (12, 32), [
            ((6, 26), 6, 6, True), (6, 10), (24, 6), (24, 14),
            ('c', (24, 18), (26, 19), (29, 20)), ('c', (32, 21), (34, 26), (34, 32)),
            (30, 32), (14, 32), (12, 32),
        ], closed=True)
        _path(self, 'blade', (6, 42), [(14, 42), (30, 42), (36, 42), ((42, 36), 6, 6, False)])
        self.add_line('rear-post', (14, 32), (14, 42))
        self.add_line('front-post', (30, 32), (30, 42))
        for post in ('rear-post', 'front-post'):
            self.relate('connect', 'boot', post)
            self.relate('connect', 'blade', post)
