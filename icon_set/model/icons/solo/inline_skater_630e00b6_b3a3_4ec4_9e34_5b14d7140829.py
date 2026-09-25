# Refinement: Put the rear skate wheels below the angled pushing foot.
# Repair: Retain the pushing skating pose with a longer torso and one coherent planted leg; four skate wheels remain.
"""Inline skater: a curved leaning back, one pushing leg and one planted skate replace the parallel arm/thigh crowding. Radius4 head(29,10), shoulder(29,22), exact4 gap. Keep paired skate wheels and the source skating action.

Inline skater: a curved leaning back, one pushing leg and one planted skate replace the parallel arm/thigh crowding. Radius4 head(29,10), shoulder(29,22), exact4 gap. Keep paired skate wheels and the source skating action.

Reconstruct inline skater using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct inline skater using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct inline skater using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Inline skater, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '630e00b6-b3a3-4ec4-9e34-5b14d7140829'
SOURCE_PATH = 'pictographic-primitives/sports/rollerblades person_630e00b6-b3a3-4ec4-9e34-5b14d7140829.svg'
AUTHOR = 'gpt-6'

class InlineSkater(Solo48):
    icon_id = 'inline-skater'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('inline', 'skater')

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
        from ._symmetry_curves import path, ellipse, line, poly, contacts

        path(self,'head',(25,10),('A',4,4,True,(33,10)),('A',4,4,True,(25,10)),closed=True)
        path(self,'torso',(29,22),('C',(29,26),(24,28),(21,30)))
        poly(self,'left-arm',(29,22),(14,22),(10,18))
        poly(self,'right-arm',(29,22),(36,24),(42,24))
        line(self,'front-leg',(21,30),(28,34))
        poly(self,'back-leg',(21,30),(13,32),(6,26))
        poly(self,'skate',(25,34),(28,34),(33,34))
        for i,p in enumerate(((25,42),(33,42),(6,38),(14,40))):self.add_dot(f'wheel-{i}',p)
        contacts(self)
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
