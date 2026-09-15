"""Tennis Backhand Player, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '93f26ff0-9c8a-481c-b581-332b3a9bf06b'
SOURCE_PATH = 'pictographic-primitives/sports/tennis backhand_93f26ff0-9c8a-481c-b581-332b3a9bf06b.svg'
AUTHOR = 'gpt-6'

class TennisBackhandPlayerVariant2(Solo48):
    icon_id = 'tennis-backhand-player-v2'
    variant_of = 'tennis-backhand-player'
    variant_label = 'Hole and centerline reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('tennis', 'backhand', 'player', 'racket', 'ball', 'sport')

    def build(self) -> None:
        """Open the tennis ball to radius 3 and preserve the right envelope."""

        def circle(n, x, y, r):
            self.add_arc(n + '-a', (x, y - r), (x, y + r), radius_x=r)
            self.add_arc(n + '-b', (x, y + r), (x, y - r), radius_x=r)
            self.add_contour(n, n + '-a', n + '-b', closed=True)

        def arc(n, a, b, r, ry=None, sweep=True):
            self.add_arc(n, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)

        def poly(n, *pts):
            for i, (a, b) in enumerate(zip(pts, pts[1:]), 1):
                self.add_line(f'{n}-{i}', a, b)

        def wave(n, y):
            for i, x in enumerate((6, 18, 30)):
                arc(f'{n}-{i}', (x, y), (x + 12, y), 6, 2, sweep=i % 2 == 0)
            self.add_contour(n, *[f'{n}-{i}' for i in range(3)])
        axis = 24

        def mirror(p):
            return (2 * axis - p[0], p[1])
        circle('head', 16, 9, 3)
        self.add_polyline('body', (16,20), (10, 30), (6, 42))
        self.add_polyline('front-leg', (10, 30), (20, 34), (22, 42))
        self.add_polyline('arms',(16,20),(20,27),(28,28))
        self.add_line('racket-arm',(28,28),(32,19))
        self.relate('connect','arms','racket-arm')
        self.relate('connect','racket-arm','racket')
        arc('racket-a', (32, 7), (32, 19), 5, 6)
        arc('racket-b', (32, 19), (32, 7), 5, 6)
        self.add_contour('racket', 'racket-a', 'racket-b', closed=True)
        circle('ball', 39, 31, 3)
        for x, y in [('body', 'front-leg'), ('body', 'arms'), ('racket-arm', 'racket')]:
            self.relate('connect', x, y)
