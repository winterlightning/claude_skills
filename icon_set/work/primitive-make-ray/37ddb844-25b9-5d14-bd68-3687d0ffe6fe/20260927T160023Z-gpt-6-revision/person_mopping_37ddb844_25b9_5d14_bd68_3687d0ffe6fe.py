# Refinement: Move the rear foot clear of the full rounded mop head.
# Refinement: Place the rear foot clear of the mop head.
# Repair: Lift the free hand one unit clear of the bent knee.
"""Reconstruct person mopping using its inspected source pose and full_body_ref.png. Head radius 5, center (35, 11), actual torso junction (30, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct person mopping using its inspected source pose and full_body_ref.png. Head radius 5, center (35, 11), actual torso junction (30, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A person leans forward with staggered legs and both arms reaching toward a long diagonal mop handle. The handle ends in a wide rounded cleaning head resting at the lower-left.

Construction: Circular head, leaning stick figure and long mop handle. Limbs share shoulder and hip nodes; reduced filled clothing outline. Bounds (6,6)-(42,42).
Lucide: person-standing: circle head and shared limb junctions."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '37ddb844-25b9-5d14-bd68-3687d0ffe6fe'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-mopping/20260927T153747Z-thuan-mac-1/reference/cleanser moping_37ddb844-25b9-5d14-bd68-3687d0ffe6fe.svg'
AUTHOR = "gpt-6"

class PersonMopping(Solo48):
    icon_id = 'person-mopping'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('person', 'mop', 'mopping', 'cleaning', 'floor', 'housework')

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
        # A flat floor mop on a slanting handle, carried by a walking figure.
        self.add_arc('head-top', (30, 11), (40, 11), radius_x=5)
        self.add_arc('head-bottom', (40, 11), (30, 11), radius_x=5)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_bezier('torso', (30, 23), ((29, 26), (27, 28), (25, 29)))
        self.add_polyline('front-leg', (25, 29), (35, 36), (40, 42))
        self.add_line('rear-leg', (25, 29), (28, 42))
        self.add_polyline('arm', (30, 23), (23, 25), (17, 25))
        self.add_line('far-arm', (30, 23), (42, 28))
        self.add_line('shaft', (17, 25), (12, 40))
        self.add_line('mop-left', (6, 40), (12, 40))
        self.add_line('mop-right', (12, 40), (18, 40))
        for a,b in (('torso','front-leg'),('torso','rear-leg'),('torso','arm'),('torso','far-arm'),('arm','shaft'),('shaft','mop-left'),('shaft','mop-right'),('mop-left','mop-right')):
            self.relate('connect',a,b)
        self.mark_human_figure('cleaner',head='head',torso='torso',torso_junction='start')
