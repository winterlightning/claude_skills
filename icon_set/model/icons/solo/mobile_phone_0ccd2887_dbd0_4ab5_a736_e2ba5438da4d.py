"""Mobile phone (phones), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ccd2887-dbd0-4ab5-a736-e2ba5438da4d'
SOURCE_PATH = 'icons-json/phones/mobile phone_0ccd2887-dbd0-4ab5-a736-e2ba5438da4d.json'
AUTHOR = 'json_to_solo'

class MobilePhonePhones(Solo48):
    icon_id = 'mobile-phone-phones'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    aliases = ()
    keywords = ('mobile', 'phone', 'phones')

    def build(self):
        self.add_line('sym-e0', (8, 34), (40, 34))
        self.add_line('sym-e1', (40, 34), (40, 40))
        self.add_arc('sym-e2-1', (40, 40), (38, 43), radius_x=4)
        self.add_arc('sym-e2-2', (38, 43), (35, 44), radius_x=5)
        self.add_line('sym-e4', (35, 44), (24, 44))
        self.add_line('sym-e5', (24, 44), (13, 44))
        self.add_arc('sym-e7-1', (13, 44), (10, 43), radius_x=5)
        self.add_arc('sym-e7-2', (10, 43), (8, 40), radius_x=4)
        self.add_line('sym-e8', (8, 40), (8, 34))
        self.add_line('sym-e9', (8, 34), (8, 8))
        self.add_arc('sym-e10', (8, 8), (13, 4), radius_x=6)
        self.add_line('sym-e11', (13, 4), (24, 4))
        self.add_line('sym-e12', (24, 4), (35, 4))
        self.add_arc('sym-e13', (35, 4), (40, 8), radius_x=6)
        self.add_line('sym-e14', (40, 8), (40, 34))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2-1', 'sym-e2-2', 'sym-e4', 'sym-e5', 'sym-e7-1', 'sym-e7-2', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
