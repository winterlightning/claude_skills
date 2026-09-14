"""Virtual coin crypto digibyte (money), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1d5f52e-e959-4a98-8aa2-0ce4e5a583cc'
SOURCE_PATH = 'icons-json/money/virtual coin crypto digibyte_c1d5f52e-e959-4a98-8aa2-0ce4e5a583cc.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoDigibyteMoney(Solo48):
    icon_id = 'virtual-coin-crypto-digibyte-money'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'digibyte', 'money')

    def build(self):
        self.add_line('e0', (27, 10), (27, 14))
        self.add_line('e1', (22, 10), (22, 14))
        self.add_line('e2', (15, 14), (22, 14))
        self.add_line('e3', (21, 18), (18, 32))
        self.add_line('e4', (18, 32), (22, 32))
        self.add_line('e5', (22, 36), (22, 32))
        self.add_line('e6', (27, 36), (27, 32))
        self.add_line('e7', (22, 14), (27, 14))
        self.add_line('e8', (27, 32), (22, 32))
        self.add_arc('e9-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e9-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e10-1', (27, 14), (34, 21), radius_x=9)
        self.add_arc('e10-2', (34, 21), (27, 32), radius_x=9)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7')
        self.add_contour('c7', 'e10-1', 'e10-2')
        self.add_contour('c8', 'e8')
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c8')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c7', 'c8')
