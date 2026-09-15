"""Reconstruct missing person pair using its inspected source pose and full_body_ref.png. Head radius 4, center (14, 12), actual torso junction (14, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Two front-facing human figures stand side by side with matching circular heads and simple bodies. The left figure has a continuous outline, while the right figure is traced with separated dashes.

Construction: Two standing people, one continuous and one broken into spaced segments. Bounds (4,8)-(44,40).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '58fce536-ad33-4c76-86df-d52bb405808c'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety missing people_58fce536-ad33-4c76-86df-d52bb405808c.svg'
AUTHOR = 'gpt-6'

class MissingPersonPairVariant2(Solo48):
    icon_id = 'missing-person-pair-v2'
    variant_of = 'missing-person-pair'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('missing', 'person', 'people', 'absence', 'outline', 'safety')

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
        """Reconstruct missing person pair using its inspected source pose and full_body_ref.png. Head radius 4, center (14, 12), actual torso junction (14, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('present-head', 14, 12, 4)
        self.ring('missing-head', 36, 12, 4)
        self.add_bezier('present-body-1', (14, 24), *(((14.0, 26.4), (14.0, 28.5), (14, 30)),))
        self.add_line('present-arms-1', (4, 28), (14, 24))
        self.add_line('present-arms-2', (14, 24), (22, 28))
        self.add_line('present-legs-1', (8, 40), (14, 30))
        self.add_line('present-legs-2', (14, 30), (20, 40))
        self.add_line('missing-body', (36, 24), (36, 27))
        self.add_line('missing-leg-left', (30, 36), (28, 40))
        self.add_line('missing-leg-right', (40, 36), (44, 40))
        self.add_contour('present-body', *('present-body-1',), closed=False)
        self.add_contour('present-arms', *('present-arms-1', 'present-arms-2'), closed=False)
        self.add_contour('present-legs', *('present-legs-1', 'present-legs-2'), closed=False)
        self.relate('connect', *('present-body', 'present-arms'))
        self.relate('connect', *('present-body', 'present-legs'))
