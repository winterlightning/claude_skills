"""Coins (money), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5cabb173-08d9-478c-9912-5357cbf2ed85'
SOURCE_PATH = 'icons-json/money/coins_5cabb173-08d9-478c-9912-5357cbf2ed85.json'
AUTHOR = 'json_to_solo'

class CoinsMoney(Solo48):
    icon_id = 'coins-money'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('coins', 'money')

    def build(self):
        self.add_arc('sym-e0', (12, 24), (36, 24), radius_x=12)
        self.add_arc('sym-e1', (36, 24), (12, 24), radius_x=12)
        self.add_arc('sym-e2', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e3', (44, 24), (4, 24), radius_x=20)
        self.add_line('sym-e4', (24, 19), (24, 29))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4')
