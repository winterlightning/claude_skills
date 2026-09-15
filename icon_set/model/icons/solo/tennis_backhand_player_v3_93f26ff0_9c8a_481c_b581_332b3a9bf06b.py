"""Reconstruct tennis backhand player using its inspected source pose and full_body_ref.png. Head radius 4, center (14, 10), actual torso junction (14, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Reconstruct tennis backhand player using its inspected source pose and full_body_ref.png. Head radius 4, center (14, 10), actual torso junction (14, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance.

Tennis Backhand Player, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '93f26ff0-9c8a-481c-b581-332b3a9bf06b'
SOURCE_PATH = 'pictographic-primitives/sports/tennis backhand_93f26ff0-9c8a-481c-b581-332b3a9bf06b.svg'
AUTHOR = 'gpt-6'

class TennisBackhandPlayerVariant3(Solo48):
    icon_id = 'tennis-backhand-player-v3'
    variant_of = 'tennis-backhand-player-v2'
    variant_label = 'Visual reconstruction after full 500-icon audit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('tennis', 'backhand', 'player', 'racket', 'ball', 'sport')

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
        """Reconstruct tennis backhand player using its inspected source pose and full_body_ref.png. Head radius 4, center (14, 10), actual torso junction (14, 22): squared distance 144, centerline clearance8 and painted clearance4. Upper torso tangent follows that axis; preserve the subject's limb action and equipment. Shared Lucide person-standing joints; updated approaching-ball example informs head/body balance."""
        self.add_arc('head-a', (10, 10), (18, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('head-b', (18, 10), (10, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('body-1', (14, 22), *(((14.0, 25.36), (11.0, 28.0), (10, 30)),))
        self.add_line('body-2', (10, 30), (6, 42))
        self.add_line('front-leg-1', (10, 30), (20, 34))
        self.add_line('front-leg-2', (20, 34), (22, 42))
        self.add_line('arms-1', (14, 22), (20, 27))
        self.add_line('arms-2', (20, 27), (28, 28))
        self.add_line('racket-arm', (28, 28), (32, 19))
        self.add_arc('racket-a', (32, 7), (32, 19), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('racket-b', (32, 19), (32, 7), radius_x=5, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('ball-a', (39, 28), (39, 34), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('ball-b', (39, 34), (39, 28), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('head', *('head-a', 'head-b'), closed=True)
        self.add_contour('front-leg', *('front-leg-1', 'front-leg-2'), closed=False)
        self.add_contour('arms', *('arms-1', 'arms-2'), closed=False)
        self.add_contour('racket', *('racket-a', 'racket-b'), closed=True)
        self.add_contour('ball', *('ball-a', 'ball-b'), closed=True)
        self.relate('connect', *('arms', 'racket-arm'))
        self.relate('connect', *('racket-arm', 'racket'))
        self.relate('connect', *('body', 'front-leg'))
        self.relate('connect', *('body', 'arms'))
        self.relate('connect', *('racket-arm', 'racket'))
        self.add_contour('body', *('body-1',), closed=False)
        self.add_contour('body-section-1', *('body-2',), closed=False)
        self.relate('connect', 'body-1', 'body-2')
        self.relate('connect', 'head-a', 'head-b')
        self.relate('connect', 'body-1', 'body-2')
        self.relate('connect', 'body-1', 'front-leg-1')
        self.relate('connect', 'body-1', 'arms-1')
        self.relate('connect', 'body-2', 'front-leg-1')
        self.relate('connect', 'front-leg-1', 'front-leg-2')
        self.relate('connect', 'arms-1', 'arms-2')
        self.relate('connect', 'arms-2', 'racket-arm')
        self.relate('connect', 'racket-arm', 'racket-a')
        self.relate('connect', 'racket-arm', 'racket-b')
        self.relate('connect', 'racket-a', 'racket-b')
        self.relate('connect', 'ball-a', 'ball-b')
