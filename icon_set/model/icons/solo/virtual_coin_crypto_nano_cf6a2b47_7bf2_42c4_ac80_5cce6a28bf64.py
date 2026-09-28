"""Virtual coin crypto nano (finance), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf6a2b47-7bf2-42c4-ac80-5cce6a28bf64'
SOURCE_PATH = 'pictographic-primitives/finance/virtual coin crypto nano_cf6a2b47-7bf2-42c4-ac80-5cce6a28bf64.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class VirtualCoinCryptoNano(Solo48):
    icon_id = 'virtual-coin-crypto-nano'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    categories = ('primitives', 'finance')
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'nano', 'finance')

    def build(self):
        self.add_line('e0', (44, 8), (29, 34))
        self.add_line('e1', (29, 34), (19, 16))
        self.add_line('e2', (18, 16), (4, 40))
        self.add_line('e3', (19, 16), (18, 16))
        self.add_contour('c0', 'e0', 'e1', 'e3', 'e2')
