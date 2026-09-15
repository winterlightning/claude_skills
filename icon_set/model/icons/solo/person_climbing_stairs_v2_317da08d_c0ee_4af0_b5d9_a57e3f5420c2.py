"""Reconstruct person climbing stairs using its inspected source pose and full_body_ref.png. Head radius 5, center (23, 11), actual torso junction (18, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct person climbing stairs using its inspected source pose and full_body_ref.png. Head radius 5, center (23, 11), actual torso junction (18, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A person faces right and steps onto a short rising staircase. One knee lifts over a step while the rear leg remains lower, and the arms swing beside the torso.

Construction: Walking figure with one foot on a three-step staircase. Distinct knee and arm positions indicate the direction of travel. Bounds (6,6)-(42,42).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '317da08d-c0ee-4af0-b5d9-a57e3f5420c2'
SOURCE_PATH = 'pictographic-primitives/wayfinding/stairs person ascend_317da08d-c0ee-4af0-b5d9-a57e3f5420c2.svg'
AUTHOR = 'gpt-6'

class PersonClimbingStairsVariant2(Solo48):
    icon_id = 'person-climbing-stairs-v2'
    variant_of = 'person-climbing-stairs'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'stairs', 'ascending', 'climbing', 'steps', 'wayfinding')

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
        """Reconstruct person climbing stairs using its inspected source pose and full_body_ref.png. Head radius 5, center (23, 11), actual torso junction (18, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('person-head-a', (18, 11), (28, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('person-head-b', (28, 11), (18, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('person-body-1', (18, 23), *(((17.02699148917896, 25.335220425970498), (16.5, 27.5), (16, 29)),))
        self.add_line('person-arms-1', (6, 27), (18, 23))
        self.add_line('person-arms-2', (18, 23), (27, 27))
        self.add_line('person-legs-1', (8, 42), (16, 29))
        self.add_line('person-legs-2', (16, 29), (26, 28))
        self.add_line('person-legs-3', (26, 28), (30, 30))
        self.add_line('stairs-1', (20, 42), (20, 36))
        self.add_line('stairs-2', (20, 36), (30, 36))
        self.add_line('stairs-3', (30, 36), (30, 30))
        self.add_line('stairs-4', (30, 30), (36, 30))
        self.add_line('stairs-5', (36, 30), (36, 24))
        self.add_line('stairs-6', (36, 24), (42, 24))
        self.add_contour('person-head', *('person-head-a', 'person-head-b'), closed=True)
        self.add_contour('person-body', *('person-body-1',), closed=False)
        self.add_contour('person-arms', *('person-arms-1', 'person-arms-2'), closed=False)
        self.add_contour('person-legs', *('person-legs-1', 'person-legs-2', 'person-legs-3'), closed=False)
        self.add_contour('stairs', *('stairs-1', 'stairs-2', 'stairs-3', 'stairs-4', 'stairs-5', 'stairs-6'), closed=False)
        self.relate('connect', *('person-body', 'person-arms'))
        self.relate('connect', *('person-body', 'person-legs'))
        self.relate('connect', *('stairs', 'person-legs'))
