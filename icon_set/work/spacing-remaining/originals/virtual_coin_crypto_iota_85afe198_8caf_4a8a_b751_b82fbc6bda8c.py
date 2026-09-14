"""Virtual coin crypto iota (finance), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85afe198-8caf-4a8a-b751-b82fbc6bda8c'
SOURCE_PATH = 'icons-json/finance/virtual coin crypto iota_85afe198-8caf-4a8a-b751-b82fbc6bda8c.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoIota(Solo48):
    icon_id = 'virtual-coin-crypto-iota'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'iota', 'finance')

    def build(self):
        self.add_arc('e0-1', (17, 8), (23, 6), radius_x=13)
        self.add_arc('e0-2', (23, 6), (33, 12), radius_x=12)
        self.add_arc('e0-3', (33, 12), (28, 26), radius_x=11)
        self.add_line('e1-1', (9, 34), (6, 25))
        self.add_arc('e1-2', (6, 25), (13, 15), radius_x=11)
        self.add_arc('e1-3', (13, 15), (25, 17), radius_x=17)
        self.add_arc('e2-1', (26, 32), (42, 21), radius_x=12, sweep=False)
        self.add_line('e2-2', (42, 21), (41, 17))
        self.add_arc('e3-1', (19, 23), (17, 34), radius_x=14, sweep=False)
        self.add_arc('e3-2', (17, 34), (22, 40), radius_x=11, sweep=False)
        self.add_line('e3-3', (22, 40), (29, 42))
        self.add_line('e3-4', (29, 42), (30, 42))
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3')
        self.add_contour('c2', 'e2-1', 'e2-2')
        self.add_contour('c3', 'e3-1', 'e3-2', 'e3-3', 'e3-4')
