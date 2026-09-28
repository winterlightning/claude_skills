"""Independent 32px profile of board-rider-over-waves.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '31dfc8f9-9e71-491e-9f9a-e8bd904e4344'
SOURCE_PATH = 'pictographic-primitives/sports/skating_31dfc8f9-9e71-491e-9f9a-e8bd904e4344.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('31dfc8f9-9e71-491e-9f9a-e8bd904e4344', 'pictographic-primitives/sports/skating_31dfc8f9-9e71-491e-9f9a-e8bd904e4344.svg'),)
PROFILE_SOURCE_KEYS = ('solo/board-rider-over-waves',)
SOLO_SOURCE_ICON_IDS = ('board-rider-over-waves',)
REFERENCE_EXPORT_SHA256 = 'b21bf3a86213005071e2a4ae04d7752e096df839500becafc96a92aa5a8adb5c'

class Drawing(Sub32):
    icon_id = 'board-rider-over-waves-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'sports'
    categories = ('sports', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 8), (10, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (10, 8), (5, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (7, 16), ((7, 18), (9, 20), (10, 21)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 16), (7, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (7, 16), (13, 16))
        self.add_line('p4-r1-2', (13, 16), (18, 11))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (7, 27), (10, 21))
        self.add_line('p5-r1-2', (10, 21), (18, 27))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (18, 5), (18, 11))
        self.add_line('p6-r1-2', (18, 11), (18, 13))
        self.add_line('p6-r1-3', (18, 13), (18, 21))
        self.add_line('p6-r1-4', (18, 21), (18, 27))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', closed=False)
        self.add_line('p7-r1-1', (18, 5), (30, 14))
        self.add_line('p7-r1-2', (30, 14), (30, 14))
        self.add_line('p7-r1-3', (30, 14), (18, 19))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', closed=False)
        self.add_line('p8-r1-1', (2, 27), (7, 27))
        self.add_line('p8-r1-2', (7, 27), (18, 27))
        self.add_line('p8-r1-3', (18, 27), (24, 27))
        self.add_arc('p8-r1-4', (24, 27), (29, 21), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', 'p8-r1-3', 'p8-r1-4', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-2')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p4-r1-2', 'p6-r1-1')
        self.relate('connect', 'p4-r1-2', 'p6-r1-2')
        self.relate('connect', 'p5-r1-1', 'p8-r1-1')
        self.relate('connect', 'p5-r1-1', 'p8-r1-2')
        self.relate('connect', 'p5-r1-2', 'p6-r1-4')
        self.relate('connect', 'p5-r1-2', 'p8-r1-2')
        self.relate('connect', 'p5-r1-2', 'p8-r1-3')
        self.relate('connect', 'p6-r1-1', 'p7-r1-1')
        self.relate('connect', 'p6-r1-4', 'p8-r1-2')
        self.relate('connect', 'p6-r1-4', 'p8-r1-3')
