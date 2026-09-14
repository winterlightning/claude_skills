"""Phone flash light (mobile), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a839aab1-1953-4a67-aa15-e9ae49616cd4'
SOURCE_PATH = 'icons-json/mobile/phone flash light_a839aab1-1953-4a67-aa15-e9ae49616cd4.json'
AUTHOR = 'json_to_solo'

class PhoneFlashLightMobile(Solo48):
    icon_id = 'phone-flash-light-mobile'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('phone', 'flash', 'light', 'mobile')

    def build(self):
        self.add_line('sym-e0', (8, 12), (40, 12))
        self.add_line('sym-e1', (40, 12), (40, 15))
        self.add_arc('sym-e2', (40, 15), (39, 16), radius_x=13)
        self.add_line('sym-e3', (39, 16), (33, 22))
        self.add_line('sym-e4', (33, 22), (33, 23))
        self.add_line('sym-e5', (33, 23), (33, 40))
        self.add_line('sym-e6', (33, 40), (33, 41))
        self.add_arc('sym-e7', (33, 41), (29, 44), radius_x=5)
        self.add_line('sym-e8', (29, 44), (24, 44))
        self.add_line('sym-e9', (24, 44), (19, 44))
        self.add_arc('sym-e10', (19, 44), (15, 41), radius_x=5)
        self.add_line('sym-e11', (15, 41), (15, 40))
        self.add_line('sym-e12', (15, 40), (15, 23))
        self.add_line('sym-e13', (15, 23), (15, 22))
        self.add_line('sym-e14', (15, 22), (9, 16))
        self.add_arc('sym-e15', (9, 16), (8, 15), radius_x=13)
        self.add_line('sym-e16', (8, 15), (8, 12))
        self.add_line('sym-e17', (8, 12), (8, 5))
        self.add_arc('sym-e18', (8, 5), (9, 4), radius_x=1)
        self.add_line('sym-e20', (9, 4), (24, 4))
        self.add_line('sym-e21', (24, 4), (39, 4))
        self.add_arc('sym-e23', (39, 4), (40, 5), radius_x=1)
        self.add_line('sym-e24', (40, 5), (40, 12))
        self.add_line('sym-e25', (24, 24), (24, 29))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e20', 'sym-e21', 'sym-e23', 'sym-e24')
        self.add_contour('sym-c1', 'sym-e25')
