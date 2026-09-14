"""Virtual coin crypto cardano (money), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdc115ba-5634-462f-867b-442517f1252f'
SOURCE_PATH = 'icons-json/money/virtual coin crypto cardano_bdc115ba-5634-462f-867b-442517f1252f.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoCardanoMoney(Solo48):
    icon_id = 'virtual-coin-crypto-cardano-money'
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
        self.add_bezier('e2', (24, 12), ((24, 11.7), (24, 11.3), (24, 11)))
        self.add_bezier('e3', (15, 16), ((15, 15.7), (15, 15.3), (15, 15)))
        self.add_bezier('e4', (33, 16), ((33, 15.7), (33, 15.3), (33, 15)))
        self.add_bezier('e5', (12, 24), ((12, 23.7), (12, 23.3), (12, 23)))
        self.add_bezier('e6', (36, 24), ((36, 23.7), (36, 23.3), (36, 23)))
        self.add_bezier('e7', (15, 32), ((15, 31.7), (15, 31.3), (15, 31)))
        self.add_bezier('e8', (33, 32), ((33, 31.7), (33, 31.3), (33, 31)))
        self.add_bezier('e9', (24, 36), ((24, 35.7), (24, 35.3), (24, 35)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e8')
        self.add_contour('c7', 'e9')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
