from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1ba4c70f-408e-58e8-8311-a5a121bceed9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fast-motion/20260927T072058Z-thuan-mac-1/reference/fast motion_1ba4c70f-408e-58e8-8311-a5a121bceed9.svg'
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
    icon_id = 'fast-motion'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video'
    categories = ('video', 'primitives')
    aliases = ()
    keywords = ('motion', 'fast', 'speed', 'trail', 'movement', 'circle', 'velocity')

    def build(self) -> None:
        # Plan (CIRCLE): a ball (r10 ring, right point on r20) rushing right,
        # trailing three staggered rows of speed lines: the top and bottom
        # rows run off its tangent points, the middle row stops 8 short of
        # it (left end on r20); a short dash leads each outer row.
        _circle(self, 'ball', 34, 24, 10)
        self.add_line('trail-top', (20, 14), (34, 14))
        self.add_line('trail-bottom', (24, 34), (34, 34))
        self.relate('connect', 'trail-top', 'ball')
        self.relate('connect', 'trail-bottom', 'ball')
        self.add_line('trail-middle', (4, 24), (16, 24))
        self.add_line('dash-top', (8, 14), (12, 14))
        self.add_line('dash-bottom', (12, 34), (16, 34))
