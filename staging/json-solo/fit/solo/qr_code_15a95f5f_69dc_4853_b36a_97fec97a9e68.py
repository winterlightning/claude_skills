"""Qr code (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '15a95f5f-69dc-4853-b36a-97fec97a9e68'
SOURCE_PATH = 'icons-json/design/qr code_15a95f5f-69dc-4853-b36a-97fec97a9e68.json'
AUTHOR = 'json_to_solo'

class QrCodeDesign(Solo48):
    icon_id = 'qr-code-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('qr', 'code', 'design')

    def build(self):
        self.add_line('e0', (19, 8), (4, 8))
        self.add_line('e1', (4, 8), (4, 35))
        self.add_line('e2', (4, 35), (19, 35))
        self.add_line('e3', (19, 35), (19, 8))
        self.add_line('e4', (44, 8), (28, 8))
        self.add_line('e5', (28, 8), (28, 40))
        self.add_line('e6', (28, 40), (44, 40))
        self.add_line('e7', (44, 40), (44, 8))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', closed=True)
        self.add_contour('c1', 'e4', 'e5', 'e6', 'e7', closed=True)
