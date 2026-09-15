"""Shop (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '36560de1-1707-4464-8a11-ce1847210523'
SOURCE_PATH = 'pictographic-primitives/shopping/shop_36560de1-1707-4464-8a11-ce1847210523.svg'
AUTHOR = 'gpt-6'

class ShopShopping(Solo48):
    icon_id = 'shop-shopping'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shop', 'shopping')

    def build(self):
        self.add_line('sym-e0', (24, 40), (41, 40))
        self.add_line('sym-e1', (41, 40), (41, 22))
        self.add_arc('sym-e2', (41, 22), (36, 22), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e3', (36, 22), (34, 20))
        self.add_arc('sym-e4', (34, 20), (32, 22), radius_x=23, radius_y=23, large_arc=False, sweep=False)
        self.add_arc('sym-e5', (32, 22), (26, 22), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e6', (26, 22), (24, 20))
        self.add_line('sym-e7', (24, 20), (22, 22))
        self.add_arc('sym-e8', (22, 22), (16, 22), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('sym-e9', (16, 22), (14, 20), radius_x=24, radius_y=24, large_arc=False, sweep=True)
        self.add_arc('sym-e10', (14, 20), (12, 22), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_arc('sym-e11', (12, 22), (7, 22), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e12', (7, 22), (7, 40))
        self.add_line('sym-e13', (7, 40), (24, 40))
        self.add_arc('sym-e14', (41, 22), (44, 18), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('sym-e17', (44, 18), (43, 15))
        self.add_line('sym-e18', (43, 15), (41, 8))
        self.add_line('sym-e19', (41, 8), (7, 8))
        self.add_line('sym-e21', (7, 8), (5, 15))
        self.add_arc('sym-e22', (5, 15), (4, 18), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('sym-e25', (4, 18), (7, 22), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', closed=True)
        self.add_contour('sym-c1', 'sym-e14', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e21', 'sym-e22', 'sym-e25', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
