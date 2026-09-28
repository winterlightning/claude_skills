"""Independent 32px profile of percentage.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1719c236-69d1-4b4e-8346-b1533e9728e9'
SOURCE_PATH = 'pictographic-primitives/symbol/percentage_1719c236-69d1-4b4e-8346-b1533e9728e9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1719c236-69d1-4b4e-8346-b1533e9728e9', 'pictographic-primitives/symbol/percentage_1719c236-69d1-4b4e-8346-b1533e9728e9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/percentage',)
SOLO_SOURCE_ICON_IDS = ('percentage',)
REFERENCE_EXPORT_SHA256 = 'e622745a5a4c90abb56be8ad59649784d60ace3b9d4d58dc1f13cbc27208dab5'

class Drawing(Sub32):
    icon_id = 'percentage-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 16), (30, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 5), (16, 5))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 27), (16, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
