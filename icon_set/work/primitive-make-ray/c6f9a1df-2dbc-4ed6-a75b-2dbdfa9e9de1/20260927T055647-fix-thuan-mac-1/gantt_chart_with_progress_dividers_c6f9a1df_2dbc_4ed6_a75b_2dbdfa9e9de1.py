from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c6f9a1df-2dbc-4ed6-a75b-2dbdfa9e9de1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gantt-chart-with-progress-dividers/20260927T055612Z-thuan-mac-1/reference/workflow gantt chart_c6f9a1df-2dbc-4ed6-a75b-2dbdfa9e9de1.svg'
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
    icon_id = 'gantt-chart-with-progress-dividers'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('gantt', 'chart', 'with', 'progress', 'dividers')

    def build(self) -> None:
        # Plan: three staggered task bars 8 tall with r3 corners on rows
        # y4-12, 20-28, 36-44: A x8..24 (divider x16), B x12..40 (divider x22),
        # C x24..40. A vertical today line x=32 runs y4..44 through B and C,
        # splitting them at shared nodes; it stays 8 right of A.
        def bar(name, x0, x1, y0, y1, splits):
            top = [((x, y0)) for x in sorted(splits)]
            bot = [((x, y1)) for x in sorted(splits, reverse=True)]
            pts = [(x0 + 3, y0)] + top + [(x1 - 3, y0)]
            steps = [p for p in pts[1:]] + [((x1, y0 + 3), 3, 3, True), (x1, y1 - 3), ((x1 - 3, y1), 3, 3, True)]
            steps += bot + [(x0 + 3, y1), ((x0, y1 - 3), 3, 3, True), (x0, y0 + 3), ((x0 + 3, y0), 3, 3, True)]
            _path(self, name, pts[0], steps, True)
            for x in splits:
                self.add_line(f'{name}-div-{x}', (x, y0), (x, y1))
                self.relate('connect', f'{name}-div-{x}', name)
        bar('bar-a', 8, 24, 4, 12, [16])
        bar('bar-b', 12, 40, 20, 28, [22, 32])
        bar('bar-c', 24, 40, 36, 44, [32])
        self.add_line('today-top', (32, 4), (32, 20))
        self.add_line('today-mid', (32, 28), (32, 36))
        for a, b in [('today-top', 'bar-b'), ('today-top', 'bar-b-div-32'), ('today-mid', 'bar-b'),
                     ('today-mid', 'bar-b-div-32'), ('today-mid', 'bar-c'), ('today-mid', 'bar-c-div-32')]:
            self.relate('connect', a, b)
