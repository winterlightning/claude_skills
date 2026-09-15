"""Credit card (payments), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '66b95d3f-a723-4cfd-830c-ed99236a5244'
SOURCE_PATH = 'pictographic-primitives/payments/credit card_66b95d3f-a723-4cfd-830c-ed99236a5244.svg'
AUTHOR = 'gpt-6'

class CreditCard(Solo48):
    icon_id = 'credit-card'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'payments'
    aliases = ()
    keywords = ('credit', 'card', 'payments')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (4, 19), (44, 19))
        self.add_line('e1', (4, 17), (4, 37))
        self.add_line('e2', (7, 40), (41, 40))
        self.add_line('e3', (44, 37), (44, 11))
        self.add_line('e4', (41, 8), (7, 8))
        self.add_arc('e5', (4, 37), (7, 40), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('e6', (41, 40), (44, 37), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('e7', (44, 11), (41, 8), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('e8-1', (7, 8), (5, 9))
        self.add_line('e8-2', (5, 9), (4, 12))
        self.add_line('e8-3', (4, 12), (4, 17))
        self.add_line('e9', (35, 31), (35, 31))
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1', 'e5', 'e2', 'e6', 'e3', 'e7', 'e4', 'e8-1', 'e8-2', 'e8-3'), closed=True)
        self.relate('connect', *('c0', 'c1'))
