"""Rounded rectangle shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5957fd82-3c5a-4a75-8fed-377ad2e68869'
SOURCE_PATH = 'icons-json/design/rounded rectangle shape_5957fd82-3c5a-4a75-8fed-377ad2e68869.json'
AUTHOR = 'json_to_solo'

class RoundedRectangleShape5957fd82(Solo48):
    icon_id = 'rounded-rectangle-shape-5957fd82'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rounded', 'rectangle', 'shape', 'design')

    def build(self):
        self.add_line('sym-e0', (24, 40), (14, 40))
        self.add_arc('sym-e1', (14, 40), (12, 39), radius_x=5)
        self.add_arc('sym-e2', (12, 39), (4, 25), radius_x=17)
        self.add_line('sym-e4', (4, 25), (4, 23))
        self.add_arc('sym-e5', (4, 23), (12, 9), radius_x=17)
        self.add_arc('sym-e6', (12, 9), (15, 8), radius_x=7)
        self.add_arc('sym-e8', (15, 8), (16, 8), radius_x=19, sweep=False)
        self.add_line('sym-e9', (16, 8), (24, 8))
        self.add_line('sym-e10', (24, 8), (32, 8))
        self.add_arc('sym-e11', (32, 8), (33, 8), radius_x=69, sweep=False)
        self.add_arc('sym-e13', (33, 8), (36, 9), radius_x=7)
        self.add_arc('sym-e14', (36, 9), (44, 23), radius_x=17)
        self.add_line('sym-e15-1', (44, 23), (44, 24))
        self.add_arc('sym-e15-2', (44, 24), (44, 25), radius_x=28, sweep=False)
        self.add_arc('sym-e17', (44, 25), (36, 39), radius_x=17)
        self.add_arc('sym-e18', (36, 39), (34, 40), radius_x=5)
        self.add_line('sym-e19', (34, 40), (24, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e15-1', 'sym-e15-2', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
