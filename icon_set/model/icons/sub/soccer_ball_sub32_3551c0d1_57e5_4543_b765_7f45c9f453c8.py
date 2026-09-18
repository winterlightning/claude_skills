"""Independent 32px profile of soccer-ball.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3551c0d1-57e5-4543-b765-7f45c9f453c8'
SOURCE_PATH = 'pictographic-primitives/sports/soccer ball_3551c0d1-57e5-4543-b765-7f45c9f453c8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3551c0d1-57e5-4543-b765-7f45c9f453c8', 'pictographic-primitives/sports/soccer ball_3551c0d1-57e5-4543-b765-7f45c9f453c8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/soccer-ball',)
SOLO_SOURCE_ICON_IDS = ('soccer-ball',)
REFERENCE_EXPORT_SHA256 = 'ff42fd9bf58c5a4a47fec98036ebd5aceccff232425aade3404d65a1fe67eae1'

class Drawing(Sub32):
    icon_id = 'soccer-ball-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'sports'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 8), (16, 2), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 2), (27, 8), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (27, 8), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (30, 16), (24, 27), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (24, 27), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-6', (16, 30), (8, 27), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-7', (8, 27), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-8', (2, 16), (5, 8), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (13, 20), (20, 20))
        self.add_line('p2-r1-2', (20, 20), (22, 13))
        self.add_line('p2-r1-3', (22, 13), (16, 9))
        self.add_line('p2-r1-4', (16, 9), (10, 13))
        self.add_line('p2-r1-5', (10, 13), (13, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (13, 20), (8, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (20, 20), (24, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (22, 13), (27, 8))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (16, 9), (16, 2))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (10, 13), (5, 8))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p6-r1-1')
        self.relate("connect", 'p1-r1-1', 'p7-r1-1')
        self.relate("connect", 'p1-r1-2', 'p5-r1-1')
        self.relate("connect", 'p1-r1-2', 'p6-r1-1')
        self.relate("connect", 'p1-r1-3', 'p5-r1-1')
        self.relate("connect", 'p1-r1-4', 'p4-r1-1')
        self.relate("connect", 'p1-r1-5', 'p4-r1-1')
        self.relate("connect", 'p1-r1-6', 'p3-r1-1')
        self.relate("connect", 'p1-r1-7', 'p3-r1-1')
        self.relate("connect", 'p1-r1-8', 'p7-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p5-r1-1')
        self.relate("connect", 'p2-r1-3', 'p5-r1-1')
        self.relate("connect", 'p2-r1-3', 'p6-r1-1')
        self.relate("connect", 'p2-r1-4', 'p6-r1-1')
        self.relate("connect", 'p2-r1-4', 'p7-r1-1')
        self.relate("connect", 'p2-r1-5', 'p3-r1-1')
        self.relate("connect", 'p2-r1-5', 'p7-r1-1')
