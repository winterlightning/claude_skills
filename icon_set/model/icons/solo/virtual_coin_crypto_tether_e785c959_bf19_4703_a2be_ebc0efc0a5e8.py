"""Virtual coin crypto tether (money), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e785c959-bf19-4703-a2be-ebc0efc0a5e8'
SOURCE_PATH = 'icons-json/money/virtual coin crypto tether_e785c959-bf19-4703-a2be-ebc0efc0a5e8.json'
AUTHOR = 'gpt-6'

class VirtualCoinCryptoTether(Solo48):
    icon_id = 'virtual-coin-crypto-tether'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'tether', 'money')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (6, 6), (24, 6))
        self.add_line('e1', (24, 21), (24, 6))
        self.add_line('e2', (41, 6), (24, 6))
        self.add_line('e3', (24, 42), (24, 38))
        self.add_arc('e4-1', (38, 20), (42, 23), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e4-2', (42, 23), (33, 28), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('e4-3', (33, 28), (6, 24), radius_x=33, radius_y=33, large_arc=False, sweep=True)
        self.add_arc('e4-4', (6, 24), (10, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e4-1', 'e4-2', 'e4-3', 'e4-4'), closed=False)
        self.add_contour('c4', *('e3',), closed=False)
        self.relate('connect', *('c0', 'c1'))
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c1', 'c2'))
