"""Decrease quote level (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a98c557e-fdec-46db-be0d-34e217dc42d5'
SOURCE_PATH = 'pictographic-primitives/interface-essential/decrease quote level_a98c557e-fdec-46db-be0d-34e217dc42d5.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class DecreaseQuoteLevel(Solo48):
    icon_id = 'decrease-quote-level'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('decrease', 'quote', 'level', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 6), (6, 42))
        self.add_line('e1', (26, 15), (17, 24))
        self.add_line('e2', (17, 24), (26, 33))
        self.add_line('e3', (42, 15), (32, 24))
        self.add_line('e4', (32, 24), (42, 33))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
