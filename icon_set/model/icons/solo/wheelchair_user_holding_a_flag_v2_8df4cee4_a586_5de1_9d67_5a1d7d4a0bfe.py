"""Reconstruct wheelchair user holding a flag using its inspected source pose and full_body_ref.png. Head radius 4, center (16, 10), actual torso junction (16, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct wheelchair user holding a flag using its inspected source pose and full_body_ref.png. Head radius 4, center (16, 10), actual torso junction (16, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct wheelchair user holding a flag using its inspected source pose and full_body_ref.png. Head radius 4, center (16, 11), actual torso junction (16, 23): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct wheelchair user holding a flag using its inspected source pose and full_body_ref.png. Head radius 4, center (16, 11), actual torso junction (16, 23): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A seated wheelchair user holds a flag to the right; preserve intentional directional asymmetry.

Live keyshape centerlines: VRECT_L (8,4)-(40,44); SQUARE (6,6)-(42,42);
HRECT_L (4,8)-(44,40). Shared dimensions preserve paired proportions.
Lucide accessibility and flag: geometric construction; supplied reference: subject identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8df4cee4-a586-5de1-9d67-5a1d7d4a0bfe'
SOURCE_PATH = 'pictographic-primitives/rewards/flag_8df4cee4-a586-5de1-9d67-5a1d7d4a0bfe.svg'
AUTHOR = 'gpt-6'

class WheelchairUserHoldingAFlagVariant2(Solo48):
    icon_id = 'wheelchair-user-holding-a-flag-v2'
    variant_of = 'wheelchair-user-holding-a-flag'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/award'
    aliases = ()
    keywords = ('award', 'reward', 'wheelchair-user-holding-a-flag')

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
        """Reconstruct wheelchair user holding a flag using its inspected source pose and full_body_ref.png. Head radius 4, center (16, 10), actual torso junction (16, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.add_arc('head-a', (12, 11), (20, 11), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('head-b', (20, 11), (12, 11), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('wheel-left', (16, 23), (16, 42), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('wheel-right', (16, 42), (16, 23), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_bezier('person-1', (16, 23), *(((16.0, 25.8), (16.0, 28.25), (16, 30)),))
        self.add_line('person-2', (16, 30), (30, 30))
        self.add_line('person-3', (30, 30), (36, 40))
        self.add_line('person-4', (36, 40), (42, 40))
        self.add_line('arm-1', (16, 23), (30, 23))
        self.add_line('arm-2', (30, 23), (32, 18))
        self.add_line('pole', (32, 26), (32, 18))
        self.add_line('flag-1', (32, 18), (32, 6))
        self.add_line('flag-2', (32, 6), (42, 6))
        self.add_line('flag-3', (42, 6), (42, 16))
        self.add_line('flag-4', (42, 16), (32, 16))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('wheel', *('wheel-left', 'wheel-right'), closed=True)
        self.add_contour('arm', *('arm-1', 'arm-2'), closed=False)
        self.add_contour('flag', *('flag-1', 'flag-2', 'flag-3', 'flag-4'), closed=False)
        self.relate('connect', *('wheel', 'person'))
        self.relate('connect', *('wheel', 'arm'))
        self.relate('connect', *('person', 'arm'))
        self.relate('connect', *('pole', 'arm'))
        self.relate('connect', *('pole', 'flag'))
        self.relate('connect', *('arm', 'flag'))
        self.add_contour('person', *('person-1',), closed=False)
        self.add_contour('person-section-1', *('person-2', 'person-3', 'person-4'), closed=False)
        self.relate('connect', 'person-1', 'person-2')
        self.relate('connect', 'person-2', 'person-3')
        self.relate('connect', 'person-3', 'person-4')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'wheel-left', 'wheel-right')
        self.relate('connect', 'wheel-left', 'person-1')
        self.relate('connect', 'wheel-left', 'arm-1')
        self.relate('connect', 'wheel-right', 'person-1')
        self.relate('connect', 'wheel-right', 'arm-1')
        self.relate('connect', 'person-1', 'person-2')
        self.relate('connect', 'person-1', 'arm-1')
        self.relate('connect', 'person-2', 'person-3')
        self.relate('connect', 'person-3', 'person-4')
        self.relate('connect', 'arm-1', 'arm-2')
        self.relate('connect', 'arm-2', 'pole')
        self.relate('connect', 'arm-2', 'flag-1')
        self.relate('connect', 'pole', 'flag-1')
        self.relate('connect', 'flag-1', 'flag-2')
        self.relate('connect', 'flag-2', 'flag-3')
        self.relate('connect', 'flag-3', 'flag-4')
