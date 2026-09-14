"""Barcode (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7b4657c-3734-40c1-a4f9-684f4d61861b'
SOURCE_PATH = 'icons-json/shopping/barcode_d7b4657c-3734-40c1-a4f9-684f4d61861b.json'
AUTHOR = 'json_to_solo'

class Barcode(Solo48):
    icon_id = 'barcode'
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
