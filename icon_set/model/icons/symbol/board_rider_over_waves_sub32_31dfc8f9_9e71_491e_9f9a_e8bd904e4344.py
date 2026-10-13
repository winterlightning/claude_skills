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
        self.add_arc('p1-r1-1', (5, 6), (9, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (9, 6), (5, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=True)
        self.add_line('p2-r1-1', (8, 16), (10, 28))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (8, 16), (22, 14))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 28), (30, 28))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (22, 28), (22, 4))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_arc('p6-r1-1', (22, 4), (22, 20), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
