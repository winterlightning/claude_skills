from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1f2dcc1e-b398-5e14-8191-3905a417325f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__football-player-kicking-ball-sports/20260927T032039Z-thuan-mac-1/reference/player kick_1f2dcc1e-b398-5e14-8191-3905a417325f.svg'
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
    icon_id = 'football-player-kicking-ball-sports'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('football', 'soccer', 'player', 'ball', 'kick', 'sport')

    def build(self) -> None:
        # Human construction: full_body_ref.png stick figure, r4 ring head set
        # straight above a vertical neck (24,20)-(24,22): 12 from the head
        # centre = 8 on centerlines, 4 of visible ink. Arms branch at the
        # shoulder (24,22); the torso runs on to the hip (24,29).
        _circle(self, 'head', 24, 8, 4)
        self.add_line('torso', (24, 20), (24, 22))
        self.add_line('torso-low', (24, 22), (24, 29))
        # Arms: left bent down at the elbow, right raised high.
        _path(self, 'arm-left', (24, 22), [(15, 20), (8, 24)])
        _path(self, 'arm-right', (24, 22), [(33, 18), (40, 11)])
        # Legs: back leg bent at the knee with the foot kicked up behind,
        # front leg striding forward; the ball sits between them.
        _path(self, 'leg-back', (24, 29), [(17, 34), (8, 32)])
        _path(self, 'leg-front', (24, 29), [(36, 30), (40, 40)])
        for a, b in [('torso', 'torso-low'), ('torso', 'arm-right'), ('torso', 'arm-left'),
                     ('torso-low', 'arm-right'), ('torso-low', 'arm-left'), ('arm-right', 'arm-left'),
                     ('torso-low', 'leg-back'), ('torso-low', 'leg-front'), ('leg-back', 'leg-front')]:
            self.relate('connect', a, b)
        _circle(self, 'ball', 27, 41, 3)
        self.mark_human_figure('player', head='head', torso='torso', torso_junction='start')
