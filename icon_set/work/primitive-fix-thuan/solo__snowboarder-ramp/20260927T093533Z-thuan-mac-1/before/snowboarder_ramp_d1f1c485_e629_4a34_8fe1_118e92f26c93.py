"""Snowboarder on ramp: VRECT_L gives the lifted board a full8-unit separation from the curved ramp. Radius4 head(20,8), shoulder(20,20), exact4 painted gap. Two spread legs preserve the landing stance; the source raised arm remains clear.

Snowboarder on ramp: remove the cramped horizontal thigh loop, and spread two clear legs onto the board. Radius4 head(20,10), shoulder(20,22), exact4 gap. Keep the raised arm and separate curved ramp from the source.

Preserve the snowboard and ramp/jump action; rebuild the raised arms as two clear shoulder branches. Head center(20, 10), radius4, torso(20, 22), exact4 painted gap. Full-body reference and the original action drawing inspected.

Snowboarder over Ramp, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd1f1c485-e629-4a34-8fe1-118e92f26c93'
SOURCE_PATH = 'pictographic-primitives/sports/snowskating_d1f1c485-e629-4a34-8fe1-118e92f26c93.svg'
AUTHOR = 'gpt-6'

class SnowboarderRamp(Solo48):
    icon_id = 'snowboarder-ramp'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('snowboard', 'ramp', 'board', 'snow', 'winter', 'athlete')

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
        """Snowboarder on ramp: VRECT_L gives the lifted board a full8-unit separation from the curved ramp. Radius4 head(20,8), shoulder(20,20), exact4 painted gap. Two spread legs preserve the landing stance; the source raised arm remains clear."""
        self.ring('head', 20, 8, 4)
        self.add_bezier('torso', (20, 20), *(((20, 23), (19, 25), (18, 26)),))
        self.add_line('left-arm-0', (20, 20), (8, 23))
        self.add_line('right-arm-0', (20, 20), (34, 22))
        self.add_line('right-arm-1', (34, 22), (34, 6))
        self.add_line('left-leg-0', (18, 26), (12, 34))
        self.add_line('right-leg-0', (18, 26), (30, 34))
        self.add_line('board-0', (8, 34), (12, 34))
        self.add_line('board-1', (12, 34), (30, 34))
        self.add_line('board-2', (30, 34), (38, 29))
        self.add_line('ramp-0', (8, 44), (32, 42))
        self.add_arc('ramp-tip', (32, 42), (40, 44), radius_x=8, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('right-arm', *('right-arm-0', 'right-arm-1'), closed=False)
        self.add_contour('board', *('board-0', 'board-1', 'board-2'), closed=False)
        self.relate('connect', *('left-arm-0', 'right-arm-0'))
        self.relate('connect', *('right-arm-0', 'right-arm-1'))
        self.relate('connect', *('left-leg-0', 'right-leg-0'))
        self.relate('connect', *('left-leg-0', 'board-0'))
        self.relate('connect', *('left-leg-0', 'board-1'))
        self.relate('connect', *('right-leg-0', 'board-1'))
        self.relate('connect', *('right-leg-0', 'board-2'))
        self.relate('connect', *('board-0', 'board-1'))
        self.relate('connect', *('board-1', 'board-2'))
        self.relate('connect', *('ramp-0', 'ramp-tip'))
        self.relate('connect', *('torso', 'left-arm-0'))
        self.relate('connect', *('torso', 'right-arm-0'))
        self.relate('connect', *('torso', 'left-leg-0'))
        self.relate('connect', *('torso', 'right-leg-0'))
