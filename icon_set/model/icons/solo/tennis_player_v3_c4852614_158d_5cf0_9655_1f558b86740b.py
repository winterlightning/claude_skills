"""Reconstruct tennis player using its inspected source pose and full_body_ref.png. Head radius 4, center (30, 10), actual torso junction (30, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Tennis Player, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c4852614-158d-5cf0-9655-1f558b86740b'
SOURCE_PATH = 'pictographic-primitives/sports/tennis player_c4852614-158d-5cf0-9655-1f558b86740b.svg'
AUTHOR = 'gpt-6'

class TennisPlayerVariant3(Solo48):
    icon_id = 'tennis-player-v3'
    variant_of = 'tennis-player-v2'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('tennis', 'player', 'racket', 'ball', 'athlete', 'sport')

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
        """Reconstruct tennis player using its inspected source pose and full_body_ref.png. Head radius 4, center (30, 10), actual torso junction (30, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.ring('head', 30, 10, 4)
        self.add_arc('racket-a', (11, 10), (11, 22), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('racket-b', (11, 22), (11, 10), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_line('arms-1', (11, 22), (18, 29))
        self.add_line('arms-2', (18, 29), (30, 22))
        self.add_line('arms-3', (30, 22), (38, 23))
        self.add_line('arms-4', (38, 23), (42, 31))
        self.add_bezier('body-1', (30, 22), *(((30.0, 25.36), (28.5, 29.5), (28, 32)),))
        self.add_line('body-2', (28, 32), (37, 42))
        self.add_line('front-leg-1', (28, 32), (20, 36))
        self.add_line('front-leg-2', (20, 36), (20, 42))
        self.add_arc('ball-a', (9, 35), (9, 41), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('ball-b', (9, 41), (9, 35), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('racket', *('racket-a', 'racket-b'), closed=True)
        self.add_contour('arms', *('arms-1', 'arms-2', 'arms-3', 'arms-4'), closed=False)
        self.add_contour('body', *('body-1', 'body-2'), closed=False)
        self.add_contour('front-leg', *('front-leg-1', 'front-leg-2'), closed=False)
        self.add_contour('ball', *('ball-a', 'ball-b'), closed=True)
        self.relate('connect', *('arms', 'racket'))
        self.relate('connect', *('arms', 'body'))
        self.relate('connect', *('body', 'front-leg'))
