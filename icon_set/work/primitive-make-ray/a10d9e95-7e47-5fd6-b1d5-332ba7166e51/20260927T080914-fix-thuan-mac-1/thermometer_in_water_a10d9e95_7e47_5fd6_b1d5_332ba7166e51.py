from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a10d9e95-7e47-5fd6-b1d5-332ba7166e51'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__thermometer-in-water/20260927T080754Z-thuan-mac-1/reference/buoy_a10d9e95-7e47-5fd6-b1d5-332ba7166e51.svg'
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
    icon_id = 'thermometer-in-water'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('thermometer', 'coolant', 'temperature', 'water', 'warning', 'engine', 'dashboard', 'gauge')

    def build(self) -> None:
        # narrow thermometer (tube half-width 4, r5 bulb on its 3-4-5 points) dipped at the water line
        _path(self, "body", (20, 24), [(20, 10), ((24, 6), 4, 4, True), ((28, 10), 4, 4, True), (28, 24),
                                        ((24, 32), 5, 5, True), ((20, 24), 5, 5, True)], True)
        ys = (40, 42, 40, 42, 40, 42, 40)
        pts = [(6 + 6 * i, y) for i, y in enumerate(ys)]
        _path(self, "wave", pts[0], [('c', (x0 + 3, y0), (x1 - 3, y1), (x1, y1)) for (x0, y0), (x1, y1) in zip(pts, pts[1:])])
        _path(self, "ripple-l", (6, 30), [('c', (8, 26), (9, 26), (11, 30))])
        _path(self, "ripple-r", (37, 30), [('c', (39, 26), (40, 26), (42, 30))])
