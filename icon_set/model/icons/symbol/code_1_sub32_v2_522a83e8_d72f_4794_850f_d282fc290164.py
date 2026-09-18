"""Independent 32px profile of code-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '522a83e8-d72f-4794-850f-d282fc290164'
SOURCE_PATH = 'pictographic-primitives/symbol/code 1_522a83e8-d72f-4794-850f-d282fc290164.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('522a83e8-d72f-4794-850f-d282fc290164', 'pictographic-primitives/symbol/code 1_522a83e8-d72f-4794-850f-d282fc290164.svg'),)
PROFILE_SOURCE_KEYS = ('solo/code-1',)
SOLO_SOURCE_ICON_IDS = ('code-1',)
REFERENCE_EXPORT_SHA256 = '6f486b7528e25d1fcefd50505267139ac491c63b459423cb928405bffb31b5a7'

class DrawingVariant2(Sub32):
    icon_id = 'code-1-sub32-v2'
    related_origin_icon_id = 'code-1-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, short_low), (11, 16))
        self.add_line('p1-r1-2', (11, 16), (2, short_high))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (19, 20), (30, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
