from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e4e81c34-fd66-5e7e-9aeb-a50605352799'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__igloo/20260927T070905Z-thuan-mac-1/reference/igloo_e4e81c34-fd66-5e7e-9aeb-a50605352799.svg'
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
    icon_id = 'igloo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'landmarks'
    categories = ('landmarks', 'primitives')
    aliases = ()
    keywords = ('igloo', 'snow', 'arctic', 'shelter', 'dome', 'winter', 'eskimo', 'ice')

    def build(self) -> None:
        # igloo as in the reference: a dome with a flat crown and r12 shoulders on straight walls,
        # one snow-block course line running from the left wall to the middle, and an r6 arched
        # entrance on the base line, 9 below the course.
        _path(self, "dome", (18, 40), [(4, 40), (4, 20), ((16, 8), 12, 12, True), (32, 8), ((44, 20), 12, 12, True),
                                       (44, 40), (30, 40)])
        _path(self, "door", (18, 40), [(18, 35), ((30, 35), 6, 6, True), (30, 40)])
        self.add_line("course", (4, 20), (26, 20))
        self.relate("connect", "door", "dome"); self.relate("connect", "course", "dome")
