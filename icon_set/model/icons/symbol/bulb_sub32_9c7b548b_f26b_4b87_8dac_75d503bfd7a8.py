"""Independent 32px profile of bulb.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9c7b548b-f26b-4b87-8dac-75d503bfd7a8'
SOURCE_PATH = 'pictographic-primitives/work/bulb_9c7b548b-f26b-4b87-8dac-75d503bfd7a8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9c7b548b-f26b-4b87-8dac-75d503bfd7a8', 'pictographic-primitives/work/bulb_9c7b548b-f26b-4b87-8dac-75d503bfd7a8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bulb',)
SOLO_SOURCE_ICON_IDS = ('bulb',)
REFERENCE_EXPORT_SHA256 = 'd5fddd089f172cf11dfe70931054bb5aa9b03c0c8e03a6670c4cc2adca612a98'

class Drawing(Sub32):
    icon_id = 'bulb-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'work'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 5), (16, 6))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (6, 8), (7, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 17), (3, 17))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, 17), (29, 17))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (12, 21), (20, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (14, 27), (18, 27))
        self.add_arc('p6-r1-2', (18, 27), (20, 26), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('p6-r1-3', (20, 26), (20, 22), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p6-r1-4', (20, 22), (22, 19))
        self.add_arc('p6-r1-5', (22, 19), (10, 19), radius_x=6, radius_y=6, large_arc=True, sweep=False)
        self.add_line('p6-r1-6', (10, 19), (12, 22))
        self.add_line('p6-r1-7', (12, 22), (13, 26))
        self.add_line('p6-r1-8', (13, 26), (14, 27))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', 'p6-r1-5', 'p6-r1-6', 'p6-r1-7', 'p6-r1-8', closed=False)
        self.add_line('p7-r1-1', (25, 9), (26, 8))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
