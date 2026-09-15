# Repair: Use one clearly visible profile ski with an upturned tip; fit the bent leg between ski and tow arm with full clearance.
"""Water skier: radius4 head (15,12), shoulder (15,24), exact4 gap. Lower the raised knee to open the trapped recess under the towing arm; retain both upturned ski curves.

Reconstruct water skier using its inspected source pose and full_body_ref.png. Head radius 4, center (15, 12), actual torso junction (15, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct water skier using its inspected source pose and full_body_ref.png. Head radius 4, center (15, 12), actual torso junction (15, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct water skier using its inspected source pose and full_body_ref.png. Head radius 4, center (15, 12), actual torso junction (15, 24): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Water Skier, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a0a86c5e-f6ab-4aef-80ad-0ea729f25840'
SOURCE_PATH = 'pictographic-primitives/sports/skating_a0a86c5e-f6ab-4aef-80ad-0ea729f25840.svg'
AUTHOR = 'gpt-6'

class WaterSkier(Solo48):
    icon_id = 'water-skier'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('water', 'skier', 'skiing', 'rider', 'glide', 'sport')

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

        path(self,'head',(11,12),('A',4,4,True,(19,12)),('A',4,4,True,(11,12)),closed=True)
        path(self,'torso',(15,24),('C',(15,27),(14,29),(14,32)))
        poly(self,'leg',(14,32),(22,32),(24,40))
        poly(self,'arms',(6,27),(15,24),(30,24),(44,21))
        path(self,'ski',(4,40),('L',(24,40)),('L',(36,40)),('A',8,8,False,(44,32)))
        contacts(self)
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
