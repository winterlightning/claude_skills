"""Tennis Player, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c4852614-158d-5cf0-9655-1f558b86740b'
SOURCE_PATH = 'pictographic-primitives/sports/tennis player_c4852614-158d-5cf0-9655-1f558b86740b.svg'
AUTHOR = 'gpt-6'

class TennisPlayerVariant2(Solo48):
    icon_id = 'tennis-player-v2'
    variant_of = 'tennis-player'
    variant_label = 'Hole and centerline reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('tennis', 'player', 'racket', 'ball', 'athlete', 'sport')

    def build(self) -> None:
        """Open the tennis ball to radius 3 while keeping it inside the left envelope."""

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
        circle('head', 29, 9, 3)
        arc('racket-a', (11, 10), (11, 22), 5, 6)
        arc('racket-b', (11, 22), (11, 10), 5, 6)
        self.add_contour('racket', 'racket-a', 'racket-b', closed=True)
        self.add_polyline('arms', (11, 22), (18, 29), (29,20), (38, 23), (42, 31))
        self.add_polyline('body', (29,20), (28, 32), (37, 42))
        self.add_polyline('front-leg', (28, 32), (20, 36), (20, 42))
        circle('ball', 9, 38, 3)
        for x, y in [('arms', 'racket'), ('arms', 'body'), ('body', 'front-leg')]:
            self.relate('connect', x, y)
