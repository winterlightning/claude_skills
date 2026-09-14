"""Xe (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '60839a91-5377-448b-895b-275188172ab8'
SOURCE_PATH = 'icons-json/symbol/xe_60839a91-5377-448b-895b-275188172ab8.json'
AUTHOR = 'json_to_solo'

class Xe(Solo48):
    icon_id = 'xe'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('xe', 'symbol')

    def build(self):
        self.add_line('sym-e0', (41, 24), (31, 24))
        self.add_line('sym-e1', (31, 24), (31, 39))
        self.add_arc('sym-e2', (31, 39), (32, 40), radius_x=2)
        self.add_line('sym-e4', (32, 40), (44, 40))
        self.add_line('sym-e5', (13, 24), (22, 40))
        self.add_line('sym-e6', (4, 40), (13, 24))
        self.add_line('sym-e7', (13, 24), (22, 8))
        self.add_line('sym-e8', (4, 8), (13, 24))
        self.add_line('sym-e9', (31, 24), (31, 9))
        self.add_arc('sym-e10', (31, 9), (32, 8), radius_x=2, sweep=False)
        self.add_line('sym-e12', (32, 8), (44, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4')
        self.add_contour('sym-c1', 'sym-e5')
        self.add_contour('sym-c2', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c3', 'sym-e8')
        self.add_contour('sym-c4', 'sym-e9', 'sym-e10', 'sym-e12')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c4')
