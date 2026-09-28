"""Independent 32px profile of swing-set.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '915b55b6-88bb-4695-9e96-85f5616755a8'
SOURCE_PATH = 'pictographic-primitives/symbol/swing_915b55b6-88bb-4695-9e96-85f5616755a8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('915b55b6-88bb-4695-9e96-85f5616755a8', 'pictographic-primitives/symbol/swing_915b55b6-88bb-4695-9e96-85f5616755a8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/swing-set',)
SOLO_SOURCE_ICON_IDS = ('swing-set',)
REFERENCE_EXPORT_SHA256 = '34f6c03b9da6aed2b66589dfadc2e4627c667ce0220dc9114eda92fe97f2e7a7'

class Drawing(Sub32):
    icon_id = 'swing-set-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 2), (11, 2))
        self.add_line('p1-r1-2', (11, 2), (21, 2))
        self.add_line('p1-r1-3', (21, 2), (27, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (5, 2), (2, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (27, 2), (30, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (11, 2), (11, 22))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (21, 2), (21, 22))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_arc('p6-r1-1', (11, 22), (21, 22), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p5-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p6-r1-1')
        self.relate('connect', 'p5-r1-1', 'p6-r1-1')
