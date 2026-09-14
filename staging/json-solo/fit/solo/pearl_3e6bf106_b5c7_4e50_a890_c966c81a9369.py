"""Pearl (products), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e6bf106-b5c7-4e50-a890-c966c81a9369'
SOURCE_PATH = 'icons-json/products/pearl_3e6bf106-b5c7-4e50-a890-c966c81a9369.json'
AUTHOR = 'json_to_solo'

class PearlProducts(Solo48):
    icon_id = 'pearl-products'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'products'
    aliases = ()
    keywords = ('pearl', 'products')

    def build(self):
        self.add_arc('sym-e0', (19, 25), (29, 25), radius_x=5)
        self.add_arc('sym-e1', (29, 25), (19, 25), radius_x=5)
        self.add_line('sym-e2', (24, 44), (23, 44))
        self.add_arc('sym-e3', (23, 44), (11, 39), radius_x=17)
        self.add_arc('sym-e4', (11, 39), (8, 35), radius_x=15)
        self.add_line('sym-e5', (8, 35), (8, 33))
        self.add_arc('sym-e6', (8, 33), (11, 35), radius_x=19, sweep=False)
        self.add_arc('sym-e7', (11, 35), (17, 36), radius_x=27, sweep=False)
        self.add_arc('sym-e8', (17, 36), (24, 36), radius_x=63)
        self.add_arc('sym-e9', (24, 36), (31, 36), radius_x=63)
        self.add_line('sym-e10', (31, 36), (37, 35))
        self.add_line('sym-e11', (37, 35), (40, 33))
        self.add_arc('sym-e12', (40, 33), (40, 35), radius_x=35, sweep=False)
        self.add_line('sym-e13', (40, 35), (37, 39))
        self.add_arc('sym-e14', (37, 39), (25, 44), radius_x=17)
        self.add_arc('sym-e15', (25, 44), (24, 44), radius_x=29, sweep=False)
        self.add_line('sym-e16', (8, 33), (8, 31))
        self.add_arc('sym-e18', (8, 31), (14, 28), radius_x=11)
        self.add_line('sym-e19', (14, 28), (19, 27))
        self.add_line('sym-e20', (19, 27), (12, 22))
        self.add_arc('sym-e21', (12, 22), (8, 16), radius_x=10)
        self.add_line('sym-e22', (8, 16), (8, 15))
        self.add_arc('sym-e24', (8, 15), (9, 13), radius_x=6)
        self.add_arc('sym-e25', (9, 13), (14, 7), radius_x=8)
        self.add_line('sym-e26', (14, 7), (16, 7))
        self.add_arc('sym-e27', (16, 7), (17, 7), radius_x=5)
        self.add_arc('sym-e28', (17, 7), (19, 6), radius_x=46, sweep=False)
        self.add_arc('sym-e29', (19, 6), (23, 4), radius_x=8)
        self.add_arc('sym-e30', (23, 4), (24, 4), radius_x=69, sweep=False)
        self.add_arc('sym-e33', (24, 4), (25, 4), radius_x=76, sweep=False)
        self.add_arc('sym-e34', (25, 4), (29, 6), radius_x=8)
        self.add_arc('sym-e35', (29, 6), (31, 7), radius_x=45, sweep=False)
        self.add_arc('sym-e36', (31, 7), (32, 7), radius_x=5)
        self.add_arc('sym-e37', (32, 7), (34, 7), radius_x=5, sweep=False)
        self.add_arc('sym-e38', (34, 7), (39, 13), radius_x=8)
        self.add_arc('sym-e39', (39, 13), (40, 15), radius_x=6)
        self.add_arc('sym-e41', (40, 15), (40, 16), radius_x=23, sweep=False)
        self.add_arc('sym-e42', (40, 16), (36, 22), radius_x=10)
        self.add_line('sym-e43', (36, 22), (29, 27))
        self.add_line('sym-e44', (29, 27), (34, 28))
        self.add_arc('sym-e45', (34, 28), (40, 31), radius_x=11)
        self.add_line('sym-e47', (40, 31), (40, 33))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
        self.add_contour('sym-c2', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', 'sym-e37', 'sym-e38', 'sym-e39', 'sym-e41', 'sym-e42', 'sym-e43', 'sym-e44', 'sym-e45', 'sym-e47')
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
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
