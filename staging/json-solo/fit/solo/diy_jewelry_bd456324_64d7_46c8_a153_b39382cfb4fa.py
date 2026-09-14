"""Batch-01/diy jewelry (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd456324-64d7-46c8-a153-b39382cfb4fa'
SOURCE_PATH = 'icons-json/accessories/batch-01/diy jewelry_bd456324-64d7-46c8-a153-b39382cfb4fa.json'
AUTHOR = 'json_to_solo'

class Batch01DiyJewelry(Solo48):
    icon_id = 'batch-01-diy-jewelry'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'diy', 'jewelry', 'accessories')

    def build(self):
        self.add_arc('sym-e0', (30, 32), (38, 32), radius_x=4, radius_y=3)
        self.add_arc('sym-e1', (38, 32), (30, 32), radius_x=4, radius_y=3)
        self.add_arc('sym-e2', (18, 32), (10, 32), radius_x=4, radius_y=3, sweep=False)
        self.add_arc('sym-e3', (10, 32), (18, 32), radius_x=4, radius_y=3, sweep=False)
        self.add_line('sym-e4', (37, 8), (38, 10))
        self.add_line('sym-e5', (38, 10), (39, 12))
        self.add_arc('sym-e6', (39, 12), (44, 16), radius_x=5)
        self.add_line('sym-e7', (44, 16), (44, 17))
        self.add_arc('sym-e9', (44, 17), (42, 22), radius_x=12)
        self.add_line('sym-e10', (42, 22), (38, 28))
        self.add_line('sym-e11', (38, 28), (37, 29))
        self.add_line('sym-e12', (24, 29), (26, 29))
        self.add_line('sym-e13', (26, 29), (28, 30))
        self.add_line('sym-e14', (28, 30), (30, 32))
        self.add_line('sym-e16', (30, 32), (30, 36))
        self.add_arc('sym-e17', (30, 36), (24, 40), radius_x=7)
        self.add_arc('sym-e20', (24, 40), (18, 36), radius_x=7)
        self.add_arc('sym-e21', (18, 36), (18, 32), radius_x=11)
        self.add_line('sym-e23', (18, 32), (20, 30))
        self.add_line('sym-e24', (20, 30), (22, 29))
        self.add_line('sym-e25', (22, 29), (24, 29))
        self.add_line('sym-e26', (11, 8), (10, 10))
        self.add_line('sym-e27', (10, 10), (9, 12))
        self.add_arc('sym-e28', (9, 12), (4, 16), radius_x=6, sweep=False)
        self.add_line('sym-e29', (4, 16), (4, 17))
        self.add_arc('sym-e31', (4, 17), (6, 22), radius_x=13, sweep=False)
        self.add_line('sym-e32', (6, 22), (10, 28))
        self.add_line('sym-e33', (10, 28), (11, 29))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c3', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e20', 'sym-e21', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
        self.add_contour('sym-c4', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e31', 'sym-e32', 'sym-e33')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
