# Centerline repair: continuous intended straight runs and matched tangent directions.
# Variant of cart-e3de8236-sub32-v2; parent file remains unchanged.
"""Independent 32px profile of cart-e3de8236.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e3de8236-b5a7-43f9-ad90-542d179369e3'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_e3de8236-b5a7-43f9-ad90-542d179369e3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e3de8236-b5a7-43f9-ad90-542d179369e3', 'pictographic-primitives/shopping/cart_e3de8236-b5a7-43f9-ad90-542d179369e3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cart-e3de8236',)
SOLO_SOURCE_ICON_IDS = ('cart-e3de8236',)
REFERENCE_EXPORT_SHA256 = '82923987077b2e5e26e4b136d709f1d0f244cd358f13409fb1c1895aa1db7c3f'

class DrawingVariant3(Sub32):
    icon_id = 'cart-e3de8236-sub32-v3'
    variant_of = 'cart-e3de8236-sub32-v2'
    variant_label = 'Continuous centerlines'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        (short_low, short_high) = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, 13), (8, 13))
        self.add_line('p1-r1-2', (8, 13), (24, 13))
        self.add_line('p1-r1-3', (24, 13), (30, 13))
        self.add_line('p1-r1-4', (30, 13), (26, 25))
        self.add_bezier('p1-r1-5', (26, 25), ((25, short_high), (24, short_high), (23, short_high)))
        self.add_line('p1-r1-6', (23, short_high), (9, short_high))
        self.add_bezier('p1-r1-7', (9, short_high), ((8, short_high), (7, short_high), (6, 25)))
        self.add_line('p1-r1-8', (6, 25), (2, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_arc('p2-r1-1', (8, 13), (24, 13), radius_x=8, radius_y=9, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
