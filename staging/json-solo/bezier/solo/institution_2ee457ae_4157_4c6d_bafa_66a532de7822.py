"""Institution (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e7', (40, 31), ((40, 30.909), (39.99, 31.091), (39.99, 31)), ((39.99, 29.918), (39.35, 28.6), (38.9, 27.627)), ((36.4, 22.182), (30.5, 18.536), (24, 18.545)), ((15.64, 18.564), (9.49, 23.764), (8, 31)))
        self.add_bezier('e8', (34, 12), ((35.41, 11.518), (37.02, 10.991), (35.45, 9.573)), ((35.04, 9.2), (34.52, 9.236), (34, 9)))
        self.add_contour('c0', 'e0', 'e7')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e8', 'e5', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c4', 'c0')
