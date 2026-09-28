"""Sub browser (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cc8fb35-b039-4c83-8757-e2a208bc6ee7'
SOURCE_PATH = 'pictographic-primitives/symbol/sub browser_1cc8fb35-b039-4c83-8757-e2a208bc6ee7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class SubBrowser(Solo48):
    icon_id = 'sub-browser'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('sub', 'browser', 'symbol')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
