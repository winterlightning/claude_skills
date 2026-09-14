"""Mail (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6d5c36b-5f72-4bbf-a205-b2d56aaf29a5'
SOURCE_PATH = 'icons-json/symbol/mail_a6d5c36b-5f72-4bbf-a205-b2d56aaf29a5.json'
AUTHOR = 'json_to_solo'

class MailA6d5c36b(Solo48):
    icon_id = 'mail-a6d5c36b'
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
        self.add_bezier('e7', (20, 23), ((22.264, 25.08), (24.273, 26.37), (27, 24)))
        self.add_bezier('e8', (6, 40), ((5.6, 39.72), (5.027, 39.43), (4.627, 39.15)), ((4.382, 38.93), (4, 37.4), (4, 37)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e7', 'e3', 'e4', 'e5', 'e6', 'e8', closed=True)
