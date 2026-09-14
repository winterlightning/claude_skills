"""Franc (money), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05008f11-fec7-4d0a-8597-ced5d395fad3'
SOURCE_PATH = 'icons-json/money/franc_05008f11-fec7-4d0a-8597-ced5d395fad3.json'
AUTHOR = 'json_to_solo'

class Franc05008f11(Solo48):
    icon_id = 'franc-05008f11'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('franc', 'money')

    def build(self):
        self.add_line('e0', (40, 4), (16, 4))
        self.add_line('e1', (16, 4), (16, 44))
        self.add_line('e2', (8, 25), (34, 25))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
