"""Turn right (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b654ed27-4d6a-4c36-8d1d-071810327791'
SOURCE_PATH = 'icons-json/transportation/turn right_b654ed27-4d6a-4c36-8d1d-071810327791.json'
AUTHOR = 'json_to_solo'

class TurnRightB654ed27(Solo48):
    icon_id = 'turn-right-b654ed27'
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
        self.add_bezier('e4', (8, 29), ((8, 28.409), (8.017, 27.364), (8.017, 26.782)), ((8.017, 25.064), (8.16, 23.309), (8.623, 21.664)), ((9.272, 19.336), (10.013, 18.009), (11.714, 16.427)), ((15.175, 13.218), (18.846, 13.309), (23.091, 13.209)), ((25.356, 13.155), (27.735, 13), (30, 13)))
        self.add_contour('c0', 'e0', 'e4', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
