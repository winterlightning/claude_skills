"""Shopping bag (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b586bc1-bc24-4649-9d1f-2c9c15a8444b'
SOURCE_PATH = 'icons-json/shopping/shopping bag_1b586bc1-bc24-4649-9d1f-2c9c15a8444b.json'
AUTHOR = 'json_to_solo'

class ShoppingBag(Solo48):
    icon_id = 'shopping-bag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shopping', 'bag')

    def build(self):
        self.add_line('sym-e0', (16, 23), (16, 17))
        self.add_line('sym-e1', (16, 17), (13, 17))
        self.add_arc('sym-e2', (13, 17), (11, 19), radius_x=2, sweep=False)
        self.add_line('sym-e3', (11, 19), (8, 40))
        self.add_line('sym-e4', (8, 40), (8, 41))
        self.add_arc('sym-e5', (8, 41), (10, 44), radius_x=4, sweep=False)
        self.add_arc('sym-e6', (10, 44), (11, 44), radius_x=1)
        self.add_line('sym-e7', (11, 44), (24, 44))
        self.add_line('sym-e8', (24, 44), (37, 44))
        self.add_line('sym-e9', (37, 44), (38, 44))
        self.add_arc('sym-e10', (38, 44), (40, 41), radius_x=4, sweep=False)
        self.add_line('sym-e11', (40, 41), (40, 40))
        self.add_line('sym-e12', (40, 40), (37, 19))
        self.add_arc('sym-e13', (37, 19), (35, 17), radius_x=2, sweep=False)
        self.add_line('sym-e14', (35, 17), (32, 17))
        self.add_line('sym-e15', (32, 17), (32, 23))
        self.add_line('sym-e16', (16, 17), (24, 17))
        self.add_line('sym-e17', (24, 17), (32, 17))
        self.add_line('sym-e18', (32, 17), (32, 11))
        self.add_line('sym-e19-1', (32, 11), (29, 6))
        self.add_arc('sym-e19-2', (29, 6), (24, 4), radius_x=8, sweep=False)
        self.add_arc('sym-e24-1', (24, 4), (19, 6), radius_x=8, sweep=False)
        self.add_arc('sym-e24-2', (19, 6), (16, 11), radius_x=8, sweep=False)
        self.add_line('sym-e25', (16, 11), (16, 17))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c1', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19-1', 'sym-e19-2', 'sym-e24-1', 'sym-e24-2', 'sym-e25', closed=True)
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
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
