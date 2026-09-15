"""Reconstruct water skier holding tow line using its inspected source pose and full_body_ref.png. Head radius 4, center (13, 12), actual torso junction (13, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct water skier holding tow line using its inspected source pose and full_body_ref.png. Head radius 4, center (13, 12), actual torso junction (13, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct water skier holding tow line using its inspected source pose and full_body_ref.png. Head radius 4, center (13, 12), actual torso junction (13, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Water Skier. Skier leans back with bent knees against a rightward tow line; simplify doubled arms and water to keep the tow and ski readable.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '080f96e6-002a-5f7e-a063-a50263d9aaeb'
SOURCE_PATH = 'pictographic-primitives/recreation/nautic sports water skiing_080f96e6-002a-5f7e-a063-a50263d9aaeb.svg'
AUTHOR = 'gpt-6'

class WaterSkierHoldingTowLine(Solo48):
    icon_id = 'water-skier-holding-tow-line'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/recreation'
    aliases = ()
    keywords = ('water', 'skier', 'holding', 'tow', 'line')

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
        """Reconstruct water skier holding tow line using its inspected source pose and full_body_ref.png. Head radius 4, center (13, 12), actual torso junction (13, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (9, 12), (17, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('head-b', (17, 12), (9, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('body-1', (13, 24), *(((13.0, 26.56124969497314), (10.0, 27.75), (9, 29)),))
        self.add_line('body-2', (9, 29), (21, 32))
        self.add_line('body-3', (21, 32), (26, 40))
        self.add_line('arms-1', (13, 24), (25, 24))
        self.add_line('arms-2', (25, 24), (32, 19))
        self.add_line('arms-3', (32, 19), (44, 19))
        self.add_line('ski-1', (8, 40), (30, 40))
        self.add_line('ski-2', (30, 40), (36, 36))
        self.add_line('water', (4, 40), (8, 40))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('arms', *('arms-1', 'arms-2', 'arms-3'), closed=False)
        self.add_contour('ski', *('ski-1', 'ski-2'), closed=False)
        self.relate('connect', *('body', 'arms'))
        self.relate('connect', *('body', 'ski'))
        self.relate('connect', *('water', 'ski'))
        self.add_contour('body', *('body-1',), closed=False)
        self.add_contour('body-section-1', *('body-2', 'body-3'), closed=False)
        self.relate('connect', 'body-1', 'body-2')
        self.relate('connect', 'body-2', 'body-3')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'body-1', 'body-2')
        self.relate('connect', 'body-1', 'arms-1')
        self.relate('connect', 'body-2', 'body-3')
        self.relate('connect', 'arms-1', 'arms-2')
        self.relate('connect', 'arms-2', 'arms-3')
        self.relate('connect', 'ski-1', 'ski-2')
        self.relate('connect', 'ski-1', 'water')
