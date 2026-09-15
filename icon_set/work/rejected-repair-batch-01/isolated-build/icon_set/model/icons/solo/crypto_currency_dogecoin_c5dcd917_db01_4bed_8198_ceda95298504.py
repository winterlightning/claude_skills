"""Crypto currency dogecoin (money), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5dcd917-db01-4bed-8198-ceda95298504'
SOURCE_PATH = 'pictographic-primitives/money/crypto currency dogecoin_c5dcd917-db01-4bed-8198-ceda95298504.svg'
AUTHOR = 'gpt-6'

class CryptoCurrencyDogecoin(Solo48):
    icon_id = 'crypto-currency-dogecoin'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('crypto', 'currency', 'dogecoin', 'money')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (18, 14), (20, 14))
        self.add_line('e1', (18, 33), (20, 33))
        self.add_line('e2', (20, 33), (28, 33))
        self.add_line('e3', (28, 14), (20, 14))
        self.add_line('e4', (20, 33), (20, 14))
        self.add_arc('e5-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e5-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('e6', (28, 33), (28, 14), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2', 'e6', 'e3'), closed=False)
        self.add_contour('c3', *('e4',), closed=False)
        self.add_contour('e5', *('e5-top', 'e5-bottom'), closed=True)
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c0', 'c3'))
        self.relate('connect', *('c2', 'c3'))
        self.relate('connect', *('c1', 'c2'))
        self.relate('connect', *('c1', 'c3'))
