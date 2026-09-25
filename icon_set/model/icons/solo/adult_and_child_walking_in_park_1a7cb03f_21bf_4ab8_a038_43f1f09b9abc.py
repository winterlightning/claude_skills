"""Adult and child walking in a park: replace the tiny filled child head with an outlined circle and connect their hands intentionally. Adult radius4 head(8,12), shoulder(8,24); child radius3 head(28,20), shoulder(28,31): both exact4 ink gaps. A smaller background tree preserves the park setting. Original and full_body_ref.png inspected.

Reconstruct adult and child walking in park using its inspected source pose and full_body_ref.png. Head radius 4, center (12, 12), actual torso junction (12, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

An adult and a smaller child walk together with their hands meeting between them. A small tiered evergreen stands above the child, placing the pair within a park scene.

Construction: Adult and child walk beside a small tree; clothing details omitted. Bounds (4,8)-(44,40).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1a7cb03f-21bf-4ab8-a038-43f1f09b9abc'
SOURCE_PATH = 'pictographic-primitives/wayfinding/family walk park_1a7cb03f-21bf-4ab8-a038-43f1f09b9abc.svg'
AUTHOR = 'gpt-6'

class AdultAndChildWalkingInPark(Solo48):
    icon_id = 'adult-and-child-walking-in-park'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('adult', 'child', 'family', 'walking', 'park', 'tree')

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
        """Adult and child walking in a park: replace the tiny filled child head with an outlined circle and connect their hands intentionally. Adult radius4 head(8,12), shoulder(8,24); child radius3 head(28,20), shoulder(28,31): both exact4 ink gaps. A smaller background tree preserves the park setting. Original and full_body_ref.png inspected."""
        self.ring('adult-head', 8, 12, 4)
        self.ring('child-head', 28, 20, 3)
        self.add_arc('tree-top', (38, 12), (44, 12), radius_x=3)
        self.add_arc('tree-br', (44, 12), (41, 15), radius_x=3)
        self.add_arc('tree-bl', (41, 15), (38, 12), radius_x=3)
        self.add_contour('tree', 'tree-top', 'tree-br', 'tree-bl', closed=True)
        self.add_line('trunk', (41, 15), (41, 26))
        self.relate('connect', 'tree', 'trunk')
        self.branches([('adult-body', [(8, 24), (8, 32)]), ('adult-left-arm', [(8, 24), (4, 29)]), ('adult-right-arm', [(8, 24), (16, 28)]), ('adult-legs', [(4, 40), (8, 32), (16, 40)]), ('child-body', [(28, 31), (28, 35)]), ('child-left-arm', [(28, 31), (20, 31), (16, 28)]), ('child-right-arm', [(28, 31), (36, 33)]), ('child-legs', [(24, 40), (28, 35), (36, 40)])])
