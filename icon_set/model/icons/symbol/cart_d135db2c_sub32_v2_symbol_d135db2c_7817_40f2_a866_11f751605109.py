"""Independent 32px profile of cart-d135db2c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'd135db2c-7817-40f2-a866-11f751605109'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_d135db2c-7817-40f2-a866-11f751605109.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d135db2c-7817-40f2-a866-11f751605109', 'pictographic-primitives/shopping/cart_d135db2c-7817-40f2-a866-11f751605109.svg'), ('b9e134df-638b-471e-a6c6-fbdef9c3658e', 'pictographic-primitives/shopping/cart_b9e134df-638b-471e-a6c6-fbdef9c3658e.svg'), ('aa216d16-932a-4199-a750-e243701b34d3', 'pictographic-primitives/shopping/cart_aa216d16-932a-4199-a750-e243701b34d3.svg'), ('fa3ca15f-b005-4f2a-a7fa-abd754bde34f', 'pictographic-primitives/shopping/cart_fa3ca15f-b005-4f2a-a7fa-abd754bde34f.svg'))
PROFILE_SOURCE_KEYS = ('solo/cart-d135db2c', 'solo/cart-shopping', 'solo/shopping-cart-extended-handle', 'solo/shopping-cart-shallow-basket')
SOLO_SOURCE_ICON_IDS = ('cart-d135db2c', 'cart-shopping', 'shopping-cart-extended-handle', 'shopping-cart-shallow-basket')
REFERENCE_EXPORT_SHA256 = '366dfbd16841d0593302c2280eb730c8dfc8a3c1cab6c6497eeb556d47f165bd'

class DrawingVariant2ContainerSymbol(Sub32):
    icon_id = 'cart-d135db2c-sub32-v2-symbol'
    related_origin_icon_id = 'cart-d135db2c-sub32-v2'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/cart-d135db2c-sub32-v2'
    counterpart_icon_id = 'cart-d135db2c-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        short_axis = 16
        short_half_span = 12
        short_low, short_high = (short_axis - short_half_span, short_axis + short_half_span)
        self.add_line('p1-r1-1', (2, 10), (27, 10))
        self.add_line('p1-r1-2', (27, 10), (22, 20))
        self.add_line('p1-r1-3', (22, 20), (8, 20))
        self.add_line('p1-r1-4', (8, 20), (2, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (27, 10), (30, short_low))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (10, short_high), (10, short_high))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (20, short_high), (20, short_high))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
