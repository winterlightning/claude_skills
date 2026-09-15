# Repair: Give the surfer a real bent leg above a level board, with the breaking wave and water below.
"""Reconstruct surfer beside breaking wave using its inspected source pose and full_body_ref.png. Head radius 5, center (17, 11), actual torso junction (17, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct surfer beside breaking wave using its inspected source pose and full_body_ref.png. Head radius 5, center (17, 11), actual torso junction (17, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Surfer Beside Breaking Wave. Surfer balances on a sloping board beside a tall breaking wave; retain one bent leg and simplify the smaller waves to one joined baseline.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '47fb6410-137e-42d1-8a6e-b98ddf51c32e'
SOURCE_PATH = 'pictographic-primitives/recreation/surfing_47fb6410-137e-42d1-8a6e-b98ddf51c32e.svg'
AUTHOR = 'gpt-6'

class SurferBesideBreakingWave(Solo48):
    icon_id = 'surfer-beside-breaking-wave'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/recreation'
    aliases = ()
    keywords = ('surfer', 'beside', 'breaking', 'wave')

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

        path(self,'head',(13,10),('A',4,4,True,(21,10)),('A',4,4,True,(13,10)),closed=True)
        poly(self,'arms',(6,22),(17,22),(27,23))
        path(self,'torso',(17,22),('C',(17,25),(14,26),(13,28)))
        line(self,'leg',(13,28),(20,34))
        poly(self,'board',(6,34),(20,34),(29,34))
        path(self,'wave',(32,6),('A',8,14,True,(40,20)),('L',(40,34)),('A',2,8,False,(42,42)))
        line(self,'water',(6,42),(42,42))
        contacts(self)
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
