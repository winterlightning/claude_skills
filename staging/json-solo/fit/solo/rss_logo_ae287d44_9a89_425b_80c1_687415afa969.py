"""Rss logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e1', (6, 6), (12, 7), radius_x=33, sweep=False)
        self.add_arc('sym-e2', (12, 7), (31, 17), radius_x=38)
        self.add_arc('sym-e3', (31, 17), (41, 36), radius_x=37)
        self.add_arc('sym-e4', (41, 36), (42, 42), radius_x=32, sweep=False)
        self.add_line('sym-e6', (6, 18), (14, 20))
        self.add_arc('sym-e7', (14, 20), (22, 26), radius_x=25)
        self.add_arc('sym-e8', (22, 26), (28, 34), radius_x=25)
        self.add_line('sym-e9', (28, 34), (30, 42))
        self.add_arc('sym-e10', (6, 32), (13, 35), radius_x=11)
        self.add_arc('sym-e11', (13, 35), (16, 42), radius_x=11)
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c1', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10', 'sym-e11')
