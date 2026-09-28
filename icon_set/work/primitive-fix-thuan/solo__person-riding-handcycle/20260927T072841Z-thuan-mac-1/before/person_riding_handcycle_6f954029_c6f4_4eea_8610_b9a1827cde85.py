"""Handcycle rider: re-author both wheels at radius6, leaving a full curved torso and8 centerline units between the arm and frame. Radius4 head(18,10), shoulder(18,22), exact4 gap. Hands meet the crank; source handcycle and full_body_ref.png inspected.

Reconstruct person riding handcycle using its inspected source pose and full_body_ref.png. Head radius 4, center (16, 12), actual torso junction (16, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct person riding handcycle using its inspected source pose and full_body_ref.png. Head radius 4, center (16, 12), actual torso junction (16, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A seated rider faces right on a low cycle with two visible round wheels. Both hands reach toward a raised hand crank, and the bent legs extend toward the front wheel.

Construction: Seated rider between two wheels, arms extending toward a raised hand crank. Bounds (4,8)-(44,40).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6f954029-c6f4-4eea-8610-b9a1827cde85'
SOURCE_PATH = 'pictographic-primitives/wayfinding/handcycle_6f954029-c6f4-4eea-8610-b9a1827cde85.svg'
AUTHOR = 'gpt-6'

class PersonRidingHandcycle(Solo48):
    icon_id = 'person-riding-handcycle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('handcycle', 'rider', 'cycle', 'accessibility', 'mobility', 'sport')

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
        """Handcycle rider: re-author both wheels at radius6, leaving a full curved torso and8 centerline units between the arm and frame. Radius4 head(18,10), shoulder(18,22), exact4 gap. Hands meet the crank; source handcycle and full_body_ref.png inspected."""
        self.ring('head', 18, 10, 4)
        self.add_bezier('torso', (18, 22), ((18, 25), (19, 28), (20, 30)))
        for name, cx in [('rear', 12), ('front', 36)]:
            self.add_arc(name + '-tl', (cx - 6, 36), (cx, 30), radius_x=6)
            self.add_arc(name + '-tr', (cx, 30), (cx + 6, 36), radius_x=6)
            self.add_arc(name + '-b', (cx + 6, 36), (cx - 6, 36), radius_x=6)
            self.add_contour(name, name + '-tl', name + '-tr', name + '-b', closed=True)
        self.branches([('arms', [(18, 22), (28, 22), (32, 18)]), ('frame', [(12, 30), (20, 30), (28, 30), (36, 30)]), ('crank', [(32, 18), (36, 30)])])
        self.relate('connect', 'torso', 'arms-0')
        for p in ['frame-0', 'frame-1']:
            self.relate('connect', 'torso', p)
        self.relate('connect', 'rear', 'frame-0')
        self.relate('connect', 'front', 'frame-2')
        self.relate('connect', 'front', 'crank-0')
