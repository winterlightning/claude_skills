from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7344408f-27b8-52a3-bfa8-c99c266f527d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__thermometer-over-wave/20260927T080754Z-thuan-mac-1/reference/engine temperature warning_7344408f-27b8-52a3-bfa8-c99c266f527d.svg'
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
    icon_id = 'thermometer-over-wave'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('thermometer', 'engine temperature', 'coolant', 'warning', 'dashboard', 'car', 'overheating', 'gauge')

    def build(self) -> None:
        # engine-temperature symbol: thermometer with scale ticks growing from its wall, over a coolant wave
        _path(self, "body", (16, 24), [(16, 10), ((20, 6), 4, 4, True), ((24, 10), 4, 4, True), (24, 12), (24, 20), (24, 24),
                                        ((20, 32), 5, 5, True), ((16, 24), 5, 5, True)], True)
        self.add_line("tick-1", (24, 12), (34, 12))
        self.add_line("tick-2", (24, 20), (31, 20))
        self.relate("connect", "tick-1", "body-3")
        self.relate("connect", "tick-1", "body-4")
        self.relate("connect", "tick-2", "body-4")
        self.relate("connect", "tick-2", "body-5")
        ys = (40, 42, 40, 42, 40, 42, 40)
        pts = [(6 + 6 * i, y) for i, y in enumerate(ys)]
        _path(self, "wave", pts[0], [('c', (x0 + 3, y0), (x1 - 3, y1), (x1, y1)) for (x0, y0), (x1, y1) in zip(pts, pts[1:])])
