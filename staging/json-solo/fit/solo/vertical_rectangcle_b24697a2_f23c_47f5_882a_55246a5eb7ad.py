"""Vertical rectangcle (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b24697a2-f23c-47f5-882a-55246a5eb7ad'
SOURCE_PATH = 'icons-json/symbol/vertical rectangcle_b24697a2-f23c-47f5-882a-55246a5eb7ad.json'
AUTHOR = 'json_to_solo'

class VerticalRectangcleSymbol(Solo48):
    icon_id = 'vertical-rectangcle-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('vertical', 'rectangcle', 'symbol')

    def build(self):
        self.add_line('sym-e0', (37, 44), (24, 44))
        self.add_line('sym-e1', (24, 44), (11, 44))
        self.add_arc('sym-e2', (11, 44), (10, 44), radius_x=1, sweep=False)
        self.add_arc('sym-e3', (10, 44), (8, 41), radius_x=4)
        self.add_line('sym-e4', (8, 41), (8, 24))
        self.add_line('sym-e5', (8, 24), (8, 7))
        self.add_arc('sym-e6', (8, 7), (10, 4), radius_x=4)
        self.add_line('sym-e7', (10, 4), (11, 4))
        self.add_line('sym-e8', (11, 4), (24, 4))
        self.add_line('sym-e9', (24, 4), (37, 4))
        self.add_line('sym-e10', (37, 4), (38, 4))
        self.add_arc('sym-e11', (38, 4), (40, 7), radius_x=4)
        self.add_line('sym-e12', (40, 7), (40, 24))
        self.add_line('sym-e13', (40, 24), (40, 41))
        self.add_arc('sym-e14', (40, 41), (38, 44), radius_x=4)
        self.add_line('sym-e15', (38, 44), (37, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
