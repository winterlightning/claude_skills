"""Earth 1 (maps), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7690749-228d-5c04-bc9a-b7e1d31171fc'
SOURCE_PATH = 'icons-json/maps/earth 1_b7690749-228d-5c04-bc9a-b7e1d31171fc.json'
AUTHOR = 'json_to_solo'

class Earth1(Solo48):
    icon_id = 'earth-1'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('earth', 'maps')

    def build(self):
        self.add_line('e0', (12, 23), (12, 28))
        self.add_line('e1', (23, 35), (25, 33))
        self.add_line('e2', (25, 29), (22, 28))
        self.add_line('e3', (29, 21), (30, 16))
        self.add_line('e4', (36, 11), (41, 14))
        self.add_line('e5', (10, 20), (11, 23))
        self.add_arc('e6-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e6-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e7', (5, 19), (12, 23), radius_x=8, sweep=False)
        self.add_line('e8-1', (12, 28), (16, 34))
        self.add_line('e8-2', (16, 34), (17, 41))
        self.add_arc('e8-3', (17, 41), (20, 39), radius_x=2, sweep=False)
        self.add_line('e8-4', (20, 39), (23, 35))
        self.add_arc('e9', (25, 33), (25, 29), radius_x=3, sweep=False)
        self.add_arc('e10', (22, 28), (12, 23), radius_x=11, sweep=False)
        self.add_arc('e11-1', (41, 34), (38, 27), radius_x=12)
        self.add_arc('e11-2', (38, 27), (36, 25), radius_x=3, sweep=False)
        self.add_line('e11-3', (36, 25), (29, 24))
        self.add_arc('e11-4', (29, 24), (29, 21), radius_x=4)
        self.add_arc('e12', (30, 16), (36, 11), radius_x=7)
        self.add_arc('e13-1', (19, 5), (17, 13), radius_x=28, sweep=False)
        self.add_arc('e13-2', (17, 13), (11, 18), radius_x=9)
        self.add_line('e13-3', (11, 18), (10, 20))
        self.add_contour('c0', 'e7', 'e0', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e1', 'e9', 'e2', 'e10')
        self.add_contour('c1', 'e11-1', 'e11-2', 'e11-3', 'e11-4', 'e3', 'e12', 'e4')
        self.add_contour('c2', 'e13-1', 'e13-2', 'e13-3', 'e5')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c2', 'e6')
        self.relate('connect', 'c2', 'c0')
