"""Reconstruct person leaning over toilet using its inspected source pose and full_body_ref.png. Head radius 5, center (21, 13), actual torso junction (16, 25): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct person leaning over toilet using its inspected source pose and full_body_ref.png. Head radius 5, center (21, 13), actual torso junction (16, 25): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct person leaning over toilet using its inspected source pose and full_body_ref.png. Head radius 5, center (21, 13), actual torso junction (16, 25): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A person kneels facing right and bends over an open toilet bowl. Both arms reach onto the rim, while the head hangs over the bowl beside its tall rear tank.

Construction: Person bends toward a toilet bowl, one hand touching the rim. Bounds (4,8)-(44,40).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a2a8bbde-27d6-42cd-96b8-9da81e48b075'
SOURCE_PATH = 'pictographic-primitives/wayfinding/vomit toilet_a2a8bbde-27d6-42cd-96b8-9da81e48b075.svg'
AUTHOR = 'gpt-6'

class PersonLeaningOverToiletVariant2(Solo48):
    icon_id = 'person-leaning-over-toilet-v2'
    variant_of = 'person-leaning-over-toilet'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('person', 'toilet', 'vomiting', 'kneeling', 'bathroom', 'illness')

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
        """Reconstruct person leaning over toilet using its inspected source pose and full_body_ref.png. Head radius 5, center (21, 13), actual torso junction (16, 25): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('person-head-a', (16, 13), (26, 13), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('person-head-b', (26, 13), (16, 13), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('person-back-1', (16, 25), *(((14.890599607549541, 27.6625609418811), (11.5, 28.0), (10, 29)),))
        self.add_line('person-back-2', (10, 29), (16, 40))
        self.add_line('person-back-3', (16, 40), (4, 40))
        self.add_line('person-arm-1', (16, 25), (23, 28))
        self.add_line('person-arm-2', (23, 28), (30, 28))
        self.add_line('toilet-1', (30, 28), (34, 28))
        self.add_line('toilet-2', (34, 28), (34, 18))
        self.add_line('toilet-3', (34, 18), (44, 18))
        self.add_line('toilet-4', (44, 18), (44, 40))
        self.add_arc('bowl', (30, 28), (38, 36), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('person-head', *('person-head-a', 'person-head-b'), closed=True)
        self.add_contour('person-arm', *('person-arm-1', 'person-arm-2'), closed=False)
        self.add_contour('toilet', *('toilet-1', 'toilet-2', 'toilet-3', 'toilet-4'), closed=False)
        self.relate('connect', *('person-back', 'person-arm'))
        self.relate('connect', *('bowl', 'toilet'))
        self.relate('connect', *('person-arm', 'toilet'))
        self.add_contour('person-back', *('person-back-1',), closed=False)
        self.add_contour('person-back-section-1', *('person-back-2', 'person-back-3'), closed=False)
        self.relate('connect', 'person-back-1', 'person-back-2')
        self.relate('connect', 'person-back-2', 'person-back-3')
        self.relate('connect', 'person-head-a', 'person-head-b')
        self.relate('connect', 'person-back-1', 'person-back-2')
        self.relate('connect', 'person-back-1', 'person-arm-1')
        self.relate('connect', 'person-back-2', 'person-back-3')
        self.relate('connect', 'person-arm-1', 'person-arm-2')
        self.relate('connect', 'person-arm-2', 'toilet-1')
        self.relate('connect', 'person-arm-2', 'bowl')
        self.relate('connect', 'toilet-1', 'toilet-2')
        self.relate('connect', 'toilet-1', 'bowl')
        self.relate('connect', 'toilet-2', 'toilet-3')
        self.relate('connect', 'toilet-3', 'toilet-4')
