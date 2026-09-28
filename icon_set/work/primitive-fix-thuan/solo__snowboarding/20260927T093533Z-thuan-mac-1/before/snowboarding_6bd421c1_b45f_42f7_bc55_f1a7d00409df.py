"""Snowboarding: establish a torso and real hip rather than attaching every limb at one point. Radius5 head(37,17), shoulder(25,22), squared distance169 and exact4 painted gap; upper torso follows the horizontal lean. Keep the raised arm and two legs on the upturned board; the far arm is hidden by this side pose. Original and full_body_ref.png inspected.

Crouching snowboarder on a sloping board. Lucide accessibility informs articulated figure strokes. Raised arm, bent knees and board retained; no clothing detail added.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6bd421c1-b45f-42f7-bc55-f1a7d00409df'
SOURCE_PATH = 'pictographic-primitives/symbol/skiing_6bd421c1-b45f-42f7-bc55-f1a7d00409df.svg'
AUTHOR = 'gpt-6'

class Snowboarding(Solo48):
    icon_id = 'snowboarding'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('snowboarding', 'snowboard', 'winter', 'sport', 'snow', 'mountain', 'ride', 'extreme')

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
        """Snowboarding: establish a torso and real hip rather than attaching every limb at one point. Radius5 head(37,17), shoulder(25,22), squared distance169 and exact4 painted gap; upper torso follows the horizontal lean. Keep the raised arm and two legs on the upturned board; the far arm is hidden by this side pose. Original and full_body_ref.png inspected."""
        self.ring('head', 37, 17, 5)
        self.add_bezier('torso', (25, 22), ((21.4, 23.5), (20, 25), (20, 27)))
        self.branches([('raised-arm', [(25, 22), (14, 20), (22, 6)]), ('left-leg', [(20, 27), (12, 34)]), ('right-leg', [(20, 27), (24, 38)]), ('board', [(6, 32), (12, 34), (24, 38), (30, 40)])])
        for p in ['raised-arm-0', 'left-leg-0', 'right-leg-0']:
            self.relate('connect', 'torso', p)
        self.add_arc('tip', (30, 40), (42, 40), radius_x=6, radius_y=2, sweep=False)
        self.relate('connect', 'board-2', 'tip')
