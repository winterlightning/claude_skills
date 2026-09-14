"""Vectors add anchor (internet), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb962df2-7d7e-4704-b588-8cea12d18d62'
SOURCE_PATH = 'icons-json/internet/vectors add anchor_eb962df2-7d7e-4704-b588-8cea12d18d62.json'
AUTHOR = 'json_to_solo'

class VectorsAddAnchorInternet(Solo48):
    icon_id = 'vectors-add-anchor-internet'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'internet'
    aliases = ()
    keywords = ('vectors', 'add', 'anchor', 'internet')

    def build(self):
        self.add_line('e0', (24, 38), (14, 27))
        self.add_line('e1', (15, 24), (33, 24))
        self.add_line('e2', (24, 10), (14, 21))
        self.add_arc('e3-top', (24, 40), (30, 40), radius_x=3, radius_y=4)
        self.add_arc('e3-bottom', (30, 40), (24, 40), radius_x=3, radius_y=4)
        self.add_arc('e4-top', (34, 24), (40, 24), radius_x=3, radius_y=4)
        self.add_arc('e4-bottom', (40, 24), (34, 24), radius_x=3, radius_y=4)
        self.add_arc('e5-top', (24, 8), (30, 8), radius_x=3, radius_y=4)
        self.add_arc('e5-bottom', (30, 8), (24, 8), radius_x=3, radius_y=4)
        self.add_arc('e6-top', (8, 24), (14, 24), radius_x=3, radius_y=4)
        self.add_arc('e6-bottom', (14, 24), (8, 24), radius_x=3, radius_y=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c2', 'e5')
        self.relate('connect', 'c2', 'e6')
