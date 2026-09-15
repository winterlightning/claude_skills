"""Reconstruct person pushing wall using its inspected source pose and full_body_ref.png. Head radius 5, center (27, 14), actual torso junction (22, 26): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

A leaning person pressing against a wall. SQUARE extremes (6,6)-(42,42). Lucide person-standing informs connected limb construction; no exact pushing match. Preserve the bent knee and right wall, and make the hand contact explicit."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fe641fda-6a23-4dc4-970c-90a6fe33f671'
SOURCE_PATH = 'pictographic-primitives/symbol/person pushing_fe641fda-6a23-4dc4-970c-90a6fe33f671.svg'
AUTHOR = 'gpt-6'

class PersonPushingWallVariant2(Solo48):
    icon_id = 'person-pushing-wall-v2'
    variant_of = 'person-pushing-wall'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('push', 'wall', 'person', 'effort', 'force', 'exercise', 'strength', 'resistance')

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
        """Reconstruct person pushing wall using its inspected source pose and full_body_ref.png. Head radius 5, center (27, 14), actual torso junction (22, 26): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('head', 27, 14, 5)
        self.add_bezier('body-back-leg-1', (22, 26), *(((20.6, 29.36), (17.5, 32.0), (16, 34)),))
        self.add_line('body-back-leg-2', (16, 34), (6, 42))
        self.add_line('arm-1', (22, 26), (30, 30))
        self.add_line('arm-2', (30, 30), (42, 22))
        self.add_line('front-leg-1', (16, 34), (28, 34))
        self.add_line('front-leg-2', (28, 34), (24, 42))
        self.add_line('wall-1', (42, 6), (42, 22))
        self.add_line('wall-2', (42, 22), (42, 42))
        self.add_contour('body-back-leg', *('body-back-leg-1', 'body-back-leg-2'), closed=False)
        self.add_contour('arm', *('arm-1', 'arm-2'), closed=False)
        self.add_contour('front-leg', *('front-leg-1', 'front-leg-2'), closed=False)
        self.add_contour('wall', *('wall-1', 'wall-2'), closed=False)
        self.relate('connect', *('body-back-leg', 'arm'))
        self.relate('connect', *('body-back-leg', 'front-leg'))
        self.relate('connect', *('arm', 'wall'))
