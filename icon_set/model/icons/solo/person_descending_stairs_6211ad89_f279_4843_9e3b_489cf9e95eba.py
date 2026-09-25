"""Reconstruct person descending stairs using its inspected source pose and full_body_ref.png. Head radius 4, center (18, 10), actual torso junction (18, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A person stands across two levels of a short staircase with the front leg reaching toward the lower left. The arms bend beside a nearly upright torso and circular head.

Construction: Walking figure with one foot on a three-step staircase. Distinct knee and arm positions indicate the direction of travel. Bounds (6,6)-(42,42).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6211ad89-f279-4843-9e3b-489cf9e95eba'
SOURCE_PATH = 'pictographic-primitives/wayfinding/stairs person decend_6211ad89-f279-4843-9e3b-489cf9e95eba.svg'
AUTHOR = 'gpt-6'

class PersonDescendingStairs(Solo48):
    icon_id = 'person-descending-stairs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('person', 'stairs', 'descending', 'steps', 'walking', 'wayfinding')

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
        """Reconstruct person descending stairs using its inspected source pose and full_body_ref.png. Head radius 4, center (18, 10), actual torso junction (18, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('person-head', 18, 10, 4)
        self.add_bezier('person-body-1', (18, 22), *(((18.0, 24.0), (21.0, 24.25), (22, 25)),))
        self.add_line('person-arms-1', (6, 25), (18, 22))
        self.add_line('person-arms-2', (18, 22), (28, 26))
        self.add_line('person-legs-1', (12, 40), (22, 25))
        self.add_line('person-legs-2', (22, 25), (30, 36))
        self.add_line('stairs-1', (20, 42), (20, 36))
        self.add_line('stairs-2', (20, 36), (30, 36))
        self.add_line('stairs-3', (30, 36), (30, 30))
        self.add_line('stairs-4', (30, 30), (36, 30))
        self.add_line('stairs-5', (36, 30), (36, 24))
        self.add_line('stairs-6', (36, 24), (42, 24))
        self.add_contour('person-body', *('person-body-1',), closed=False)
        self.add_contour('person-arms', *('person-arms-1', 'person-arms-2'), closed=False)
        self.add_contour('person-legs', *('person-legs-1', 'person-legs-2'), closed=False)
        self.add_contour('stairs', *('stairs-1', 'stairs-2', 'stairs-3', 'stairs-4', 'stairs-5', 'stairs-6'), closed=False)
        self.relate('connect', *('person-body', 'person-arms'))
        self.relate('connect', *('person-body', 'person-legs'))
        self.relate('connect', *('stairs', 'person-legs'))
