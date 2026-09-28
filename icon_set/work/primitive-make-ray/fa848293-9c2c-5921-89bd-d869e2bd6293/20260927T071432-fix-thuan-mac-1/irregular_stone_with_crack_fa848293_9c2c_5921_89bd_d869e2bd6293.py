from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fa848293-9c2c-5921-89bd-d869e2bd6293'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__irregular-stone-with-crack/20260927T070909Z-thuan-mac-1/reference/material stone_fa848293-9c2c-5921-89bd-d869e2bd6293.svg'
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
    icon_id = 'irregular-stone-with-crack'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('irregular', 'stone', 'with', 'crack')

    def build(self) -> None:
        # irregular stone: eight-sided outline with round joins; a zigzag crack runs in from the left edge
        self.add_polyline("stone", (15, 6), (30, 6), (42, 16), (42, 30), (30, 42), (16, 40), (6, 28), (8, 16), closed=True)
        self.add_polyline("crack", (7, 22), (16, 20), (21, 25), (27, 30))
        self.relate("connect", "stone", "crack")
