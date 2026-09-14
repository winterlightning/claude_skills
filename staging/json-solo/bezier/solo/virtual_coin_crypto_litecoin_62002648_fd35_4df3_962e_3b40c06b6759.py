"""Virtual coin crypto litecoin (money), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62002648-fd35-4df3-962e-3b40c06b6759'
SOURCE_PATH = 'icons-json/money/virtual coin crypto litecoin_62002648-fd35-4df3-962e-3b40c06b6759.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoLitecoinMoney(Solo48):
    icon_id = 'virtual-coin-crypto-litecoin-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'litecoin', 'money')

    def build(self):
        self.add_line('e0', (24, 4), (17, 23))
        self.add_line('e1', (17, 23), (31, 20))
        self.add_line('e2', (8, 25), (17, 23))
        self.add_line('e3', (17, 23), (10, 44))
        self.add_line('e4', (10, 44), (40, 44))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4')
        self.relate('connect', 'c0', 'c1')
