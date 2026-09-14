"""Virtual coin crypto basic attention token (money), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7fa3e9a-e0a8-484a-95ee-ba978824d02e'
SOURCE_PATH = 'icons-json/money/virtual coin crypto basic attention token_d7fa3e9a-e0a8-484a-95ee-ba978824d02e.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoBasicAttentionTokenMoney(Solo48):
    icon_id = 'virtual-coin-crypto-basic-attention-token-money'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'basic', 'attention', 'token', 'money')

    def build(self):
        self.add_line('e0', (35, 31), (13, 31))
        self.add_line('e1', (13, 31), (24, 12))
        self.add_line('e2', (24, 12), (35, 31))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
