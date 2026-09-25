"""Independent 32px profile of arrows-diagonal-resize.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'eab2ea44-17e8-4abd-a74b-7e5c171a7bae'
SOURCE_PATH = 'pictographic-primitives/symbol/arrows left right 1_eab2ea44-17e8-4abd-a74b-7e5c171a7bae.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('eab2ea44-17e8-4abd-a74b-7e5c171a7bae', 'pictographic-primitives/symbol/arrows left right 1_eab2ea44-17e8-4abd-a74b-7e5c171a7bae.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrows-diagonal-resize',)
SOLO_SOURCE_ICON_IDS = ('arrows-diagonal-resize',)
REFERENCE_EXPORT_SHA256 = '365667a38a52e3912ff5f6573ad8ffa3d41e6f4c8c28e6f61e284e52b2c26efc'

class Drawing(Sub32):
    icon_id = 'arrows-diagonal-resize-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 19), (22, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (13, 2), (22, 2))
        self.add_line('p2-r1-2', (22, 2), (22, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (27, 13), (10, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (10, 22), (10, 30))
        self.add_line('p4-r1-2', (10, 30), (19, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
