# Repair: Rebalance the crouched stance and board together; keep the balancing arms clear of both bent legs.
"""Reconstruct snowboarder balancing using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct snowboarder balancing using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Snowboarder Balancing, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0a6543da-6660-4cf0-a837-4d651dbe574a'
SOURCE_PATH = 'pictographic-primitives/sports/skiing board slide_0a6543da-6660-4cf0-a837-4d651dbe574a.svg'
AUTHOR = 'gpt-6'

class SnowboarderBalancing(Solo48):
    icon_id = 'snowboarder-balancing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('snowboard', 'rider', 'snow', 'winter', 'balance', 'sport')

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

        path(self,'head',(24,11),('A',5,5,True,(34,11)),('A',5,5,True,(24,11)),closed=True)
        poly(self,'arms',(6,6),(11,18),(24,23),(24,24),(40,24))
        path(self,'torso',(24,23),('C',(22.6,26.36),(19,30),(18,32)))
        line(self,'left-leg',(18,32),(12,40))
        poly(self,'right-leg',(18,32),(30,33),(30,42))
        poly(self,'board',(6,36),(8,39),(12,40),(30,42),(38,42),(42,37))
        contacts(self)
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
