"""Satellite (tv), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89743831-f496-4d64-9252-39621b32abcc'
SOURCE_PATH = 'icons-json/tv/satellite_89743831-f496-4d64-9252-39621b32abcc.json'
AUTHOR = 'json_to_solo'

class Satellite(Solo48):
    icon_id = 'satellite'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tv'
    aliases = ()
    keywords = ('satellite', 'tv')

    def build(self):
        self.add_line('e0', (40, 32), (35, 27))
        self.add_line('e1', (14, 32), (8, 44))
        self.add_line('e2', (9, 44), (27, 44))
        self.add_line('e3', (27, 44), (22, 36))
        self.add_line('e4', (14, 4), (20, 10))
        self.add_line('e5', (35, 13), (35, 27))
        self.add_line('e6', (20, 10), (32, 10))
        self.add_line('e7', (20, 10), (35, 27))
        self.add_arc('e8-top', (32, 9), (38, 9), radius_x=3, radius_y=4)
        self.add_arc('e8-bottom', (38, 9), (32, 9), radius_x=3, radius_y=4)
        self.add_arc('e9', (15, 31), (40, 32), radius_x=17, sweep=False)
        self.add_arc('e10', (15, 31), (14, 32), radius_x=19, sweep=False)
        self.add_arc('e11', (8, 44), (9, 44), radius_x=23)
        self.add_arc('e12', (15, 31), (14, 4), radius_x=22)
        self.add_contour('c0', 'e9', 'e0')
        self.add_contour('c1', 'e10', 'e1', 'e11', 'e2', 'e3')
        self.add_contour('c2', 'e12', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'e8')
        self.relate('connect', 'c4', 'e8')
