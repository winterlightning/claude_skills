"""Bell (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6969bce5-a6ce-4d22-88c4-77791dfa309a'
SOURCE_PATH = 'icons-json/symbol/bell_6969bce5-a6ce-4d22-88c4-77791dfa309a.json'
AUTHOR = 'json_to_solo'

class Bell6969bce5(Solo48):
    icon_id = 'bell-6969bce5'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bell', 'symbol')

    def build(self):
        self.add_line('sym-e0', (44, 40), (39, 40))
        self.add_line('sym-e1', (39, 40), (9, 40))
        self.add_line('sym-e2', (9, 40), (4, 40))
        self.add_line('sym-e3', (24, 8), (24, 12))
        self.add_bezier('sym-e4', (24, 12), ((17.955, 12.101), (12.164, 14.518), (10, 20)))
        self.add_bezier('sym-e5', (10, 20), ((9.445, 21.432), (9, 23.467), (9, 25)))
        self.add_line('sym-e6', (9, 25), (9, 40))
        self.add_bezier('sym-e7', (24, 12), ((30.045, 12.101), (35.836, 14.518), (38, 20)))
        self.add_bezier('sym-e8', (38, 20), ((38.555, 21.432), (39, 23.467), (39, 25)))
        self.add_line('sym-e9', (39, 25), (39, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8', 'sym-e9')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
