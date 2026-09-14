"""Money wallet (finance), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91844974-1ccf-5069-b269-c37c2543e7f4'
SOURCE_PATH = 'icons-json/finance/money wallet_91844974-1ccf-5069-b269-c37c2543e7f4.json'
AUTHOR = 'json_to_solo'

class MoneyWallet(Solo48):
    icon_id = 'money-wallet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    aliases = ()
    keywords = ('money', 'wallet', 'finance')

    def build(self):
        self.add_line('e0', (41, 19), (41, 12))
        self.add_line('e1', (37, 8), (9, 8))
        self.add_line('e2', (4, 11), (4, 36))
        self.add_line('e3', (8, 40), (36, 40))
        self.add_line('e4', (41, 34), (41, 28))
        self.add_line('e5', (33, 28), (41, 28))
        self.add_line('e6', (43, 19), (34, 19))
        self.add_arc('e7', (41, 12), (37, 8), radius_x=4, sweep=False)
        self.add_line('e8-1', (9, 8), (7, 8))
        self.add_arc('e8-2', (7, 8), (4, 11), radius_x=4, sweep=False)
        self.add_arc('e9', (4, 36), (8, 40), radius_x=4, sweep=False)
        self.add_arc('e10-1', (36, 40), (41, 37), radius_x=6, sweep=False)
        self.add_arc('e10-2', (41, 37), (41, 34), radius_x=8, sweep=False)
        self.add_arc('e11-1', (34, 19), (30, 21), radius_x=4, sweep=False)
        self.add_arc('e11-2', (30, 21), (33, 28), radius_x=5, sweep=False)
        self.add_arc('e12-1', (41, 28), (44, 26), radius_x=3, sweep=False)
        self.add_line('e12-2', (44, 26), (44, 21))
        self.add_line('e12-3', (44, 21), (43, 19))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8-1', 'e8-2', 'e2', 'e9', 'e3', 'e10-1', 'e10-2', 'e4')
        self.add_contour('c1', 'e11-1', 'e11-2', 'e5', 'e12-1', 'e12-2', 'e12-3', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
