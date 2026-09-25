# Repair: Lift the rear hand clear of the rear thigh during the tripping action.
"""Reconstruct person tripping over rock using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A person pitches forward toward the right with one arm extended and the rear leg stretched behind. A small angular rock sits just ahead of the lowered front foot.

Construction: Runner pitching forward toward a small triangular obstacle. Bounds (6,6)-(42,42).
Lucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '33343e0b-3052-52e7-b5fb-b5849fef9eaf'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety rocky road_33343e0b-3052-52e7-b5fb-b5849fef9eaf.svg'
AUTHOR = 'gpt-6'

class PersonTrippingOverRock(Solo48):
    icon_id = 'person-tripping-over-rock'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('tripping', 'person', 'rock', 'hazard', 'fall', 'safety')

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
        """Reconstruct person tripping over rock using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('person-head', 29, 11, 5)
        self.add_bezier('person-torso-1', (24, 23), *(((22.6, 26.36), (19.5, 28.25), (18, 30)),))
        self.add_line('person-arms-1', (10, 23), (18, 21))
        self.add_line('person-arms-2', (18, 21), (24, 23))
        self.add_line('person-arms-3', (24, 23), (34, 29))
        self.add_line('person-legs-1', (6, 37), (18, 30))
        self.add_line('person-legs-2', (18, 30), (24, 35))
        self.add_line('person-legs-3', (24, 35), (20, 42))
        self.add_line('rock-1', (34, 42), (38, 37))
        self.add_line('rock-2', (38, 37), (42, 42))
        self.add_contour('person-torso', *('person-torso-1',), closed=False)
        self.add_contour('person-arms', *('person-arms-1', 'person-arms-2', 'person-arms-3'), closed=False)
        self.add_contour('person-legs', *('person-legs-1', 'person-legs-2', 'person-legs-3'), closed=False)
        self.add_contour('rock', *('rock-1', 'rock-2'), closed=False)
        self.relate('connect', *('person-torso', 'person-arms'))
        self.relate('connect', *('person-torso', 'person-legs'))
        self.mark_human_figure('person', head='person-head', torso='person-torso-1', torso_junction='start')
