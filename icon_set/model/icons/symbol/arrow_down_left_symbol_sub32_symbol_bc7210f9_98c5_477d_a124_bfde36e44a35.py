"""Independent 32px profile of arrow-down-left-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'bc7210f9-98c5-477d-a124-bfde36e44a35'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow down left_bc7210f9-98c5-477d-a124-bfde36e44a35.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bc7210f9-98c5-477d-a124-bfde36e44a35', 'pictographic-primitives/symbol/arrow down left_bc7210f9-98c5-477d-a124-bfde36e44a35.svg'), ('4b844c7f-1011-5ebf-a235-17cf6f0014b7', 'pictographic-primitives/interface-essential/keyboard arrow bottom left_4b844c7f-1011-5ebf-a235-17cf6f0014b7.svg'))
PROFILE_SOURCE_KEYS = ('solo/arrow-down-left-symbol', 'solo/keyboard-arrow-bottom-left')
SOLO_SOURCE_ICON_IDS = ('arrow-down-left-symbol', 'keyboard-arrow-bottom-left')
REFERENCE_EXPORT_SHA256 = '435443b5987fa20e86a1251bce8f95f818bb1bf270fa25a8e23c3ea640d327de'

class DrawingContainerSymbol(Sub32):
    icon_id = 'arrow-down-left-symbol-sub32-symbol'
    related_origin_icon_id = 'arrow-down-left-symbol-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/arrow-down-left-symbol-sub32'
    counterpart_icon_id = 'arrow-down-left-symbol-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 2), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 17), (2, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (15, 30), (2, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
