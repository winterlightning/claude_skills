"""Virtual coin crypto basic attention token (money), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7fa3e9a-e0a8-484a-95ee-ba978824d02e'
SOURCE_PATH = 'icons-json/money/virtual coin crypto basic attention token_d7fa3e9a-e0a8-484a-95ee-ba978824d02e.json'
AUTHOR = 'gpt-6'

class VirtualCoinCryptoBasicAttentionToken(Solo48):
    icon_id = 'virtual-coin-crypto-basic-attention-token'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'basic', 'attention', 'token', 'money')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (34, 30), (14, 30))
        self.add_line('e1', (14, 30), (24, 13))
        self.add_line('e2', (24, 13), (34, 30))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0', 'e1', 'e2'), closed=True)
        self.add_contour('e3', *('e3-top', 'e3-bottom'), closed=True)
