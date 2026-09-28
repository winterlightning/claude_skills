from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b2f5d7e0-b9d2-5d79-a078-0114d3e1d86a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__simple-bird-shape/20260927T072849Z-thuan-mac-1/reference/chick_b2f5d7e0-b9d2-5d79-a078-0114d3e1d86a.svg'
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
    icon_id = 'simple-bird-shape'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('bird', 'chick', 'minimal', 'simple', 'silhouette', 'beak', 'shape', 'animal')

    def build(self) -> None:
        # Chick facing right (reference silhouette): r10 domed head about
        # (26,16), straight chest x=36 with a wedge beak, round belly
        # (rx15/ry12 about (21,30)) and the tail point at the left (6,30).
        _path(self, 'chick', (16, 16), [((26, 6), 10, 10, True), ((36, 16), 10, 10, True), (42, 21), (36, 24),
                                        (36, 30), ((21, 42), 15, 12, True), ((6, 30), 15, 12, True),
                                        ('c', (12, 30), (16, 26), (16, 20)), (16, 16)], True)
        self.add_dot('eye', (27, 17))
