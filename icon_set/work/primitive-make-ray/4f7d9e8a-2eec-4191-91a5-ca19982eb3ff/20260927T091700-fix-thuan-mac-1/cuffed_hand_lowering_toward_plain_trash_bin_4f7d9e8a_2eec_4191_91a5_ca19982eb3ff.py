from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4f7d9e8a-2eec-4191-91a5-ca19982eb3ff'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cuffed-hand-lowering-toward-plain-trash-bin/20260927T091424Z-thuan-mac-1/reference/recycling hand trash_4f7d9e8a-2eec-4191-91a5-ca19982eb3ff.svg'
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
    icon_id = 'cuffed-hand-lowering-toward-plain-trash-bin'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'ecology'
    categories = ('primitives', 'ecology')
    aliases = ()
    keywords = ('hand', 'bin', 'trash', 'waste', 'disposal', 'cuff', 'recycling', 'ecology')

    def build(self) -> None:
        # Plan (VRECT_L): cuff box (32,6)-(40,20) at top-right, taller than the
        # wrist; hand = back of the hand rising from the cuff to a knuckle (26,4),
        # then a long index finger pointing down-left on a 1:3 band (r5 tip about
        # (14,13)), a V notch and an r4 thumb about (28,15) closing on the cuff.
        # Plain tapered cup bin below: rim line y=28, rounded bottom corners.
        _path(self, 'cuff', (32, 8), [(32, 6), (40, 6), (40, 20), (32, 20), (32, 15)])
        self.add_line('cuff-side', (32, 8), (32, 15))
        _path(self, 'hand', (32, 8), [
            (26, 4), (11, 9), ((14, 18), 5, 5, False), (24, 15),
            ((28, 19), 4, 4, False), ((32, 15), 4, 4, False),
        ])
        for a, b in (('cuff', 'cuff-side'), ('hand', 'cuff'), ('hand', 'cuff-side')):
            self.relate('connect', a, b)
        self.add_line('rim', (8, 28), (34, 28))
        _path(self, 'bin', (11, 28), [
            (13, 41), ('c', (13.5, 43), (14.5, 44), (16, 44)), (26, 44),
            ('c', (27.5, 44), (28.5, 43), (29, 41)), (31, 28),
        ])
        self.relate('connect', 'rim', 'bin')
