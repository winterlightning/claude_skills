"""Virtual coin crypto zcash (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02dc2ba8-1815-4b82-8693-b7f4166690fe'
SOURCE_PATH = 'icons-json/money/virtual coin crypto zcash_02dc2ba8-1815-4b82-8693-b7f4166690fe.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoZcash(Solo48):
    icon_id = 'virtual-coin-crypto-zcash'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'zcash', 'money')

    def build(self):
        self.add_line('e0', (24, 4), (24, 10))
        self.add_line('e1', (8, 10), (24, 10))
        self.add_line('e2', (24, 44), (24, 38))
        self.add_line('e3', (40, 38), (24, 38))
        self.add_line('e4', (24, 10), (40, 10))
        self.add_line('e5', (40, 10), (9, 38))
        self.add_line('e6', (9, 38), (24, 38))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
