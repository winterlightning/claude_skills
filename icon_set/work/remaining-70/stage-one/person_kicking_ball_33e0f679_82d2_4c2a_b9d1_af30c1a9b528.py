# Repair: Open the bend of the kicking knee away from the planted thigh.
"""Reconstruct person kicking ball using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct person kicking ball using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A player running right toward a ball. SQUARE extremes (6,6)-(42,42). Lucide person-standing informs the round head and connected stick limbs; preserve the source swung arms and backward leg. Widen clearance around the ball and head while retaining the kicking pose."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '33e0f679-82d2-4c2a-b9d1-af30c1a9b528'
SOURCE_PATH = 'pictographic-primitives/symbol/person playing ball_33e0f679-82d2-4c2a-b9d1-af30c1a9b528.svg'
AUTHOR = 'gpt-6'

class PersonKickingBall(Solo48):
    icon_id = 'person-kicking-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('football', 'soccer', 'kick', 'ball', 'sport', 'player', 'person', 'game')

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
        """Reconstruct person kicking ball using its inspected source pose and full_body_ref.png. Head radius 5, center (29, 11), actual torso junction (24, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (24, 11), (34, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (34, 11), (24, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('body', (24, 23), *(((22.759652654107917, 25.976833630141), (21.0, 28.25), (20, 30)),))
        self.add_line('arm-back-1', (24, 23), (14, 20))
        self.add_line('arm-back-2', (14, 20), (8, 26))
        self.add_line('arm-front-1', (24, 23), (31, 26))
        self.add_line('arm-front-2', (31, 26), (42, 20))
        self.add_line('leg-back-1', (20, 30), (14, 38))
        self.add_line('leg-back-2', (14, 38), (6, 38))
        self.add_line('leg-front-1', (20, 30), (28, 35))
        self.add_line('leg-front-2', (28, 35), (22, 42))
        self.add_arc('ball-top', (34, 38), (42, 38), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('ball-bottom', (42, 38), (34, 38), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('arm-back', *('arm-back-1', 'arm-back-2'), closed=False)
        self.add_contour('arm-front', *('arm-front-1', 'arm-front-2'), closed=False)
        self.add_contour('leg-back', *('leg-back-1', 'leg-back-2'), closed=False)
        self.add_contour('leg-front', *('leg-front-1', 'leg-front-2'), closed=False)
        self.add_contour('ball', *('ball-top', 'ball-bottom'), closed=True)
        self.relate('connect', *('body', 'arm-back'))
        self.relate('connect', *('body', 'arm-front'))
        self.relate('connect', *('body', 'leg-back'))
        self.relate('connect', *('body', 'leg-front'))
