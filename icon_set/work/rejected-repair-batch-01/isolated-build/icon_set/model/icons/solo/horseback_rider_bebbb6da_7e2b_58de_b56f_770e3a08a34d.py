"""Reconstruct horseback rider using its inspected source pose and full_body_ref.png. Head radius 4, center (18, 8), actual torso junction (18, 20): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct horseback rider using its inspected source pose and full_body_ref.png. Head radius 4, center (18, 8), actual torso junction (18, 20): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Horse Rider. Upright rider on a right-facing horse; retain long muzzle, ear, tail and two visible legs, omit reins and doubled limbs.
Keyshape VRECT_L, visible extremes (6, 2, 42, 46); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bebbb6da-7e2b-58de-b56f-770e3a08a34d'
SOURCE_PATH = 'pictographic-primitives/recreation/outdoors horse_bebbb6da-7e2b-58de-b56f-770e3a08a34d.svg'
AUTHOR = 'gpt-6'

class HorsebackRider(Solo48):
    icon_id = 'horseback-rider'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/recreation'
    aliases = ()
    keywords = ('horseback', 'rider')

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
        """Reconstruct horseback rider using its inspected source pose and full_body_ref.png. Head radius 4, center (18, 8), actual torso junction (18, 20): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.add_arc('rider-head-a', (14, 8), (22, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('rider-head-b', (22, 8), (14, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('rider-1', (18, 20), *(((18.0, 23.2), (18.0, 26.0), (18, 28)),))
        self.add_line('rider-2', (18, 28), (27, 28))
        self.add_line('arm-1', (18, 20), (26, 22))
        self.add_line('arm-2', (26, 22), (32, 17))
        self.add_line('horse-1', (9, 44), (9, 36))
        self.add_line('horse-2', (9, 36), (9, 30))
        self.add_line('horse-3', (9, 30), (15, 28))
        self.add_line('horse-4', (15, 28), (27, 28))
        self.add_line('horse-5', (27, 28), (32, 17))
        self.add_line('horse-6', (32, 17), (33, 12))
        self.add_line('horse-7', (33, 12), (40, 20))
        self.add_line('horse-8', (40, 20), (40, 25))
        self.add_line('horse-9', (40, 25), (34, 24))
        self.add_line('horse-10', (34, 24), (33, 33))
        self.add_line('horse-11', (33, 33), (33, 36))
        self.add_line('horse-12', (33, 36), (33, 44))
        self.add_line('tail-1', (9, 30), (8, 37))
        self.add_line('belly', (9, 36), (33, 36))
        self.add_contour('rider-head', *('rider-head-a', 'rider-head-b'), closed=True)
        self.add_contour('arm', *('arm-1', 'arm-2'), closed=False)
        self.add_contour('horse', *('horse-1', 'horse-2', 'horse-3', 'horse-4', 'horse-5', 'horse-6', 'horse-7', 'horse-8', 'horse-9', 'horse-10', 'horse-11', 'horse-12'), closed=False)
        self.add_contour('tail', *('tail-1',), closed=False)
        self.relate('connect', *('rider', 'arm'))
        self.relate('connect', *('rider', 'horse'))
        self.relate('connect', *('arm', 'horse'))
        self.relate('connect', *('tail', 'horse'))
        self.relate('connect', *('belly', 'horse'))
        self.add_contour('rider', *('rider-1',), closed=False)
        self.add_contour('rider-section-1', *('rider-2',), closed=False)
        self.relate('connect', 'rider-1', 'rider-2')
        self.relate('connect', 'rider-head-a', 'rider-head-b')
        self.relate('connect', 'rider-1', 'rider-2')
        self.relate('connect', 'rider-1', 'arm-1')
        self.relate('connect', 'rider-2', 'horse-4')
        self.relate('connect', 'rider-2', 'horse-5')
        self.relate('connect', 'arm-1', 'arm-2')
        self.relate('connect', 'arm-2', 'horse-5')
        self.relate('connect', 'arm-2', 'horse-6')
        self.relate('connect', 'horse-1', 'horse-2')
        self.relate('connect', 'horse-1', 'belly')
        self.relate('connect', 'horse-2', 'horse-3')
        self.relate('connect', 'horse-2', 'tail-1')
        self.relate('connect', 'horse-2', 'belly')
        self.relate('connect', 'horse-3', 'horse-4')
        self.relate('connect', 'horse-3', 'tail-1')
        self.relate('connect', 'horse-4', 'horse-5')
        self.relate('connect', 'horse-5', 'horse-6')
        self.relate('connect', 'horse-6', 'horse-7')
        self.relate('connect', 'horse-7', 'horse-8')
        self.relate('connect', 'horse-8', 'horse-9')
        self.relate('connect', 'horse-9', 'horse-10')
        self.relate('connect', 'horse-10', 'horse-11')
        self.relate('connect', 'horse-11', 'horse-12')
        self.relate('connect', 'horse-11', 'belly')
        self.relate('connect', 'horse-12', 'belly')
