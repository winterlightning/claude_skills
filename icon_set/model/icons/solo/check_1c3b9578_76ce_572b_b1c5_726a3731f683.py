"""Check (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c3b9578-76ce-572b-b1c5-726a3731f683'
SOURCE_PATH = 'pictographic-primitives/interface-essential/check_1c3b9578-76ce-572b-b1c5-726a3731f683.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Check(Solo48):
    icon_id = 'check-1c3b9578'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('check', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 6), (16, 42))
        self.add_line('e1', (16, 42), (6, 31))
        self.add_contour('c0', 'e0', 'e1')
