"""Reconstruct racing cyclist using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch.

Reconstruct racing cyclist using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Racing cyclist, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1cb7d2ba-c91a-4cd1-bd29-7ebbabf08914'
SOURCE_PATH = 'pictographic-primitives/sports/race_1cb7d2ba-c91a-4cd1-bd29-7ebbabf08914.svg'
AUTHOR = 'gpt-6'

class RacingCyclistVariant2(Solo48):
    icon_id = 'racing-cyclist-v2'
    variant_of = 'racing-cyclist'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('racing', 'cyclist')

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
        """Reconstruct racing cyclist using its inspected source pose and full_body_ref.png. Head radius 5, center (30, 11), actual torso junction (25, 23): squared distance 169, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance. Adjust the adjoining arm/pack endpoints together so the enlarged head remains clear of every branch."""
        self.add_arc('head-a', (25, 11), (35, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('head-b', (35, 11), (25, 11), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('wheel-rear-a', (12, 30), (12, 42), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('wheel-rear-b', (12, 42), (12, 30), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('wheel-front-a', (36, 30), (36, 42), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('wheel-front-b', (36, 42), (36, 30), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_bezier('rider-1', (25, 23), *(((23.912143413559157, 25.610855807458023), (19.75, 23.75), (18, 24)),))
        self.add_line('rider-2', (18, 24), (25, 29))
        self.add_line('rider-3', (25, 29), (21, 38))
        self.add_line('arms-1', (25, 23), (29, 25))
        self.add_line('arms-2', (29, 25), (37, 24))
        self.add_line('fork', (31, 24), (36, 36))
        self.add_line('frame', (12, 36), (18, 24))
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('wheel-rear', *('wheel-rear-a', 'wheel-rear-b'), closed=True)
        self.add_contour('wheel-front', *('wheel-front-a', 'wheel-front-b'), closed=True)
        self.add_contour('rider', *('rider-1', 'rider-2', 'rider-3'), closed=False)
        self.add_contour('arms', *('arms-1', 'arms-2'), closed=False)
        self.relate('connect', *('rider', 'arms'))
        self.relate('connect', *('fork', 'arms'))
        self.relate('connect', *('fork', 'wheel-front'))
        self.relate('connect', *('frame', 'wheel-rear'))
        self.relate('connect', *('frame', 'rider'))
