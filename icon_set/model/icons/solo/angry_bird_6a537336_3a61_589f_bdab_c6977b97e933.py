"""Angry Bird, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6a537336-3a61-589f-bdab-c6977b97e933'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-01/angry birds_6a537336-3a61-589f-bdab-c6977b97e933.svg'
AUTHOR = 'gpt-6'

class AngryBird(Solo48):
    icon_id = 'angry-bird'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/gaming'
    aliases = ()
    keywords = ('bird', 'angry', 'angry birds', 'mobile game', 'character', 'cartoon', 'video game', 'game')

    def build(self):
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.

        def circle(name, x, y, r):
            self.add_arc(name + '-a', (x, y - r), (x, y + r), radius_x=r)
            self.add_arc(name + '-b', (x, y + r), (x, y - r), radius_x=r)
            self.add_contour(name, name + '-a', name + '-b', closed=True)

        def arc(name, a, b, r, ry=None, sweep=True):
            self.add_arc(name, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)

        def poly(name, *pts):
            for i, (a, b) in enumerate(zip(pts, pts[1:]), 1):
                self.add_line(f'{name}-{i}', a, b)
        arc('body-left', (24, 12), (8, 28), 16, sweep=False)
        arc('body-bottom', (8, 28), (40, 28), 16, sweep=False)
        arc('body-right', (40, 28), (24, 12), 16, sweep=False)
        self.add_contour('body', 'body-left', 'body-bottom', 'body-right', closed=True)
        self.add_polyline('tuft', (24, 12), (20, 4), (29, 4))
        self.relate('connect', 'tuft', 'body')
        self.add_polyline('brows', (19, 23), (24, 25), (29, 23))
        self.add_polyline('beak', (21, 33), (24, 35), (27, 33))
