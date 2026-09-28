from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '27f83d9a-087f-47d3-81f1-dfcb21caefa7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__workflow-with-winding-connector/20260927T133651Z-thuan-mac-1/reference/workflow gantt chart_27f83d9a-087f-47d3-81f1-dfcb21caefa7.svg'
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


def _smooth(icon, name, pts, closed=True):
    """Catmull-Rom through integer knots, as cubics (closed loop or open run)."""
    n = len(pts)
    members = []
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p1, p2 = pts[i], pts[(i + 1) % n]
        p0 = pts[i - 1] if (closed or i > 0) else p1
        p3 = pts[(i + 2) % n] if (closed or i + 2 < n) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        m = f"{name}-{i + 1}"
        icon.add_bezier(m, p1, (c1, c2, p2)); members.append(m)
    icon.add_contour(name, *members, closed=closed)
    return members


class Drawing(Solo48):
    icon_id = 'workflow-with-winding-connector'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('workflow', 'with', 'winding', 'connector')

    def build(self) -> None:
        # Workflow: start box top-left, a connector winding down and right into the end box,
        # a middle task box to the right of the connector (reference arrangement).
        def box(name, x0, x1, y0, y1):
            _path(self, name, (x0, y0), [(x1, y0), (x1, y1), (x0, y1), (x0, y0)], True)
        box("step-start", 6, 22, 6, 14)
        box("step-middle", 30, 42, 18, 26)
        box("step-end", 22, 42, 34, 42)
        _path(self, "connector", (14, 14), [(14, 34), ((18, 38), 4, 4, False), (22, 38)])
        self.relate("connect", "step-start-3", "connector-1")
        self.relate("connect", "connector-3", "step-end-4")
