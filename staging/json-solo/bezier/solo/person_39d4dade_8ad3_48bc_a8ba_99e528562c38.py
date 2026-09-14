"""Person (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39d4dade-8ad3-48bc-a8ba-99e528562c38'
SOURCE_PATH = 'icons-json/symbol/person_39d4dade-8ad3-48bc-a8ba-99e528562c38.json'
AUTHOR = 'json_to_solo'

class PersonSymbol(Solo48):
    icon_id = 'person-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('person', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 33))
        self.add_bezier('sym-e1', (24, 33), ((23.988, 33), (24.012, 33), (24, 33)))
        self.add_bezier('sym-e2', (24, 33), ((19.465, 33), (14.586, 30.992), (11, 28)))
        self.add_bezier('sym-e3', (11, 28), ((9.905, 27.082), (9.002, 26.027), (8, 25)))
        self.add_bezier('sym-e4', (8, 25), ((8, 24.845), (8.126, 25.164), (8, 25)))
        self.add_arc('sym-e5', (16, 12), (32, 12), radius_x=8)
        self.add_arc('sym-e6', (32, 12), (16, 12), radius_x=8)
        self.add_bezier('sym-e7', (24, 33), ((24.012, 33), (23.988, 33), (24, 33)))
        self.add_bezier('sym-e8', (24, 33), ((28.535, 33), (33.414, 30.992), (37, 28)))
        self.add_bezier('sym-e9', (37, 28), ((38.095, 27.082), (38.998, 26.027), (40, 25)))
        self.add_bezier('sym-e10', (40, 25), ((40, 24.845), (39.874, 25.164), (40, 25)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6', closed=True)
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
