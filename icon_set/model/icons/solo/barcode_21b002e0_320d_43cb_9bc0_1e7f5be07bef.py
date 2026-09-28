"""Barcode (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21b002e0-320d-43cb-9bc0-1e7f5be07bef'
SOURCE_PATH = 'pictographic-primitives/shopping/barcode_21b002e0-320d-43cb-9bc0-1e7f5be07bef.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Barcode(Solo48):
    icon_id = 'barcode'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('barcode', 'shopping')

    def build(self):
        self.add_line('e0', (4, 21), (4, 8))
        self.add_line('e1', (24, 34), (24, 8))
        self.add_line('e2', (34, 27), (34, 8))
        self.add_line('e3', (44, 34), (44, 8))
        self.add_line('e4', (14, 8), (14, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
