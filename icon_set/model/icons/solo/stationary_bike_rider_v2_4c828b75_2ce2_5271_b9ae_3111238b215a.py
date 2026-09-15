"""Reconstruct stationary bike rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct stationary bike rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Stationary Bike Rider, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4c828b75-2ce2-5271-b9ae-3111238b215a'
SOURCE_PATH = 'pictographic-primitives/sports/sport gym cycling_4c828b75-2ce2-5271-b9ae-3111238b215a.svg'
AUTHOR = 'gpt-6'

class StationaryBikeRiderVariant2(Solo48):
    icon_id = 'stationary-bike-rider-v2'
    variant_of = 'stationary-bike-rider'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('cycling', 'bike', 'stationary', 'fitness', 'exercise', 'rider')

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
        """Reconstruct stationary bike rider using its inspected source pose and full_body_ref.png. Head radius 5, center (24, 11), actual torso junction (19, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (19, 11), (29, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (29, 11), (19, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('rider-1', (19, 23), *(((17.759652654107917, 25.976833630141), (13.75, 26.0), (12, 27)),))
        self.add_line('rider-2', (12, 27), (24, 30))
        self.add_line('rider-3', (24, 30), (20, 34))
        self.add_line('arms-1', (19, 23), (26, 26))
        self.add_line('arms-2', (26, 26), (38, 22))
        self.add_line('fork', (38, 22), (34, 34))
        self.add_line('top-1', (10, 34), (20, 34))
        self.add_line('top-2', (20, 34), (34, 34))
        self.add_line('top-3', (34, 34), (38, 34))
        self.add_arc('right', (38, 34), (38, 42), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('bottom', (38, 42), (10, 42))
        self.add_arc('left', (10, 42), (10, 34), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('rider', *('rider-1', 'rider-2', 'rider-3'), closed=False)
        self.add_contour('arms', *('arms-1', 'arms-2'), closed=False)
        self.add_contour('base', *('top-1', 'top-2', 'top-3', 'right', 'bottom', 'left'), closed=True)
        self.relate('connect', *('rider', 'arms'))
        self.relate('connect', *('arms', 'fork'))
        self.relate('connect', *('fork', 'base'))
        self.relate('connect', *('rider', 'base'))
