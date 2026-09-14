"""Phone box (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b7a921e-0a41-4b3f-b6dd-57df1cbed0b2'
SOURCE_PATH = 'icons-json/symbol/phone box_2b7a921e-0a41-4b3f-b6dd-57df1cbed0b2.json'
AUTHOR = 'json_to_solo'

class PhoneBox2b7a921e(Solo48):
    icon_id = 'phone-box-2b7a921e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('phone', 'box', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 29), (24, 44))
        self.add_line('sym-e1', (8, 14), (10, 14))
        self.add_line('sym-e2', (10, 14), (38, 14))
        self.add_line('sym-e3', (38, 14), (40, 14))
        self.add_line('sym-e4', (38, 44), (38, 14))
        self.add_bezier('sym-e5', (38, 14), ((38, 12.945), (37.55, 11.9), (37, 11)))
        self.add_bezier('sym-e6', (37, 11), ((34.64, 7.136), (29.98, 4), (25, 4)))
        self.add_bezier('sym-e7', (25, 4), ((24.78, 4), (24.22, 4), (24, 4)))
        self.add_bezier('sym-e8', (24, 4), ((23.953, 4), (24.047, 4), (24, 4)))
        self.add_bezier('sym-e9', (24, 4), ((23.977, 4), (24.023, 4), (24, 4)))
        self.add_bezier('sym-e10', (24, 4), ((23.977, 4), (24.023, 4), (24, 4)))
        self.add_bezier('sym-e11', (24, 4), ((23.953, 4), (24.047, 4), (24, 4)))
        self.add_bezier('sym-e12', (24, 4), ((23.78, 4), (23.22, 4), (23, 4)))
        self.add_bezier('sym-e13', (23, 4), ((18.02, 4), (13.36, 7.136), (11, 11)))
        self.add_bezier('sym-e14', (11, 11), ((10.45, 11.9), (10, 12.945), (10, 14)))
        self.add_line('sym-e15', (10, 14), (10, 44))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
