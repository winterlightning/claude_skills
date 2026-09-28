from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '48e5cfea-33eb-5928-8f29-422a48899ccf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__football-player-controlling-ball/20260927T032039Z-thuan-mac-1/reference/player_48e5cfea-33eb-5928-8f29-422a48899ccf.svg'
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
    icon_id = 'football-player-controlling-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('football', 'soccer', 'player', 'ball', 'control', 'sport')

    def build(self) -> None:
        # Human construction: full_body_ref.png stick figure, r5 ring head set
        # straight above a vertical neck (26,24)-(26,26); the neck is 13 below
        # the head centre = 8 on centerlines, 4 of visible ink. Arms branch at
        # the shoulder (26,26) so they never approach the head.
        _circle(self, 'head', 26, 11, 5)
        self.add_line('torso', (26, 24), (26, 26))
        self.add_line('torso-low', (26, 26), (26, 34))
        # Right arm raised high; left arm held out over the ball.
        _path(self, 'arm-right', (26, 26), [(35, 25), (42, 17)])
        _path(self, 'arm-left', (26, 26), [(16, 27)])
        # Legs from the hip: support leg down to the turf, other leg lifted back.
        _path(self, 'leg-support', (26, 34), [(22, 42)])
        _path(self, 'leg-lifted', (26, 34), [(32, 39), (37, 36)])
        for a, b in [('torso', 'torso-low'), ('torso', 'arm-right'), ('torso', 'arm-left'),
                     ('torso-low', 'arm-right'), ('torso-low', 'arm-left'), ('arm-right', 'arm-left'),
                     ('torso-low', 'leg-support'), ('torso-low', 'leg-lifted'), ('leg-support', 'leg-lifted')]:
            self.relate('connect', a, b)
        # Ball on the ground in front of the player.
        _circle(self, 'ball', 10, 38, 4)
        self.mark_human_figure('player', head='head', torso='torso', torso_junction='start')
