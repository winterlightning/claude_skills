from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b59d74df-f296-42de-9d2c-6b949b2542d4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__drink-glass-with-bent-straw/20260926T160438Z-thuan-mac-2/reference/drink_b59d74df-f296-42de-9d2c-6b949b2542d4.svg'
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
    icon_id = 'drink-glass-with-bent-straw'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('drink', 'glass', 'with', 'bent', 'straw')

    def build(self) -> None:
        # Plan: tapered drink glass with a bent straw on VRECT_L (8..40 x 4..44).
        # Glass: rim y=14 (x 8..34) tapering 1:6 to the base y=44 (x 13..29), so the
        # walls pass integer points at y=26. The liquid surface is a gentle wave
        # across the glass at y=26. The straw rises from the liquid at slope 1:2
        # through the rim at (24,14) to the top (29,4) and bends right along the
        # top edge, as in the reference; 8.9 clear of the right wall.
        _path(self, 'glass', (8, 14), [
            (24, 14), (34, 14), (32, 26), (29, 44), (13, 44), (10, 26), (8, 14),
        ], closed=True)
        _path(self, 'liquid', (10, 26), [
            ('c', (12, 24), (15, 24), (18, 26)),
            ('c', (22, 29), (28, 29), (32, 26)),
        ])
        _path(self, 'straw', (18, 26), [(24, 14), (29, 4), (40, 4)])
        self.relate('connect', 'glass', 'liquid')
        self.relate('connect', 'glass', 'straw')
        self.relate('connect', 'liquid', 'straw')
