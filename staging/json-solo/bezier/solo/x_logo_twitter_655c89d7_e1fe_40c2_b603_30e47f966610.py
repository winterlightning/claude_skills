"""X logo twitter (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '655c89d7-e1fe-40c2-b603-30e47f966610'
SOURCE_PATH = 'icons-json/logos/x logo twitter_655c89d7-e1fe-40c2-b603-30e47f966610.json'
AUTHOR = 'json_to_solo'

class XLogoTwitterLogos(Solo48):
    icon_id = 'x-logo-twitter-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('x', 'logo', 'twitter', 'logos')

    def build(self):
        self.add_line('e0', (42, 6), (24, 24))
        self.add_line('e1', (24, 24), (42, 42))
        self.add_line('e2', (6, 6), (24, 24))
        self.add_line('e3', (24, 24), (6, 42))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.relate('connect', 'c0', 'c1')
