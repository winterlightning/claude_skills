"""Reconstruct pool jump using its inspected source pose and full_body_ref.png. Head radius 5, center (36, 18), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct pool jump using its inspected source pose and full_body_ref.png. Head radius 5, center (36, 18), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct pool jump using its inspected source pose and full_body_ref.png. Head radius 5, center (36, 18), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Pool Jump, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0647ba7a-9aee-4d01-9f39-460d6cba1bee'
SOURCE_PATH = 'pictographic-primitives/sports/swimming jump_0647ba7a-9aee-4d01-9f39-460d6cba1bee.svg'
AUTHOR = 'gpt-6'

class PoolJump(Solo48):
    icon_id = 'pool-jump'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('pool', 'jump', 'swimmer', 'water', 'diving', 'sport')

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
        """Reconstruct pool jump using its inspected source pose and full_body_ref.png. Head radius 5, center (36, 18), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (31, 18), (41, 18), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (41, 18), (31, 18), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('body-1', (16, 6), (24, 23))
        self.add_bezier('body-2', (24, 23), *(((20.64, 24.4), (15.0, 22.25), (12, 22)),))
        self.add_line('body-3', (12, 22), (23, 30))
        self.add_line('body-4', (23, 30), (18, 32))
        self.add_line('arm', (24, 23), (12, 13))
        self.add_line('edge-1', (6, 42), (14, 42))
        self.add_line('edge-2', (14, 42), (14, 40))
        self.add_line('edge-3', (14, 40), (30, 40))
        self.add_arc('water-a', (30, 40), (36, 40), radius_x=3, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('water-b', (36, 40), (42, 40), radius_x=3, radius_y=2, large_arc=False, sweep=False)
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('edge', *('edge-1', 'edge-2', 'edge-3'), closed=False)
        self.add_contour('water', *('water-a', 'water-b'), closed=False)
        self.relate('connect', *('arm', 'body'))
        self.relate('connect', *('edge', 'water'))
        self.add_contour('body', *('body-1',), closed=False)
        self.add_contour('body-section-1', *('body-2',), closed=False)
        self.add_contour('body-section-2', *('body-3', 'body-4'), closed=False)
        self.relate('connect', 'body-1', 'body-2')
        self.relate('connect', 'body-2', 'body-3')
        self.relate('connect', 'body-3', 'body-4')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'body-1', 'body-2')
        self.relate('connect', 'body-1', 'arm')
        self.relate('connect', 'body-2', 'body-3')
        self.relate('connect', 'body-2', 'arm')
        self.relate('connect', 'body-3', 'body-4')
        self.relate('connect', 'edge-1', 'edge-2')
        self.relate('connect', 'edge-2', 'edge-3')
        self.relate('connect', 'edge-3', 'water-a')
        self.relate('connect', 'water-a', 'water-b')
