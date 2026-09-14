"""Barcode (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf664f43-31f6-4459-9d12-7a1d85a97306'
SOURCE_PATH = 'icons-json/shopping/barcode_bf664f43-31f6-4459-9d12-7a1d85a97306.json'
AUTHOR = 'json_to_solo'

class Barcode(Solo48):
    icon_id = 'barcode'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('barcode', 'shopping')

    def build(self):
        self.add_line('e0', (4, 40), (4, 8))
        self.add_line('e1', (31, 40), (31, 8))
        self.add_line('e2', (18, 40), (18, 8))
        self.add_line('e3', (44, 40), (44, 9))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
