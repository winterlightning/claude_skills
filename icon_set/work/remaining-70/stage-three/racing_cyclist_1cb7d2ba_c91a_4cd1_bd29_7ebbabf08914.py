# Repair: Lengthen the racing back and thigh, retain both wheels and connect the hands to the actual fork. Exact 13-5=8 head gap.
"""Reconstruct racing cyclist using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct racing cyclist using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct racing cyclist using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Racing cyclist, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1cb7d2ba-c91a-4cd1-bd29-7ebbabf08914'
SOURCE_PATH = 'pictographic-primitives/sports/race_1cb7d2ba-c91a-4cd1-bd29-7ebbabf08914.svg'
AUTHOR = 'gpt-6'

class RacingCyclist(Solo48):
    icon_id = 'racing-cyclist'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('racing', 'cyclist')

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

        path(self,'head',(25,11),('A',5,5,True,(35,11)),('A',5,5,True,(25,11)),closed=True)
        ellipse(self,'rear-wheel',12,36,6)
        ellipse(self,'front-wheel',36,36,6)
        path(self,'torso',(25,23),('C',(24,25.4),(18,23),(13,24)))
        poly(self,'leg',(13,24),(22,33),(20,38))
        poly(self,'arms',(25,23),(32,27),(37,24))
        line(self,'fork',(37,24),(36,36))
        line(self,'frame',(12,36),(13,24))
        contacts(self)
        self.relate('connect','fork','front-wheel')
        self.relate('connect','frame','rear-wheel')
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
