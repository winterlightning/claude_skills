"""Mobile phone (mobile), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b193343f-83cb-42e1-82cf-a7eac0dd3950'
SOURCE_PATH = 'icons-json/mobile/mobile phone_b193343f-83cb-42e1-82cf-a7eac0dd3950.json'
AUTHOR = 'json_to_solo'

class MobilePhoneMobile(Solo48):
    icon_id = 'mobile-phone-mobile'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('mobile', 'phone')

    def build(self):
        self.add_line('sym-e0', (22, 36), (26, 36))
        self.add_line('sym-e1', (35, 44), (24, 44))
        self.add_line('sym-e2', (24, 44), (13, 44))
        self.add_arc('sym-e4', (13, 44), (8, 40), radius_x=6)
        self.add_line('sym-e5', (8, 40), (8, 8))
        self.add_arc('sym-e6', (8, 8), (13, 4), radius_x=6)
        self.add_line('sym-e8', (13, 4), (24, 4))
        self.add_line('sym-e9', (24, 4), (35, 4))
        self.add_arc('sym-e11', (35, 4), (40, 8), radius_x=6)
        self.add_line('sym-e12', (40, 8), (40, 40))
        self.add_arc('sym-e13', (40, 40), (35, 44), radius_x=6)
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e13', closed=True)
