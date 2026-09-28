from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '63a44219-0af5-5214-abed-771271356b20'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ski-goggles/20260927T072849Z-thuan-mac-1/reference/glasses ski_63a44219-0af5-5214-abed-771271356b20.svg'
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
    icon_id = 'ski-goggles'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('ski', 'goggles')

    def build(self) -> None:
        # Wide ski goggles: flat strap line with a shallow dip over the nose,
        # two rounded lens lobes and a nose arch in the bottom edge.
        _path(self, 'goggles', (12, 10), [(19, 10), ('c', (20.5, 10), (20.5, 12), (22, 12)), (26, 12),
                                          ('c', (27.5, 12), (27.5, 10), (29, 10)), (36, 10),
                                          ((44, 18), 8, 8, True), (44, 26), ((32, 38), 12, 12, True),
                                          ('c', (28, 38), (28, 26), (24, 26)), ('c', (20, 26), (20, 38), (16, 38)),
                                          ((4, 26), 12, 12, True), (4, 18), ((12, 10), 8, 8, True)], True)
