"""Currency pound (money), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbbacb30-44fc-5de5-a355-689497bccffd'
SOURCE_PATH = 'icons-json/money/currency pound_dbbacb30-44fc-5de5-a355-689497bccffd.json'
AUTHOR = 'json_to_solo'

class CurrencyPoundMoney(Solo48):
    icon_id = 'currency-pound-money'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('currency', 'pound', 'money')

    def build(self):
        self.add_line('e0', (17, 24), (17, 35))
        self.add_line('e1', (9, 24), (30, 24))
        self.add_line('e2', (40, 44), (10, 44))
        self.add_bezier('e3', (39, 11), ((38.147, 7.455), (35.84, 5.282), (31.595, 4.382)), ((30.827, 4.218), (29.952, 4.009), (29.152, 4.009)), ((28.931, 4.009), (28.711, 4), (28.49, 4)), ((28.487, 4), (28.483, 4), (28.48, 4)), ((28.107, 4), (27.733, 4.018), (27.36, 4.018)), ((26.144, 4.018), (24.939, 4.273), (23.787, 4.564)), ((19.957, 5.545), (17.643, 8.236), (16.832, 11.482)), ((16.395, 13.227), (16.619, 15.209), (16.597, 16.973)), ((16.576, 19.318), (17, 21.664), (17, 24)))
        self.add_bezier('e4', (17, 35), ((17, 37.6), (14.485, 40.645), (12.395, 42.436)), ((12.085, 42.7), (10.496, 44), (10.133, 44)), ((9.419, 44), (8.715, 44), (8, 44)))
        self.add_contour('c0', 'e3', 'e0', 'e4')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c0')
