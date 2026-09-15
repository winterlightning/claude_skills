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

class SurferBesideBreakingWaveVariant2(Solo48):
    icon_id = 'surfer-beside-breaking-wave-v2'
    variant_of = 'surfer-beside-breaking-wave'
    variant_label = 'Visual reconstruction after full 500-icon audit'
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
        """Reconstruct surfer beside breaking wave using its inspected source pose and full_body_ref.png. Head radius 5, center (17, 11), actual torso junction (17, 24): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.add_arc('head-a', (12, 11), (22, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (22, 11), (12, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('arms-1', (6, 24), (17, 24))
        self.add_line('arms-2', (17, 24), (27, 25))
        self.add_bezier('body-1', (17, 24), *(((17.0, 26.0), (14.0, 26.25), (13, 27)),))
        self.add_line('body-2', (13, 27), (20, 31))
        self.add_line('board-1', (6, 29), (20, 31))
        self.add_line('board-2', (20, 31), (29, 33))
        self.add_arc('wave-crest', (32, 6), (40, 20), radius_x=8, radius_y=14, large_arc=False, sweep=True)
        self.add_line('wave-wall', (40, 20), (40, 34))
        self.add_arc('wave-foot', (40, 34), (42, 42), radius_x=2, radius_y=8, large_arc=False, sweep=False)
        self.add_line('water', (6, 42), (42, 42))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('arms', *('arms-1', 'arms-2'), closed=False)
        self.add_contour('board', *('board-1', 'board-2'), closed=False)
        self.add_contour('breaking-wave', *('wave-crest', 'wave-wall', 'wave-foot'), closed=False)
        self.relate('connect', *('arms', 'body'))
        self.relate('connect', *('board', 'body'))
        self.relate('connect', *('water', 'breaking-wave'))
        self.add_contour('body', *('body-1',), closed=False)
        self.add_contour('body-section-1', *('body-2',), closed=False)
        self.relate('connect', 'body-1', 'body-2')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'arms-1', 'arms-2')
        self.relate('connect', 'arms-1', 'body-1')
        self.relate('connect', 'arms-2', 'body-1')
        self.relate('connect', 'body-1', 'body-2')
        self.relate('connect', 'body-2', 'board-1')
        self.relate('connect', 'body-2', 'board-2')
        self.relate('connect', 'board-1', 'board-2')
        self.relate('connect', 'wave-crest', 'wave-wall')
        self.relate('connect', 'wave-wall', 'wave-foot')
        self.relate('connect', 'wave-foot', 'water')
