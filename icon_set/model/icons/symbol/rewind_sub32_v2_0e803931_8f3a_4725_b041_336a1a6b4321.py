"""Independent 32px profile of rewind.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '0e803931-8f3a-4725-b041-336a1a6b4321'
SOURCE_PATH = 'pictographic-primitives/interface-essential/rewind_0e803931-8f3a-4725-b041-336a1a6b4321.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0e803931-8f3a-4725-b041-336a1a6b4321', 'pictographic-primitives/interface-essential/rewind_0e803931-8f3a-4725-b041-336a1a6b4321.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rewind',)
SOLO_SOURCE_ICON_IDS = ('rewind',)
REFERENCE_EXPORT_SHA256 = '191baa892d21d7204ad9e0abdf469105b2de9e7630b49fa1b32e9745c6c0054f'

class DrawingVariant2(Sub32):
    icon_id = 'rewind-sub32-v2'
    related_origin_icon_id = 'rewind-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (14, 13), (2, short_low))
        self.add_line('p1-r1-2', (2, short_low), (2, short_high))
        self.add_line('p1-r1-3', (2, short_high), (14, 19))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (30, 16), (14, 6))
        self.add_line('p2-r1-2', (14, 6), (14, 26))
        self.add_line('p2-r1-3', (14, 26), (30, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
