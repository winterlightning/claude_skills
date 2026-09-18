"""Independent 32px profile of arrow-bottom-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0ae4f1cf-6b9f-48d8-bd6d-83d0f2255432'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow bottom_0ae4f1cf-6b9f-48d8-bd6d-83d0f2255432.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0ae4f1cf-6b9f-48d8-bd6d-83d0f2255432', 'pictographic-primitives/symbol/arrow bottom_0ae4f1cf-6b9f-48d8-bd6d-83d0f2255432.svg'), ('cccc0ae2-455e-5543-acd2-86328a04cbec', 'pictographic-primitives/arrows/arrow button bottom 1_cccc0ae2-455e-5543-acd2-86328a04cbec.svg'))
PROFILE_SOURCE_KEYS = ('solo/arrow-bottom-symbol', 'solo/arrow-button-bottom-1')
SOLO_SOURCE_ICON_IDS = ('arrow-bottom-symbol', 'arrow-button-bottom-1')
REFERENCE_EXPORT_SHA256 = '9ec597e0f406140f8860ffa9d27a4143e7f8e33e585523ce83d74a6ec7f423d2'

class DrawingVariant3ContainerSymbol(Sub32):
    icon_id = 'arrow-bottom-symbol-sub32-v3-symbol'
    related_origin_icon_id = 'arrow-bottom-symbol-sub32-v3'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/arrow-bottom-symbol-sub32-v3'
    counterpart_icon_id = 'arrow-bottom-symbol-sub32-v3'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (16, short_high), (9, 16))
        self.add_line('p1-r1-2', (9, 16), (2, short_low))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, short_high), (23, 16))
        self.add_line('p2-r1-2', (23, 16), (30, short_low))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
