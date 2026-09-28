"""Independent 32px profile of forward-arrow.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '798dac3e-8c58-4024-b8ae-ece2107e6007'
SOURCE_PATH = 'pictographic-primitives/symbol/forward arrow_798dac3e-8c58-4024-b8ae-ece2107e6007.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('798dac3e-8c58-4024-b8ae-ece2107e6007', 'pictographic-primitives/symbol/forward arrow_798dac3e-8c58-4024-b8ae-ece2107e6007.svg'),)
PROFILE_SOURCE_KEYS = ('solo/forward-arrow',)
SOLO_SOURCE_ICON_IDS = ('forward-arrow',)
REFERENCE_EXPORT_SHA256 = '97c732dddcbcac10acff0d35a93a368f785b31edc1c20edf99a0f560951df346'

class DrawingVariant2(Sub32):
    icon_id = 'forward-arrow-sub32-v2'
    related_origin_icon_id = 'forward-arrow-sub32'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (20, 2), (short_high, 10))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (short_low, 30), (short_low, 24))
        self.add_arc('p2-r1-2', (4, 24), (18, 10), radius_x=14, radius_y=14, sweep=True)
        self.add_line('p2-r1-6', (18, 10), (28, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (20, 18), (short_high, 10))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-6')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-6', 'p3-r1-1')
