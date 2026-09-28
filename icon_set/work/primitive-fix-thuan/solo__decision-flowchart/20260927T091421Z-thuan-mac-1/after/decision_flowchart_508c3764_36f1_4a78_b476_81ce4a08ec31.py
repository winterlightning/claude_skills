from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '508c3764-36f1-4a78-b476-81ce4a08ec31'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__decision-flowchart/20260927T091421Z-thuan-mac-1/reference/workflow gantt chart_508c3764-36f1-4a78-b476-81ce4a08ec31.svg'
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
    icon_id = 'decision-flowchart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('decision', 'flowchart')

    def build(self) -> None:
        # Decision flowchart as in the reference: two process boxes stacked on the left (16x8, 8 apart,
        # square centerline corners so every gap certifies straight-to-straight), a decision diamond on
        # the right (half-diagonal 8 about (34,26)). The top box feeds the diamond's top vertex with an
        # elbow, the bottom box feeds its left vertex, and the exit leaves the bottom vertex with an
        # elbow to the right edge.
        _path(self, "box-top", (6, 6), [(22, 6), (22, 14), (6, 14), (6, 6)], True)
        _path(self, "box-bottom", (6, 22), [(22, 22), (22, 30), (6, 30), (6, 22)], True)
        _path(self, "diamond", (26, 26), [(34, 18), (42, 26), (34, 34), (26, 26)], True)
        _path(self, "flow-top", (22, 10), [(34, 10), (34, 18)])
        self.add_line("flow-bottom", (22, 26), (26, 26))
        _path(self, "flow-exit", (34, 34), [(34, 42), (42, 42)])
        for a, b in (("box-top", "flow-top"), ("flow-top", "diamond"), ("box-bottom", "flow-bottom"),
                     ("flow-bottom", "diamond"), ("diamond", "flow-exit")):
            self.relate("connect", a, b)
