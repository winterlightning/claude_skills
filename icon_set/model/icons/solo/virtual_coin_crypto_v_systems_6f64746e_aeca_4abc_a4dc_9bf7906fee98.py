"""Virtual coin crypto v systems (money), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f64746e-aeca-4abc-a4dc-9bf7906fee98'
SOURCE_PATH = 'icons-json/money/virtual coin crypto v systems_6f64746e-aeca-4abc-a4dc-9bf7906fee98.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoVSystems(Solo48):
    icon_id = 'virtual-coin-crypto-v-systems'
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
        self.add_arc('e7', (12, 8), (14, 9), radius_x=3)
        self.add_arc('e8', (26, 31), (26, 32), radius_x=33, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2', 'e8', 'e3', closed=True)
        self.add_contour('c1', 'e4', 'e5', 'e6', closed=True)
