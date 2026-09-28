# Refinement: Level the upper arm below the head instead of letting it encroach on the exact neck gap.
# Repair: Rebalance the surfer head and torso above a broad two-foot stance; preserve the upturned board and both arms. Head gap 11-3=8.
"""Reconstruct surfer on board using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 13), actual torso junction (25, 25): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct surfer on board using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 13), actual torso junction (25, 25): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct surfer on board using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 13), actual torso junction (25, 25): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Surfer on Board. Crouching surfer extends arms for balance on a right-sloping board; retain upward-curling left tip.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '07b26145-f859-446a-aa54-ec18b20ca4a5'
SOURCE_PATH = 'pictographic-primitives/recreation/nautic sports surfing water_07b26145-f859-446a-aa54-ec18b20ca4a5.svg'
AUTHOR = 'gpt-6'

class SurferOnBoard(Solo48):
    icon_id = 'surfer-on-board'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'recreation'
    categories = ('primitives', 'recreation')
    aliases = ()
    keywords = ('surfer', 'on', 'board')

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

        path(self,'head',(22,11),('A',3,3,True,(28,11)),('A',3,3,True,(22,11)),closed=True)
        poly(self,'arms',(10,12),(15,22),(25,22),(38,24))
        path(self,'torso',(25,22),('C',(25,25),(20,28),(18,30)))
        line(self,'front-leg',(18,30),(27,38))
        line(self,'rear-leg',(18,30),(10,36))
        path(self,'board',(4,29),('A',9,9,True,(10,36)),('L',(27,38)),('L',(44,40)))
        contacts(self)
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
