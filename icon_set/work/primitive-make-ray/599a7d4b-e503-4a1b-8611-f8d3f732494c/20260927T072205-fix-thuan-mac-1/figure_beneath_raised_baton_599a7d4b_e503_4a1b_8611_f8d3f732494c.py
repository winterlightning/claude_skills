from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '599a7d4b-e503-4a1b-8611-f8d3f732494c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__figure-beneath-raised-baton/20260927T072058Z-thuan-mac-1/reference/protester_599a7d4b-e503-4a1b-8611-f8d3f732494c.svg'
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
    icon_id = 'figure-beneath-raised-baton'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'crime'
    categories = ('crime', 'primitives')
    aliases = ()
    keywords = ('person', 'baton', 'arm', 'protester', 'figure', 'gesture', 'scene', 'uncertain')

    def build(self) -> None:
        # Plan: protester bust - an r5 head over rounded shoulders (9 clear);
        # the near arm is raised as an outlined 1:2 tube (edges offset (8,-4))
        # ending in a rounded fist at the top left and running down into the
        # shoulder line; a police baton swings in over the head from the top
        # right.
        _path(self, 'arm-body', (18, 42), [
            (6, 18),
            ('c', (6, 14), (6, 11), (8, 10)),
            ('c', (10, 9), (13, 11), (14, 14)),
            (26, 38),
            ('c', (28, 36.5), (30, 36), (32, 36)),
            ('c', (38, 36), (42, 38), (42, 42)),
        ])
        _circle(self, 'head', 34, 22, 5)
        self.add_line('baton', (24, 10), (42, 6))
