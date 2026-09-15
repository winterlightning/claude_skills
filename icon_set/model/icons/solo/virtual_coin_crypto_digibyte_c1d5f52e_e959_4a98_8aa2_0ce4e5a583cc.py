'Digibyte coin: circular rim, a smooth D bowl and regularly spaced currency ticks.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1d5f52e-e959-4a98-8aa2-0ce4e5a583cc'
SOURCE_PATH = 'pictographic-primitives/money/virtual coin crypto digibyte_c1d5f52e-e959-4a98-8aa2-0ce4e5a583cc.svg'
AUTHOR = 'gpt-6'

class VirtualCoinCryptoDigibyte(Solo48):
    icon_id = 'virtual-coin-crypto-digibyte'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'digibyte', 'money')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('coin-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('coin-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_line('top', (18, 16), (26, 16))
        self.add_arc('bowl', (26, 16), (26, 32), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('bottom', (26, 32), (18, 32))
        self.add_line('stem', (18, 32), (18, 16))
        self.add_line('top-tick', (24, 13), (24, 16))
        self.add_line('bottom-tick', (24, 32), (24, 35))
        self.add_contour('coin', *('coin-top', 'coin-bottom'), closed=True)
        self.add_contour('d', *('top', 'bowl', 'bottom', 'stem'), closed=True)
        self.relate('connect', *('top-tick', 'd'))
        self.relate('connect', *('bottom-tick', 'd'))
