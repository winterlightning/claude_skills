"""Warehouse (shipping), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f5402f0-5566-4c6d-ac0c-c86e0360848e'
SOURCE_PATH = 'icons-json/shipping/warehouse_8f5402f0-5566-4c6d-ac0c-c86e0360848e.json'
AUTHOR = 'json_to_solo'

class Warehouse8f5402f0(Solo48):
    icon_id = 'warehouse-8f5402f0'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('warehouse', 'shipping')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 6))
        self.add_line('sym-e1', (24, 6), (7, 17))
        self.add_bezier('sym-e2', (7, 17), ((6.755, 17.344), (6.115, 18.583), (6, 19)))
        self.add_bezier('sym-e3', (6, 19), ((6, 19.425), (6.139, 18.542), (6, 19)))
        self.add_line('sym-e4', (6, 19), (6, 42))
        self.add_line('sym-e5', (6, 42), (24, 42))
        self.add_line('sym-e6', (24, 42), (42, 42))
        self.add_line('sym-e7', (42, 42), (42, 19))
        self.add_bezier('sym-e8', (42, 19), ((41.861, 18.542), (42, 19.425), (42, 19)))
        self.add_bezier('sym-e9', (42, 19), ((41.885, 18.583), (41.245, 17.344), (41, 17)))
        self.add_line('sym-e10', (41, 17), (24, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', closed=True)
