"""Reconstruct walking stick figure with raised knee using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 9), actual torso junction (24, 21): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A stick figure steps toward the right with one knee raised and the forward arm bent horizontally. The other arm and leg extend backward beneath the upright torso and circular head.

Construction: Circular head and connected shoulder/hip graph preserve the reference posture; clothing outlines and minor folds omitted. Bounds (8,4)-(40,44).
Lucide: person-standing: separate round head, common limb junctions."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '645f152d-7c3c-5449-b4c0-0ccbea4e680d'
SOURCE_PATH = 'pictographic-primitives/wayfinding/walking_645f152d-7c3c-5449-b4c0-0ccbea4e680d.svg'
AUTHOR = 'gpt-6'

class WalkingStickFigureWithRaisedKneeVariant2(Solo48):
    icon_id = 'walking-stick-figure-with-raised-knee-v2'
    variant_of = 'walking-stick-figure-with-raised-knee'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'walking', 'stick', 'figure', 'knee', 'stride')

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
        """Reconstruct walking stick figure with raised knee using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 9), actual torso junction (24, 21): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('person-head', 29, 9, 5)
        self.add_bezier('person-body-1', (24, 21), *(((22.6, 24.36), (22.5, 28.5), (22, 31)),))
        self.add_line('person-arms-1', (8, 29), (14, 21))
        self.add_line('person-arms-2', (14, 21), (24, 21))
        self.add_line('person-arms-3', (24, 21), (30, 27))
        self.add_line('person-arms-4', (30, 27), (40, 29))
        self.add_line('person-legs-1', (10, 44), (20, 37))
        self.add_line('person-legs-2', (20, 37), (22, 31))
        self.add_line('person-legs-3', (22, 31), (36, 36))
        self.add_line('person-legs-4', (36, 36), (38, 44))
        self.add_contour('person-body', *('person-body-1',), closed=False)
        self.add_contour('person-arms', *('person-arms-1', 'person-arms-2', 'person-arms-3', 'person-arms-4'), closed=False)
        self.add_contour('person-legs', *('person-legs-1', 'person-legs-2', 'person-legs-3', 'person-legs-4'), closed=False)
        self.relate('connect', *('person-body', 'person-arms'))
        self.relate('connect', *('person-body', 'person-legs'))
