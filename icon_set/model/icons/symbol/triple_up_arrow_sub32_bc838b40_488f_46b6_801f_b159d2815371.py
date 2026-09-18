"""Independent 32px profile of triple-up-arrow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'bc838b40-488f-46b6-801f-b159d2815371'
SOURCE_PATH = 'pictographic-primitives/symbol/triple up arrow_bc838b40-488f-46b6-801f-b159d2815371.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bc838b40-488f-46b6-801f-b159d2815371', 'pictographic-primitives/symbol/triple up arrow_bc838b40-488f-46b6-801f-b159d2815371.svg'),)
PROFILE_SOURCE_KEYS = ('solo/triple-up-arrow',)
SOLO_SOURCE_ICON_IDS = ('triple-up-arrow',)
REFERENCE_EXPORT_SHA256 = 'b2ae280b2482e0ac6ea53266ea8f0e39dbb151daf8c1223f8f2e35ac576d5f34'

class Drawing(Sub32):
    icon_id = 'triple-up-arrow-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 17), (16, 5))
        self.add_line('p1-r1-2', (16, 5), (20, 8))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 5), (12, 8))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 21), (6, 17))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (6, 17), (6, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (6, 17), (9, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (26, 17), (23, 20))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (26, 27), (26, 17))
        self.add_line('p7-r1-2', (26, 17), (30, 20))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'p6-r1-1', 'p7-r1-1')
        self.relate('connect', 'p6-r1-1', 'p7-r1-2')
