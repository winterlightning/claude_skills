from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'af9d6fe4-e412-4354-8460-f5ecb1c67b10'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diamond-mesh-network-wifi/20260927T072058Z-thuan-mac-1/reference/mesh wifi 3_af9d6fe4-e412-4354-8460-f5ecb1c67b10.svg'
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
    icon_id = 'diamond-mesh-network-wifi'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('mesh', 'wifi', 'network', 'nodes', 'wireless', 'topology', 'connection')

    def build(self) -> None:
        # Plan (CIRCLE, 4-fold): four r3 node rings on the cardinals (outer
        # points on r20); 45-degree links join neighbouring rings at their
        # cardinal points to make the diamond; a wifi arc and dot sit in the
        # middle, 8+ from every link and ring.
        nodes = {'top': (24, 7), 'right': (41, 24), 'bottom': (24, 41), 'left': (7, 24)}
        for name, (x, y) in nodes.items():
            _circle(self, f'node-{name}', x, y, 3)
        links = [('top', (27, 7), 'right', (41, 21)), ('right', (41, 27), 'bottom', (27, 41)),
                 ('bottom', (21, 41), 'left', (7, 27)), ('left', (7, 21), 'top', (21, 7))]
        for a, p, b, q in links:
            self.add_line(f'link-{a}-{b}', p, q)
            self.relate('connect', f'link-{a}-{b}', f'node-{a}')
            self.relate('connect', f'link-{a}-{b}', f'node-{b}')
        self.add_arc('wifi-arc', (19, 22), (29, 22), radius_x=5, radius_y=3, sweep=True)
        self.add_dot('wifi-dot', (24, 29))
