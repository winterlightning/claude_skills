"""Reconstruct adult and child walking in park using its inspected source pose and full_body_ref.png. Head radius 4, center (12, 12), actual torso junction (12, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

An adult and a smaller child walk together with their hands meeting between them. A small tiered evergreen stands above the child, placing the pair within a park scene.

Construction: Adult and child walk beside a small tree; clothing details omitted. Bounds (4,8)-(44,40).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1a7cb03f-21bf-4ab8-a038-43f1f09b9abc'
SOURCE_PATH = 'pictographic-primitives/wayfinding/family walk park_1a7cb03f-21bf-4ab8-a038-43f1f09b9abc.svg'
AUTHOR = 'gpt-6'

class AdultAndChildWalkingInParkVariant2(Solo48):
    icon_id = 'adult-and-child-walking-in-park-v2'
    variant_of = 'adult-and-child-walking-in-park'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
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
        """Reconstruct adult and child walking in park using its inspected source pose and full_body_ref.png. Head radius 4, center (12, 12), actual torso junction (12, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('adult-head', 12, 12, 4)
        self.add_bezier('adult-body-1', (12, 24), *(((12.0, 26.4), (12.0, 28.5), (12, 30)),))
        self.add_line('adult-arms-1', (4, 28), (12, 24))
        self.add_line('adult-arms-2', (12, 24), (22, 28))
        self.add_line('adult-legs-1', (6, 40), (12, 30))
        self.add_line('adult-legs-2', (12, 30), (20, 40))
        self.add_line('child-head', (30, 26), (30, 26))
        self.add_line('child-body-1', (32, 35), (32, 37))
        self.add_line('child-body-2', (32, 37), (28, 40))
        self.add_line('child-leg-1', (32, 37), (38, 40))
        self.add_line('child-arms-1', (29, 35), (32, 35))
        self.add_line('child-arms-2', (32, 35), (38, 34))
        self.add_arc('tree-crown-top', (32, 14), (44, 14), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('tree-crown-bottom-joint-1', (44, 14), (38, 20), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('tree-crown-bottom-joint-2', (38, 20), (32, 14), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('tree-trunk', (38, 20), (38, 26))
        self.add_contour('adult-body', *('adult-body-1',), closed=False)
        self.add_contour('adult-arms', *('adult-arms-1', 'adult-arms-2'), closed=False)
        self.add_contour('adult-legs', *('adult-legs-1', 'adult-legs-2'), closed=False)
        self.add_contour('child-body', *('child-body-1', 'child-body-2'), closed=False)
        self.add_contour('child-leg', *('child-leg-1',), closed=False)
        self.add_contour('child-arms', *('child-arms-1', 'child-arms-2'), closed=False)
        self.add_contour('tree-crown', *('tree-crown-top', 'tree-crown-bottom-joint-1', 'tree-crown-bottom-joint-2'), closed=True)
        self.relate('connect', *('adult-body', 'adult-arms'))
        self.relate('connect', *('adult-body', 'adult-legs'))
        self.relate('connect', *('child-body', 'child-leg'))
        self.relate('connect', *('child-body', 'child-arms'))
        self.relate('connect', *('tree-crown', 'tree-trunk'))
