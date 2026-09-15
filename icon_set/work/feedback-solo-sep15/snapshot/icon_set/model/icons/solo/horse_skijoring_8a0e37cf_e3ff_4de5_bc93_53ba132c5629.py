"""Reconstruct horse skijoring using its inspected source pose and full_body_ref.png. Head radius 4, center (10, 10), actual torso junction (10, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct horse skijoring using its inspected source pose and full_body_ref.png. Head radius 4, center (10, 10), actual torso junction (10, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Horse Skijoring, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8a0e37cf-e3ff-4de5-bc93-53ba132c5629'
SOURCE_PATH = 'pictographic-primitives/sports/skijoring_8a0e37cf-e3ff-4de5-bc93-53ba132c5629.svg'
AUTHOR = 'gpt-6'

class HorseSkijoring(Solo48):
    icon_id = 'horse-skijoring'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('skijoring', 'horse', 'ski', 'rider', 'snow', 'winter')

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
        """Reconstruct horse skijoring using its inspected source pose and full_body_ref.png. Head radius 4, center (10, 10), actual torso junction (10, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.add_arc('skier-head-a', (6, 10), (14, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('skier-head-b', (14, 10), (6, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('skier-1', (10, 22), *(((10.0, 24.912043955712207), (8.5, 27.25), (8, 29)),))
        self.add_line('skier-2', (8, 29), (14, 33))
        self.add_line('skier-3', (14, 33), (12, 42))
        self.add_line('tether-1', (10, 22), (14, 23))
        self.add_line('tether-2', (14, 23), (22, 28))
        self.add_line('ski-1', (6, 42), (12, 42))
        self.add_line('ski-2', (12, 42), (14, 42))
        self.add_line('horse-1', (22, 42), (22, 36))
        self.add_line('horse-2', (22, 36), (22, 28))
        self.add_line('horse-3', (22, 28), (30, 28))
        self.add_line('horse-4', (30, 28), (34, 16))
        self.add_line('horse-5', (34, 16), (38, 12))
        self.add_line('horse-6', (38, 12), (42, 18))
        self.add_line('horse-7', (42, 18), (36, 22))
        self.add_line('horse-8', (36, 22), (36, 36))
        self.add_line('horse-9', (36, 36), (36, 42))
        self.add_line('belly', (22, 36), (36, 36))
        self.add_contour('skier-head', *('skier-head-a', 'skier-head-b'), closed=True)
        self.add_contour('tether', *('tether-1', 'tether-2'), closed=False)
        self.add_contour('ski', *('ski-1', 'ski-2'), closed=False)
        self.add_contour('horse', *('horse-1', 'horse-2', 'horse-3', 'horse-4', 'horse-5', 'horse-6', 'horse-7', 'horse-8', 'horse-9'), closed=False)
        self.relate('connect', *('skier', 'tether'))
        self.relate('connect', *('ski', 'skier'))
        self.relate('connect', *('horse', 'tether'))
        self.relate('connect', *('belly', 'horse'))
        self.add_contour('skier', *('skier-1',), closed=False)
        self.add_contour('skier-section-1', *('skier-2', 'skier-3'), closed=False)
        self.relate('connect', 'skier-1', 'skier-2')
        self.relate('connect', 'skier-2', 'skier-3')
        self.relate('connect', 'skier-head-a', 'skier-head-b')
        self.relate('connect', 'skier-1', 'skier-2')
        self.relate('connect', 'skier-1', 'tether-1')
        self.relate('connect', 'skier-2', 'skier-3')
        self.relate('connect', 'skier-3', 'ski-1')
        self.relate('connect', 'skier-3', 'ski-2')
        self.relate('connect', 'tether-1', 'tether-2')
        self.relate('connect', 'tether-2', 'horse-2')
        self.relate('connect', 'tether-2', 'horse-3')
        self.relate('connect', 'ski-1', 'ski-2')
        self.relate('connect', 'horse-1', 'horse-2')
        self.relate('connect', 'horse-1', 'belly')
        self.relate('connect', 'horse-2', 'horse-3')
        self.relate('connect', 'horse-2', 'belly')
        self.relate('connect', 'horse-3', 'horse-4')
        self.relate('connect', 'horse-4', 'horse-5')
        self.relate('connect', 'horse-5', 'horse-6')
        self.relate('connect', 'horse-6', 'horse-7')
        self.relate('connect', 'horse-7', 'horse-8')
        self.relate('connect', 'horse-8', 'horse-9')
        self.relate('connect', 'horse-8', 'belly')
        self.relate('connect', 'horse-9', 'belly')
