"""Virtual coin crypto tether (money), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e785c959-bf19-4703-a2be-ebc0efc0a5e8'
SOURCE_PATH = 'icons-json/money/virtual coin crypto tether_e785c959-bf19-4703-a2be-ebc0efc0a5e8.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoTetherMoney(Solo48):
    icon_id = 'virtual-coin-crypto-tether-money'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'tether', 'money')

    def build(self):
        self.add_line('e0', (6, 6), (24, 6))
        self.add_line('e1', (24, 21), (24, 6))
        self.add_line('e2', (41, 6), (24, 6))
        self.add_line('e3', (24, 42), (24, 37))
        self.add_arc('e4-1', (38, 21), (42, 24), radius_x=4)
        self.add_arc('e4-2', (42, 24), (33, 29), radius_x=10)
        self.add_arc('e4-3', (33, 29), (6, 25), radius_x=33)
        self.add_arc('e4-4', (6, 25), (10, 21), radius_x=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e4-1', 'e4-2', 'e4-3', 'e4-4')
        self.add_contour('c4', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
