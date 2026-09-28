from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3fe88fdd-16b8-494f-b26e-461659c58008'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hairpin-turn-right/20260926T162509Z-thuan-mac/reference/hairpin turn right_3fe88fdd-16b8-494f-b26e-461659c58008.svg'
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
    icon_id = 'hairpin-turn-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('hairpin', 'turn', 'right', 'transportation')

    def build(self) -> None:
        # Plan: hairpin-turn arrow as in the reference, on SQUARE (6..42): a
        # straight stem up the left edge (x=6, y 42..20), an r14 semicircle over
        # the top (centre (20,20), apex (20,6)) and a shorter right leg down to
        # the tip (34,34), finished by a 45-degree open arrowhead whose arms reach
        # (26,26) and the right edge (42,26).
        _path(self, 'road', (6, 42), [
            (6, 20), ((20, 6), 14, 14, True), ((34, 20), 14, 14, True), (34, 34),
        ])
        _path(self, 'head', (26, 26), [(34, 34), (42, 26)])
        self.relate('connect', 'road', 'head')
