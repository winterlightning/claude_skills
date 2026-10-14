"""Independent 32px profile of warehouse-shipping.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '8f5402f0-5566-4c6d-ac0c-c86e0360848e'
SOURCE_PATH = 'pictographic-primitives/shipping/warehouse_8f5402f0-5566-4c6d-ac0c-c86e0360848e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8f5402f0-5566-4c6d-ac0c-c86e0360848e', 'pictographic-primitives/shipping/warehouse_8f5402f0-5566-4c6d-ac0c-c86e0360848e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/warehouse-shipping',)
SOLO_SOURCE_ICON_IDS = ('warehouse-shipping',)
REFERENCE_EXPORT_SHA256 = 'adbb41eda7891fb79a7fd604778f1345c955d7fd89b4344c9b1786f5eb0d53ba'

class Drawing(Sub32):
    icon_id = 'warehouse-shipping-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shipping'
    categories = ('primitives', 'shipping')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Warehouse: pitched roof with rounded eaves, square base, a wide door 4 units clear of the walls.
        self.add_line('w-1', (2, 30), (2, 15))
        self.add_bezier('w-2', (2, 15), ((2, 12.333333), (3, 12.333333), (4, 11)))
        self.add_line('w-3', (4, 11), (16, 2))
        self.add_line('w-4', (16, 2), (28, 11))
        self.add_bezier('w-5', (28, 11), ((29, 12.333333), (30, 12.333333), (30, 15)))
        self.add_line('w-6', (30, 15), (30, 30))
        self.add_line('w-7', (30, 30), (2, 30))
        self.add_contour('house', 'w-1', 'w-2', 'w-3', 'w-4', 'w-5', 'w-6', 'w-7')
        self.add_polyline('door', (10, 30), (10, 18), (22, 18), (22, 30))
        self.relate('connect', 'house', 'door')
