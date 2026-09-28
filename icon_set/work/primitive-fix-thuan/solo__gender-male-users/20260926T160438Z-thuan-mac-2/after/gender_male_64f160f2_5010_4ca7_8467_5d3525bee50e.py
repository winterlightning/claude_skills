from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '64f160f2-5010-4ca7-8467-5d3525bee50e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gender-male-users/20260926T160438Z-thuan-mac-2/reference/gender male_64f160f2-5010-4ca7-8467-5d3525bee50e.svg'
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
    icon_id = 'gender-male-users'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('gender', 'male', 'users')

    def build(self) -> None:
        # Plan: male sign (Lucide mars) on SQUARE. Ring r15 about (21,27) touching the
        # left and bottom edges; its upper-right quarter is two cubics through the
        # 45-degree point (32,16) (a 45-degree point on an integer circle is never on
        # the grid), the other three quarters are cardinal arcs. The shaft leaves the
        # ring there at 45 degrees to the top-right corner (42,6), where the open
        # right-angle arrowhead (two 9-long arms along the edges) meets it.
        k = 15 * 4 / 3 * 0.198912  # cubic handle for a 45-degree arc of radius 15
        d = k / 2 ** 0.5
        _path(self, 'ring', (21, 12), [
            ('c', (21 + k, 12), (32 - d, 16 - d), (32, 16)),
            ('c', (32 + d, 16 + d), (36, 27 - k), (36, 27)),
            ((21, 42), 15, 15, True), ((6, 27), 15, 15, True), ((21, 12), 15, 15, True),
        ], closed=True)
        self.add_line('shaft', (32, 16), (42, 6))
        _path(self, 'arrowhead', (33, 6), [(42, 6), (42, 15)])
        self.relate('connect', 'ring', 'shaft')
        self.relate('connect', 'shaft', 'arrowhead')
