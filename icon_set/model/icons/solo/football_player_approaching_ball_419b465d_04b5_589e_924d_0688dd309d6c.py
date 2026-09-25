# Repair: Preserve the approved head at (29,11) and shoulder (24,23); use a coherent torso curve tangent to the head axis. Gap 13-5=8 centerline units.
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
    category = 'sports'
    categories = ('sports', 'primitives')
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
        from ._symmetry_curves import path, ellipse, line, poly, contacts

        path(self,'head',(24,11),('A',5,5,True,(34,11)),('A',5,5,True,(24,11)),closed=True)
        ellipse(self,'ball',39,39,3)
        path(self,'body',(24,23),('C',(22.5,26.6),(18.5,28.25),(17,30)))
        poly(self,'left-arm',(24,23),(14,22),(8,26))
        poly(self,'right-arm',(24,23),(34,28),(42,28))
        poly(self,'back-leg',(17,30),(12,36),(6,36))
        poly(self,'front-leg',(17,30),(28,36),(26,42))
        contacts(self)
        self.mark_human_figure('person',head='head',torso='body-1',torso_junction='start')
