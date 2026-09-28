# Repair: Use the vertical keyshape to fit torso, bent leg and exercise-bike base with eight-unit clearances.
"""Reconstruct stationary bike rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct stationary bike rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct stationary bike rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Stationary Bike Rider, independently authored on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4c828b75-2ce2-5271-b9ae-3111238b215a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__stationary-bike-rider/20260927T094403Z-thuan-mac-1/reference/sport gym cycling_4c828b75-2ce2-5271-b9ae-3111238b215a.svg'
AUTHOR = 'gpt-6'

class StationaryBikeRider(Solo48):
    icon_id = 'stationary-bike-rider'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
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
        from icon_set.model.icons.solo._symmetry_curves import path, ellipse, line, poly, contacts

        path(self,'head',(20,8),('A',4,4,True,(28,8)),('A',4,4,True,(20,8)),closed=True)
        path(self,'torso',(24,20),('C',(24,24),(19,26),(16,28)))
        line(self,'leg',(16,28),(24,32))
        poly(self,'arms',(24,20),(32,20),(40,16))
        line(self,'fork',(40,16),(32,40))
        path(self,'wheel',(8,40),('A',4,4,True,(16,40)),('A',4,4,True,(8,40)),closed=True)
        line(self,'base',(16,40),(40,40))
        contacts(self)
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
