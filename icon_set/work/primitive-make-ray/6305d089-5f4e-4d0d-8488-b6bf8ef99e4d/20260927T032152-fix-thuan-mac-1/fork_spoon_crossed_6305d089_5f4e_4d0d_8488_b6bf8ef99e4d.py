from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6305d089-5f4e-4d0d-8488-b6bf8ef99e4d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fork-spoon-crossed/20260927T032037Z-thuan-mac-1/reference/spoon and fork_6305d089-5f4e-4d0d-8488-b6bf8ef99e4d.svg'
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
    icon_id = 'fork-spoon-crossed'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Plan: crossed cutlery on the two 45-degree axes, crossing at (26,26).
        # Fork on y=x: handle (42,42) up to a middle tine tip (8,8); outer tines
        # offset +-(6,-6) (8.5 apart) join in a smooth U through apex (20,20).
        # Spoon on x+y=52: handle from (10,42) to an oval bowl about (36,16)
        # (half-length 4, half-width 3 in axis units), bowl foot S(32,20)
        # kept 8.5 off the fork line.
        self.add_line('fork-tine-mid', (8, 8), (20, 20))
        self.add_line('fork-neck', (20, 20), (26, 26))
        self.add_line('fork-handle', (26, 26), (42, 42))
        _path(self, 'fork-head', (6, 18), [(10, 22), ('c', (13, 25), (17, 23), (20, 20)),
                                          ('c', (23, 17), (25, 13), (22, 10)), (18, 6)])
        self.add_line('spoon-handle', (10, 42), (26, 26))
        self.add_line('spoon-neck', (26, 26), (32, 20))
        k = 0.5523
        c, a, b = (36, 16), 4, 3
        ends = [(c[0] - a, c[1] + a), (c[0] - b, c[1] - b), (c[0] + a, c[1] - a), (c[0] + b, c[1] + b)]
        def v(p, q): return (q[0] - c[0], q[1] - c[1])
        steps = []
        for i in range(4):
            p0, p1 = ends[i], ends[(i + 1) % 4]
            t0, t1 = v(c, p1), v(c, p0)
            steps.append(('c', (p0[0] + k * t0[0], p0[1] + k * t0[1]), (p1[0] + k * t1[0], p1[1] + k * t1[1]), p1))
        _path(self, 'spoon-bowl', ends[0], steps, True)
        for x, y in [('fork-tine-mid', 'fork-neck'), ('fork-neck', 'fork-handle'), ('fork-head', 'fork-tine-mid'),
                     ('fork-head', 'fork-neck'), ('spoon-handle', 'spoon-neck'), ('spoon-neck', 'spoon-bowl'),
                     ('spoon-handle', 'fork-neck'), ('spoon-handle', 'fork-handle'),
                     ('spoon-neck', 'fork-neck'), ('spoon-neck', 'fork-handle')]:
            self.relate('connect', x, y)
