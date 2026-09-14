"""Weights (sports), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e19c45b5-82c3-4520-898b-27160ddd0cc8'
SOURCE_PATH = 'icons-json/sports/weights_e19c45b5-82c3-4520-898b-27160ddd0cc8.json'
AUTHOR = 'json_to_solo'

class Weights(Solo48):
    icon_id = 'weights'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('weights', 'sports')

    def build(self):
        self.add_line('sym-e0', (44, 24), (40, 24))
        self.add_line('sym-e1', (40, 24), (40, 11))
        self.add_line('sym-e2', (40, 11), (39, 8))
        self.add_line('sym-e3', (39, 8), (32, 8))
        self.add_arc('sym-e4', (32, 8), (31, 11), radius_x=4, sweep=False)
        self.add_line('sym-e5', (31, 11), (31, 24))
        self.add_line('sym-e6', (31, 24), (24, 24))
        self.add_line('sym-e7', (24, 24), (17, 24))
        self.add_line('sym-e8', (17, 24), (17, 11))
        self.add_line('sym-e9', (17, 11), (16, 8))
        self.add_line('sym-e10', (16, 8), (9, 8))
        self.add_line('sym-e11', (9, 8), (8, 11))
        self.add_line('sym-e12', (8, 11), (8, 24))
        self.add_line('sym-e13', (8, 24), (4, 24))
        self.add_line('sym-e14', (31, 24), (31, 37))
        self.add_line('sym-e15', (31, 37), (32, 40))
        self.add_line('sym-e16', (32, 40), (39, 40))
        self.add_line('sym-e17', (39, 40), (40, 37))
        self.add_line('sym-e18', (40, 37), (40, 24))
        self.add_line('sym-e19', (17, 24), (17, 37))
        self.add_line('sym-e20', (17, 37), (16, 40))
        self.add_line('sym-e21', (16, 40), (9, 40))
        self.add_arc('sym-e22', (9, 40), (8, 37), radius_x=4)
        self.add_line('sym-e23', (8, 37), (8, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13')
        self.add_contour('sym-c1', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
        self.add_contour('sym-c2', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
