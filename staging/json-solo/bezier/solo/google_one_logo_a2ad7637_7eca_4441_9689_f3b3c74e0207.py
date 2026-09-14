"""Google one logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2ad7637-7eca-4441-9689-f3b3c74e0207'
SOURCE_PATH = 'icons-json/logos/google one logo_a2ad7637-7eca-4441-9689-f3b3c74e0207.json'
AUTHOR = 'json_to_solo'

class GoogleOneLogoLogos(Solo48):
    icon_id = 'google-one-logo-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google', 'one', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (10, 15), (30, 5))
        self.add_line('e1', (40, 8), (40, 39))
        self.add_line('e2', (24, 40), (24, 19))
        self.add_bezier('e3', (30, 5), ((30.624, 4.7), (32.704, 4.009), (33.6, 4.009)), ((33.663, 4.009), (33.726, 4), (33.789, 4)), ((33.79, 4), (33.791, 4), (33.792, 4)), ((33.92, 4), (34.032, 4.009), (34.144, 4.009)), ((36.464, 4.009), (40, 6.718), (40, 8)))
        self.add_bezier('e4', (40, 39), ((40, 41.073), (35.44, 43.982), (31.84, 43.982)), ((31.664, 43.982), (31.472, 44), (31.296, 44)), ((31.293, 44), (31.29, 44), (31.287, 44)), ((31.099, 44), (30.925, 43.982), (30.752, 43.982)), ((27.952, 43.982), (24, 41.645), (24, 40)))
        self.add_bezier('e5', (24, 19), ((20.8, 20.4), (17.12, 21.973), (12.736, 21.027)), ((11.2, 20.691), (10.032, 20.064), (9.168, 19.273)), ((8.592, 18.736), (8.016, 18.055), (8.016, 17.409)), ((8.016, 17.364), (8, 17.32), (8, 17.275)), ((8, 17.274), (8, 17.273), (8, 17.273)), ((8, 17.191), (8.016, 17.1), (8.016, 17.018)), ((8.016, 16.409), (9.184, 15.391), (10, 15)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4', 'e2', 'e5', closed=True)
