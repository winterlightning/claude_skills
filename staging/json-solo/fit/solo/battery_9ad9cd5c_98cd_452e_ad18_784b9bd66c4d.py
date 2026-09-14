"""Battery (photography), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ad9cd5c-98cd-452e-ad18-784b9bd66c4d'
SOURCE_PATH = 'icons-json/photography/battery_9ad9cd5c-98cd-452e-ad18-784b9bd66c4d.json'
AUTHOR = 'json_to_solo'

class Battery9ad9cd5c(Solo48):
    icon_id = 'battery-9ad9cd5c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('battery', 'photography')

    def build(self):
        self.add_line('sym-e0', (15, 12), (17, 12))
        self.add_line('sym-e1', (17, 12), (31, 12))
        self.add_line('sym-e2', (31, 12), (33, 12))
        self.add_line('sym-e3', (33, 12), (38, 12))
        self.add_arc('sym-e4', (38, 12), (40, 14), radius_x=3)
        self.add_line('sym-e6', (40, 14), (40, 16))
        self.add_arc('sym-e10', (40, 16), (40, 17), radius_x=23, sweep=False)
        self.add_arc('sym-e17', (40, 17), (40, 16), radius_x=23)
        self.add_arc('sym-e24', (40, 16), (40, 17), radius_x=23, sweep=False)
        self.add_line('sym-e28', (40, 17), (40, 19))
        self.add_arc('sym-e29', (40, 19), (40, 25), radius_x=25, sweep=False)
        self.add_line('sym-e30', (40, 25), (40, 42))
        self.add_arc('sym-e31', (40, 42), (38, 44), radius_x=2)
        self.add_line('sym-e32', (38, 44), (24, 44))
        self.add_line('sym-e33', (24, 44), (10, 44))
        self.add_arc('sym-e34', (10, 44), (8, 42), radius_x=2)
        self.add_line('sym-e35', (8, 42), (8, 25))
        self.add_line('sym-e36-1', (8, 25), (8, 24))
        self.add_line('sym-e36-2', (8, 24), (8, 19))
        self.add_line('sym-e37', (8, 19), (8, 17))
        self.add_line('sym-e41', (8, 17), (8, 16))
        self.add_line('sym-e45', (8, 16), (8, 14))
        self.add_arc('sym-e47', (8, 14), (10, 12), radius_x=3)
        self.add_line('sym-e48', (10, 12), (15, 12))
        self.add_line('sym-e52', (8, 17), (8, 16))
        self.add_line('sym-e59', (8, 16), (8, 17))
        self.add_arc('sym-e63', (17, 12), (19, 5), radius_x=7)
        self.add_arc('sym-e64', (19, 5), (20, 4), radius_x=2)
        self.add_line('sym-e66', (20, 4), (24, 4))
        self.add_line('sym-e67', (24, 4), (28, 4))
        self.add_arc('sym-e69', (28, 4), (29, 5), radius_x=2)
        self.add_arc('sym-e70', (29, 5), (31, 12), radius_x=7)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e10', 'sym-e17', 'sym-e24', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36-1', 'sym-e36-2', 'sym-e37', 'sym-e41', 'sym-e45', 'sym-e47', 'sym-e48', closed=True)
        self.add_contour('sym-c1', 'sym-e52', 'sym-e59', closed=True)
        self.add_contour('sym-c2', 'sym-e63', 'sym-e64', 'sym-e66', 'sym-e67', 'sym-e69', 'sym-e70')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
