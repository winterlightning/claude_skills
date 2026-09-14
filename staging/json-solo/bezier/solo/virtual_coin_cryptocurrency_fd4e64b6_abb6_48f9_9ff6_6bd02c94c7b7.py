"""Virtual coin cryptocurrency (money), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd4e64b6-abb6-48f9-9ff6-6bd02c94c7b7'
SOURCE_PATH = 'icons-json/money/virtual coin cryptocurrency_fd4e64b6-abb6-48f9-9ff6-6bd02c94c7b7.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptocurrencyMoney(Solo48):
    icon_id = 'virtual-coin-cryptocurrency-money'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'cryptocurrency', 'money')

    def build(self):
        self.add_line('e0', (17, 33), (17, 16))
        self.add_line('e1', (19, 15), (24, 22))
        self.add_line('e2', (24, 22), (29, 15))
        self.add_line('e3', (31, 16), (31, 33))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e5', (17, 16), ((17.173, 15.818), (17, 15.227), (17.2, 15.082)), ((17.636, 14.745), (18.527, 15), (19, 15)))
        self.add_bezier('e6', (29, 15), ((30.445, 14.773), (30.345, 14.818), (31, 16)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e2', 'e6', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
