"""Currency pound bill (money), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a52b466-8e1b-412a-aaa1-cea9d33e173c'
SOURCE_PATH = 'icons-json/money/currency pound bill_7a52b466-8e1b-412a-aaa1-cea9d33e173c.json'
AUTHOR = 'json_to_solo'

class CurrencyPoundBillMoney(Solo48):
    icon_id = 'currency-pound-bill-money'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('currency', 'pound', 'bill', 'money')

    def build(self):
        self.add_line('e0', (27, 18), (26, 17))
        self.add_line('e1', (28, 33), (20, 33))
        self.add_line('e2', (20, 33), (21, 30))
        self.add_line('e3', (21, 30), (21, 25))
        self.add_line('e4', (25, 25), (21, 25))
        self.add_line('e5', (39, 40), (9, 40))
        self.add_line('e6', (9, 39), (9, 34))
        self.add_line('e7', (9, 14), (9, 9))
        self.add_line('e8', (9, 8), (39, 8))
        self.add_line('e9', (39, 9), (39, 14))
        self.add_line('e10', (39, 34), (39, 40))
        self.add_arc('e11-1', (26, 17), (23, 17), radius_x=2, sweep=False)
        self.add_arc('e11-2', (23, 17), (21, 25), radius_x=11, sweep=False)
        self.add_arc('e12', (19, 25), (21, 25), radius_x=20)
        self.add_line('e13', (9, 40), (9, 39))
        self.add_arc('e14-1', (9, 34), (6, 31), radius_x=28)
        self.add_line('e14-2', (6, 31), (4, 24))
        self.add_line('e14-3', (4, 24), (6, 17))
        self.add_arc('e14-4', (6, 17), (9, 14), radius_x=20, sweep=False)
        self.add_line('e15', (9, 9), (9, 8))
        self.add_line('e16', (39, 8), (39, 9))
        self.add_arc('e17-1', (39, 14), (43, 18), radius_x=11)
        self.add_line('e17-2', (43, 18), (44, 24))
        self.add_line('e17-3', (44, 24), (42, 31))
        self.add_line('e17-4', (42, 31), (39, 34))
        self.add_contour('c0', 'e0', 'e11-1', 'e11-2')
        self.add_contour('c1', 'e12')
        self.add_contour('c2', 'e1', 'e2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5', 'e13', 'e6', 'e14-1', 'e14-2', 'e14-3', 'e14-4', 'e7', 'e15', 'e8', 'e16', 'e9', 'e17-1', 'e17-2', 'e17-3', 'e17-4', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
