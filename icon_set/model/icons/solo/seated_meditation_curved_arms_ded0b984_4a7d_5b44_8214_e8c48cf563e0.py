# Repair: Rest both hands directly on the crossed knees. Preserve the broad smooth shoulders and exact 8-unit head gap.
"""Meditating figure: radius5 head center(24,11), shoulder(24,24), exact4 painted gap. Preserve crossed legs and two separate curved resting arms; full_body_ref.png proportions.

Meditating figure: radius5 head center(24,11), shoulder(24,24), exact4 painted gap. Preserve crossed legs and two separate curved resting arms; full_body_ref.png proportions.

A figure sits upright with two crossed legs beneath a rounded torso. Both arms curve inward toward the abdomen, leaving a small central gap below the circular head.
Construction: Bounds (6,6)-(42,42). Mirrored arms curve inward over crossed legs; remove double limb contours and fingers.
Lucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ded0b984-4a7d-5b44-8214-e8c48cf563e0'
SOURCE_PATH = 'pictographic-primitives/sports/yoga meditate_ded0b984-4a7d-5b44-8214-e8c48cf563e0.svg'
AUTHOR = 'gpt-6'

class SeatedMeditationCurvedArms(Solo48):
    icon_id = 'seated-meditation-curved-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('seated', 'meditation', 'curved', 'arms', 'yoga', 'exercise')

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

        path(self,'head',(19,11),('A',5,5,True,(29,11)),('A',5,5,True,(19,11)),closed=True)
        path(self,'shoulders',(10,28),('C',(13,24),(19,24),(24,24)),('C',(29,24),(35,24),(38,28)))
        line(self,'arm-l',(10,28),(6,34))
        line(self,'arm-r',(38,28),(42,34))
        line(self,'torso',(24,24),(24,38))
        poly(self,'leg-l',(6,34),(24,38),(42,42))
        poly(self,'leg-r',(42,34),(24,38),(6,42))
        contacts(self)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
