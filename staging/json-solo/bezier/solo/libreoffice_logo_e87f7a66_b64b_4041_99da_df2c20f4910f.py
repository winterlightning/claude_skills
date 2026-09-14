"""Libreoffice logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e87f7a66-b64b-4041-99da-df2c20f4910f'
SOURCE_PATH = 'icons-json/logos/libreoffice logo_e87f7a66-b64b-4041-99da-df2c20f4910f.json'
AUTHOR = 'json_to_solo'

class LibreofficeLogoLogos(Solo48):
    icon_id = 'libreoffice-logo-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('libreoffice', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (30, 4), (40, 15))
        self.add_line('e1', (30, 4), (30, 13))
        self.add_line('e2', (32, 15), (40, 15))
        self.add_line('e3', (30, 4), (11, 4))
        self.add_line('e4', (8, 6), (8, 42))
        self.add_line('e5', (11, 44), (37, 44))
        self.add_line('e6', (40, 41), (40, 15))
        self.add_bezier('e7', (30, 13), ((30.421, 14), (31.074, 14.545), (32, 15)))
        self.add_bezier('e8', (11, 4), ((10.941, 4), (10.408, 4), (10.349, 4)), ((9.558, 4), (8.691, 4.6), (8.227, 5.273)), ((8.118, 5.445), (8.101, 5.827), (8, 6)))
        self.add_bezier('e9', (8, 42), ((8.522, 42.909), (9.187, 43.991), (10.324, 43.991)), ((10.392, 43.991), (10.933, 44), (11, 44)))
        self.add_bezier('e10', (37, 44), ((38.499, 43.436), (39.486, 42.573), (40, 41)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2')
        self.add_contour('c2', 'e3', 'e8', 'e4', 'e9', 'e5', 'e10', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
