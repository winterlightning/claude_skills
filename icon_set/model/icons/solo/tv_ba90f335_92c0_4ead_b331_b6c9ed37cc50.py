"""Tv (tv), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba90f335-92c0-4ead-b331-b6c9ed37cc50'
SOURCE_PATH = 'icons-json/tv/tv_ba90f335-92c0-4ead-b331-b6c9ed37cc50.json'
AUTHOR = 'json_to_solo'

class TvTv(Solo48):
    icon_id = 'tv-tv'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tv'
    aliases = ()
    keywords = ('tv',)

    def build(self):
        self.add_line('e0', (16, 4), (23, 12))
        self.add_line('e1', (14, 44), (17, 38))
        self.add_line('e2', (34, 44), (31, 38))
        self.add_line('e3', (32, 4), (25, 12))
        self.add_line('e4', (25, 12), (33, 12))
        self.add_line('e5', (16, 12), (23, 12))
        self.add_line('e6', (25, 12), (23, 12))
        self.add_arc('e7-1', (33, 12), (39, 15), radius_x=6)
        self.add_line('e7-2', (39, 15), (40, 24))
        self.add_line('e7-3', (40, 24), (39, 34))
        self.add_arc('e7-4', (39, 34), (31, 38), radius_x=8)
        self.add_line('e8', (31, 38), (17, 38))
        self.add_line('e9-1', (17, 38), (10, 36))
        self.add_arc('e9-2', (10, 36), (8, 30), radius_x=10)
        self.add_line('e9-3', (8, 30), (8, 25))
        self.add_line('e9-4', (8, 25), (9, 15))
        self.add_arc('e9-5', (9, 15), (11, 13), radius_x=4)
        self.add_line('e9-6', (11, 13), (16, 12))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e6')
        self.add_contour('c4', 'e4', 'e7-1', 'e7-2', 'e7-3', 'e7-4')
        self.add_contour('c5', 'e8')
        self.add_contour('c6', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e9-5', 'e9-6', 'e5')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
