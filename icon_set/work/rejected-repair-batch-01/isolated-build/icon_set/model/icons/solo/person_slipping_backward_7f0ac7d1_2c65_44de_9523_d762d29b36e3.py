"""Reconstruct person slipping backward using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct person slipping backward using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct person slipping backward using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A person slipping with arms flung out and feet to the lower left. SQUARE extremes (6,6)-(42,42). Lucide person-standing informs the connected stick framework; follow the source image pose rather than mirroring its directional text. Preserve the asymmetric splayed limbs and falling lean."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7f0ac7d1-2c65-44de-9523-d762d29b36e3'
SOURCE_PATH = 'pictographic-primitives/symbol/person slipping rocky_7f0ac7d1-2c65-44de-9523-d762d29b36e3.svg'
AUTHOR = 'gpt-6'

class PersonSlippingBackward(Solo48):
    icon_id = 'person-slipping-backward'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('slip', 'fall', 'person', 'accident', 'hazard', 'trip', 'injury', 'warning')

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
        """Reconstruct person slipping backward using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (24, 11), (34, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (34, 11), (24, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('body-leg-1', (24, 23), *(((22.6, 26.36), (21.0, 29.75), (20, 32)),))
        self.add_line('body-leg-2', (20, 32), (14, 42))
        self.add_line('arm-left-1', (24, 23), (14, 20))
        self.add_line('arm-left-2', (14, 20), (10, 10))
        self.add_line('arm-right-1', (24, 23), (36, 28))
        self.add_line('arm-right-2', (36, 28), (42, 32))
        self.add_line('leg-left-1', (20, 32), (12, 32))
        self.add_line('leg-left-2', (12, 32), (6, 38))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('arm-left', *('arm-left-1', 'arm-left-2'), closed=False)
        self.add_contour('arm-right', *('arm-right-1', 'arm-right-2'), closed=False)
        self.add_contour('leg-left', *('leg-left-1', 'leg-left-2'), closed=False)
        self.relate('connect', *('body-leg', 'arm-left'))
        self.relate('connect', *('body-leg', 'arm-right'))
        self.relate('connect', *('body-leg', 'leg-left'))
        self.add_contour('body-leg', *('body-leg-1',), closed=False)
        self.add_contour('body-leg-section-1', *('body-leg-2',), closed=False)
        self.relate('connect', 'body-leg-1', 'body-leg-2')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'body-leg-1', 'body-leg-2')
        self.relate('connect', 'body-leg-1', 'arm-left-1')
        self.relate('connect', 'body-leg-1', 'arm-right-1')
        self.relate('connect', 'body-leg-1', 'leg-left-1')
        self.relate('connect', 'body-leg-2', 'leg-left-1')
        self.relate('connect', 'arm-left-1', 'arm-left-2')
        self.relate('connect', 'arm-left-1', 'arm-right-1')
        self.relate('connect', 'arm-right-1', 'arm-right-2')
        self.relate('connect', 'leg-left-1', 'leg-left-2')
