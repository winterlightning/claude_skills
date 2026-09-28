from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4b7521df-9e30-4205-9f5c-c5cc20293e20'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fire-sprinkler/20260927T032037Z-thuan-mac-1/reference/safety extinguish fire_4b7521df-9e30-4205-9f5c-c5cc20293e20.svg'
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
    icon_id = 'fire-sprinkler'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('sprinkler', 'fire', 'water', 'safety', 'extinguish', 'flame')

    def build(self) -> None:
        # Plan: ceiling line y4 (x8..40) with the sprinkler pipe hanging from
        # it (24,4)-(24,8); below it the Lucide `flame` rebuilt at 10/7 scale:
        # r10 body about (24,34) (bottom 44), tip (24,16) 8 below the pipe,
        # and the notch bowl (rx4 ry3 about (19,30)) on the lower left.
        self.add_line('ceiling-l', (8, 4), (24, 4))
        self.add_line('ceiling-r', (24, 4), (40, 4))
        self.add_line('pipe', (24, 4), (24, 8))
        for a, b in [('ceiling-l', 'ceiling-r'), ('ceiling-l', 'pipe'), ('ceiling-r', 'pipe')]:
            self.relate('connect', a, b)
        _path(self, 'flame', (19, 33), [
            ((23, 30), 4, 3, False),
            ('c', (23, 28), (23, 27), (22, 25)),
            ('c', (20, 22), (19.5, 18.5), (24, 16)),
            ('c', (26, 19), (30, 22), (32, 26)),
            ('c', (33.5, 28.5), (34, 31), (34, 34)),
            ((24, 44), 10, 10, True), ((14, 34), 10, 10, True),
            ('c', (14, 32.4), (14.6, 30.7), (15, 30)),
            ((19, 33), 4, 3, False),
        ], True)
