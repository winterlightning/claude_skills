"""Barcode (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7b4657c-3734-40c1-a4f9-684f4d61861b'
SOURCE_PATH = 'pictographic-primitives/shopping/barcode_d7b4657c-3734-40c1-a4f9-684f4d61861b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class BarcodeD7b4657c(Solo48):
    icon_id = 'barcode-d7b4657c'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('barcode', 'shopping')

    def build(self):
        self.add_line('e0', (6, 42), (6, 6))
        self.add_line('e1', (30, 42), (30, 6))
        self.add_line('e2', (42, 33), (42, 6))
        self.add_line('e3', (17, 6), (17, 33))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
