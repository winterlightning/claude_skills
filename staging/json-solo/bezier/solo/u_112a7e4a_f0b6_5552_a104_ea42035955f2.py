"""U (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '112a7e4a-f0b6-5552-a104-ea42035955f2'
SOURCE_PATH = 'icons-json/typeface/U_112a7e4a-f0b6-5552-a104-ea42035955f2.json'
AUTHOR = 'json_to_solo'

class U112a7e4a(Solo48):
    icon_id = 'u-112a7e4a'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('u', 'typeface')

    def build(self):
        self.add_bezier('sym-e0', (24, 44), ((24.151, 43.995), (23.851, 44), (24, 44)))
        self.add_bezier('sym-e1', (24, 44), ((30.27, 44), (36.56, 40.1), (39, 35)))
        self.add_bezier('sym-e2', (39, 35), ((39.71, 33.536), (40, 31.618), (40, 30)))
        self.add_line('sym-e3', (40, 30), (40, 4))
        self.add_bezier('sym-e4', (24, 44), ((23.849, 43.995), (24.149, 44), (24, 44)))
        self.add_bezier('sym-e5', (24, 44), ((17.73, 44), (11.44, 40.1), (9, 35)))
        self.add_bezier('sym-e6', (9, 35), ((8.29, 33.536), (8, 31.618), (8, 30)))
        self.add_line('sym-e7', (8, 30), (8, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.relate('connect', 'sym-c0', 'sym-c1')
