"""Reconstruct person walking down slope using its inspected source pose and full_body_ref.png. Head radius 5, center (27, 11), actual torso junction (22, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A person faces right and walks along a ground line sloping downward in that direction. One foot rests ahead on the incline while the other trails behind the leaning torso.

Construction: Walking person on a downward-sloping ground line. Feet share actual ground attachment points. Bounds (6,6)-(42,42).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e3784f07-e09a-57a7-a89e-249e8d5c4a3c'
SOURCE_PATH = 'pictographic-primitives/wayfinding/walking descend_e3784f07-e09a-57a7-a89e-249e8d5c4a3c.svg'
AUTHOR = 'gpt-6'

class PersonWalkingDownSlope(Solo48):
    icon_id = 'person-walking-down-slope'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('person', 'walking', 'slope', 'downhill', 'descent', 'pedestrian')

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
        """Reconstruct person walking down slope using its inspected source pose and full_body_ref.png. Head radius 5, center (27, 11), actual torso junction (22, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('person-head', 27, 11, 5)
        self.add_bezier('person-body-1', (22, 23), *(((21.02699148917896, 25.335220425970498), (20.5, 27.5), (20, 29)),))
        self.add_line('person-arms-1', (10, 26), (22, 23))
        self.add_line('person-arms-2', (22, 23), (32, 28))
        self.add_line('person-legs-1', (12, 37), (20, 29))
        self.add_line('person-legs-2', (20, 29), (30, 40))
        self.add_line('slope-1', (6, 36), (12, 37))
        self.add_line('slope-2', (12, 37), (30, 40))
        self.add_line('slope-3', (30, 40), (42, 42))
        self.add_contour('person-body', *('person-body-1',), closed=False)
        self.add_contour('person-arms', *('person-arms-1', 'person-arms-2'), closed=False)
        self.add_contour('person-legs', *('person-legs-1', 'person-legs-2'), closed=False)
        self.add_contour('slope', *('slope-1', 'slope-2', 'slope-3'), closed=False)
        self.relate('connect', *('person-body', 'person-arms'))
        self.relate('connect', *('person-body', 'person-legs'))
        self.relate('connect', *('slope', 'person-legs'))
