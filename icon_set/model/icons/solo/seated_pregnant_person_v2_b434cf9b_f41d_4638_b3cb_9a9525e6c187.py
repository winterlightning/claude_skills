"""Reconstruct seated pregnant person using its inspected source pose and full_body_ref.png. Head radius 4, center (18, 8), actual torso junction (18, 20): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A pregnant person sits facing right on a curved-backed seat. The rounded belly projects prominently above the bent thighs, while the lower leg drops in front of the seat.

Construction: Seated profile with rounded abdomen and a simple chair back. Bounds (8,4)-(40,44).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b434cf9b-f41d-4638-b3cb-9a9525e6c187'
SOURCE_PATH = 'pictographic-primitives/wayfinding/disability sit pregnancy_b434cf9b-f41d-4638-b3cb-9a9525e6c187.svg'
AUTHOR = 'gpt-6'

class SeatedPregnantPersonVariant2(Solo48):
    icon_id = 'seated-pregnant-person-v2'
    variant_of = 'seated-pregnant-person'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('pregnant', 'seated', 'pregnancy', 'maternity', 'chair', 'person')

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
        """Reconstruct seated pregnant person using its inspected source pose and full_body_ref.png. Head radius 4, center (18, 8), actual torso junction (18, 20): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('head', 18, 8, 4)
        self.add_bezier('back-and-leg-1', (18, 20), *(((18.0, 23.36), (19.5, 29.0), (20, 32)),))
        self.add_line('back-and-leg-2', (20, 32), (32, 32))
        self.add_line('back-and-leg-3', (32, 32), (36, 44))
        self.add_arc('belly', (18, 20), (40, 34), radius_x=22, radius_y=15, large_arc=False, sweep=True)
        self.add_line('front-leg', (40, 34), (40, 44))
        self.add_line('chair-1', (8, 23), (8, 42))
        self.add_line('chair-2', (8, 42), (22, 42))
        self.add_contour('back-and-leg', *('back-and-leg-1', 'back-and-leg-2', 'back-and-leg-3'), closed=False)
        self.add_contour('abdomen', *('belly', 'front-leg'), closed=False)
        self.add_contour('chair', *('chair-1', 'chair-2'), closed=False)
        self.relate('connect', *('back-and-leg', 'abdomen'))
