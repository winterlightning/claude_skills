from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3744324f-3989-4c12-8a15-5cbfbc7b6920'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tick-parasite/20260927T080808Z-thuan-mac-1/reference/pets tick_3744324f-3989-4c12-8a15-5cbfbc7b6920.svg'
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
    icon_id = 'tick-parasite'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'pets'
    categories = ('pets', 'primitives')
    aliases = ()
    keywords = ('tick', 'parasite', 'flea', 'insect', 'pest', 'pet-health', 'bug')

    def build(self) -> None:
        # Tick (reference): oval body through integer knots (smooth
        # Catmull-Rom cubics), a short head nub on top, and four curved legs
        # per side like the reference, each an r13 arc turning 45 degrees:
        # front leg leaves up-left and ends heading up, middle legs leave
        # sideways (attachments 8 apart) and bend up / down, back leg leaves
        # down-left and ends heading down. Mirrored about x=24.
        knots = [(24, 12), (30, 15), (33, 20), (33, 28), (30, 33), (24, 36),
                 (18, 33), (15, 28), (15, 20), (18, 15)]
        n = len(knots)
        steps = []
        for i in range(n):
            p0, p1, p2, p3 = knots[i - 1], knots[i], knots[(i + 1) % n], knots[(i + 2) % n]
            c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
            c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
            steps.append(('c', c1, c2, p2))
        _path(self, 'body', knots[0], steps, True)
        self.add_line('head', (24, 12), (24, 6))
        self.relate('connect', 'head', 'body')
        legs = [((18, 15), (14, 6), True), ((15, 20), (6, 16), True),
                ((15, 28), (6, 32), False), ((18, 33), (14, 42), False)]
        for i, (a, b, sw) in enumerate(legs):
            self.add_arc(f'leg-left-{i}', a, b, radius_x=13, radius_y=13, sweep=sw)
            self.add_arc(f'leg-right-{i}', (48 - a[0], a[1]), (48 - b[0], b[1]), radius_x=13, radius_y=13, sweep=not sw)
            self.relate('connect', f'leg-left-{i}', 'body')
            self.relate('connect', f'leg-right-{i}', 'body')
