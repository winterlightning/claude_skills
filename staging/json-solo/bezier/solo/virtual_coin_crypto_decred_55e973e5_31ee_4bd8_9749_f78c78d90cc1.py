"""Virtual coin crypto decred (money), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55e973e5-31ee-4bd8-9749-f78c78d90cc1'
SOURCE_PATH = 'icons-json/money/virtual coin crypto decred_55e973e5-31ee-4bd8-9749-f78c78d90cc1.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoDecredMoney(Solo48):
    icon_id = 'virtual-coin-crypto-decred-money'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'decred', 'money')

    def build(self):
        self.add_line('e0', (16, 14), (20, 19))
        self.add_line('e1', (20, 19), (17, 19))
        self.add_line('e2', (30, 27), (27, 27))
        self.add_line('e3', (27, 27), (31, 31))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('e5', (17, 19), ((16.373, 19), (15.336, 19.027), (14.818, 19.336)), ((11.782, 21.173), (11.1, 25.564), (13.1, 28.373)), ((15.5, 31.745), (19.373, 30.9), (23, 31)))
        self.add_bezier('e6', (24, 14), ((26.464, 14.055), (29.364, 13.655), (31.5, 15.136)), ((35.045, 17.591), (35.545, 23.209), (31.955, 25.891)), ((31.455, 26.273), (30.564, 26.755), (30, 27)))
        self.add_contour('c0', 'e0', 'e1', 'e5')
        self.add_contour('c1', 'e6', 'e2', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
