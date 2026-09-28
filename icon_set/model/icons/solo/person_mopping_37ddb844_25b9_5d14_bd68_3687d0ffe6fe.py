# Refinement: Move the rear foot clear of the full rounded mop head.
# Refinement: Place the rear foot clear of the mop head.
# Repair: Lift the free hand one unit clear of the bent knee.
"""Reconstruct person mopping using its inspected source pose and full_body_ref.png. Head radius 5, center (35, 11), actual torso junction (30, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct person mopping using its inspected source pose and full_body_ref.png. Head radius 5, center (35, 11), actual torso junction (30, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A person leans forward with staggered legs and both arms reaching toward a long diagonal mop handle. The handle ends in a wide rounded cleaning head resting at the lower-left.

Construction: Circular head, leaning stick figure and long mop handle. Limbs share shoulder and hip nodes; reduced filled clothing outline. Bounds (6,6)-(42,42).
Lucide: person-standing: circle head and shared limb junctions."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '37ddb844-25b9-5d14-bd68-3687d0ffe6fe'
SOURCE_PATH = 'pictographic-primitives/wayfinding/cleanser moping_37ddb844-25b9-5d14-bd68-3687d0ffe6fe.svg'
AUTHOR = 'gpt-6'

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
        """Reconstruct person mopping using its inspected source pose and full_body_ref.png. Head radius 5, center (35, 11), actual torso junction (30, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.add_arc('head-a', (30, 11), (40, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (40, 11), (30, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('body-1', (30, 23), *(((28.798423126783593, 25.88378449571938), (26.25, 27.5), (25, 29)),))
        self.add_line('body-2', (25, 29), (35, 36))
        self.add_line('body-3', (35, 36), (40, 42))
        self.add_line('rear-leg-1', (25, 29), (28, 42))
        self.add_line('arm-1', (30, 23), (23, 25))
        self.add_line('arm-2', (23, 25), (17, 25))
        self.add_line('mop-shaft', (17, 25), (10, 34))
        self.add_line('mop-head-0', (10, 34), (14, 34))
        self.add_arc('mop-head-1', (14, 34), (18, 38), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('mop-head-2', (18, 38), (18, 38))
        self.add_arc('mop-head-3', (18, 38), (14, 42), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('mop-head-4', (14, 42), (10, 42))
        self.add_arc('mop-head-5', (10, 42), (6, 38), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('mop-head-6', (6, 38), (6, 38))
        self.add_arc('mop-head-7', (6, 38), (10, 34), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('far-arm', (30, 23), (42, 28))
        self.add_line('foot', (40, 42), (42, 42))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('rear-leg', *('rear-leg-1',), closed=False)
        self.add_contour('arm', *('arm-1', 'arm-2'), closed=False)
        self.add_contour('mop-head', *('mop-head-0', 'mop-head-1', 'mop-head-2', 'mop-head-3', 'mop-head-4', 'mop-head-5', 'mop-head-6', 'mop-head-7'), closed=True)
        self.relate('connect', *('body', 'rear-leg'))
        self.relate('connect', *('body', 'arm'))
        self.relate('connect', *('arm', 'mop-shaft'))
        self.relate('connect', *('mop-shaft', 'mop-head'))
        self.relate('connect', *('body', 'far-arm'))
        self.relate('connect', *('body', 'foot'))
        self.add_contour('body', *('body-1',), closed=False)
        self.add_contour('body-section-1', *('body-2', 'body-3'), closed=False)
        self.relate('connect', 'body-1', 'body-2')
        self.relate('connect', 'body-2', 'body-3')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'body-1', 'body-2')
        self.relate('connect', 'body-1', 'rear-leg-1')
        self.relate('connect', 'body-1', 'arm-1')
        self.relate('connect', 'body-1', 'far-arm')
        self.relate('connect', 'body-2', 'body-3')
        self.relate('connect', 'body-2', 'rear-leg-1')
        self.relate('connect', 'body-3', 'foot')
        self.relate('connect', 'arm-1', 'arm-2')
        self.relate('connect', 'arm-1', 'far-arm')
        self.relate('connect', 'arm-2', 'mop-shaft')
        self.relate('connect', 'mop-shaft', 'mop-head-0')
        self.relate('connect', 'mop-shaft', 'mop-head-7')
        self.relate('connect', 'mop-head-0', 'mop-head-1')
        self.relate('connect', 'mop-head-0', 'mop-head-7')
        self.relate('connect', 'mop-head-1', 'mop-head-2')
        self.relate('connect', 'mop-head-1', 'mop-head-3')
        self.relate('connect', 'mop-head-2', 'mop-head-3')
        self.relate('connect', 'mop-head-3', 'mop-head-4')
        self.relate('connect', 'mop-head-4', 'mop-head-5')
        self.relate('connect', 'mop-head-5', 'mop-head-6')
        self.relate('connect', 'mop-head-5', 'mop-head-7')
        self.relate('connect', 'mop-head-6', 'mop-head-7')
        self.mark_human_figure('person', head='head', torso='body-1', torso_junction='start')
