"""Inline skater: a curved leaning back, one pushing leg and one planted skate replace the parallel arm/thigh crowding. Radius4 head(29,10), shoulder(29,22), exact4 gap. Keep paired skate wheels and the source skating action.

Inline skater: a curved leaning back, one pushing leg and one planted skate replace the parallel arm/thigh crowding. Radius4 head(29,10), shoulder(29,22), exact4 gap. Keep paired skate wheels and the source skating action.

Reconstruct inline skater using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct inline skater using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct inline skater using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Inline skater, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '630e00b6-b3a3-4ec4-9e34-5b14d7140829'
SOURCE_PATH = 'pictographic-primitives/sports/rollerblades person_630e00b6-b3a3-4ec4-9e34-5b14d7140829.svg'
AUTHOR = 'gpt-6'

class InlineSkater(Solo48):
    icon_id = 'inline-skater'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('inline', 'skater')

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
        """Inline skater: a curved leaning back, one pushing leg and one planted skate replace the parallel arm/thigh crowding. Radius4 head(29,10), shoulder(29,22), exact4 gap. Keep paired skate wheels and the source skating action."""
        self.add_arc('head-a', (25, 10), (33, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('head-b', (33, 10), (25, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('torso', (29, 22), *(((29, 25), (24, 26), (21, 27)),))
        self.add_line('left-arm-0', (29, 22), (14, 22))
        self.add_line('left-arm-1', (14, 22), (10, 18))
        self.add_line('right-arm-0', (29, 22), (36, 24))
        self.add_line('right-arm-1', (36, 24), (42, 24))
        self.add_line('front-leg-0', (21, 27), (30, 30))
        self.add_line('front-leg-1', (30, 30), (28, 34))
        self.add_line('back-leg-0', (21, 27), (13, 30))
        self.add_line('back-leg-1', (13, 30), (6, 26))
        self.add_line('skate-0', (25, 34), (28, 34))
        self.add_line('skate-1', (28, 34), (33, 34))
        self.add_line('front-a', (25, 42), (25, 42))
        self.add_line('front-b', (33, 42), (33, 42))
        self.add_line('rear-a', (6, 36), (6, 36))
        self.add_line('rear-b', (14, 39), (14, 39))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('left-arm', *('left-arm-0', 'left-arm-1'), closed=False)
        self.add_contour('right-arm', *('right-arm-0', 'right-arm-1'), closed=False)
        self.add_contour('front-leg', *('front-leg-0', 'front-leg-1'), closed=False)
        self.add_contour('back-leg', *('back-leg-0', 'back-leg-1'), closed=False)
        self.add_contour('skate', *('skate-0', 'skate-1'), closed=False)
        self.relate('connect', *('left-arm-0', 'left-arm-1'))
        self.relate('connect', *('left-arm-0', 'right-arm-0'))
        self.relate('connect', *('right-arm-0', 'right-arm-1'))
        self.relate('connect', *('front-leg-0', 'front-leg-1'))
        self.relate('connect', *('front-leg-0', 'back-leg-0'))
        self.relate('connect', *('front-leg-1', 'skate-0'))
        self.relate('connect', *('front-leg-1', 'skate-1'))
        self.relate('connect', *('back-leg-0', 'back-leg-1'))
        self.relate('connect', *('skate-0', 'skate-1'))
        self.relate('connect', *('torso', 'left-arm-0'))
        self.relate('connect', *('torso', 'right-arm-0'))
        self.relate('connect', *('torso', 'front-leg-0'))
        self.relate('connect', *('torso', 'back-leg-0'))
