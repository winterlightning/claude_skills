"""Rss logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae287d44-9a89-425b-80c1-687415afa969'
SOURCE_PATH = 'icons-json/logos/rss logo_ae287d44-9a89-425b-80c1-687415afa969.json'
AUTHOR = 'json_to_solo'

class RssLogoLogos(Solo48):
    icon_id = 'rss-logo-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('rss', 'logo', 'logos')

    def build(self):
        self.add_bezier('sym-e0', (6, 6), ((6.074, 6), (6, 6), (6, 6)))
        self.add_bezier('sym-e1', (6, 6), ((8.078, 6), (9.963, 6.591), (12, 7)))
        self.add_bezier('sym-e2', (12, 7), ((19.152, 8.429), (25.887, 12.008), (31, 17)))
        self.add_bezier('sym-e3', (31, 17), ((35.992, 22.113), (39.571, 28.848), (41, 36)))
        self.add_bezier('sym-e4', (41, 36), ((41.409, 38.037), (42, 39.922), (42, 42)))
        self.add_bezier('sym-e5', (42, 42), ((42, 42), (42, 41.926), (42, 42)))
        self.add_bezier('sym-e6', (6, 18), ((8.798, 18.131), (11.415, 18.953), (14, 20)))
        self.add_bezier('sym-e7', (14, 20), ((17.04, 21.239), (19.621, 23.621), (22, 26)))
        self.add_bezier('sym-e8', (22, 26), ((24.379, 28.379), (26.761, 30.96), (28, 34)))
        self.add_bezier('sym-e9', (28, 34), ((29.047, 36.585), (29.869, 39.202), (30, 42)))
        self.add_bezier('sym-e10', (6, 32), ((8.706, 32.102), (11.248, 33.248), (13, 35)))
        self.add_bezier('sym-e11', (13, 35), ((14.752, 36.752), (15.898, 39.294), (16, 42)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10', 'sym-e11')
