"""Shop (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c6a59d7-f0de-4dca-8f97-74c02d16025e'
SOURCE_PATH = 'icons-json/shopping/shop_4c6a59d7-f0de-4dca-8f97-74c02d16025e.json'
AUTHOR = 'json_to_solo'

class Shop(Solo48):
    icon_id = 'shop'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shop', 'shopping')

    def build(self):
        self.add_line('e0', (29, 40), (29, 30))
        self.add_line('e1', (29, 30), (19, 30))
        self.add_line('e2', (19, 30), (19, 40))
        self.add_line('e3', (29, 40), (19, 40))
        self.add_line('e4', (29, 40), (41, 40))
        self.add_line('e5', (41, 40), (41, 21))
        self.add_line('e6', (19, 40), (8, 40))
        self.add_line('e7', (8, 40), (8, 22))
        self.add_line('e8', (44, 16), (41, 8))
        self.add_line('e9', (41, 8), (7, 8))
        self.add_line('e10', (7, 8), (4, 17))
        self.add_arc('e11', (34, 18), (34, 19), radius_x=23, sweep=False)
        self.add_arc('e12', (24, 18), (24, 20), radius_x=19, sweep=False)
        self.add_arc('e13', (14, 18), (14, 20), radius_x=19, sweep=False)
        self.add_arc('e14', (41, 21), (34, 19), radius_x=5)
        self.add_arc('e15-1', (41, 21), (43, 20), radius_x=6, sweep=False)
        self.add_line('e15-2', (43, 20), (44, 17))
        self.add_arc('e15-3', (44, 17), (44, 16), radius_x=25)
        self.add_line('e16-1', (4, 17), (4, 19))
        self.add_arc('e16-2', (4, 19), (8, 22), radius_x=7, sweep=False)
        self.add_arc('e17', (14, 20), (8, 22), radius_x=4)
        self.add_arc('e18', (14, 20), (24, 20), radius_x=6, sweep=False)
        self.add_arc('e19', (24, 20), (34, 19), radius_x=6, sweep=False)
        self.add_contour('c0', 'e11')
        self.add_contour('c1', 'e12')
        self.add_contour('c2', 'e13')
        self.add_contour('c3', 'e0', 'e1', 'e2')
        self.add_contour('c4', 'e3')
        self.add_contour('c5', 'e4', 'e5')
        self.add_contour('c6', 'e6', 'e7')
        self.add_contour('c7', 'e14')
        self.add_contour('c8', 'e15-1', 'e15-2', 'e15-3', 'e8', 'e9', 'e10', 'e16-1', 'e16-2')
        self.add_contour('c9', 'e17')
        self.add_contour('c10', 'e18')
        self.add_contour('c11', 'e19')
        self.relate('connect', 'c0', 'c11')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c11', 'c7')
        self.relate('connect', 'c1', 'c10')
        self.relate('connect', 'c1', 'c11')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c2')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c2', 'c9')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c6', 'c9')
        self.relate('connect', 'c8', 'c9')
