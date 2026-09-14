"""Warehouse (shipping), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62aa0b8f-c53c-4172-b253-31b1a4da82d8'
SOURCE_PATH = 'icons-json/shipping/warehouse_62aa0b8f-c53c-4172-b253-31b1a4da82d8.json'
AUTHOR = 'json_to_solo'

class Warehouse62aa0b8f(Solo48):
    icon_id = 'warehouse-62aa0b8f'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('warehouse', 'shipping')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 6))
        self.add_line('sym-e1', (24, 6), (7, 17))
        self.add_arc('sym-e2', (7, 17), (6, 19), radius_x=4, sweep=False)
        self.add_line('sym-e4', (6, 19), (6, 42))
        self.add_line('sym-e5', (6, 42), (24, 42))
        self.add_line('sym-e6', (24, 42), (42, 42))
        self.add_line('sym-e7', (42, 42), (42, 19))
        self.add_line('sym-e9', (42, 19), (41, 17))
        self.add_line('sym-e10', (41, 17), (24, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', closed=True)
