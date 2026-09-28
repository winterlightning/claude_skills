from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '610733a3-dfd5-42df-9651-d396d039493b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__geometric-shapes-in-rounded-square-batch-006-02/20260926T152555Z-thuan-mac-2/reference/shapes_610733a3-dfd5-42df-9651-d396d039493b.svg'
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
    icon_id = 'geometric-shapes-in-rounded-square-batch-006-02'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('geometric', 'shapes', 'in', 'rounded', 'square')

    def build(self) -> None:
        # Plan: three geometric shapes inside a square frame on SQUARE. Frame corners
        # are square on the centerline (round joins paint the ink corners) so each
        # inner shape can sit exactly 8 from the walls straight-to-straight; inner
        # region 14..34. As in the reference: a ring (r3, exempt small circle)
        # top-right, a 6x6 square left-middle and a triangle bottom-right. The
        # triangle is small enough to ink solid (an outlined triangle with a valid
        # hole needs ~12x10, which cannot keep 8 from the other shapes).
        self.add_polyline('frame', (6, 6), (42, 6), (42, 42), (6, 42), closed=True)
        _circle(self, 'circle', 31, 17, 3)
        self.add_polyline('square', (14, 24), (20, 24), (20, 30), (14, 30), closed=True)
        self.add_polyline('triangle', (28, 34), (34, 34), (31, 30), closed=True)
