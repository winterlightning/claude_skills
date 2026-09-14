"""Google near by logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e3', (15, 32), ((12.15, 28.109), (8, 23.945), (8, 19)))
        self.add_bezier('sym-e4', (8, 19), ((8, 18.827), (8, 19.173), (8, 19)))
        self.add_bezier('sym-e5', (8, 19), ((8, 18.7), (8, 18.3), (8, 18)))
        self.add_bezier('sym-e6', (8, 18), ((8, 10.782), (15.2, 4), (23, 4)))
        self.add_bezier('sym-e7', (23, 4), ((23.12, 4), (23.88, 4), (24, 4)))
        self.add_bezier('sym-e8', (24, 4), ((24.083, 4), (23.916, 4), (24, 4)))
        self.add_bezier('sym-e9', (24, 4), ((24.084, 4), (23.917, 4), (24, 4)))
        self.add_bezier('sym-e10', (24, 4), ((24.12, 4), (24.88, 4), (25, 4)))
        self.add_bezier('sym-e11', (25, 4), ((32.8, 4), (40, 10.782), (40, 18)))
        self.add_bezier('sym-e12', (40, 18), ((40, 18.3), (40, 18.7), (40, 19)))
        self.add_bezier('sym-e13', (40, 19), ((40, 19.173), (40, 18.827), (40, 19)))
        self.add_bezier('sym-e14', (40, 19), ((40, 23.945), (35.85, 28.109), (33, 32)))
        self.add_line('sym-e15', (33, 32), (27, 40))
        self.add_bezier('sym-e16', (27, 40), ((26.39, 40.827), (25.66, 42.2), (25, 43)))
        self.add_bezier('sym-e17', (25, 43), ((24.67, 43.4), (24.33, 43.591), (24, 44)))
        self.add_bezier('sym-e18', (24, 44), ((23.983, 43.978), (24.017, 44), (24, 44)))
        self.add_bezier('sym-e19', (24, 44), ((23.983, 44), (24.017, 43.978), (24, 44)))
        self.add_bezier('sym-e20', (24, 44), ((23.67, 43.591), (23.33, 43.4), (23, 43)))
        self.add_bezier('sym-e21', (23, 43), ((22.34, 42.2), (21.61, 40.827), (21, 40)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
