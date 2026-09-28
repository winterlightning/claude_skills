from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f99e66ec-4007-4de6-af8e-e56fc675139c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__six-mobile-phones-in-grid/20260927T072849Z-thuan-mac-1/reference/devicefarm_f99e66ec-4007-4de6-af8e-e56fc675139c.svg'
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
    icon_id = 'six-mobile-phones-in-grid'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('phone', 'tablet', 'device', 'mobile', 'screen', 'technology', 'communication', 'hardware')

    def build(self) -> None:
        # Six phones in a 3x2 grid (device farm): 8x12 portrait bodies with
        # r2 corners, 8 apart. The reference home bar has no room: a chin
        # needs 8 between bar and bottom edge.
        for col, x in enumerate((4, 20, 36)):
            for row, y in enumerate((8, 28)):
                _path(self, f'phone-{col}{row}', (x + 2, y), [(x + 6, y), ((x + 8, y + 2), 2, 2, True), (x + 8, y + 10),
                                                          ((x + 6, y + 12), 2, 2, True), (x + 2, y + 12),
                                                          ((x, y + 10), 2, 2, True), (x, y + 2), ((x + 2, y), 2, 2, True)], True)
