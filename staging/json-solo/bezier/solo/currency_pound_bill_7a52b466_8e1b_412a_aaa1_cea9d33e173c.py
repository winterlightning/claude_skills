"""Currency pound bill (money), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e11', (26, 17), ((24.955, 16.668), (23.927, 16.209), (22.973, 17.046)), ((20.936, 18.843), (21, 22.169), (21, 25)))
        self.add_bezier('e12', (19, 25), ((19.609, 25), (20.391, 25), (21, 25)))
        self.add_bezier('e13', (9, 40), ((8.873, 39.84), (9.073, 39.926), (8.955, 39.729)), ((8.782, 39.434), (9.164, 39.295), (9, 39)))
        self.add_bezier('e14', (9, 34), ((6.436, 31.403), (4.018, 29.415), (4.018, 24.64)), ((4.018, 24.325), (4, 23.998), (4, 23.671)), ((4, 23.666), (4, 23.661), (4, 23.655)), ((4.009, 23.495), (4.009, 23.335), (4.018, 23.163)), ((4.018, 18.72), (6.527, 16.326), (9, 14)))
        self.add_bezier('e15', (9, 9), ((9.082, 8.594), (8.7, 8.406), (8.782, 8)), ((9.009, 8), (8.773, 8), (9, 8)))
        self.add_bezier('e16', (39, 8), ((39.136, 8.16), (38.964, 8), (39.064, 8.197)), ((39.227, 8.517), (38.836, 8.68), (39, 9)))
        self.add_bezier('e17', (39, 14), ((41.573, 15.92), (43.982, 18.572), (43.982, 22.831)), ((43.982, 23.249), (44, 23.655), (44, 24.074)), ((44, 24.079), (44, 24.084), (44, 24.089)), ((44, 24.417), (43.991, 24.744), (43.991, 25.083)), ((43.991, 29.403), (41.3, 31.686), (39, 34)))
        self.add_contour('c0', 'e0', 'e11')
        self.add_contour('c1', 'e12')
        self.add_contour('c2', 'e1', 'e2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5', 'e13', 'e6', 'e14', 'e7', 'e15', 'e8', 'e16', 'e9', 'e17', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
