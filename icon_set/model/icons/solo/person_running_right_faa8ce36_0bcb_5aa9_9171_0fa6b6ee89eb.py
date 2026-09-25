"""Reconstruct person running right using its inspected source pose and full_body_ref.png. Head radius 5, center (33, 11), actual torso junction (28, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A person runs toward the right with a forward-leaning torso and a circular head. One arm reaches ahead, the other bends behind, and the rear leg stretches diagonally backward.

Construction: Runner leaning right with bent arms and a long trailing leg. Bounds (6,6)-(42,42).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'faa8ce36-0bcb-5aa9-9171-0fa6b6ee89eb'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety exit right_faa8ce36-0bcb-5aa9-9171-0fa6b6ee89eb.svg'
AUTHOR = 'gpt-6'

class PersonRunningRight(Solo48):
    icon_id = 'person-running-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('person', 'running', 'right', 'escape', 'motion', 'wayfinding')

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
        """Reconstruct person running right using its inspected source pose and full_body_ref.png. Head radius 5, center (33, 11), actual torso junction (28, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('person-head', 33, 11, 5)
        self.add_bezier('person-torso-1', (28, 23), *(((26.69457209627099, 26.133026968949626), (23.5, 27.5), (22, 29)),))
        self.add_line('person-arms-1', (12, 25), (18, 19))
        self.add_line('person-arms-2', (18, 19), (28, 23))
        self.add_line('person-arms-3', (28, 23), (32, 29))
        self.add_line('person-arms-4', (32, 29), (42, 29))
        self.add_line('person-legs-1', (6, 42), (22, 29))
        self.add_line('person-legs-2', (22, 29), (30, 36))
        self.add_line('person-legs-3', (30, 36), (26, 42))
        self.add_contour('person-torso', *('person-torso-1',), closed=False)
        self.add_contour('person-arms', *('person-arms-1', 'person-arms-2', 'person-arms-3', 'person-arms-4'), closed=False)
        self.add_contour('person-legs', *('person-legs-1', 'person-legs-2', 'person-legs-3'), closed=False)
        self.relate('connect', *('person-torso', 'person-arms'))
        self.relate('connect', *('person-torso', 'person-legs'))
