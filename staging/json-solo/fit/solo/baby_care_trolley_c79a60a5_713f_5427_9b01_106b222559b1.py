"""Baby care trolley (babies), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c79a60a5-713f-5427-9b01-106b222559b1'
SOURCE_PATH = 'icons-json/babies/baby care trolley_c79a60a5-713f-5427-9b01-106b222559b1.json'
AUTHOR = 'json_to_solo'

class BabyCareTrolley(Solo48):
    icon_id = 'baby-care-trolley'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    aliases = ()
    keywords = ('baby', 'care', 'trolley', 'babies')

    def build(self):
        self.add_line('e0', (15, 14), (15, 19))
        self.add_line('e1', (40, 19), (15, 19))
        self.add_line('e2', (26, 4), (26, 19))
        self.add_line('e3', (21, 36), (24, 31))
        self.add_line('e4', (31, 31), (35, 35))
        self.add_arc('e5-top', (32, 39), (40, 39), radius_x=4, radius_y=5)
        self.add_arc('e5-bottom', (40, 39), (32, 39), radius_x=4, radius_y=5)
        self.add_arc('e6-top', (14, 39), (22, 39), radius_x=4, radius_y=5)
        self.add_arc('e6-bottom', (22, 39), (14, 39), radius_x=4, radius_y=5)
        self.add_arc('e7', (8, 9), (15, 14), radius_x=5)
        self.add_arc('e8', (15, 19), (31, 31), radius_x=12, sweep=False)
        self.add_arc('e9-1', (31, 31), (40, 19), radius_x=13, sweep=False)
        self.add_arc('e9-2', (40, 19), (26, 4), radius_x=16, sweep=False)
        self.add_contour('c0', 'e7', 'e0', 'e8')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e9-1', 'e9-2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'e6')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c4', 'e5')
