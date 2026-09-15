'Dash coin: a true circular rim and a clean inner mark with evenly spaced horizontal strokes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91519619-9519-44cb-86d4-0419a8a6ffd1'
SOURCE_PATH = 'pictographic-primitives/money/virtual coin crypto dash_91519619-9519-44cb-86d4-0419a8a6ffd1.svg'
AUTHOR = 'gpt-6'

class VirtualCoinCryptoDash(Solo48):
    icon_id = 'virtual-coin-crypto-dash'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'dash', 'money')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('coin-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('coin-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_line('top', (19, 15), (29, 15))
        self.add_arc('round', (29, 15), (33, 19), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('return-1', (33, 19), (30, 33))
        self.add_line('return-2', (30, 33), (18, 33))
        self.add_line('dash', (13, 24), (23, 24))
        self.add_contour('coin', *('coin-top', 'coin-bottom'), closed=True)
        self.add_contour('return', *('return-1', 'return-2'), closed=False)
        self.relate('connect', *('top', 'round'))
        self.relate('connect', *('round', 'return'))
