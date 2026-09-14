"""Bell (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e4', (24, 12), (10, 20), radius_x=14, sweep=False)
        self.add_line('sym-e5', (10, 20), (9, 25))
        self.add_line('sym-e6', (9, 25), (9, 40))
        self.add_arc('sym-e7', (24, 12), (38, 20), radius_x=14)
        self.add_arc('sym-e8', (38, 20), (39, 25), radius_x=12, sweep=False)
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
