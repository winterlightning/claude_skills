# Repair: Use the vertical keyshape to fit torso, bent leg and exercise-bike base with eight-unit clearances.
"""Reconstruct stationary bike rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct stationary bike rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct stationary bike rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Stationary Bike Rider, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4c828b75-2ce2-5271-b9ae-3111238b215a'
SOURCE_PATH = 'pictographic-primitives/sports/sport gym cycling_4c828b75-2ce2-5271-b9ae-3111238b215a.svg'
AUTHOR = 'gpt-6'

class StationaryBikeRider(Solo48):
    icon_id = 'stationary-bike-rider'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('cycling', 'bike', 'stationary', 'fitness', 'exercise', 'rider')

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

        path(self,'head',(20,8),('A',4,4,True,(28,8)),('A',4,4,True,(20,8)),closed=True)
        path(self,'torso',(24,20),('C',(24,24),(19,26),(16,28)))
        poly(self,'leg',(16,28),(24,28),(20,36))
        poly(self,'arms',(24,20),(32,20),(36,16))
        line(self,'fork',(36,16),(32,36))
        path(self,'base',(12,36),('L',(20,36)),('L',(32,36)),('L',(36,36)),('A',4,4,True,(36,44)),('L',(12,44)),('A',4,4,True,(12,36)),closed=True)
        contacts(self)
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
