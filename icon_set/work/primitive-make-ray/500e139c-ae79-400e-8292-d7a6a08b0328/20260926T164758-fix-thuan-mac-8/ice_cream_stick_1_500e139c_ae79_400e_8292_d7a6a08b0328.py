from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '500e139c-ae79-400e-8292-d7a6a08b0328'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ice-cream-stick-1/20260926T164653Z-thuan-mac/reference/ice cream stick 1_500e139c-ae79-400e-8292-d7a6a08b0328.svg'
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
    icon_id = 'ice-cream-stick-1'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('ice', 'cream', 'stick', 'food')

    def build(self) -> None:
        # Plan: ice pop as in the reference, on VRECT_M (x 10..38, y 4..44): a
        # half-ellipse dome (rx14, ry12, top y=4) as wide as the body, a straight
        # coating line across at y=16, straight sides down to r4 rounded bottom
        # corners at y=34, and a long centred stick from the bottom to y=44.
        # Mirrored about x=24.
        _path(self, 'pop', (10, 16), [
            ((24, 4), 14, 12, True), ((38, 16), 14, 12, True), (38, 30), ((34, 34), 4, 4, True), (24, 34),
            (14, 34), ((10, 30), 4, 4, True), (10, 16),
        ], closed=True)
        self.add_line('coating', (10, 16), (38, 16))
        self.relate('connect', 'pop', 'coating')
        self.add_line('stick', (24, 34), (24, 44))
        self.relate('connect', 'pop', 'stick')
