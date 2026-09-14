"""Virtual coin crypto nxt (money), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3db323b5-46ab-4e33-a2b3-1d6e7be6de97'
SOURCE_PATH = 'icons-json/money/virtual coin crypto nxt_3db323b5-46ab-4e33-a2b3-1d6e7be6de97.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoNxtMoney(Solo48):
    icon_id = 'virtual-coin-crypto-nxt-money'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'nxt', 'money')

    def build(self):
        self.add_line('e0', (4, 8), (9, 8))
        self.add_line('e1', (9, 8), (22, 38))
        self.add_line('e2', (22, 8), (34, 38))
        self.add_line('e3', (36, 40), (43, 40))
        self.add_line('e4', (34, 8), (44, 8))
        self.add_line('e5', (44, 8), (44, 24))
        self.add_line('e6', (4, 33), (11, 33))
        self.add_arc('e8', (34, 38), (36, 40), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e8', 'e3')
        self.add_contour('c2', 'e4', 'e5')
        self.add_contour('c3', 'e6')
