from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '91683884-b0eb-5afc-b49b-78ad39aa8ee5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hot-steaming-food-bowl/20260926T164653Z-thuan-mac/reference/pasta bowl warm_91683884-b0eb-5afc-b49b-78ad39aa8ee5.svg'
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
    icon_id = 'hot-steaming-food-bowl'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('hot', 'steaming', 'food', 'bowl')

    def build(self) -> None:
        # Plan: hot bowl as in the reference, on SQUARE (6..42): a full-width rim
        # line (y=28) closed by a shallow half-ellipse body (rx18, ry14, bottom
        # y=42), and three tall thin wavy steam lines above it (x 12/24/36,
        # y 6..19), each two tangent-continuous cubics (one wave) drawn in phase
        # so neighbours stay more than 8 apart.
        _path(self, 'bowl', (6, 28), [(42, 28), ((24, 42), 18, 14, True), ((6, 28), 18, 14, True)], closed=True)
        for i, x in enumerate((12, 24, 36)):
            _path(self, f'steam-{i}', (x, 19), [('c', (x + 3, 16), (x + 3, 15), (x, 12)),
                                                 ('c', (x - 3, 9), (x - 3, 8), (x, 6))])
