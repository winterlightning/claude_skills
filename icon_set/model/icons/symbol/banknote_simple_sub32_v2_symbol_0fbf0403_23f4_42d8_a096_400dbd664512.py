"""Independent 32px profile of banknote-simple.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0fbf0403-23f4-42d8-a096-400dbd664512'
SOURCE_PATH = 'pictographic-primitives/symbol/money bill_0fbf0403-23f4-42d8-a096-400dbd664512.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0fbf0403-23f4-42d8-a096-400dbd664512', 'pictographic-primitives/symbol/money bill_0fbf0403-23f4-42d8-a096-400dbd664512.svg'), ('76664091-6ef6-44a2-8c4c-a2b2e41d7461', 'pictographic-primitives/symbol/cash card_76664091-6ef6-44a2-8c4c-a2b2e41d7461.svg'))
PROFILE_SOURCE_KEYS = ('solo/banknote-simple', 'solo/banknote-coin-mark')
SOLO_SOURCE_ICON_IDS = ('banknote-simple', 'banknote-coin-mark')
REFERENCE_EXPORT_SHA256 = '5d9498d5dfd55a394a8885d47b51d1c493a2d045e1141eaea4167a7c66c7162a'

class DrawingVariant2ContainerSymbol(Sub32):
    icon_id = 'banknote-simple-sub32-v2-symbol'
    related_origin_icon_id = 'banknote-simple-sub32-v2'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/banknote-simple-sub32-v2'
    counterpart_icon_id = 'banknote-simple-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, short_low), (30, short_low))
        self.add_line('p1-r1-2', (30, short_low), (30, short_high))
        self.add_line('p1-r1-3', (30, short_high), (2, short_high))
        self.add_line('p1-r1-4', (2, short_high), (2, short_low))
        self.add_line('p1-r1-5', (2, short_low), (2, short_low))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_arc('p2-r1-1', (11, 16), (21, 16), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (21, 16), (11, 16), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
