"""Page mail (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a98051e-e248-4ae8-8a84-a56070dcb2ad'
SOURCE_PATH = 'pictographic-primitives/symbol/page mail_2a98051e-e248-4ae8-8a84-a56070dcb2ad.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class PageMail(Solo48):
    icon_id = 'page-mail'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('page', 'mail', 'symbol')

    def build(self):
        self.add_line('e0', (44, 8), (4, 8))
        self.add_line('e1', (44, 8), (24, 30))
        self.add_line('e2', (24, 30), (4, 8))
        self.add_line('e3', (4, 8), (4, 40))
        self.add_line('e4', (4, 40), (44, 40))
        self.add_line('e5', (44, 8), (44, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
