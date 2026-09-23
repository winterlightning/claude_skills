# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of glass-drinks.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3ad0cd10-bf8c-4b51-9e81-06a67e3d6f68'
SOURCE_PATH = 'pictographic-primitives/drinks/glass_3ad0cd10-bf8c-4b51-9e81-06a67e3d6f68.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3ad0cd10-bf8c-4b51-9e81-06a67e3d6f68', 'pictographic-primitives/drinks/glass_3ad0cd10-bf8c-4b51-9e81-06a67e3d6f68.svg'),)
PROFILE_SOURCE_KEYS = ('solo/glass-drinks',)
SOLO_SOURCE_ICON_IDS = ('glass-drinks',)
REFERENCE_EXPORT_SHA256 = '662a8a79c3d9b0d8ce5e0b122772975def9dc35523a0ef12cfa1da0319e642f0'

class DrawingVariant2(Sub32):
    icon_id = 'glass-drinks-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'drinks'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (short_low, 8), (short_low, 2))
        self.add_line('p1-r1-2', (short_low, 2), (short_high, 2))
        self.add_line('p1-r1-3', (short_high, 2), (short_high, 8))
        self.add_arc('p1-r1-4', (short_high, 8), (16, 19), radius_x=12, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (16, 19), (short_low, 8), radius_x=12, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (16, 19), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (9, 30), (16, 30))
        self.add_line('p3-r1-2', (16, 30), (23, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-2')
