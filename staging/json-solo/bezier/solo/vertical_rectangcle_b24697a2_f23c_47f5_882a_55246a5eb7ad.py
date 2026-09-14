"""Vertical rectangcle (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e2', (11, 44), ((10.832, 43.936), (10.16, 44), (10, 44)))
        self.add_bezier('sym-e3', (10, 44), ((8.905, 43.536), (8.362, 42.1), (8, 41)))
        self.add_line('sym-e4', (8, 41), (8, 24))
        self.add_line('sym-e5', (8, 24), (8, 7))
        self.add_bezier('sym-e6', (8, 7), ((8.362, 5.9), (8.905, 4.464), (10, 4)))
        self.add_bezier('sym-e7', (10, 4), ((10.16, 4), (10.832, 4.064), (11, 4)))
        self.add_line('sym-e8', (11, 4), (24, 4))
        self.add_line('sym-e9', (24, 4), (37, 4))
        self.add_bezier('sym-e10', (37, 4), ((37.168, 4.064), (37.84, 4), (38, 4)))
        self.add_bezier('sym-e11', (38, 4), ((39.095, 4.464), (39.638, 5.9), (40, 7)))
        self.add_line('sym-e12', (40, 7), (40, 24))
        self.add_line('sym-e13', (40, 24), (40, 41))
        self.add_bezier('sym-e14', (40, 41), ((39.638, 42.1), (39.095, 43.536), (38, 44)))
        self.add_bezier('sym-e15', (38, 44), ((37.84, 44), (37.168, 43.936), (37, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
