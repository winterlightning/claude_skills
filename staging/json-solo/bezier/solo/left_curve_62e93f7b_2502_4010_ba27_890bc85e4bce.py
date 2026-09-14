"""Left curve (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62e93f7b-2502-4010-ba27-890bc85e4bce'
SOURCE_PATH = 'icons-json/transportation/left curve_62e93f7b-2502-4010-ba27-890bc85e4bce.json'
AUTHOR = 'json_to_solo'

class LeftCurveTransportation(Solo48):
    icon_id = 'left-curve-transportation'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('left', 'curve', 'transportation')

    def build(self):
        self.add_line('e0', (19, 4), (8, 11))
        self.add_line('e1', (19, 19), (8, 11))
        self.add_line('e2', (40, 44), (40, 19))
        self.add_line('e3', (29, 11), (8, 11))
        self.add_bezier('e4', (40, 19), ((40, 18.4), (39.533, 17.264), (39.253, 16.7)), ((37.747, 13.773), (33.653, 11), (29, 11)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e4', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
