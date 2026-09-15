"""Reconstruct snowboarder balancing using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct snowboarder balancing using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Snowboarder Balancing, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0a6543da-6660-4cf0-a837-4d651dbe574a'
SOURCE_PATH = 'pictographic-primitives/sports/skiing board slide_0a6543da-6660-4cf0-a837-4d651dbe574a.svg'
AUTHOR = 'gpt-6'

class SnowboarderBalancingVariant2(Solo48):
    icon_id = 'snowboarder-balancing-v2'
    variant_of = 'snowboarder-balancing'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
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
        """Reconstruct snowboarder balancing using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (24, 11), (34, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (34, 11), (24, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('arms-1', (6, 6), (11, 18))
        self.add_line('arms-2', (11, 18), (24, 23))
        self.add_line('arms-3', (24, 23), (40, 30))
        self.add_bezier('torso', (24, 23), *(((22.798423126783593, 25.88378449571938), (20.25, 27.5), (19, 29)),))
        self.add_line('leg-left-1', (19, 29), (12, 31))
        self.add_line('leg-left-2', (12, 31), (12, 36))
        self.add_line('leg-right-1', (19, 29), (30, 32))
        self.add_line('leg-right-2', (30, 32), (30, 40))
        self.add_line('board-1', (6, 32), (8, 35))
        self.add_line('board-2', (8, 35), (12, 36))
        self.add_line('board-3', (12, 36), (30, 40))
        self.add_line('board-4', (30, 40), (38, 42))
        self.add_line('board-5', (38, 42), (42, 37))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('arms', *('arms-1', 'arms-2', 'arms-3'), closed=False)
        self.add_contour('leg-left', *('leg-left-1', 'leg-left-2'), closed=False)
        self.add_contour('leg-right', *('leg-right-1', 'leg-right-2'), closed=False)
        self.add_contour('board', *('board-1', 'board-2', 'board-3', 'board-4', 'board-5'), closed=False)
        self.relate('connect', *('torso', 'arms'))
        self.relate('connect', *('torso', 'leg-left'))
        self.relate('connect', *('torso', 'leg-right'))
        self.relate('connect', *('leg-left', 'leg-right'))
        self.relate('connect', *('board', 'leg-left'))
        self.relate('connect', *('board', 'leg-right'))
