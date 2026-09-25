"""Two people whose inward arms form a cracked heart. Lucide heart/heart-crack and users-round inform lobes and paired heads; physical arm/heart contacts retained.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c2a597c8-14e7-4ae0-abaa-97e0be0e581e'
SOURCE_PATH = 'pictographic-primitives/symbol/two persons with broken heart_c2a597c8-14e7-4ae0-abaa-97e0be0e581e.svg'
AUTHOR = 'gpt-6'

class CoupleBrokenHeart(Solo48):
    icon_id = 'couple-broken-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('broken-heart', 'couple', 'breakup', 'divorce', 'heartbreak', 'relationship', 'people', 'sad')

    def oval(self, n, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(n + '-top', (cx - rx, cy), (cx + rx, cy), radius_x=rx, radius_y=ry)
        self.add_arc(n + '-bottom', (cx + rx, cy), (cx - rx, cy), radius_x=rx, radius_y=ry)
        self.add_contour(n, n + '-top', n + '-bottom', closed=True)

    def raw(self, n, points):
        for j, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(n + '-' + str(j), a, b)

    def path(self, n, points, closed=False):
        self.add_polyline(n, *points, closed=closed)

    def build(self):
        """Reduce the full zigzag crack to a short cleft so the heart has one broad opening."""
        for n, cx in [('left', 10), ('right', 38)]:
            self.oval(n + '-head', cx, 10, 4)
        self.add_line('left-body', (6, 42), (6, 30))
        self.add_arc('left-arm', (6, 30), (14, 22), radius_x=8)
        self.add_line('left-hand', (14, 22), (16, 22))
        self.add_contour('left-person', 'left-body', 'left-arm', 'left-hand')
        self.add_line('right-body', (42, 42), (42, 30))
        self.add_arc('right-arm', (42, 30), (34, 22), radius_x=8, sweep=False)
        self.add_line('right-hand', (34, 22), (32, 22))
        self.add_contour('right-person', 'right-body', 'right-arm', 'right-hand')
        self.add_arc('heart-left-upper', (24, 26), (16, 22), radius_x=5, sweep=False)
        self.add_arc('heart-left-outer', (16, 22), (14, 26), radius_x=5, sweep=False)
        self.raw('heart-point', [(14, 26), (24, 38), (34, 26)])
        self.add_arc('heart-right-outer', (34, 26), (32, 22), radius_x=5, sweep=False)
        self.add_arc('heart-right-upper', (32, 22), (24, 26), radius_x=5, sweep=False)
        self.add_contour('heart', 'heart-left-upper', 'heart-left-outer', 'heart-point-1', 'heart-point-2', 'heart-right-outer', 'heart-right-upper', closed=True)
        self.relate('connect', 'heart', 'left-person')
        self.relate('connect', 'heart', 'right-person')
        self.path('crack', [(24, 26), (24, 30)])
        self.relate('connect', 'crack', 'heart')
