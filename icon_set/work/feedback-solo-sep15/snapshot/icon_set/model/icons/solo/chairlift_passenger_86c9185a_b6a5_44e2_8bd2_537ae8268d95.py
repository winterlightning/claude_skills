"""Chairlift Passenger, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '86c9185a-b6a5-44e2-8bd2-537ae8268d95'
SOURCE_PATH = 'pictographic-primitives/sports/skiing cable car_86c9185a-b6a5-44e2-8bd2-537ae8268d95.svg'
AUTHOR = 'gpt-6'

class ChairliftPassenger(Solo48):
    icon_id = 'chairlift-passenger'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('chairlift', 'passenger', 'lift', 'cable', 'ski', 'winter')

    def build(self) -> None:

        def circle(n, x, y, r):
            self.add_arc(n + '-a', (x, y - r), (x, y + r), radius_x=r)
            self.add_arc(n + '-b', (x, y + r), (x, y - r), radius_x=r)
            self.add_contour(n, n + '-a', n + '-b', closed=True)

        def arc(n, a, b, r, ry=None, sweep=True):
            self.add_arc(n, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)

        def poly(n, *pts):
            for i, (a, b) in enumerate(zip(pts, pts[1:]), 1):
                self.add_line(f'{n}-{i}', a, b)
        axis = 24

        def mirror(p):
            return (2 * axis - p[0], p[1])
        self.add_polyline('cable', (6, 16), (12, 14), (42, 6))
        self.add_polyline('hanger', (12, 14), (12, 35), (20, 35))
        self.relate('connect', 'cable', 'hanger')
        # Shared full_body_ref.png: head bottom 27, seated body 35; visible gap 4.
        circle('head', 26, 24, 3)
        self.add_line('rider', (20,35), (31,35))
        self.add_line('elbow', (17,32), (20,35))
        self.add_line('shin', (31,35), (33,42))
        self.relate('connect','elbow','rider')
        self.relate('connect','shin','rider')
        self.relate('connect','elbow','hanger')
        self.relate('connect', 'rider', 'hanger')
