"""A running player moves toward a round ball at the lower right. One leg bends backward, the other drops forward, and both arms curve outward to balance the stride.

Forward approach, trailing bent leg and lower-right ball retained.
Human reference: icon_set/references/human_ref/full_body_ref.png; retain its
circular head and connected round-ended limbs. Lucide person-standing original
and atomic-debug inform shared shoulder/hip nodes and a separate circular head.

Head center (29, 11) and shoulder (24, 23) follow the upper torso tangent.
Head center to shoulder is exactly sqrt(5**2 + 12**2) = 13.
With head radius 5 and stroke width 4, the head-outline/body centerline gap
is 13 - 5 = 8 and the painted gap is 8 - 4 = 4. This is measured to the
actual torso endpoint, not an arm positioned nearer the head.
The circular head is enlarged to balance the figure and preserve exact spacing
on the integer grid. Shared reference: full_body_ref.png.
SQUARE ink bounds remain (4, 4)-(44, 44); asymmetric limbs preserve the stride.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '419b465d-04b5-589e-924d-0688dd309d6c'
SOURCE_PATH = 'pictographic-primitives/sports/player ball_419b465d-04b5-589e-924d-0688dd309d6c.svg'
AUTHOR = 'gpt-6'

class FootballPlayerApproachingBall(Solo48):
    icon_id = 'football-player-approaching-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('football', 'soccer', 'player', 'ball', 'running', 'sport')

    def circle(self, name, x, y, r):
        self.add_arc(name + '-top', (x - r, y), (x + r, y), radius_x=r)
        self.add_arc(name + '-bottom', (x + r, y), (x - r, y), radius_x=r)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

    def skeleton(self, branches):
        parts = []
        for name, points in branches:
            members = []
            for index, (a, b) in enumerate(zip(points, points[1:])):
                key = f'{name}-{index}'
                members.append(key)
                self.add_line(key, a, b)
                parts.append((key, a, b))
            if len(members) > 1:
                self.add_contour(name, *members)
        for index, (a, p, q) in enumerate(parts):
            for b, r, s in parts[index + 1:]:
                if p in (r, s) or q in (r, s):
                    self.relate('connect', a, b)

    def build(self):
        head_center = (29, 11)
        head_radius = 5
        shoulder = (24, 23)
        hip = (17, 30)
        self.circle('head', *head_center, head_radius)
        self.circle('ball', 39, 39, 3)
        self.add_arc('body', shoulder, hip, radius_x=13)
        self.skeleton([
            ('left-arm', [shoulder, (14, 22), (10, 28)]),
            ('right-arm', [shoulder, (34, 28), (42, 28)]),
            ('back-leg', [hip, (12, 36), (6, 36)]),
            ('front-leg', [hip, (28, 36), (26, 42)]),
        ])
        for member in ('left-arm-0', 'right-arm-0', 'back-leg-0', 'front-leg-0'):
            self.relate('connect', 'body', member)
