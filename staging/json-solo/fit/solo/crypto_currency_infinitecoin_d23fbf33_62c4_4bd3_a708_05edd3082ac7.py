"""Crypto currency infinitecoin (money), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd23fbf33-62c4-4bd3-a708-05edd3082ac7'
SOURCE_PATH = 'icons-json/money/crypto currency infinitecoin_d23fbf33-62c4-4bd3-a708-05edd3082ac7.json'
AUTHOR = 'json_to_solo'

class CryptoCurrencyInfinitecoinMoney(Solo48):
    icon_id = 'crypto-currency-infinitecoin-money'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('crypto', 'currency', 'infinitecoin', 'money')

    def build(self):
        self.add_arc('sym-e0', (24, 24), (36, 40), radius_x=31, sweep=False)
        self.add_line('sym-e2', (36, 40), (37, 40))
        self.add_arc('sym-e3-1', (37, 40), (42, 35), radius_x=7, sweep=False)
        self.add_line('sym-e3-2', (42, 35), (44, 25))
        self.add_line('sym-e5', (44, 25), (44, 24))
        self.add_arc('sym-e6-1', (44, 24), (42, 14), radius_x=26, sweep=False)
        self.add_arc('sym-e6-2', (42, 14), (36, 8), radius_x=9, sweep=False)
        self.add_line('sym-e8', (36, 8), (35, 8))
        self.add_arc('sym-e9', (35, 8), (24, 22), radius_x=25, sweep=False)
        self.add_arc('sym-e10', (24, 22), (13, 8), radius_x=25, sweep=False)
        self.add_line('sym-e11', (13, 8), (12, 8))
        self.add_arc('sym-e13-1', (12, 8), (6, 14), radius_x=9, sweep=False)
        self.add_arc('sym-e13-2', (6, 14), (4, 24), radius_x=26, sweep=False)
        self.add_line('sym-e14', (4, 24), (4, 25))
        self.add_line('sym-e16-1', (4, 25), (6, 35))
        self.add_arc('sym-e16-2', (6, 35), (11, 40), radius_x=7, sweep=False)
        self.add_arc('sym-e17', (11, 40), (12, 40), radius_x=22)
        self.add_arc('sym-e19', (12, 40), (24, 24), radius_x=31, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3-1', 'sym-e3-2', 'sym-e5', 'sym-e6-1', 'sym-e6-2', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13-1', 'sym-e13-2', 'sym-e14', 'sym-e16-1', 'sym-e16-2', 'sym-e17', 'sym-e19', closed=True)
