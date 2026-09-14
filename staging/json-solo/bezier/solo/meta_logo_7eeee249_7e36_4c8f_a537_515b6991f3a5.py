"""Meta logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7eeee249-7e36-4c8f-a537-515b6991f3a5'
SOURCE_PATH = 'icons-json/logos/meta logo_7eeee249-7e36-4c8f-a537-515b6991f3a5.json'
AUTHOR = 'json_to_solo'

class MetaLogoLogos(Solo48):
    icon_id = 'meta-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('meta', 'logo', 'logos')

    def build(self):
        self.add_bezier('sym-e0', (24, 21), ((23.691, 20.392), (23.309, 19.608), (23, 19)))
        self.add_bezier('sym-e1', (23, 19), ((22.445, 17.912), (21.591, 17.008), (21, 16)))
        self.add_bezier('sym-e2', (21, 16), ((18.918, 12.416), (16.109, 8), (13, 8)))
        self.add_bezier('sym-e3', (13, 8), ((12.936, 8), (13.064, 8), (13, 8)))
        self.add_bezier('sym-e4', (13, 8), ((12.691, 8), (12.309, 8), (12, 8)))
        self.add_bezier('sym-e5', (12, 8), ((7.418, 8), (4, 17.56), (4, 25)))
        self.add_bezier('sym-e6', (4, 25), ((4, 25.16), (4, 24.84), (4, 25)))
        self.add_bezier('sym-e7', (4, 25), ((4, 25.448), (4, 26.552), (4, 27)))
        self.add_bezier('sym-e8', (4, 27), ((4, 32.84), (6.282, 40), (10, 40)))
        self.add_bezier('sym-e9', (10, 40), ((10.1, 40), (9.9, 40), (10, 40)))
        self.add_bezier('sym-e10', (10, 40), ((10.173, 40), (10.827, 40), (11, 40)))
        self.add_bezier('sym-e11', (11, 40), ((13.927, 40), (17.191, 33.824), (19, 30)))
        self.add_line('sym-e12', (19, 30), (24, 21))
        self.add_bezier('sym-e13', (24, 21), ((24.309, 20.392), (24.691, 19.608), (25, 19)))
        self.add_bezier('sym-e14', (25, 19), ((25.555, 17.912), (26.409, 17.008), (27, 16)))
        self.add_bezier('sym-e15', (27, 16), ((29.082, 12.416), (31.891, 8), (35, 8)))
        self.add_bezier('sym-e16', (35, 8), ((35.064, 8), (34.936, 8), (35, 8)))
        self.add_bezier('sym-e17', (35, 8), ((35.309, 8), (35.691, 8), (36, 8)))
        self.add_bezier('sym-e18', (36, 8), ((40.582, 8), (44, 17.56), (44, 25)))
        self.add_bezier('sym-e19', (44, 25), ((44, 25.16), (44, 24.84), (44, 25)))
        self.add_bezier('sym-e20', (44, 25), ((44, 25.448), (44, 26.552), (44, 27)))
        self.add_bezier('sym-e21', (44, 27), ((44, 32.84), (41.718, 40), (38, 40)))
        self.add_bezier('sym-e22', (38, 40), ((37.9, 40), (38.1, 40), (38, 40)))
        self.add_bezier('sym-e23', (38, 40), ((37.827, 40), (37.173, 40), (37, 40)))
        self.add_bezier('sym-e24', (37, 40), ((34.073, 40), (30.809, 33.824), (29, 30)))
        self.add_line('sym-e25', (29, 30), (24, 21))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
