"""Independent 32px profile of phone-with-down-arrow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '14b5fcaa-27a4-4bd9-8940-7690a86b2fe1'
SOURCE_PATH = 'pictographic-primitives/symbol/phone with down arrow_14b5fcaa-27a4-4bd9-8940-7690a86b2fe1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('14b5fcaa-27a4-4bd9-8940-7690a86b2fe1', 'pictographic-primitives/symbol/phone with down arrow_14b5fcaa-27a4-4bd9-8940-7690a86b2fe1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/phone-with-down-arrow',)
SOLO_SOURCE_ICON_IDS = ('phone-with-down-arrow',)
REFERENCE_EXPORT_SHA256 = '6d59e59faac650060dd379c21f1326f2b68af82b1c6a8ac06bb179ed5806a02d'

class Drawing(Sub32):
    icon_id = 'phone-with-down-arrow-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Incoming call: arrow pointing down-left into the corner, and a clean handset (one body arc,
        # rounded caps, straight pad edges), mirrored across its diagonal.
        self.add_line('p1-r1-1', (30, 2), (21, 11))
        self.add_line('p1-r1-2', (21, 11), (28, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (21, 4), (21, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('ear-1', (5, 18), (11, 10))
        self.add_line('ear-2', (11, 10), (11, 7))
        self.add_line('ear-3', (11, 7), (6, 2))
        self.add_arc('ear-cap', (6, 2), (2, 6), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('body', (2, 6), (26, 30), radius_x=24, radius_y=24, large_arc=False, sweep=False)
        self.add_arc('mouth-cap', (26, 30), (30, 26), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('mouth-3', (30, 26), (25, 21))
        self.add_line('mouth-2', (25, 21), (22, 21))
        self.add_line('mouth-1', (22, 21), (14, 27))
        self.add_contour('handset', 'ear-1', 'ear-2', 'ear-3', 'ear-cap', 'body', 'mouth-cap', 'mouth-3', 'mouth-2', 'mouth-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'ear-1', 'body')
        self.relate('connect', 'mouth-1', 'body')
