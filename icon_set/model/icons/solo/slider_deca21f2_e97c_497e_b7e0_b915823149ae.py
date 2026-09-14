"""Slider (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'deca21f2-e97c-497e-b7e0-b915823149ae'
SOURCE_PATH = 'icons-json/symbol/slider_deca21f2-e97c-497e-b7e0-b915823149ae.json'
AUTHOR = 'json_to_solo'

class Slider(Solo48):
    icon_id = 'slider'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('slider', 'symbol')

    def build(self):
        self.add_line('e0', (21, 12), (44, 12))
        self.add_line('e1', (12, 12), (4, 12))
        self.add_line('e2', (38, 27), (44, 27))
        self.add_line('e3', (29, 27), (4, 27))
        self.add_line('e4', (4, 40), (44, 40))
        self.add_arc('e5-top', (28, 27), (38, 27), radius_x=5, radius_y=4)
        self.add_arc('e5-bottom', (38, 27), (28, 27), radius_x=5, radius_y=4)
        self.add_arc('e6-top', (12, 12), (22, 12), radius_x=5, radius_y=4)
        self.add_arc('e6-bottom', (22, 12), (12, 12), radius_x=5, radius_y=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c2', 'e5')
        self.relate('connect', 'c3', 'e5')
