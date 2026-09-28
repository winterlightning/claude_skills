"""Barcode (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7b1e1e5-d8dd-49d8-91d5-f83818d726c9'
SOURCE_PATH = 'pictographic-primitives/shopping/barcode_e7b1e1e5-d8dd-49d8-91d5-f83818d726c9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class BarcodeE7b1e1e5(Solo48):
    icon_id = 'barcode-e7b1e1e5'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('barcode', 'shopping')

    def build(self):
        self.add_line('e0', (6, 22), (6, 6))
        self.add_line('e1', (30, 35), (30, 6))
        self.add_line('e2', (42, 28), (42, 6))
        self.add_line('e3', (18, 6), (18, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
