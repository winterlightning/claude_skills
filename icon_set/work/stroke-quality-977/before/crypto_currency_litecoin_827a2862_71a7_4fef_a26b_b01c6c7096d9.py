"""Crypto currency litecoin (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '827a2862-71a7-4fef-a26b-b01c6c7096d9'
SOURCE_PATH = 'pictographic-primitives/money/crypto currency litecoin_827a2862-71a7-4fef-a26b-b01c6c7096d9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class CryptoCurrencyLitecoin(Solo48):
    icon_id = 'crypto-currency-litecoin'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('crypto', 'currency', 'litecoin', 'money')

    def build(self):
        self.add_line('e0', (21, 4), (16, 26))
        self.add_line('e1', (16, 26), (8, 30))
        self.add_line('e2', (40, 44), (12, 44))
        self.add_line('e3', (12, 44), (16, 26))
        self.add_line('e4', (16, 26), (30, 19))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4')
        self.relate('connect', 'c0', 'c1')
