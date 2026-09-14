"""Virtual coin crypto v systems (money), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f64746e-aeca-4abc-a4dc-9bf7906fee98'
SOURCE_PATH = 'icons-json/money/virtual coin crypto v systems_6f64746e-aeca-4abc-a4dc-9bf7906fee98.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoVSystemsMoney(Solo48):
    icon_id = 'virtual-coin-crypto-v-systems-money'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'v', 'systems', 'money')

    def build(self):
        self.add_line('e0', (20, 40), (4, 8))
        self.add_line('e1', (4, 8), (12, 8))
        self.add_line('e2', (14, 9), (26, 31))
        self.add_line('e3', (26, 32), (20, 40))
        self.add_line('e4', (25, 8), (44, 8))
        self.add_line('e5', (44, 8), (34, 26))
        self.add_line('e6', (34, 26), (25, 8))
        self.add_bezier('e7', (12, 8), ((12.055, 8), (12.291, 8), (12.345, 8.01)), ((12.991, 8.01), (13.527, 8.6), (14, 9)))
        self.add_bezier('e8', (26, 31), ((26, 31.32), (26, 31.68), (26, 32)))
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2', 'e8', 'e3', closed=True)
        self.add_contour('c1', 'e4', 'e5', 'e6', closed=True)
