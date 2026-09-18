"""Independent 32px profile of help-wheel.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '32cc640b-fd6f-5d01-b576-fd631edb4656'
SOURCE_PATH = 'pictographic-primitives/interface-essential/help wheel_32cc640b-fd6f-5d01-b576-fd631edb4656.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('32cc640b-fd6f-5d01-b576-fd631edb4656', 'pictographic-primitives/interface-essential/help wheel_32cc640b-fd6f-5d01-b576-fd631edb4656.svg'),)
PROFILE_SOURCE_KEYS = ('solo/help-wheel',)
SOLO_SOURCE_ICON_IDS = ('help-wheel',)
REFERENCE_EXPORT_SHA256 = '99ee72f465828cf91428c142fb909bc274c3bdd053f39c1ebc3a89ff49e024d8'

class Drawing(Sub32):
    icon_id = 'help-wheel-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (9, 16), (23, 16), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (23, 16), (9, 16), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (12, 10), (8, 5))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (20, 10), (24, 5))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (20, 22), (24, 27))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (12, 22), (8, 27))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
