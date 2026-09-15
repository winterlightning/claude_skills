"""Virtual coin crypto holo (finance), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f78271eb-4357-4efb-8b9c-a23fe0c4d8ae'
SOURCE_PATH = 'pictographic-primitives/finance/virtual coin crypto holo_f78271eb-4357-4efb-8b9c-a23fe0c4d8ae.svg'
AUTHOR = 'gpt-6'

class VirtualCoinCryptoHolo(Solo48):
    icon_id = 'virtual-coin-crypto-holo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', 'holo', 'finance')

    def build(self):
        self.add_line('sym-e0', (9, 24), (39, 24))
        self.add_line('sym-e3', (4, 8), (5, 8))
        self.add_arc('sym-e4', (5, 8), (9, 9), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_arc('sym-e5', (9, 9), (18, 20), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('sym-e6', (18, 20), (19, 24), radius_x=23, radius_y=23, large_arc=False, sweep=False)
        self.add_arc('sym-e7', (19, 24), (18, 28), radius_x=23, radius_y=23, large_arc=False, sweep=False)
        self.add_arc('sym-e8', (18, 28), (9, 39), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('sym-e9', (9, 39), (5, 40), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_arc('sym-e10', (5, 40), (4, 40), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_line('sym-e12', (44, 8), (39, 9))
        self.add_arc('sym-e13', (39, 9), (29, 24), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_arc('sym-e14', (29, 24), (39, 39), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_line('sym-e15', (39, 39), (44, 40))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', closed=False)
        self.add_contour('sym-c2', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
