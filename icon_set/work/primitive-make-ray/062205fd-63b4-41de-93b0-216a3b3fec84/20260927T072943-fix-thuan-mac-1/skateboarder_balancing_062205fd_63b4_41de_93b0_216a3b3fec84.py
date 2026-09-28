from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '062205fd-63b4-41de-93b0-216a3b3fec84'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__skateboarder-balancing/20260927T072849Z-thuan-mac-1/reference/skateboard person_062205fd-63b4-41de-93b0-216a3b3fec84.svg'
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
    icon_id = 'skateboarder-balancing'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Human construction: full_body_ref.png stick figure; r5 ring head
        # straight above a vertical neck (26,22)-(26,24) (gap exactly 8).
        _circle(self, 'head', 26, 9, 5)
        self.add_line('torso', (26, 22), (26, 24))
        # Arms spread level for balance (reference's wide arm bar).
        self.add_line('arm-left', (26, 24), (8, 24))
        self.add_line('arm-right', (26, 24), (40, 24))
        self.add_line('torso-low', (26, 24), (22, 32))
        # Back leg held straight out behind, 8 below the arms and 8 above the
        # board; front leg down to the board over the rear wheel.
        self.add_line('leg-back', (22, 32), (8, 32))
        self.add_line('leg-front', (22, 32), (30, 40))
        _path(self, 'board', (12, 40), [(16, 40), (30, 40), (34, 40), (38, 40)])
        _circle(self, 'wheel-left', 16, 42, 2)
        _circle(self, 'wheel-right', 34, 42, 2)
        for a, b in [('torso', 'arm-left'), ('torso', 'arm-right'), ('torso', 'torso-low'), ('arm-left', 'arm-right'),
                     ('arm-left', 'torso-low'), ('arm-right', 'torso-low'), ('torso-low', 'leg-back'),
                     ('torso-low', 'leg-front'), ('leg-back', 'leg-front'), ('leg-front', 'board'),
                     ('wheel-left', 'board'), ('wheel-right', 'board')]:
            self.relate('connect', a, b)
        self.mark_human_figure('skater', head='head', torso='torso', torso_junction='start')
