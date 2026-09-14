"""Credit card (payments), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '66b95d3f-a723-4cfd-830c-ed99236a5244'
SOURCE_PATH = 'icons-json/payments/credit card_66b95d3f-a723-4cfd-830c-ed99236a5244.json'
AUTHOR = 'json_to_solo'

class CreditCardPayments(Solo48):
    icon_id = 'credit-card-payments'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'payments'
    aliases = ()
    keywords = ('credit', 'card', 'payments')

    def build(self):
        self.add_line('e0', (4, 19), (44, 19))
        self.add_line('e1', (4, 17), (4, 37))
        self.add_line('e2', (7, 40), (41, 40))
        self.add_line('e3', (44, 37), (44, 11))
        self.add_line('e4', (41, 8), (7, 8))
        self.add_bezier('e5', (4, 37), ((4, 38.39), (5.736, 40), (7, 40)))
        self.add_bezier('e6', (41, 40), ((42.309, 40), (44, 38.45), (44, 37)))
        self.add_bezier('e7', (44, 11), ((44, 9.29), (42.227, 8.44), (41, 8)))
        self.add_bezier('e8', (7, 8), ((5.327, 8.65), (4.009, 9.77), (4.009, 11.87)), ((4, 12.02), (4, 12.17), (4, 12.32)), ((4, 13.88), (4, 15.44), (4, 17)))
        self.add_dot('e9', (36, 31))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3', 'e7', 'e4', 'e8', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
