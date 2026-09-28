from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '012ac09f-44c3-417b-a7cd-1dcaf5b7540e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__gantt-chart-with-linked-tasks/20260927T055612Z-thuan-mac-1/reference/workflow gantt chart_012ac09f-44c3-417b-a7cd-1dcaf5b7540e.svg'
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
    icon_id = 'gantt-chart-with-linked-tasks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('gantt', 'chart', 'with', 'linked', 'tasks')

    def build(self) -> None:
        # Plan: L axis (x6 up to y6, baseline y42). Task bars are outlined
        # rectangles 10 tall: A (14..28, 6..16) in row 1; C (14..22) and B
        # (30..42) in row 2 (24..34), 8 apart. A dependency link leaves A's
        # right side (28,11), runs to x36 and drops onto B's top (36,24).
        self.add_line('axis-y', (6, 6), (6, 42))
        self.add_line('axis-x', (6, 42), (42, 42))
        self.relate('connect', 'axis-y', 'axis-x')
        _path(self, 'bar-a', (28, 11), [(28, 16), (14, 16), (14, 6), (28, 6), (28, 11)], True)
        _path(self, 'bar-b', (36, 24), [(42, 24), (42, 34), (30, 34), (30, 24), (36, 24)], True)
        _path(self, 'bar-c', (14, 24), [(22, 24), (22, 34), (14, 34), (14, 24)], True)
        _path(self, 'link', (28, 11), [(36, 11), (36, 24)])
        self.relate('connect', 'link', 'bar-a')
        self.relate('connect', 'link', 'bar-b')
