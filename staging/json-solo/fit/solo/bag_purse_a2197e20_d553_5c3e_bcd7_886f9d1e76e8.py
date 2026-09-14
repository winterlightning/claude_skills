"""Batch-03/bag purse (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2197e20-d553-5c3e-bcd7-886f9d1e76e8'
SOURCE_PATH = 'icons-json/accessories/batch-03/bag purse_a2197e20-d553-5c3e-bcd7-886f9d1e76e8.json'
AUTHOR = 'json_to_solo'

class Batch03BagPurse(Solo48):
    icon_id = 'batch-03-bag-purse'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'bag', 'purse', 'accessories')

    def build(self):
        self.add_arc('sym-e0', (28, 31), (25, 29), radius_x=2, sweep=False)
        self.add_arc('sym-e1', (25, 29), (24, 29), radius_x=77, sweep=False)
        self.add_arc('sym-e4', (24, 29), (23, 29), radius_x=76, sweep=False)
        self.add_arc('sym-e5', (23, 29), (20, 31), radius_x=2, sweep=False)
        self.add_arc('sym-e6', (20, 31), (24, 34), radius_x=3, sweep=False)
        self.add_arc('sym-e7', (24, 34), (28, 31), radius_x=3, sweep=False)
        self.add_line('sym-e8', (28, 31), (32, 31))
        self.add_arc('sym-e9', (32, 31), (40, 26), radius_x=8, sweep=False)
        self.add_line('sym-e10', (40, 26), (40, 22))
        self.add_arc('sym-e11', (40, 22), (35, 16), radius_x=6, sweep=False)
        self.add_line('sym-e12', (35, 16), (33, 16))
        self.add_line('sym-e13', (33, 16), (24, 16))
        self.add_line('sym-e14', (24, 16), (15, 16))
        self.add_line('sym-e15', (15, 16), (13, 16))
        self.add_arc('sym-e16', (13, 16), (8, 22), radius_x=6, sweep=False)
        self.add_line('sym-e17', (8, 22), (8, 26))
        self.add_arc('sym-e18', (8, 26), (16, 31), radius_x=8, sweep=False)
        self.add_line('sym-e19', (16, 31), (20, 31))
        self.add_line('sym-e20', (33, 16), (33, 13))
        self.add_arc('sym-e21', (33, 13), (26, 6), radius_x=8, sweep=False)
        self.add_line('sym-e22', (26, 6), (25, 6))
        self.add_line('sym-e23', (25, 6), (24, 6))
        self.add_line('sym-e26', (24, 6), (23, 6))
        self.add_line('sym-e27', (23, 6), (22, 6))
        self.add_arc('sym-e28', (22, 6), (15, 13), radius_x=8, sweep=False)
        self.add_arc('sym-e29', (15, 13), (15, 16), radius_x=18, sweep=False)
        self.add_line('sym-e30', (40, 26), (42, 34))
        self.add_line('sym-e31', (42, 34), (42, 36))
        self.add_line('sym-e32', (42, 36), (42, 37))
        self.add_arc('sym-e33', (42, 37), (35, 42), radius_x=8)
        self.add_line('sym-e34', (35, 42), (24, 42))
        self.add_line('sym-e35', (24, 42), (13, 42))
        self.add_arc('sym-e36', (13, 42), (6, 37), radius_x=8)
        self.add_line('sym-e37', (6, 37), (6, 36))
        self.add_line('sym-e38', (6, 36), (6, 34))
        self.add_line('sym-e39', (6, 34), (8, 26))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.add_contour('sym-c1', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29')
        self.add_contour('sym-c2', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', 'sym-e37', 'sym-e38', 'sym-e39')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
