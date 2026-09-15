"""Mail (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6d5c36b-5f72-4bbf-a205-b2d56aaf29a5'
SOURCE_PATH = 'pictographic-primitives/symbol/mail_a6d5c36b-5f72-4bbf-a205-b2d56aaf29a5.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MailSymbol(Solo48):
    icon_id = 'mail-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('mail', 'symbol')

    def build(self):
        self.add_line('e0', (44, 8), (4, 8))
        self.add_line('e1', (4, 37), (4, 8))
        self.add_line('e2', (4, 8), (20, 23))
        self.add_line('e3', (27, 24), (44, 9))
        self.add_line('e4', (44, 9), (44, 38))
        self.add_line('e5', (44, 38), (42, 40))
        self.add_line('e6', (42, 40), (6, 40))
        self.add_arc('e7', (20, 23), (27, 24), radius_x=4, sweep=False)
        self.add_line('e8', (6, 40), (4, 37))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e7', 'e3', 'e4', 'e5', 'e6', 'e8', closed=True)
