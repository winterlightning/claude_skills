"""Instagram logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fdabadaa-f611-4ce2-8758-6fcb7cf26b17'
SOURCE_PATH = 'icons-json/logos/instagram logo_fdabadaa-f611-4ce2-8758-6fcb7cf26b17.json'
AUTHOR = 'json_to_solo'

class InstagramLogoLogos(Solo48):
    icon_id = 'instagram-logo-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('instagram', 'logo', 'logos')

    def build(self):
        self.add_arc('sym-e0', (16, 24), (32, 24), radius_x=8)
        self.add_arc('sym-e1', (32, 24), (16, 24), radius_x=8)
        self.add_line('sym-e2', (24, 42), (35, 42))
        self.add_bezier('sym-e3', (35, 42), ((35.344, 42), (35.673, 42), (36, 42)))
        self.add_bezier('sym-e4', (36, 42), ((38.839, 41.215), (41.149, 38.847), (42, 36)))
        self.add_bezier('sym-e5', (42, 36), ((42, 35.607), (42, 35.417), (42, 35)))
        self.add_line('sym-e6', (42, 35), (42, 20))
        self.add_line('sym-e7', (42, 20), (42, 13))
        self.add_bezier('sym-e8', (42, 13), ((42, 12.656), (42, 12.335), (42, 12)))
        self.add_bezier('sym-e9', (42, 12), ((41.264, 9.235), (38.733, 6.826), (36, 6)))
        self.add_bezier('sym-e10', (36, 6), ((35.599, 6), (35.425, 6), (35, 6)))
        self.add_line('sym-e11', (35, 6), (24, 6))
        self.add_line('sym-e12', (24, 6), (13, 6))
        self.add_bezier('sym-e13', (13, 6), ((12.575, 6), (12.401, 6), (12, 6)))
        self.add_bezier('sym-e14', (12, 6), ((9.267, 6.826), (6.736, 9.235), (6, 12)))
        self.add_bezier('sym-e15', (6, 12), ((6, 12.335), (6, 12.656), (6, 13)))
        self.add_line('sym-e16', (6, 13), (6, 20))
        self.add_line('sym-e17', (6, 20), (6, 35))
        self.add_bezier('sym-e18', (6, 35), ((6, 35.417), (6, 35.607), (6, 36)))
        self.add_bezier('sym-e19', (6, 36), ((6.851, 38.847), (9.161, 41.215), (12, 42)))
        self.add_bezier('sym-e20', (12, 42), ((12.327, 42), (12.656, 42), (13, 42)))
        self.add_line('sym-e21', (13, 42), (24, 42))
        self.add_line('sym-e22', (31, 20), (42, 20))
        self.add_line('sym-e23', (17, 20), (6, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
        self.add_contour('sym-c2', 'sym-e22')
        self.add_contour('sym-c3', 'sym-e23')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
