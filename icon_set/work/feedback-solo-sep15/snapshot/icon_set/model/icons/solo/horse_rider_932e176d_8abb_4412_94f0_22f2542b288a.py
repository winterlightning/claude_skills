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
    category = 'objects/sports'
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
        """Horse rider: lower the saddle/back as one owner to open the arm-to-horse counter; give the torso and rider leg real length. Radius5 head(24,9), shoulder(19,21), exact13 center distance and4 painted clearance. The torso tangent follows the forward lean. Source horse rider and full_body_ref.png inspected. VRECT_L gives room for the horse legs."""
        self.ring('head', 24, 9, 5)
        self.add_bezier('torso', (19, 21), ((17, 26), (15, 29), (14, 32)))
        self.branches([('arms', [(19, 21), (26, 24), (34, 20)]), ('leg', [(14, 32), (22, 35), (20, 43)]), ('horse', [(14, 32), (28, 32), (34, 20), (38, 20), (40, 28), (34, 28), (31, 36), (38, 40), (37, 44)]), ('rear-leg', [(14, 32), (12, 38), (8, 44)]), ('tail', [(8, 35), (8, 33), (14, 32)])])
        for p in ['arms-0', 'leg-0', 'horse-0', 'rear-leg-0', 'tail-1']:
            self.relate('connect', 'torso', p)
