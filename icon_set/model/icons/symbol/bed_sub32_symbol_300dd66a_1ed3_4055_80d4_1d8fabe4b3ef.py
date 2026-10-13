"""Independent 32px profile of bed.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '300dd66a-1ed3-4055-80d4-1d8fabe4b3ef'
SOURCE_PATH = 'pictographic-primitives/state/bed_300dd66a-1ed3-4055-80d4-1d8fabe4b3ef.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('300dd66a-1ed3-4055-80d4-1d8fabe4b3ef', 'pictographic-primitives/state/bed_300dd66a-1ed3-4055-80d4-1d8fabe4b3ef.svg'), ('95113cf8-8d4a-42f4-be40-9ff828544b7a', 'pictographic-primitives/symbol/bed_95113cf8-8d4a-42f4-be40-9ff828544b7a.svg'))
PROFILE_SOURCE_KEYS = ('solo/bed', 'solo/bed-symbol')
SOLO_SOURCE_ICON_IDS = ('bed', 'bed-symbol')
REFERENCE_EXPORT_SHA256 = '1367e16a7aaa6416e25a2ce6c9f814eda55b163a7f4fe47ac1ebdb65b9f80b42'

class DrawingContainerSymbol(Sub32):
    icon_id = 'bed-sub32-symbol'
    related_origin_icon_id = 'bed-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/bed-sub32'
    counterpart_icon_id = 'bed-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (2, 16))
        self.add_line('p1-r1-2', (2, 16), (2, 22))
        self.add_line('p1-r1-3', (2, 22), (2, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (30, 16), (30, 22))
        self.add_line('p2-r1-2', (30, 22), (30, 27))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 16), (30, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 22), (30, 22))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-3', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-2', 'p4-r1-1')
