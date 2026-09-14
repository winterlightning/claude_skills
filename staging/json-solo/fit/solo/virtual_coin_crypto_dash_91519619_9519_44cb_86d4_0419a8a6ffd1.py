"""Virtual coin crypto dash (money), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91519619-9519-44cb-86d4-0419a8a6ffd1'
SOURCE_PATH = 'icons-json/money/virtual coin crypto dash_91519619-9519-44cb-86d4-0419a8a6ffd1.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoDashMoney(Solo48):
    icon_id = 'virtual-coin-crypto-dash-money'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'dash', 'money')

    def build(self):
        self.add_line('e0', (14, 31), (29, 31))
        self.add_line('e1', (32, 29), (34, 21))
        self.add_line('e2', (30, 16), (19, 16))
        self.add_line('e3', (11, 24), (24, 24))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_line('e5', (29, 31), (32, 29))
        self.add_arc('e6', (34, 21), (30, 16), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
