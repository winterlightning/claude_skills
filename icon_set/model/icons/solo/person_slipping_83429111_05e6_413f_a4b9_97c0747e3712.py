# Refinement: Lengthen the falling body so the outstretched leg clears the upper arm.
# Refinement: Separate the falling legs and move the short ground mark beneath the body.
# Repair: Lift the outstretched leg to separate it from the lower leg.
"""Reconstruct person slipping using its inspected source pose and full_body_ref.png. Head radius 4, center (26, 10), actual torso junction (26, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A person falls backward above a short flat ground line, with both arms raised. The torso tilts diagonally and the bent legs lift leftward away from the floor.

Construction: Backward-tilted figure throws both arms upward and lifts the feet above a short ground mark. Bounds (6,6)-(42,42).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '83429111-05e6-413f-a4b9-97c0747e3712'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety slippery_83429111-05e6-413f-a4b9-97c0747e3712.svg'
AUTHOR = 'gpt-6'

class PersonSlipping(Solo48):
    icon_id = 'person-slipping'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('slipping', 'falling', 'person', 'floor', 'hazard', 'safety')

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
        """Reconstruct person slipping using its inspected source pose and full_body_ref.png. Head radius 4, center (26, 10), actual torso junction (26, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('person-head', 26, 10, 4)
        self.add_bezier('person-torso-1', (26, 22), *(((26.0, 25.36), (21.5, 26.5), (20, 31)),))
        self.add_line('person-arms-1', (12, 14), (17, 22))
        self.add_line('person-arms-2', (17, 22), (26, 22))
        self.add_line('person-arms-3', (26, 22), (42, 22))
        self.add_line('person-legs-1', (6, 28), (20, 31))
        self.add_line('person-legs-2', (20, 31), (14, 39))
        self.add_line('person-legs-3', (14, 39), (6, 36))
        self.add_line('ground', (24, 42), (32, 42))
        self.add_contour('person-torso', *('person-torso-1',), closed=False)
        self.add_contour('person-arms', *('person-arms-2', 'person-arms-3'), closed=False)
        self.add_contour('person-legs', *('person-legs-1', 'person-legs-2', 'person-legs-3'), closed=False)
        self.relate('connect', *('person-arms-1', 'person-arms'))
        self.relate('connect', *('person-torso', 'person-arms'))
        self.relate('connect', *('person-torso', 'person-legs'))
        self.mark_human_figure('person', head='person-head', torso='person-torso-1', torso_junction='start')
