"""Independent 32px profile of arrow-down-arrows.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'ef18ef0e-e836-4934-9efb-25902b8f8869'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow down_ef18ef0e-e836-4934-9efb-25902b8f8869.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ef18ef0e-e836-4934-9efb-25902b8f8869', 'pictographic-primitives/arrows/arrow down_ef18ef0e-e836-4934-9efb-25902b8f8869.svg'), ('b6a9ec80-0591-424e-824e-f6719ae172f4', 'pictographic-primitives/symbol/arrow thin bottom_b6a9ec80-0591-424e-824e-f6719ae172f4.svg'), ('da8197be-3886-4dca-a884-f78ecdff8eaf', 'pictographic-primitives/interface-essential/keyboard arrow down_da8197be-3886-4dca-a884-f78ecdff8eaf.svg'))
PROFILE_SOURCE_KEYS = ('solo/arrow-down-arrows', 'solo/arrow-thin-bottom-symbol', 'solo/keyboard-arrow-down')
SOLO_SOURCE_ICON_IDS = ('arrow-down-arrows', 'arrow-thin-bottom-symbol', 'keyboard-arrow-down')
REFERENCE_EXPORT_SHA256 = '7a0fc5acf3ee523035693a370dc0eb7566dc99f7fded0229e8193db335717983'

class DrawingVariant2ContainerSymbol(Sub32):
    icon_id = 'arrow-down-arrows-sub32-v2-symbol'
    related_origin_icon_id = 'arrow-down-arrows-sub32-v2'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/arrow-down-arrows-sub32-v2'
    counterpart_icon_id = 'arrow-down-arrows-sub32-v2'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'arrows'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (short_low, 21), (16, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (16, 30), (16, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 30), (short_high, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
