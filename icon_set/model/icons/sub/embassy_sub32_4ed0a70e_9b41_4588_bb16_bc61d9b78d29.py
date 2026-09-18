"""Independent 32px profile of embassy.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4ed0a70e-9b41-4588-bb16-bc61d9b78d29'
SOURCE_PATH = 'pictographic-primitives/symbol/embassy_4ed0a70e-9b41-4588-bb16-bc61d9b78d29.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4ed0a70e-9b41-4588-bb16-bc61d9b78d29', 'pictographic-primitives/symbol/embassy_4ed0a70e-9b41-4588-bb16-bc61d9b78d29.svg'),)
PROFILE_SOURCE_KEYS = ('solo/embassy',)
SOLO_SOURCE_ICON_IDS = ('embassy',)
REFERENCE_EXPORT_SHA256 = '2d184c606668088db58c4615fae1e8702aaef16f72c63e50e853b9674d2964a4'

class Drawing(Sub32):
    icon_id = 'embassy-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (4, 16), (28, 16), radius_x=12, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (28, 16), (4, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 27), (30, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (6, 16), (6, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (13, 16), (13, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (20, 16), (20, 27))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (26, 16), (26, 27))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
