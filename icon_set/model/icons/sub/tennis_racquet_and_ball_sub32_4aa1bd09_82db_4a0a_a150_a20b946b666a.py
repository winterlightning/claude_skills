"""Independent 32px profile of tennis-racquet-and-ball.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4aa1bd09-82db-4a0a-a150-a20b946b666a'
SOURCE_PATH = 'pictographic-primitives/sports/tennis_4aa1bd09-82db-4a0a-a150-a20b946b666a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4aa1bd09-82db-4a0a-a150-a20b946b666a', 'pictographic-primitives/sports/tennis_4aa1bd09-82db-4a0a-a150-a20b946b666a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/tennis-racquet-and-ball',)
SOLO_SOURCE_ICON_IDS = ('tennis-racquet-and-ball',)
REFERENCE_EXPORT_SHA256 = 'd3a947aa723e9fbe9cefd4266f11e1bbcd166b0cc721f9f73b1a9eb0b6375e67'

class Drawing(Sub32):
    icon_id = 'tennis-racquet-and-ball-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/sports'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (18, 16), (16, 5), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 5), (27, 4), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (27, 4), (28, 14), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (28, 14), (18, 16), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (18, 16), (22, 10))
        self.add_line('p2-r1-2', (22, 10), (27, 4))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 5), (22, 10))
        self.add_line('p3-r1-2', (22, 10), (28, 14))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (18, 16), (2, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_bezier('p5-r1-1', (2, 4), ((2, 3), (3, 2), (4, 2)))
        self.add_bezier('p5-r1-2', (4, 2), ((6, 2), (7, 3), (7, 4)))
        self.add_arc('p5-r1-3', (7, 4), (2, 4), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-1', 'p4-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p3-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-2')
        self.relate("connect", 'p1-r1-4', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-2')
