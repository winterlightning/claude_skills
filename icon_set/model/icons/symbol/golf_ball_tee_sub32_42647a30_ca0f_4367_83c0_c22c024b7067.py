"""Independent 32px profile of golf-ball-tee.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '42647a30-ca0f-4367-83c0-c22c024b7067'
SOURCE_PATH = 'pictographic-primitives/symbol/golf_42647a30-ca0f-4367-83c0-c22c024b7067.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('42647a30-ca0f-4367-83c0-c22c024b7067', 'pictographic-primitives/symbol/golf_42647a30-ca0f-4367-83c0-c22c024b7067.svg'),)
PROFILE_SOURCE_KEYS = ('solo/golf-ball-tee',)
SOLO_SOURCE_ICON_IDS = ('golf-ball-tee',)
REFERENCE_EXPORT_SHA256 = 'ff243eab90f588edf29d30f8c61c394113b7a658fd78484c8793dfd3f9a3688b'

class Drawing(Sub32):
    icon_id = 'golf-ball-tee-sub32'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (8, 10), (24, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (24, 10), (8, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 10), (16, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (10, 25), (16, 25))
        self.add_line('p3-r1-2', (16, 25), (22, 25))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (16, 25), (16, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
