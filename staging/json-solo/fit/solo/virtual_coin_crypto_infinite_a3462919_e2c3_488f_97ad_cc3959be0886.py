"""Virtual coin crypto infinite (finance), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3462919-e2c3-488f-97ad-cc3959be0886'
SOURCE_PATH = 'icons-json/finance/virtual coin crypto infinite_a3462919-e2c3-488f-97ad-cc3959be0886.json'
AUTHOR = 'json_to_solo'

class VirtualCoinCryptoInfiniteFinance(Solo48):
    icon_id = 'virtual-coin-crypto-infinite-finance'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'infinite', 'finance')

    def build(self):
        self.add_line('sym-e1', (24, 23), (23, 21))
        self.add_line('sym-e2', (23, 21), (21, 17))
        self.add_arc('sym-e3', (21, 17), (13, 8), radius_x=14, sweep=False)
        self.add_line('sym-e5', (13, 8), (12, 8))
        self.add_arc('sym-e6-1', (12, 8), (6, 14), radius_x=8, sweep=False)
        self.add_arc('sym-e6-2', (6, 14), (4, 24), radius_x=26, sweep=False)
        self.add_line('sym-e8', (4, 24), (4, 25))
        self.add_line('sym-e9-1', (4, 25), (6, 35))
        self.add_arc('sym-e9-2', (6, 35), (11, 40), radius_x=7, sweep=False)
        self.add_arc('sym-e10', (11, 40), (12, 40), radius_x=22)
        self.add_arc('sym-e12-1', (12, 40), (18, 35), radius_x=9, sweep=False)
        self.add_line('sym-e12-2', (18, 35), (24, 22))
        self.add_line('sym-e13-1', (24, 22), (30, 35))
        self.add_arc('sym-e13-2', (30, 35), (36, 40), radius_x=9, sweep=False)
        self.add_line('sym-e15', (36, 40), (37, 40))
        self.add_arc('sym-e16-1', (37, 40), (42, 35), radius_x=7, sweep=False)
        self.add_line('sym-e16-2', (42, 35), (44, 25))
        self.add_line('sym-e17', (44, 25), (44, 24))
        self.add_arc('sym-e19-1', (44, 24), (42, 14), radius_x=26, sweep=False)
        self.add_arc('sym-e19-2', (42, 14), (36, 8), radius_x=8, sweep=False)
        self.add_line('sym-e20', (36, 8), (35, 8))
        self.add_arc('sym-e22', (35, 8), (27, 17), radius_x=14, sweep=False)
        self.add_line('sym-e23', (27, 17), (25, 21))
        self.add_line('sym-e24', (25, 21), (24, 23))
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6-1', 'sym-e6-2', 'sym-e8', 'sym-e9-1', 'sym-e9-2', 'sym-e10', 'sym-e12-1', 'sym-e12-2', 'sym-e13-1', 'sym-e13-2', 'sym-e15', 'sym-e16-1', 'sym-e16-2', 'sym-e17', 'sym-e19-1', 'sym-e19-2', 'sym-e20', 'sym-e22', 'sym-e23', 'sym-e24', closed=True)
