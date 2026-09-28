from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fc8dfaad-7235-42f0-b2b5-49b5793896e5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__thermometer/20260927T080754Z-thuan-mac-1/reference/temperature thermometer_fc8dfaad-7235-42f0-b2b5-49b5793896e5.svg'
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
    icon_id = 'thermometer'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'weather'
    categories = ('weather', 'primitives')
    aliases = ()
    keywords = ('thermometer', 'temperature', 'heat', 'cold', 'measurement', 'weather')

    def build(self) -> None:
        # narrow Lucide-style tube (half-width 6) into an r10 bulb at the 6-8-10 points
        _path(self, "body", (18, 26), [(18, 10), ((24, 4), 6, 6, True), ((30, 10), 6, 6, True), (30, 26),
                                        ((24, 44), 10, 10, True), ((18, 26), 10, 10, True)], True)
        self.add_dot("mercury", (24, 34))
