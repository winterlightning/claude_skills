"""Turn right (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b654ed27-4d6a-4c36-8d1d-071810327791'
SOURCE_PATH = 'icons-json/transportation/turn right_b654ed27-4d6a-4c36-8d1d-071810327791.json'
AUTHOR = 'json_to_solo'

class TurnRightTransportation(Solo48):
    icon_id = 'turn-right-transportation'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('turn', 'right', 'transportation')

    def build(self):
        self.add_line('e0', (8, 44), (8, 29))
        self.add_line('e1', (30, 13), (40, 13))
        self.add_line('e2', (40, 13), (31, 4))
        self.add_line('e3', (40, 13), (32, 21))
        self.add_line('e4-1', (8, 29), (9, 20))
        self.add_arc('e4-2', (9, 20), (16, 14), radius_x=11)
        self.add_arc('e4-3', (16, 14), (30, 13), radius_x=70)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
