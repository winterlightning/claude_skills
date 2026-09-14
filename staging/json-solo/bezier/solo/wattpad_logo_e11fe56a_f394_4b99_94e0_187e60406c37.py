"""Wattpad logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e11fe56a-f394-4b99-94e0-187e60406c37'
SOURCE_PATH = 'icons-json/logos/wattpad logo_e11fe56a-f394-4b99-94e0-187e60406c37.json'
AUTHOR = 'json_to_solo'

class WattpadLogoLogos(Solo48):
    icon_id = 'wattpad-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('wattpad', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (44, 8), (44, 38))
        self.add_line('e1', (42, 40), (15, 40))
        self.add_line('e2', (4, 29), (4, 8))
        self.add_line('e3', (4, 8), (12, 8))
        self.add_line('e4', (12, 8), (12, 29))
        self.add_line('e5', (20, 32), (20, 8))
        self.add_line('e6', (20, 8), (28, 8))
        self.add_line('e7', (28, 8), (28, 32))
        self.add_line('e8', (28, 32), (36, 32))
        self.add_line('e9', (36, 32), (36, 8))
        self.add_line('e10', (36, 8), (44, 8))
        self.add_bezier('e11', (44, 38), ((44, 38.623), (43.3, 39.579), (42.745, 39.857)), ((42.564, 39.949), (42.182, 39.924), (42, 40)))
        self.add_bezier('e12', (15, 40), ((14.2, 40), (13.255, 39.756), (12.509, 39.512)), ((8.582, 38.248), (5.473, 35.183), (4.445, 31.453)), ((4.245, 30.762), (4.009, 29.987), (4.009, 29.263)), ((4.009, 29.196), (4, 29.067), (4, 29)))
        self.add_bezier('e13', (12, 29), ((12, 29.615), (12.582, 30.434), (12.936, 30.931)), ((14.645, 33.347), (17.409, 32.042), (20, 32)))
        self.add_contour('c0', 'e0', 'e11', 'e1', 'e12', 'e2', 'e3', 'e4', 'e13', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', closed=True)
