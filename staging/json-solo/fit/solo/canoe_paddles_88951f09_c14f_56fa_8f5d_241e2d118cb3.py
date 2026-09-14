"""Canoe paddles (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88951f09-c14f-56fa-8f5d-241e2d118cb3'
SOURCE_PATH = 'icons-json/outdoors/canoe paddles_88951f09-c14f-56fa-8f5d-241e2d118cb3.json'
AUTHOR = 'json_to_solo'

class CanoePaddles88951f09(Solo48):
    icon_id = 'canoe-paddles-88951f09'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('canoe', 'paddles', 'outdoors')

    def build(self):
        self.add_line('e0', (40, 31), (40, 37))
        self.add_line('e1', (28, 39), (28, 32))
        self.add_line('e2', (30, 28), (34, 24))
        self.add_line('e3', (34, 24), (34, 4))
        self.add_line('e4', (20, 18), (20, 8))
        self.add_line('e5', (8, 9), (8, 17))
        self.add_line('e6', (10, 20), (14, 24))
        self.add_line('e7', (14, 24), (14, 43))
        self.add_line('e8', (20, 10), (8, 10))
        self.add_line('e9', (40, 38), (28, 38))
        self.add_arc('e10', (34, 24), (40, 31), radius_x=17)
        self.add_line('e11-1', (40, 37), (39, 42))
        self.add_arc('e11-2', (39, 42), (38, 43), radius_x=5, sweep=False)
        self.add_line('e11-3', (38, 43), (34, 44))
        self.add_line('e11-4', (34, 44), (30, 43))
        self.add_arc('e11-5', (30, 43), (28, 39), radius_x=4)
        self.add_arc('e12', (28, 32), (30, 28), radius_x=5)
        self.add_arc('e13', (14, 24), (20, 18), radius_x=13, sweep=False)
        self.add_arc('e14-1', (20, 8), (15, 4), radius_x=6, sweep=False)
        self.add_line('e14-2', (15, 4), (10, 5))
        self.add_arc('e14-3', (10, 5), (8, 8), radius_x=4, sweep=False)
        self.add_line('e14-4', (8, 8), (8, 9))
        self.add_line('e15', (8, 17), (10, 20))
        self.add_contour('c0', 'e10', 'e0', 'e11-1', 'e11-2', 'e11-3', 'e11-4', 'e11-5', 'e1', 'e12', 'e2', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e13', 'e4', 'e14-1', 'e14-2', 'e14-3', 'e14-4', 'e5', 'e15', 'e6', closed=True)
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e8')
        self.add_contour('c5', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c4', 'c2')
        self.relate('connect', 'c4', 'c2')
        self.relate('connect', 'c5', 'c0')
        self.relate('connect', 'c5', 'c0')
