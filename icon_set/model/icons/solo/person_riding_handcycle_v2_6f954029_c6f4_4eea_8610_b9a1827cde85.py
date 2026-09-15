"""Reconstruct person riding handcycle using its inspected source pose and full_body_ref.png. Head radius 4, center (16, 12), actual torso junction (16, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A seated rider faces right on a low cycle with two visible round wheels. Both hands reach toward a raised hand crank, and the bent legs extend toward the front wheel.

Construction: Seated rider between two wheels, arms extending toward a raised hand crank. Bounds (4,8)-(44,40).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6f954029-c6f4-4eea-8610-b9a1827cde85'
SOURCE_PATH = 'pictographic-primitives/wayfinding/handcycle_6f954029-c6f4-4eea-8610-b9a1827cde85.svg'
AUTHOR = 'gpt-6'

class PersonRidingHandcycleVariant2(Solo48):
    icon_id = 'person-riding-handcycle-v2'
    variant_of = 'person-riding-handcycle'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
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
        """Reconstruct person riding handcycle using its inspected source pose and full_body_ref.png. Head radius 4, center (16, 12), actual torso junction (16, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('person-head', 16, 12, 4)
        self.add_arc('rear-wheel-top-joint-1', (4, 33), (11, 26), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('rear-wheel-top-joint-2', (11, 26), (18, 33), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('rear-wheel-bottom', (18, 33), (4, 33), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('front-wheel-top-joint-1', (30, 33), (37, 26), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('front-wheel-top-joint-2', (37, 26), (44, 33), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('front-wheel-bottom', (44, 33), (30, 33), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_bezier('person-body-1', (16, 24), *(((16.0, 25.131370849898477), (17.5, 25.5), (18, 26)),))
        self.add_line('person-body-2', (18, 26), (26, 26))
        self.add_line('person-arms-1', (16, 24), (26, 24))
        self.add_line('person-arms-2', (26, 24), (32, 18))
        self.add_line('frame-1', (11, 26), (18, 26))
        self.add_line('frame-2', (18, 26), (26, 26))
        self.add_line('frame-3', (26, 26), (37, 26))
        self.add_line('crank', (32, 18), (37, 26))
        self.add_contour('rear-wheel', *('rear-wheel-top-joint-1', 'rear-wheel-top-joint-2', 'rear-wheel-bottom'), closed=True)
        self.add_contour('front-wheel', *('front-wheel-top-joint-1', 'front-wheel-top-joint-2', 'front-wheel-bottom'), closed=True)
        self.add_contour('person-body', *('person-body-1', 'person-body-2'), closed=False)
        self.add_contour('person-arms', *('person-arms-1', 'person-arms-2'), closed=False)
        self.add_contour('frame', *('frame-1', 'frame-2', 'frame-3'), closed=False)
        self.relate('connect', *('person-body', 'person-arms'))
        self.relate('connect', *('frame', 'rear-wheel'))
        self.relate('connect', *('frame', 'front-wheel'))
        self.relate('connect', *('frame', 'person-body'))
        self.relate('connect', *('crank', 'person-arms'))
        self.relate('connect', *('crank', 'frame'))
