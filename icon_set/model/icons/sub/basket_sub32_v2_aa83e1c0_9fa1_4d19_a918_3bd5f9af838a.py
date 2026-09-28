# Repair: shared short-axis extrema retain the full source composition on the legal SUB32 envelope.
"""Independent 32px profile of basket.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'aa83e1c0-9fa1-4d19-a918-3bd5f9af838a'
SOURCE_PATH = 'pictographic-primitives/symbol/basket_aa83e1c0-9fa1-4d19-a918-3bd5f9af838a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('aa83e1c0-9fa1-4d19-a918-3bd5f9af838a', 'pictographic-primitives/symbol/basket_aa83e1c0-9fa1-4d19-a918-3bd5f9af838a.svg'), ('790ba4c2-a8e0-42c1-a644-383157d2d39b', 'pictographic-primitives/spas/cart_790ba4c2-a8e0-42c1-a644-383157d2d39b.svg'))
PROFILE_SOURCE_KEYS = ('solo/basket', 'solo/cart-spas')
SOLO_SOURCE_ICON_IDS = ('basket', 'cart-spas')
REFERENCE_EXPORT_SHA256 = 'f4a50091acf6871506137f4677997823d3dcffd98e55c6abbb8ebe0758235806'

class DrawingVariant2(Sub32):
    icon_id = 'basket-sub32-v2'
    variant_label = 'Repair 32px envelope'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, 13), (8, 13))
        self.add_line('p1-r1-2', (8, 13), (24, 13))
        self.add_line('p1-r1-3', (24, 13), (30, 13))
        self.add_line('p1-r1-4', (30, 13), (26, short_high))
        self.add_line('p1-r1-5', (26, short_high), (6, short_high))
        self.add_line('p1-r1-6', (6, short_high), (2, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (8, 13), (12, short_low))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (24, 13), (20, short_low))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
