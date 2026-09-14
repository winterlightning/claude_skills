"""Currency euro (money), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97a90c1d-c6ec-4a14-bf95-871280f765d5'
SOURCE_PATH = 'icons-json/money/currency euro_97a90c1d-c6ec-4a14-bf95-871280f765d5.json'
AUTHOR = 'json_to_solo'

class CurrencyEuroMoney(Solo48):
    icon_id = 'currency-euro-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('currency', 'euro', 'money')

    def build(self):
        self.add_line('e0', (15, 20), (8, 20))
        self.add_line('e1', (8, 27), (14, 27))
        self.add_line('e2', (29, 27), (14, 27))
        self.add_line('e3', (32, 20), (15, 20))
        self.add_line('e4-1', (40, 4), (29, 5))
        self.add_arc('e4-2', (29, 5), (15, 20), radius_x=19, sweep=False)
        self.add_line('e5-1', (40, 44), (29, 43))
        self.add_arc('e5-2', (29, 43), (23, 40), radius_x=22)
        self.add_arc('e5-3', (23, 40), (14, 27), radius_x=20)
        self.add_arc('e6', (15, 20), (14, 27), radius_x=31, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e5-1', 'e5-2', 'e5-3')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3', 'e6')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
