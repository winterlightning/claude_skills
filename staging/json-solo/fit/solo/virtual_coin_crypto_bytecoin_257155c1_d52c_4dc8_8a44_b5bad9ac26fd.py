"""Virtual coin crypto bytecoin (money), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '257155c1-d52c-4dc8-8a44-b5bad9ac26fd'
SOURCE_PATH = 'icons-json/money/virtual coin crypto bytecoin_257155c1-d52c-4dc8-8a44-b5bad9ac26fd.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoBytecoinMoney(Solo48):
    icon_id = 'virtual-coin-crypto-bytecoin-money'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'bytecoin', 'money')

    def build(self):
        self.add_line('e0', (6, 24), (13, 24))
        self.add_line('e1', (34, 42), (14, 42))
        self.add_line('e2', (13, 41), (13, 24))
        self.add_line('e3', (35, 24), (13, 24))
        self.add_line('e4', (35, 24), (37, 22))
        self.add_line('e5', (31, 6), (15, 6))
        self.add_line('e6', (13, 8), (13, 24))
        self.add_arc('e7-1', (35, 24), (42, 33), radius_x=10)
        self.add_arc('e7-2', (42, 33), (34, 42), radius_x=10)
        self.add_arc('e8', (14, 42), (13, 41), radius_x=48)
        self.add_arc('e9-1', (37, 22), (40, 14), radius_x=7, sweep=False)
        self.add_arc('e9-2', (40, 14), (31, 6), radius_x=10, sweep=False)
        self.add_line('e10', (15, 6), (13, 8))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e7-1', 'e7-2', 'e1', 'e8', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e9-1', 'e9-2', 'e5', 'e10', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
