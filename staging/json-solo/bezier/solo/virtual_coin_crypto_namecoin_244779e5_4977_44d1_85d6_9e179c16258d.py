"""Virtual coin crypto namecoin (money), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '244779e5-4977-44d1-85d6-9e179c16258d'
SOURCE_PATH = 'icons-json/money/virtual coin crypto namecoin_244779e5-4977-44d1-85d6-9e179c16258d.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoNamecoinMoney(Solo48):
    icon_id = 'virtual-coin-crypto-namecoin-money'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'namecoin', 'money')

    def build(self):
        self.add_line('e0', (4, 40), (18, 8))
        self.add_line('e1', (18, 8), (34, 35))
        self.add_line('e2', (32, 40), (34, 35))
        self.add_line('e3', (44, 9), (34, 35))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
