from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8d47f316-c40a-4959-bfb4-5b4ee2cac87e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__coworkers-with-laptop/20260927T072058Z-thuan-mac-1/reference/co working space team laptop_8d47f316-c40a-4959-bfb4-5b4ee2cac87e.svg'
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


def _smooth(knots, closed=False):
    """Catmull-Rom steps through integer knots (horizontal/vertical tangents stay exact)."""
    pts = list(knots)
    n = len(pts)
    steps = []
    for i in range(n - 1 if not closed else n):
        p0 = pts[i - 1] if (i > 0 or closed) else pts[i]
        p1, p2 = pts[i], pts[(i + 1) % n]
        p3 = pts[(i + 2) % n] if (i + 2 < n or closed) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        steps.append(('c', c1, c2, p2))
    return steps


class Drawing(Solo48):
    icon_id = 'coworkers-with-laptop'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'office'
    categories = ('office', 'primitives')
    aliases = ()
    keywords = ('coworkers', 'laptop', 'team', 'desk', 'people', 'office')

    def build(self) -> None:
        # Plan: two coworkers across a table - the near one (left, head r7) and
        # the far one (right, head r5, set back) - with an open laptop whose
        # screen leans back between them and hides their inner shoulders.
        self.add_line('table', (4, 40), (44, 40))
        _path(self, 'screen', (20, 40), [(21, 34), (22, 28), (34, 28), (33, 34), (32, 40)])
        self.relate('connect', 'screen', 'table')
        _circle(self, 'head-near', 12, 15, 7)
        _path(self, 'shoulders-near', (4, 40), [('c', (4, 34), (8, 31), (12, 31)), ('c', (16, 31), (20, 32), (21, 34))])
        _circle(self, 'head-far', 38, 13, 5)
        _path(self, 'shoulders-far', (44, 40), [('c', (44, 31), (41, 27), (38, 27)), ('c', (35, 27), (33, 30), (33, 34))])
        for part in ('shoulders-near', 'shoulders-far'):
            self.relate('connect', part, 'table')
            self.relate('connect', part, 'screen')
