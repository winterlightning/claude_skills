from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7b497a79-d5cc-43a6-98ba-cd8d83a4f562'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__domed-coffee-maker-with-side-spout-and-handle/20260927T072058Z-thuan-mac-1/reference/coffee cold press_7b497a79-d5cc-43a6-98ba-cd8d83a4f562.svg'
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
    icon_id = 'domed-coffee-maker-with-side-spout-and-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'drinks'
    categories = ('drinks', 'primitives')
    aliases = ()
    keywords = ('pour', 'over', 'coffee', 'maker')

    def build(self) -> None:
        # Plan (near-mirrored about x=24): cold-press brewer - r12 dome lid on
        # a brim line; a brew chamber whose sides slope in 1:4 from the brim
        # (12..36) to (16..32), sitting on a rounded carafe (15..33); a D
        # handle on the left from the brim end to the chamber side, and a
        # pouring lip rising off the brim on the right.
        self.add_arc('dome', (12, 18), (36, 18), radius_x=12, radius_y=12, sweep=True)
        _path(self, 'brim', (6, 18), [(12, 18), (36, 18), (38, 18), (42, 14)])
        _path(self, 'chamber-left', (12, 18), [(14, 26), (16, 34)])
        self.add_line('chamber-right', (36, 18), (32, 34))
        _path(self, 'carafe', (15, 34), [(16, 34), (32, 34), (33, 34), (33, 38), ('c', (33, 40.5), (31.5, 42), (29, 42)),
                                         (19, 42), ('c', (16.5, 42), (15, 40.5), (15, 38)), (15, 34)], True)
        _path(self, 'handle', (6, 18), [('c', (6, 23), (9, 26.5), (14, 26))])
        for a, b in [('dome', 'brim'), ('chamber-left', 'brim'), ('chamber-right', 'brim'), ('chamber-left', 'carafe'),
                     ('chamber-right', 'carafe'), ('handle', 'brim'), ('handle', 'chamber-left')]:
            self.relate('connect', a, b)
