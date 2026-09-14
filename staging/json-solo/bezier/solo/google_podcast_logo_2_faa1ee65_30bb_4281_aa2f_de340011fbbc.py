"""Google podcast logo 2 (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'faa1ee65-30bb-4281-aa2f-de340011fbbc'
SOURCE_PATH = 'icons-json/logos/google podcast logo 2_faa1ee65-30bb-4281-aa2f-de340011fbbc.json'
AUTHOR = 'json_to_solo'

class GooglePodcastLogo2Logos(Solo48):
    icon_id = 'google-podcast-logo-2-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google', 'podcast', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (24, 4), (24, 44))
        self.add_line('e1', (16, 11), (16, 37))
        self.add_line('e2', (32, 11), (32, 37))
        self.add_line('e3', (40, 21), (40, 27))
        self.add_line('e4', (8, 27), (8, 22))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
