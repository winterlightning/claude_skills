"""Data transfer vertical (internet), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0849f3ca-877f-519c-a98f-27fe4d0ea572'
SOURCE_PATH = 'icons-json/internet/data transfer vertical_0849f3ca-877f-519c-a98f-27fe4d0ea572.json'
AUTHOR = 'json_to_solo'

class DataTransferVerticalInternet(Solo48):
    icon_id = 'data-transfer-vertical-internet'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'internet'
    aliases = ()
    keywords = ('data', 'transfer', 'vertical', 'internet')

    def build(self):
        self.add_line('e0', (20, 11), (30, 4))
        self.add_line('e1', (30, 29), (30, 4))
        self.add_line('e2', (30, 4), (40, 11))
        self.add_line('e3', (18, 19), (18, 44))
        self.add_line('e4', (18, 44), (8, 37))
        self.add_line('e5', (18, 44), (28, 38))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
