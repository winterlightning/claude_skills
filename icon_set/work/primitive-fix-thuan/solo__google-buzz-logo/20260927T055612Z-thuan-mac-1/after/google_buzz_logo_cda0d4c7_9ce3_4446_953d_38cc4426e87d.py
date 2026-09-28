from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'cda0d4c7-9ce3-4446-953d-38cc4426e87d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-buzz-logo/20260927T055612Z-thuan-mac-1/reference/google buzz logo_cda0d4c7-9ce3-4446-953d-38cc4426e87d.svg'
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
    icon_id = 'google-buzz-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google-buzz', 'google', 'social', 'speech-bubble', 'logo', 'brand', 'chat')

    def build(self) -> None:
        # Plan: Buzz bubble = ellipse (about (24,22), rx18 ry16) drawn as
        # tangent cubics through integer knots, opening at P1(8,29)/P2(24,38)
        # into a tail with tip T(7,42). The long stroke runs on x+y=49 from T
        # through the rim at K(38,11) and out to (42,7); two strokes square to
        # it: from the rim at U(11,12) in to (24,25), and from (26,23) out to
        # the rim at Q(37,34).
        import math
        cx, cy, rx, ry = 24, 22, 18, 16
        knots = [(8, 29), (6, 22), (11, 12), (24, 6), (38, 11), (42, 22), (37, 34), (24, 38)]
        def tan(p):
            nx, ny = (p[0] - cx) / rx ** 2, (p[1] - cy) / ry ** 2
            t = (-ny, nx); n = math.hypot(*t)
            return (t[0] / n, t[1] / n)   # clockwise on screen
        steps = []
        for a, b in zip(knots, knots[1:]):
            L = math.dist(a, b) / 3 * 1.05
            ta, tb = tan(a), tan(b)
            steps.append(('c', (a[0] + L * ta[0], a[1] + L * ta[1]), (b[0] - L * tb[0], b[1] - L * tb[1]), b))
        steps += [(7, 42), (8, 29)]
        _path(self, 'bubble', knots[0], steps, True)
        self.add_line('slash-low', (7, 42), (24, 25))
        self.add_line('slash-mid', (24, 25), (26, 23))
        self.add_line('slash-high', (26, 23), (38, 11))
        self.add_line('slash-out', (38, 11), (42, 7))
        self.add_line('arm-a', (11, 12), (24, 25))
        self.add_line('arm-b', (26, 23), (37, 34))
        for a, b in [('slash-low', 'bubble'), ('slash-low', 'slash-mid'), ('slash-mid', 'slash-high'),
                     ('slash-high', 'slash-out'), ('slash-high', 'bubble'), ('slash-out', 'bubble'),
                     ('arm-a', 'bubble'), ('arm-a', 'slash-low'), ('arm-a', 'slash-mid'),
                     ('arm-b', 'bubble'), ('arm-b', 'slash-mid'), ('arm-b', 'slash-high')]:
            self.relate('connect', a, b)
