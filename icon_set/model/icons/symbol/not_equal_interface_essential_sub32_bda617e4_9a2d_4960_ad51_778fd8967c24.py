"""Independent 32px profile of not-equal-interface-essential.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'bda617e4-9a2d-4960-ad51-778fd8967c24'
SOURCE_PATH = 'pictographic-primitives/interface-essential/not equal_bda617e4-9a2d-4960-ad51-778fd8967c24.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bda617e4-9a2d-4960-ad51-778fd8967c24', 'pictographic-primitives/interface-essential/not equal_bda617e4-9a2d-4960-ad51-778fd8967c24.svg'),)
PROFILE_SOURCE_KEYS = ('solo/not-equal-interface-essential',)
SOLO_SOURCE_ICON_IDS = ('not-equal-interface-essential',)
REFERENCE_EXPORT_SHA256 = '23eb6247f06069cb4db480303d8829b9f5b46e72742317d203248e1e84e0fe2e'

class Drawing(Sub32):
    icon_id = 'not-equal-interface-essential-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (22, 2), (14, 20))
        self.add_line('p1-r1-2', (14, 20), (27, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (5, 13), (27, 13))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (5, 20), (14, 20))
        self.add_line('p3-r1-2', (14, 20), (10, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-2')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-2')
