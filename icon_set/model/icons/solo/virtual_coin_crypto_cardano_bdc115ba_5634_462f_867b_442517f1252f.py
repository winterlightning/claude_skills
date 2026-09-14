"""Virtual coin crypto cardano (money), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdc115ba-5634-462f-867b-442517f1252f'
SOURCE_PATH = 'icons-json/money/virtual coin crypto cardano_bdc115ba-5634-462f-867b-442517f1252f.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoCardano(Solo48):
    icon_id = 'virtual-coin-crypto-cardano'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'cardano', 'money')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-top', (19, 24), (29, 24), radius_x=5)
        self.add_arc('e1-bottom', (29, 24), (19, 24), radius_x=5)
        self.add_arc('e2', (24, 12), (24, 11), radius_x=15)
        self.add_arc('e3', (15, 16), (15, 15), radius_x=15)
        self.add_line('e4', (33, 16), (33, 15))
        self.add_arc('e5', (12, 24), (12, 23), radius_x=28)
        self.add_arc('e6', (36, 24), (36, 23), radius_x=25)
        self.add_arc('e7', (15, 32), (15, 31), radius_x=41)
        self.add_arc('e8', (33, 32), (33, 31), radius_x=32)
        self.add_arc('e9', (24, 36), (24, 35), radius_x=38)
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e8')
        self.add_contour('c7', 'e9')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
