"""Virtual coin crypto decred (money), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55e973e5-31ee-4bd8-9749-f78c78d90cc1'
SOURCE_PATH = 'icons-json/money/virtual coin crypto decred_55e973e5-31ee-4bd8-9749-f78c78d90cc1.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoDecredMoney(Solo48):
    icon_id = 'virtual-coin-crypto-decred-money'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'decred', 'money')

    def build(self):
        self.add_line('e0', (16, 14), (20, 19))
        self.add_line('e1', (20, 19), (17, 19))
        self.add_line('e2', (30, 27), (27, 27))
        self.add_line('e3', (27, 27), (31, 31))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e5-1', (17, 19), (12, 25), radius_x=6, sweep=False)
        self.add_arc('e5-2', (12, 25), (23, 31), radius_x=8, sweep=False)
        self.add_arc('e6-1', (24, 14), (34, 18), radius_x=9)
        self.add_arc('e6-2', (34, 18), (30, 27), radius_x=7)
        self.add_contour('c0', 'e0', 'e1', 'e5-1', 'e5-2')
        self.add_contour('c1', 'e6-1', 'e6-2', 'e2', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
