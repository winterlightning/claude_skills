"""Mastodon logo 1 (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64a67a06-6c5c-4d48-a6cd-25ab4d165966'
SOURCE_PATH = 'icons-json/logos/mastodon logo 1_64a67a06-6c5c-4d48-a6cd-25ab4d165966.json'
AUTHOR = 'json_to_solo'

class MastodonLogo1Logos(Solo48):
    icon_id = 'mastodon-logo-1-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('mastodon', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (24, 38), (28, 38))
        self.add_line('e1', (28, 42), (20, 42))
        self.add_line('e2', (6, 26), (6, 16))
        self.add_line('e3', (14, 6), (35, 6))
        self.add_line('e4', (42, 14), (42, 24))
        self.add_line('e5', (33, 32), (18, 32))
        self.add_arc('e6', (18, 32), (24, 38), radius_x=5, sweep=False)
        self.add_arc('e7', (28, 38), (28, 42), radius_x=2)
        self.add_arc('e8-1', (20, 42), (9, 36), radius_x=15)
        self.add_arc('e8-2', (9, 36), (7, 32), radius_x=14)
        self.add_line('e8-3', (7, 32), (6, 26))
        self.add_line('e9-1', (6, 16), (7, 10))
        self.add_arc('e9-2', (7, 10), (14, 6), radius_x=9)
        self.add_arc('e10-1', (35, 6), (40, 8), radius_x=8)
        self.add_line('e10-2', (40, 8), (42, 14))
        self.add_arc('e11', (42, 24), (33, 32), radius_x=9)
        self.add_contour('c0', 'e6', 'e0', 'e7', 'e1', 'e8-1', 'e8-2', 'e8-3', 'e2', 'e9-1', 'e9-2', 'e3', 'e10-1', 'e10-2', 'e4', 'e11', 'e5', closed=True)
