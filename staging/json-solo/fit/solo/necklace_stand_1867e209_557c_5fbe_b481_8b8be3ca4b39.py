"""Batch-01/necklace stand (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1867e209-557c-5fbe-b481-8b8be3ca4b39'
SOURCE_PATH = 'icons-json/accessories/batch-01/necklace stand_1867e209-557c-5fbe-b481-8b8be3ca4b39.json'
AUTHOR = 'json_to_solo'

class Batch01NecklaceStand(Solo48):
    icon_id = 'batch-01-necklace-stand'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'necklace', 'stand', 'accessories')

    def build(self):
        self.add_line('sym-e0', (11, 40), (15, 40))
        self.add_line('sym-e1', (15, 40), (33, 40))
        self.add_line('sym-e2', (33, 40), (37, 40))
        self.add_arc('sym-e3', (24, 26), (34, 21), radius_x=12, sweep=False)
        self.add_arc('sym-e4', (34, 21), (37, 16), radius_x=23, sweep=False)
        self.add_line('sym-e5', (37, 16), (34, 17))
        self.add_arc('sym-e6', (34, 17), (24, 20), radius_x=19)
        self.add_arc('sym-e7', (24, 20), (14, 17), radius_x=19)
        self.add_line('sym-e8', (14, 17), (11, 16))
        self.add_arc('sym-e9', (11, 16), (14, 21), radius_x=23, sweep=False)
        self.add_arc('sym-e10', (14, 21), (24, 26), radius_x=12, sweep=False)
        self.add_arc('sym-e11', (33, 40), (39, 32), radius_x=14)
        self.add_arc('sym-e12', (39, 32), (44, 26), radius_x=10, sweep=False)
        self.add_line('sym-e15', (44, 26), (44, 20))
        self.add_line('sym-e16', (44, 20), (44, 19))
        self.add_arc('sym-e17', (44, 19), (37, 16), radius_x=6, sweep=False)
        self.add_line('sym-e18', (37, 16), (36, 15))
        self.add_arc('sym-e19', (36, 15), (33, 12), radius_x=6)
        self.add_line('sym-e20', (33, 12), (31, 8))
        self.add_line('sym-e21', (31, 8), (30, 8))
        self.add_line('sym-e22', (30, 8), (25, 8))
        self.add_arc('sym-e23', (25, 8), (24, 8), radius_x=41)
        self.add_arc('sym-e24', (24, 8), (23, 8), radius_x=39)
        self.add_line('sym-e25', (23, 8), (18, 8))
        self.add_line('sym-e26', (18, 8), (17, 8))
        self.add_line('sym-e27', (17, 8), (15, 12))
        self.add_arc('sym-e28', (15, 12), (12, 15), radius_x=7)
        self.add_line('sym-e29', (12, 15), (11, 16))
        self.add_arc('sym-e30', (11, 16), (4, 19), radius_x=6, sweep=False)
        self.add_line('sym-e31', (4, 19), (4, 20))
        self.add_line('sym-e32', (4, 20), (4, 26))
        self.add_arc('sym-e35', (4, 26), (9, 32), radius_x=10, sweep=False)
        self.add_arc('sym-e36', (9, 32), (15, 40), radius_x=14)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', closed=True)
        self.add_contour('sym-c2', 'sym-e11', 'sym-e12', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e35', 'sym-e36')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
