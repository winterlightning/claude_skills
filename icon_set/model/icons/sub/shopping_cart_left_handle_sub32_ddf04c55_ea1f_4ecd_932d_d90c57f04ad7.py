"""Independent 32px profile of shopping-cart-left-handle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'ddf04c55-ea1f-4ecd-932d-d90c57f04ad7'
SOURCE_PATH = 'pictographic-primitives/shopping/cart_ddf04c55-ea1f-4ecd-932d-d90c57f04ad7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ddf04c55-ea1f-4ecd-932d-d90c57f04ad7', 'pictographic-primitives/shopping/cart_ddf04c55-ea1f-4ecd-932d-d90c57f04ad7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shopping-cart-left-handle',)
SOLO_SOURCE_ICON_IDS = ('shopping-cart-left-handle',)
REFERENCE_EXPORT_SHA256 = 'b120d56527394bc2eda1d4b5623ec3a12f293089d0909a90fd821a80ca0d84b2'

class Drawing(Sub32):
    icon_id = 'shopping-cart-left-handle-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/shopping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (6, 5))
        self.add_line('p1-r1-2', (6, 5), (8, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (8, 10), (30, 10))
        self.add_line('p2-r1-2', (30, 10), (29, 16))
        self.add_arc('p2-r1-3', (29, 16), (24, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (24, 20), (10, 20))
        self.add_line('p2-r1-5', (10, 20), (8, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (11, 27), (11, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (24, 27), (24, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-5')
