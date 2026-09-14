"""U (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e1', (24, 44), (39, 35), radius_x=17, sweep=False)
        self.add_line('sym-e2', (39, 35), (40, 30))
        self.add_line('sym-e3', (40, 30), (40, 4))
        self.add_arc('sym-e5', (24, 44), (9, 35), radius_x=17)
        self.add_line('sym-e6', (9, 35), (8, 30))
        self.add_line('sym-e7', (8, 30), (8, 4))
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6', 'sym-e7')
        self.relate('connect', 'sym-c0', 'sym-c1')
