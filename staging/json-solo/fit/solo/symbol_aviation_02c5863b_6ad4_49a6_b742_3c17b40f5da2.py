"""Symbol aviation (war), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02c5863b-6ad4-49a6-b742-3c17b40f5da2'
SOURCE_PATH = 'icons-json/war/symbol aviation_02c5863b-6ad4-49a6-b742-3c17b40f5da2.json'
AUTHOR = 'json_to_solo'

class SymbolAviationWar(Solo48):
    icon_id = 'symbol-aviation-war'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('symbol', 'aviation', 'war')

    def build(self):
        self.add_arc('sym-e0', (24, 22), (12, 40), radius_x=29)
        self.add_arc('sym-e2', (12, 40), (11, 40), radius_x=22, sweep=False)
        self.add_arc('sym-e3-1', (11, 40), (6, 35), radius_x=8)
        self.add_arc('sym-e3-2', (6, 35), (4, 25), radius_x=26)
        self.add_line('sym-e5', (4, 25), (4, 24))
        self.add_line('sym-e6', (4, 24), (5, 15))
        self.add_arc('sym-e7', (5, 15), (9, 10), radius_x=14)
        self.add_arc('sym-e8', (9, 10), (12, 8), radius_x=4)
        self.add_arc('sym-e9', (12, 8), (20, 16), radius_x=13)
        self.add_line('sym-e10', (20, 16), (23, 21))
        self.add_line('sym-e11', (23, 21), (24, 22))
        self.add_arc('sym-e12', (24, 22), (36, 40), radius_x=29, sweep=False)
        self.add_line('sym-e14', (36, 40), (37, 40))
        self.add_arc('sym-e15-1', (37, 40), (42, 35), radius_x=8, sweep=False)
        self.add_arc('sym-e15-2', (42, 35), (44, 25), radius_x=26, sweep=False)
        self.add_line('sym-e17', (44, 25), (44, 24))
        self.add_line('sym-e18', (44, 24), (43, 15))
        self.add_arc('sym-e19', (43, 15), (39, 10), radius_x=13, sweep=False)
        self.add_arc('sym-e20', (39, 10), (36, 8), radius_x=4, sweep=False)
        self.add_arc('sym-e21', (36, 8), (28, 16), radius_x=13, sweep=False)
        self.add_line('sym-e22', (28, 16), (25, 21))
        self.add_line('sym-e23', (25, 21), (24, 22))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3-1', 'sym-e3-2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15-1', 'sym-e15-2', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
