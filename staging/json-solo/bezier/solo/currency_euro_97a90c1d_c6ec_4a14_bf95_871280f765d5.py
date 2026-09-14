"""Currency euro (money), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e4', (40, 4), ((38.63, 4), (37.27, 4.009), (35.9, 4.009)), ((28.75, 4.009), (21.52, 7.3), (17.84, 12.964)), ((16.34, 15.282), (15.66, 17.4), (15, 20)))
        self.add_bezier('e5', (40, 44), ((38.89, 44), (37.78, 43.991), (36.67, 43.991)), ((28.49, 43.991), (21.28, 40.645), (17.05, 34.173)), ((15.51, 31.818), (14.76, 29.618), (14, 27)))
        self.add_bezier('e6', (15, 20), ((14.56, 22.145), (14.02, 24.809), (14, 27)))
        self.add_contour('c0', 'e4', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3', 'e6')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
