"""Baby care clothes (babies), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ed514c7-2c36-54a9-8ae4-a874afb8b2f1'
SOURCE_PATH = 'icons-json/babies/baby care clothes_8ed514c7-2c36-54a9-8ae4-a874afb8b2f1.json'
AUTHOR = 'json_to_solo'

class BabyCareClothes(Solo48):
    icon_id = 'baby-care-clothes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    aliases = ()
    keywords = ('baby', 'care', 'clothes', 'babies')

    def build(self):
        self.add_line('e0', (10, 10), (5, 12))
        self.add_line('e1', (4, 14), (7, 18))
        self.add_line('e2', (9, 19), (13, 17))
        self.add_line('e3', (13, 17), (13, 32))
        self.add_line('e4', (35, 32), (35, 18))
        self.add_line('e5', (43, 12), (36, 8))
        self.add_line('e6', (18, 8), (14, 8))
        self.add_arc('e7', (14, 8), (10, 10), radius_x=8, sweep=False)
        self.add_line('e8-1', (5, 12), (4, 13))
        self.add_line('e8-2', (4, 13), (4, 14))
        self.add_arc('e9', (7, 18), (9, 19), radius_x=2, sweep=False)
        self.add_line('e10-1', (13, 32), (17, 34))
        self.add_line('e10-2', (17, 34), (20, 39))
        self.add_line('e10-3', (20, 39), (22, 40))
        self.add_line('e10-4', (22, 40), (24, 40))
        self.add_line('e10-5', (24, 40), (29, 39))
        self.add_arc('e10-6', (29, 39), (35, 32), radius_x=7)
        self.add_arc('e11-1', (35, 18), (44, 14), radius_x=6, sweep=False)
        self.add_line('e11-2', (44, 14), (43, 12))
        self.add_line('e12-1', (36, 8), (31, 8))
        self.add_arc('e12-2', (31, 8), (24, 12), radius_x=7)
        self.add_arc('e12-3', (24, 12), (20, 11), radius_x=8)
        self.add_arc('e12-4', (20, 11), (18, 8), radius_x=4)
        self.add_contour('c0', 'e7', 'e0', 'e8-1', 'e8-2', 'e1', 'e9', 'e2', 'e3', 'e10-1', 'e10-2', 'e10-3', 'e10-4', 'e10-5', 'e10-6', 'e4', 'e11-1', 'e11-2', 'e5', 'e12-1', 'e12-2', 'e12-3', 'e12-4', 'e6', closed=True)
