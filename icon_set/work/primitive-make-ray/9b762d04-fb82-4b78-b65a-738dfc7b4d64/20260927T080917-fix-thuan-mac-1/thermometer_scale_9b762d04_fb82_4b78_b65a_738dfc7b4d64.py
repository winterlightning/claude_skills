from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9b762d04-fb82-4b78-b65a-738dfc7b4d64'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__thermometer-scale/20260927T080754Z-thuan-mac-1/reference/thermometer_9b762d04-fb82-4b78-b65a-738dfc7b4d64.svg'
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
    icon_id = 'thermometer-scale'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # thermometer (tube half-width 6 into r10 bulb) with two scale dashes to the right
        _path(self, "body", (12, 26), [(12, 10), ((18, 4), 6, 6, True), ((24, 10), 6, 6, True), (24, 26),
                                        ((18, 44), 10, 10, True), ((12, 26), 10, 10, True)], True)
        self.add_dot("mercury", (18, 34))
        self.add_line("tick-1", (33, 10), (40, 10))
        self.add_line("tick-2", (33, 18), (40, 18))
