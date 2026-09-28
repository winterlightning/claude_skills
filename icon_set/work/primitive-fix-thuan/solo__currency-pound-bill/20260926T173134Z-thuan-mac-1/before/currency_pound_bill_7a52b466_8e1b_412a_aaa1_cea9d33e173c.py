'Pound note: straight symmetric border and a simple legible currency stroke.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a52b466-8e1b-412a-aaa1-cea9d33e173c'
SOURCE_PATH = 'pictographic-primitives/money/currency pound bill_7a52b466-8e1b-412a-aaa1-cea9d33e173c.svg'
AUTHOR = 'gpt-6'

class CurrencyPoundBill(Solo48):
    icon_id = 'currency-pound-bill'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    categories = ('primitives', 'money')
    aliases = ()
    keywords = ('currency', 'pound', 'bill', 'money')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('bill-1', (8, 8), (40, 8))
        self.add_line('bill-2', (40, 8), (44, 18))
        self.add_line('bill-3', (44, 18), (44, 30))
        self.add_line('bill-4', (44, 30), (40, 40))
        self.add_line('bill-5', (40, 40), (8, 40))
        self.add_line('bill-6', (8, 40), (4, 30))
        self.add_line('bill-7', (4, 30), (4, 18))
        self.add_line('bill-8', (4, 18), (8, 8))
        self.add_line('pound-1', (29, 17), (26, 16))
        self.add_line('pound-2', (26, 16), (22, 19))
        self.add_line('pound-3', (22, 19), (22, 32))
        self.add_line('pound-4', (22, 32), (29, 32))
        self.add_line('bar', (18, 24), (28, 24))
        self.add_contour('bill', *('bill-1', 'bill-2', 'bill-3', 'bill-4', 'bill-5', 'bill-6', 'bill-7', 'bill-8'), closed=False)
        self.add_contour('pound', *('pound-1', 'pound-2', 'pound-3', 'pound-4'), closed=False)
        self.relate('connect', *('pound', 'bar'))
