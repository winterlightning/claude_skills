# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of cart-e7cacb27.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e7cacb27-40ca-4398-ba88-df122b223505'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_e7cacb27-40ca-4398-ba88-df122b223505.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e7cacb27-40ca-4398-ba88-df122b223505', 'pictographic-primitives/shopping/cart_e7cacb27-40ca-4398-ba88-df122b223505.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cart-e7cacb27',)
SOLO_SOURCE_ICON_IDS = ('cart-e7cacb27',)
REFERENCE_EXPORT_SHA256 = '235d3a2457088956e887d8e02fa7ce2412de05c17e87d7e1dd409c16788f9591'

class DrawingVariant2(Sub32):
    icon_id = 'cart-e7cacb27-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shopping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (8, 10), (30, 10))
        self.add_line('p1-r1-2', (30, 10), (26, 20))
        self.add_line('p1-r1-3', (26, 20), (10, 20))
        self.add_line('p1-r1-4', (10, 20), (8, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, short_low), (6, short_low))
        self.add_line('p2-r1-2', (6, short_low), (8, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (10, short_high), (10, short_high))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (20, short_high), (20, short_high))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-4', 'p2-r1-2')
