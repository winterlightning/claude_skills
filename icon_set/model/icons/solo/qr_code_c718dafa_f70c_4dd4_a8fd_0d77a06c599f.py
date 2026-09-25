"""Qr code (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c718dafa-f70c-4dd4-a8fd-0d77a06c599f'
SOURCE_PATH = 'pictographic-primitives/shopping/qr code_c718dafa-f70c-4dd4-a8fd-0d77a06c599f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class QrCodeShopping(Solo48):
    icon_id = 'qr-code-shopping'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('qr', 'code', 'shopping')

    def build(self):
        self.add_line('e0', (4, 40), (4, 8))
        self.add_line('e1', (18, 8), (18, 27))
        self.add_line('e2', (30, 8), (30, 27))
        self.add_line('e3', (44, 8), (44, 40))
        self.add_line('e4', (18, 38), (18, 40))
        self.add_line('e5', (30, 38), (30, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
