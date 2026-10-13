"""Independent 32px profile of gauge.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'f851be15-9995-4280-9f7a-d66f70d256fd'
SOURCE_PATH = 'pictographic-primitives/symbol/gauge_f851be15-9995-4280-9f7a-d66f70d256fd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f851be15-9995-4280-9f7a-d66f70d256fd', 'pictographic-primitives/symbol/gauge_f851be15-9995-4280-9f7a-d66f70d256fd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/gauge',)
SOLO_SOURCE_ICON_IDS = ('gauge',)
REFERENCE_EXPORT_SHA256 = 'b1057982da61ba3025d8140132084e8edf2e373a8ff9b1c1d87ed8a2a61c10ee'

class Drawing(Sub32):
    icon_id = 'gauge-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (21, 7), (21, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (7, 7), (11, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 22), (7, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, 14), (26, 18))
        self.add_line('p4-r1-2', (26, 18), (18, 22))
        self.add_arc('p4-r1-3', (18, 22), (17, 28), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('p4-r1-4', (17, 28), (20, 30), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('p4-r1-5', (20, 30), (25, 23), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_line('p4-r1-6', (25, 23), (30, 14))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', closed=False)
