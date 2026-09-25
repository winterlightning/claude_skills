"""Preserve the snowboard and ramp/jump action; rebuild the raised arms as two clear shoulder branches. Head center(23, 11), radius5, torso(23, 24), exact4 painted gap. Full-body reference and the original action drawing inspected.

Snowboard Jump, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b8a4c620-274c-490b-adc6-1f6dfce51d92'
SOURCE_PATH = 'pictographic-primitives/sports/snowskating_b8a4c620-274c-490b-adc6-1f6dfce51d92.svg'
AUTHOR = 'gpt-6'

class SnowboardJump(Solo48):
    icon_id = 'snowboard-jump'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('snowboard', 'jump', 'board', 'snow', 'winter', 'athlete')

    def ring(self, name, x, y, r):
        self.add_arc(name + '-a', (x - r, y), (x + r, y), radius_x=r)
        self.add_arc(name + '-b', (x + r, y), (x - r, y), radius_x=r)
        self.add_contour(name, name + '-a', name + '-b', closed=True)

    def branches(self, branches):
        parts = []
        for name, points in branches:
            members = []
            for i, (a, b) in enumerate(zip(points, points[1:])):
                key = f'{name}-{i}'
                self.add_line(key, a, b)
                members.append(key)
                parts.append((key, a, b))
            if len(members) > 1:
                self.add_contour(name, *members)
        for i, (name, a, b) in enumerate(parts):
            for other, c, d in parts[i + 1:]:
                if a in (c, d) or b in (c, d):
                    self.relate('connect', name, other)

    def build(self):
        """Preserve the snowboard and ramp/jump action; rebuild the raised arms as two clear shoulder branches. Head center(23, 11), radius5, torso(23, 24), exact4 painted gap. Full-body reference and the original action drawing inspected."""
        self.ring('head', 23, 11, 5)
        self.add_bezier('torso-1', (23, 24), *(((23, 26), (19, 27), (19, 28)),))
        self.add_line('torso-2', (19, 28), (26, 31))
        self.add_line('torso-3', (26, 31), (24, 37))
        self.add_line('rear-leg-1', (19, 28), (12, 35))
        self.add_line('rear-leg-2', (12, 35), (14, 42))
        self.add_line('board-1', (6, 42), (14, 42))
        self.add_line('board-2', (14, 42), (24, 37))
        self.add_line('board-3', (24, 37), (40, 29))
        self.add_contour('torso', *('torso-1', 'torso-2', 'torso-3'), closed=False)
        self.add_contour('rear-leg', *('rear-leg-1', 'rear-leg-2'), closed=False)
        self.add_contour('board', *('board-1', 'board-2', 'board-3'), closed=False)
        self.relate('connect', *('torso', 'rear-leg'))
        self.relate('connect', *('board', 'torso'))
        self.relate('connect', *('board', 'rear-leg'))
        self.branches([('left-arm', [(23, 24), (12, 24), (6, 17)]), ('right-arm', [(23, 24), (35, 24), (42, 15)])])
        self.relate('connect', 'torso-1', 'left-arm-0')
        self.relate('connect', 'torso-1', 'right-arm-0')
