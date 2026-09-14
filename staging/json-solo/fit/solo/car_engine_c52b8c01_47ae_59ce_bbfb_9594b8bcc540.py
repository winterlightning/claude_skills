"""Car engine (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c52b8c01-47ae-59ce-bbfb-9594b8bcc540'
SOURCE_PATH = 'icons-json/transportation/car engine_c52b8c01-47ae-59ce-bbfb-9594b8bcc540.json'
AUTHOR = 'json_to_solo'

class CarEngineC52b8c01(Solo48):
    icon_id = 'car-engine-c52b8c01'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'engine', 'transportation')

    def build(self):
        self.add_line('e0', (37, 22), (42, 22))
        self.add_line('e1', (44, 25), (44, 30))
        self.add_line('e2', (40, 34), (37, 34))
        self.add_line('e3', (30, 8), (17, 8))
        self.add_line('e4', (23, 8), (23, 14))
        self.add_line('e5', (9, 25), (4, 25))
        self.add_line('e6', (4, 18), (4, 31))
        self.add_line('e7', (19, 40), (34, 40))
        self.add_line('e8', (37, 37), (37, 19))
        self.add_line('e9', (37, 19), (33, 16))
        self.add_line('e10', (30, 14), (16, 14))
        self.add_line('e11', (15, 14), (9, 18))
        self.add_line('e12', (9, 18), (9, 33))
        self.add_arc('e13-1', (42, 22), (44, 23), radius_x=3)
        self.add_arc('e13-2', (44, 23), (44, 25), radius_x=6, sweep=False)
        self.add_arc('e14', (44, 30), (40, 34), radius_x=4)
        self.add_arc('e15', (9, 33), (19, 40), radius_x=31, sweep=False)
        self.add_arc('e16', (34, 40), (37, 37), radius_x=3, sweep=False)
        self.add_arc('e17', (33, 16), (30, 14), radius_x=4, sweep=False)
        self.add_line('e18', (16, 14), (15, 14))
        self.add_contour('c0', 'e0', 'e13-1', 'e13-2', 'e1', 'e14', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e15', 'e7', 'e16', 'e8', 'e9', 'e17', 'e10', 'e18', 'e11', 'e12', closed=True)
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c4')
