"""Proton preview (internet), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a59dce1d-df8f-4b36-a178-738d4288393a'
SOURCE_PATH = 'icons-json/internet/proton preview_a59dce1d-df8f-4b36-a178-738d4288393a.json'
AUTHOR = 'json_to_solo'

class ProtonPreview(Solo48):
    icon_id = 'proton-preview'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'internet'
    aliases = ()
    keywords = ('proton', 'preview', 'internet')

    def build(self):
        self.add_line('e0', (16, 37), (22, 29))
        self.add_line('e1', (34, 19), (30, 21))
        self.add_line('e2', (15, 12), (22, 20))
        self.add_arc('e3-top', (9, 39), (17, 39), radius_x=4, radius_y=5)
        self.add_arc('e3-bottom', (17, 39), (9, 39), radius_x=4, radius_y=5)
        self.add_arc('e4-top', (34, 16), (40, 16), radius_x=3, radius_y=4)
        self.add_arc('e4-bottom', (40, 16), (34, 16), radius_x=3, radius_y=4)
        self.add_arc('e5-top', (8, 9), (16, 9), radius_x=4, radius_y=5)
        self.add_arc('e5-bottom', (16, 9), (8, 9), radius_x=4, radius_y=5)
        self.add_arc('e6-top', (21, 25), (31, 25), radius_x=5)
        self.add_arc('e6-bottom', (31, 25), (21, 25), radius_x=5)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c2', 'e5')
        self.relate('connect', 'c2', 'e6')
