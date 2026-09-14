"""Sub browser (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cc8fb35-b039-4c83-8757-e2a208bc6ee7'
SOURCE_PATH = 'icons-json/symbol/sub browser_1cc8fb35-b039-4c83-8757-e2a208bc6ee7.json'
AUTHOR = 'json_to_solo'

class SubBrowserSymbol(Solo48):
    icon_id = 'sub-browser-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('sub', 'browser', 'symbol')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
