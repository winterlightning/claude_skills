"""Virtual coin crypto litecoin (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62002648-fd35-4df3-962e-3b40c06b6759'
SOURCE_PATH = 'pictographic-primitives/money/virtual coin crypto litecoin_62002648-fd35-4df3-962e-3b40c06b6759.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class VirtualCoinCryptoLitecoin(Solo48):
    icon_id = 'virtual-coin-crypto-litecoin'
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
