from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '773496ab-eaad-56ae-8665-60874f75a398'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-angler-with-catch/20260927T072849Z-thuan-mac-1/reference/fishing sit_773496ab-eaad-56ae-8665-60874f75a398.svg'
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
    icon_id = 'seated-angler-with-catch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('fishing', 'angler', 'rod', 'fish', 'catch', 'sitting', 'hobby', 'outdoors', 'outdoors-batch-02')

    def build(self) -> None:
        # Human construction: full_body_ref.png stick figure seated on a box
        # at the right; r4 ring head straight above the neck (38,22)-(38,24).
        _circle(self, 'head', 38, 10, 4)
        self.add_line('torso', (38, 22), (38, 26))
        self.add_line('torso-low', (38, 26), (38, 32))
        # Arms forward to the rod butt; thigh down to the knee, shin to the
        # ground; the seat box edge drops from the hip.
        self.add_line('arm', (38, 26), (28, 22))
        _path(self, 'leg', (38, 32), [(30, 36), (30, 42)])
        self.add_line('seat', (38, 32), (38, 42))
        # Rod arcing up to its tip at the top left; line straight down to the
        # hanging fish (head up, open V tail).
        _path(self, 'rod', (28, 22), [('c', (24, 12), (17, 6), (10, 6))])
        self.add_line('line', (10, 6), (10, 17))
        _path(self, 'fish', (10, 17), [((14, 24), 4, 7, True), ((10, 31), 4, 7, True), ((6, 24), 4, 7, True),
                                       ((10, 17), 4, 7, True)], True)
        _path(self, 'tail', (6, 38), [(10, 31), (14, 38)])
        for a, b in [('torso', 'torso-low'), ('torso', 'arm'), ('torso-low', 'arm'), ('torso-low', 'leg'),
                     ('torso-low', 'seat'), ('leg', 'seat'), ('arm', 'rod'), ('rod', 'line'), ('line', 'fish'),
                     ('fish', 'tail')]:
            self.relate('connect', a, b)
        self.mark_human_figure('angler', head='head', torso='torso', torso_junction='start')
