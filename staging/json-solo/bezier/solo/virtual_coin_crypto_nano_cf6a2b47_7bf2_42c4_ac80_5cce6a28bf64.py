"""Virtual coin crypto nano (finance), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf6a2b47-7bf2-42c4-ac80-5cce6a28bf64'
SOURCE_PATH = 'icons-json/finance/virtual coin crypto nano_cf6a2b47-7bf2-42c4-ac80-5cce6a28bf64.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoNanoFinance(Solo48):
    icon_id = 'virtual-coin-crypto-nano-finance'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'nano', 'finance')

    def build(self):
        self.add_line('e0', (44, 8), (29, 34))
        self.add_line('e1', (29, 34), (19, 16))
        self.add_line('e2', (18, 16), (4, 40))
        self.add_bezier('e3', (19, 16), ((18.691, 16), (18.309, 16), (18, 16)))
        self.add_contour('c0', 'e0', 'e1', 'e3', 'e2')
