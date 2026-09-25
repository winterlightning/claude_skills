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
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shipping'
    categories = ('primitives', 'shipping')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 24), (2, 15))
        self.add_bezier('p1-r1-2', (2, 15), ((2, 13), (3, 13), (4, 12)))
        self.add_line('p1-r1-3', (4, 12), (16, 5))
        self.add_line('p1-r1-4', (16, 5), (28, 12))
        self.add_bezier('p1-r1-5', (28, 12), ((29, 13), (30, 13), (30, 15)))
        self.add_line('p1-r1-6', (30, 15), (30, 24))
        self.add_arc('p1-r1-7', (30, 24), (27, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (27, 27), (22, 27))
        self.add_line('p1-r1-9', (22, 27), (10, 27))
        self.add_line('p1-r1-10', (10, 27), (5, 27))
        self.add_arc('p1-r1-11', (5, 27), (2, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_line('p2-r1-1', (10, 27), (10, 22))
        self.add_line('p2-r1-2', (10, 22), (10, 16))
        self.add_line('p2-r1-3', (10, 16), (22, 16))
        self.add_line('p2-r1-4', (22, 16), (22, 22))
        self.add_line('p2-r1-5', (22, 22), (22, 27))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (10, 22), (22, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-8', 'p2-r1-5')
        self.relate('connect', 'p1-r1-9', 'p2-r1-1')
        self.relate('connect', 'p1-r1-9', 'p2-r1-5')
        self.relate('connect', 'p1-r1-10', 'p2-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
        self.relate('connect', 'p2-r1-4', 'p3-r1-1')
        self.relate('connect', 'p2-r1-5', 'p3-r1-1')
