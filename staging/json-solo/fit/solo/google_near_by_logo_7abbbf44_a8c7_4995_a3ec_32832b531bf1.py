"""Google near by logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7abbbf44-a8c7-4995-a3ec-32832b531bf1'
SOURCE_PATH = 'icons-json/logos/google near by logo_7abbbf44-a8c7-4995-a3ec-32832b531bf1.json'
AUTHOR = 'json_to_solo'

class GoogleNearByLogoLogos(Solo48):
    icon_id = 'google-near-by-logo-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google', 'near', 'by', 'logo', 'logos')

    def build(self):
        self.add_arc('sym-e0', (18, 19), (30, 19), radius_x=6, radius_y=5)
        self.add_arc('sym-e1', (30, 19), (18, 19), radius_x=6, radius_y=5)
        self.add_line('sym-e2', (21, 40), (15, 32))
        self.add_arc('sym-e3', (15, 32), (8, 19), radius_x=24)
        self.add_line('sym-e5', (8, 19), (8, 18))
        self.add_arc('sym-e6', (8, 18), (23, 4), radius_x=16)
        self.add_arc('sym-e7', (23, 4), (24, 4), radius_x=70, sweep=False)
        self.add_line('sym-e10', (24, 4), (25, 4))
        self.add_arc('sym-e11', (25, 4), (40, 18), radius_x=16)
        self.add_line('sym-e12', (40, 18), (40, 19))
        self.add_arc('sym-e14', (40, 19), (33, 32), radius_x=24)
        self.add_line('sym-e15', (33, 32), (27, 40))
        self.add_arc('sym-e16', (27, 40), (25, 43), radius_x=53, sweep=False)
        self.add_line('sym-e17', (25, 43), (24, 44))
        self.add_line('sym-e20', (24, 44), (23, 43))
        self.add_arc('sym-e21', (23, 43), (21, 40), radius_x=52)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e20', 'sym-e21', closed=True)
