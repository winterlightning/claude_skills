"""Stair climber: radius4 head (18,10), shoulder (18,22), exact4 gap. Lift the leading hand above the raised knee to open the triangular recess; preserve the foot on the actual step.

Stair climber: radius4 head (18,10), shoulder (18,22), exact4 gap. Lift the leading hand above the raised knee to open the triangular recess; preserve the foot on the actual step.

Reconstruct person climbing stairs using its inspected source pose and full_body_ref.png. Head radius 5, center (23, 11), actual torso junction (18, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct person climbing stairs using its inspected source pose and full_body_ref.png. Head radius 5, center (23, 11), actual torso junction (18, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A person faces right and steps onto a short rising staircase. One knee lifts over a step while the rear leg remains lower, and the arms swing beside the torso.

Construction: Walking figure with one foot on a three-step staircase. Distinct knee and arm positions indicate the direction of travel. Bounds (6,6)-(42,42).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '317da08d-c0ee-4af0-b5d9-a57e3f5420c2'
SOURCE_PATH = 'pictographic-primitives/wayfinding/stairs person ascend_317da08d-c0ee-4af0-b5d9-a57e3f5420c2.svg'
AUTHOR = 'gpt-6'

class PersonClimbingStairs(Solo48):
    icon_id = 'person-climbing-stairs'
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
        """Stair climber: radius4 head (18,10), shoulder (18,22), exact4 gap. Lift the leading hand above the raised knee to open the triangular recess; preserve the foot on the actual step."""
        self.add_arc('person-head-a', (14, 10), (22, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('person-head-b', (22, 10), (14, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('person-body-1', (18, 22), *(((17.02699148917896, 25.335220425970498), (16.5, 27.5), (16, 29)),))
        self.add_line('person-arms-1', (6, 27), (18, 22))
        self.add_line('person-legs-1', (8, 42), (16, 29))
        self.add_line('person-legs-2', (16, 29), (26, 28))
        self.add_line('person-legs-3', (26, 28), (30, 30))
        self.add_line('stairs-1', (20, 42), (20, 36))
        self.add_line('stairs-2', (20, 36), (30, 36))
        self.add_line('stairs-3', (30, 36), (30, 30))
        self.add_line('stairs-4', (30, 30), (36, 30))
        self.add_line('stairs-5', (36, 30), (36, 24))
        self.add_line('stairs-6', (36, 24), (42, 24))
        self.add_line('forward-arm-0', (18, 22), (26, 22))
        self.add_line('forward-arm-1', (26, 22), (29, 18))
        self.add_contour('person-head', *('person-head-a', 'person-head-b'), closed=True)
        self.add_contour('person-body', *('person-body-1',), closed=False)
        self.add_contour('person-legs', *('person-legs-1', 'person-legs-2', 'person-legs-3'), closed=False)
        self.add_contour('stairs', *('stairs-1', 'stairs-2', 'stairs-3', 'stairs-4', 'stairs-5', 'stairs-6'), closed=False)
        self.add_contour('forward-arm', *('forward-arm-0', 'forward-arm-1'), closed=False)
        self.relate('connect', *('person-body', 'person-arms-1'))
        self.relate('connect', *('person-body', 'person-legs'))
        self.relate('connect', *('stairs', 'person-legs'))
        self.relate('connect', *('forward-arm-0', 'forward-arm-1'))
        self.relate('connect', *('forward-arm-0', 'person-body-1'))
        self.relate('connect', *('forward-arm-0', 'person-arms-1'))
