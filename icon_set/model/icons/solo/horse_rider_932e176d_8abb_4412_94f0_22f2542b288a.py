# Repair: Reconstruct the horse neck and saddle together; preserve circular rider head, reins and distinct horse/rider legs. Human reference full_body_ref.png; head gap 12-4=8.
"""Horse rider: lower the saddle/back as one owner to open the arm-to-horse counter; give the torso and rider leg real length. Radius5 head(24,9), shoulder(19,21), exact13 center distance and4 painted clearance. The torso tangent follows the forward lean. Source horse rider and full_body_ref.png inspected. VRECT_L gives room for the horse legs.

Reconstruct horse rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct horse rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct horse rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Horse Rider, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '932e176d-8abb-4412-94f0-22f2542b288a'
SOURCE_PATH = 'pictographic-primitives/sports/sport horse riding_932e176d-8abb-4412-94f0-22f2542b288a.svg'
AUTHOR = 'gpt-6'

class HorseRider(Solo48):
    icon_id = 'horse-rider'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('horse', 'rider', 'equestrian', 'helmet', 'animal', 'sport')

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

        path(self,'head',(12,8),('A',4,4,True,(20,8)),('A',4,4,True,(12,8)),closed=True)
        path(self,'torso',(16,20),('C',(16,24),(16,28),(16,30)))
        poly(self,'arm',(16,20),(24,20),(26,18))
        path(self,'horse',(8,44),('L',(8,38)),('L',(8,30)),('L',(16,30)),('L',(24,30)),('L',(26,18)),('L',(28,10)),('L',(40,18)),('L',(40,26)),('L',(36,26)),('L',(36,38)),('L',(40,40)),('L',(38,44)))
        poly(self,'belly',(8,38),(16,38),(36,38))
        poly(self,'rider-leg',(16,30),(16,38),(16,40))
        line(self,'tail',(8,30),(8,22))
        contacts(self)
        self.mark_human_figure('rider',head='head',torso='torso-1',torso_junction='start')
