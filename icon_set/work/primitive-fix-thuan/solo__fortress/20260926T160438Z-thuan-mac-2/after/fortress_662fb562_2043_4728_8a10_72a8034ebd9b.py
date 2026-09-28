from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '662fb562-2043-4728-8a10-72a8034ebd9b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fortress/20260926T160438Z-thuan-mac-2/reference/fortress_662fb562-2043-4728-8a10-72a8034ebd9b.svg'
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
    icon_id = 'fortress'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'protection'
    categories = ('protection', 'primitives')
    aliases = ()
    keywords = ('fortress', 'protection')

    def build(self) -> None:
        # Plan: fortress tower on HRECT_L (4..44 x 8..40), mirrored about x=24.
        # Top block spans the full width with three merlons and two crenels, each
        # exactly 8 wide and 8 deep (parallel edges exactly 8 apart). The block's
        # lower corners round (r6) into the narrower body (walls x=10/38), whose
        # foot has r3 corners, as in the reference.
        _path(self, 'tower', (4, 8), [
            (12, 8), (12, 16), (20, 16), (20, 8), (28, 8), (28, 16), (36, 16), (36, 8), (44, 8),
            (44, 18), ((38, 24), 6, 6, True), (38, 37), ((35, 40), 3, 3, True),
            (13, 40), ((10, 37), 3, 3, True), (10, 24), ((4, 18), 6, 6, True), (4, 8),
        ], closed=True)
