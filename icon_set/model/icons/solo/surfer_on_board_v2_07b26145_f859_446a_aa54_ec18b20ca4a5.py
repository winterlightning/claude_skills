"""Reconstruct surfer on board using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 13), actual torso junction (25, 25): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

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

class SurferOnBoardVariant2(Solo48):
    icon_id = 'surfer-on-board-v2'
    variant_of = 'surfer-on-board'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/recreation'
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
        """Reconstruct surfer on board using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 13), actual torso junction (25, 25): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (25, 13), (35, 13), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (35, 13), (25, 13), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('arms-1', (10, 14), (15, 21))
        self.add_line('arms-2', (15, 21), (25, 25))
        self.add_line('arms-3', (25, 25), (38, 31))
        self.add_bezier('body-1', (25, 25), *(((24.01490396347187, 27.364230487667513), (21.25, 28.0), (20, 29)),))
        self.add_line('body-2', (20, 29), (28, 34))
        self.add_line('body-3', (28, 34), (27, 38))
        self.add_line('rear-leg-1', (20, 29), (14, 34))
        self.add_line('rear-leg-2', (14, 34), (10, 36))
        self.add_arc('board-tip', (4, 29), (10, 36), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_line('board-1', (10, 36), (27, 38))
        self.add_line('board-2', (27, 38), (44, 40))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('arms', *('arms-1', 'arms-2', 'arms-3'), closed=False)
        self.add_contour('body', *('body-1', 'body-2', 'body-3'), closed=False)
        self.add_contour('rear-leg', *('rear-leg-1', 'rear-leg-2'), closed=False)
        self.add_contour('surfboard', *('board-tip', 'board-1', 'board-2'), closed=False)
        self.relate('connect', *('arms', 'body'))
        self.relate('connect', *('rear-leg', 'body'))
        self.relate('connect', *('surfboard', 'rear-leg'))
        self.relate('connect', *('surfboard', 'body'))
