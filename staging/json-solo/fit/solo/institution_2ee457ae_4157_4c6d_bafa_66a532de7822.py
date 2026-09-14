"""Institution (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ee457ae-4157-4c6d-bafa-66a532de7822'
SOURCE_PATH = 'icons-json/symbol/institution_2ee457ae-4157-4c6d-bafa-66a532de7822.json'
AUTHOR = 'json_to_solo'

class InstitutionSymbol(Solo48):
    icon_id = 'institution-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('institution', 'symbol')

    def build(self):
        self.add_line('e0', (8, 31), (40, 31))
        self.add_line('e1', (37, 44), (37, 31))
        self.add_line('e2', (37, 44), (11, 44))
        self.add_line('e3', (11, 31), (11, 44))
        self.add_line('e4', (24, 12), (34, 12))
        self.add_line('e5', (34, 9), (24, 4))
        self.add_line('e6', (24, 4), (24, 19))
        self.add_arc('e7-1', (40, 31), (31, 20), radius_x=15, sweep=False)
        self.add_arc('e7-2', (31, 20), (8, 31), radius_x=17, sweep=False)
        self.add_arc('e8-1', (34, 12), (36, 11), radius_x=3, sweep=False)
        self.add_arc('e8-2', (36, 11), (34, 9), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0', 'e7-1', 'e7-2')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e8-1', 'e8-2', 'e5', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c4', 'c0')
