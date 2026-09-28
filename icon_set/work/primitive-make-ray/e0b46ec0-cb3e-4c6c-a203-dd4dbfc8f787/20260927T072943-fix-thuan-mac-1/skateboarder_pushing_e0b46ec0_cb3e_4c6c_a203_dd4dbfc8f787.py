from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e0b46ec0-cb3e-4c6c-a203-dd4dbfc8f787'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__skateboarder-pushing/20260927T072849Z-thuan-mac-1/reference/skateboard person_e0b46ec0-cb3e-4c6c-a203-dd4dbfc8f787.svg'
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
    icon_id = 'skateboarder-pushing'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Human construction: full_body_ref.png stick figure; r5 ring head
        # straight above a vertical neck (25,22)-(25,24) (gap exactly 8).
        _circle(self, 'head', 25, 9, 5)
        self.add_line('torso', (25, 22), (25, 24))
        self.add_line('arm-left', (25, 24), (8, 24))
        self.add_line('arm-right', (25, 24), (40, 24))
        self.add_line('torso-low', (25, 24), (21, 32))
        # Pushing leg reaches back and down to the ground; the other foot
        # rides the board right over the front wheel.
        _path(self, 'leg-push', (21, 32), [(13, 38), (8, 44)])
        self.add_line('leg-board', (21, 32), (26, 40))
        _path(self, 'board', (24, 40), [(26, 40), (38, 40), (40, 40)])
        _circle(self, 'wheel-front', 26, 42, 2)
        _circle(self, 'wheel-back', 38, 42, 2)
        for a, b in [('torso', 'arm-left'), ('torso', 'arm-right'), ('torso', 'torso-low'), ('arm-left', 'arm-right'),
                     ('arm-left', 'torso-low'), ('arm-right', 'torso-low'), ('torso-low', 'leg-push'),
                     ('torso-low', 'leg-board'), ('leg-push', 'leg-board'), ('leg-board', 'board'),
                     ('leg-board', 'wheel-front'), ('wheel-front', 'board'), ('wheel-back', 'board')]:
            self.relate('connect', a, b)
        self.mark_human_figure('skater', head='head', torso='torso', torso_junction='start')
