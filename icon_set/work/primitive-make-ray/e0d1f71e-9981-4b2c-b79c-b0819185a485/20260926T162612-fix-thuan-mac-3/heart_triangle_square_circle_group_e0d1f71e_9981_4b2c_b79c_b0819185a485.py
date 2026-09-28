from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e0d1f71e-9981-4b2c-b79c-b0819185a485'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__heart-triangle-square-circle-group/20260926T162509Z-thuan-mac/reference/photo shape_e0d1f71e-9981-4b2c-b79c-b0819185a485.svg'
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
    icon_id = 'heart-triangle-square-circle-group'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('shapes', 'heart', 'triangle', 'square', 'circle', 'geometry', 'forms', 'design')

    def build(self) -> None:
        # Plan: four outlined shapes in a 2x2 grid, as in the reference, on
        # SQUARE (6..42): cells are 14 wide with 8 between them (x 6..20 /
        # 28..42, y 6..20 / 28..42). Heart top-left: two cubic lobes from the
        # centre notch (13,9) round the tops (10,6)/(16,6) to the flanks
        # (7,13)/(19,13), straight sides to the tip (13,19). Triangle top-right:
        # apex (35,6), base y=20 (1:2 sides). Square bottom-left: sharp-cornered
        # 14x14 (straight-only, so its 8-unit gap to the circle certifies).
        # Circle bottom-right: r7 about (35,35).
        _path(self, 'heart', (13, 19), [
            (7, 13), ('c', (5.5, 11.5), (6, 6), (10, 6)), ('c', (12, 6), (13, 7.5), (13, 9)),
            ('c', (13, 7.5), (14, 6), (16, 6)), ('c', (20, 6), (20.5, 11.5), (19, 13)), (13, 19),
        ], closed=True)
        _path(self, 'triangle', (35, 6), [(42, 20), (28, 20), (35, 6)], closed=True)
        _path(self, 'square', (6, 28), [(20, 28), (20, 42), (6, 42), (6, 28)], closed=True)
        _circle(self, 'circle', 35, 35, 7)
