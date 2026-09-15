"""Reconstruct stooped walking person using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 9), actual torso junction (24, 21): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A person walks toward the right with a rounded back and lowered head. The arms hang forward near the waist, and the legs separate into a short staggered stride.

Construction: Circular head and connected shoulder/hip graph preserve the reference posture; clothing outlines and minor folds omitted. Bounds (8,4)-(40,44).
Lucide: person-standing: separate round head, common limb junctions."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '822cd704-4a41-5ae3-98e9-c89f5e699b25'
SOURCE_PATH = 'pictographic-primitives/wayfinding/walking stooped_822cd704-4a41-5ae3-98e9-c89f5e699b25.svg'
AUTHOR = 'gpt-6'

class StoopedWalkingPersonVariant2(Solo48):
    icon_id = 'stooped-walking-person-v2'
    variant_of = 'stooped-walking-person'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'walking', 'stooped', 'posture', 'pedestrian', 'figure')

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
        """Reconstruct stooped walking person using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 9), actual torso junction (24, 21): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('person-head', 29, 9, 5)
        self.add_bezier('person-body-1', (24, 21), *(((22.6, 24.36), (19.5, 27.75), (18, 30)),))
        self.add_line('person-arms-1', (24, 21), (26, 29))
        self.add_line('person-arms-2', (26, 29), (34, 32))
        self.add_line('person-legs-1', (8, 44), (18, 30))
        self.add_line('person-legs-2', (18, 30), (30, 36))
        self.add_line('person-legs-3', (30, 36), (30, 44))
        self.add_line('person-hand-1', (34, 32), (40, 32))
        self.add_contour('person-body', *('person-body-1',), closed=False)
        self.add_contour('person-arms', *('person-arms-1', 'person-arms-2'), closed=False)
        self.add_contour('person-legs', *('person-legs-1', 'person-legs-2', 'person-legs-3'), closed=False)
        self.add_contour('person-hand', *('person-hand-1',), closed=False)
        self.relate('connect', *('person-body', 'person-arms'))
        self.relate('connect', *('person-body', 'person-legs'))
        self.relate('connect', *('person-arms', 'person-hand'))
