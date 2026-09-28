from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ef989e1c-ca2d-4808-9e01-23f51f35f24a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dog-food-bowl/20260927T032037Z-thuan-mac-1/reference/dog food_ef989e1c-ca2d-4808-9e01-23f51f35f24a.svg'
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
    icon_id = 'dog-food-bowl'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'pets'
    categories = ('pets', 'primitives')
    aliases = ()
    keywords = ('dog-food', 'bowl', 'kibble', 'feeding', 'pet', 'food', 'dish')

    def build(self) -> None:
        # Plan: sloped bowl (rim y24, base y38) under a three-bump kibble mound
        # that rises from the rim corners (8,24)/(40,24); mirrored about x=24.
        _path(self, 'bowl', (8, 24), [(40, 24), (44, 38), (4, 38), (8, 24)], True)
        _path(self, 'food', (8, 24), [((16, 17), 8, 7, True), ((24, 10), 8, 7, True),
                                      ((32, 17), 8, 7, True), ((40, 24), 8, 7, True)])
        self.relate('connect', 'food', 'bowl')
