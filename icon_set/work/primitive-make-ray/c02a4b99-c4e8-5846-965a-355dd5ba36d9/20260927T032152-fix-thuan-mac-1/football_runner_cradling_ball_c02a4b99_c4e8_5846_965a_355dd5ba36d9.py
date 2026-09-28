from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c02a4b99-c4e8-5846-965a-355dd5ba36d9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__football-runner-cradling-ball/20260927T032037Z-thuan-mac-1/reference/american football run ball_c02a4b99-c4e8-5846-965a-355dd5ba36d9.svg'
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


class Drawing(Solo48):
    icon_id = 'football-runner-cradling-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('football', 'runner', 'cradling', 'ball')

    def build(self) -> None:
        # Plan: stick runner facing left (full_body_ref vocabulary). r5 head at
        # (24,11) over a vertical neck (24,24)-(24,26) (gap exactly 8); the
        # torso then leans forward to a set-back hip (28,34). The front arm
        # tucks into the football (rx5 ry4 about (11,26)); the back arm swings
        # bent behind; the front leg strides with a bent knee, the back leg
        # kicks up behind.
        _circle(self, 'head', 24, 11, 5)
        self.add_line('torso', (24, 24), (24, 26))
        self.add_line('torso-low', (24, 26), (28, 34))
        _path(self, 'ball', (16, 26), [((11, 30), 5, 4, True), ((6, 26), 5, 4, True),
                                      ((11, 22), 5, 4, True), ((16, 26), 5, 4, True)], True)
        self.add_line('arm-front', (24, 26), (16, 26))
        _path(self, 'arm-back', (24, 26), [(34, 22), (40, 28)])
        _path(self, 'leg-front', (28, 34), [(20, 36), (18, 42)])
        _path(self, 'leg-back', (28, 34), [(34, 41), (42, 36)])
        for a, b in [('torso', 'torso-low'), ('torso', 'arm-front'), ('torso', 'arm-back'),
                     ('torso-low', 'arm-front'), ('torso-low', 'arm-back'), ('arm-front', 'arm-back'),
                     ('arm-front', 'ball'), ('torso-low', 'leg-front'), ('torso-low', 'leg-back'),
                     ('leg-front', 'leg-back')]:
            self.relate('connect', a, b)
        self.mark_human_figure('runner', head='head', torso='torso', torso_junction='start')
