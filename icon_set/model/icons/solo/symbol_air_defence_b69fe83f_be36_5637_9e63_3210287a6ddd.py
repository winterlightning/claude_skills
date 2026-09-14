"""Symbol air defence (war), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b69fe83f-be36-5637-9e63-3210287a6ddd'
SOURCE_PATH = 'icons-json/war/symbol air defence_b69fe83f-be36-5637-9e63-3210287a6ddd.json'
AUTHOR = 'json_to_solo'

class SymbolAirDefence(Solo48):
    icon_id = 'symbol-air-defence'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('symbol', 'air', 'defence', 'war')

    def build(self):
        self.add_line('sym-e0', (24, 40), (6, 40))
        self.add_arc('sym-e1', (6, 40), (4, 39), radius_x=19, sweep=False)
        self.add_arc('sym-e2', (4, 39), (8, 33), radius_x=20)
        self.add_arc('sym-e3', (8, 33), (24, 26), radius_x=21)
        self.add_arc('sym-e6', (24, 26), (40, 33), radius_x=21)
        self.add_arc('sym-e7', (40, 33), (44, 39), radius_x=19)
        self.add_arc('sym-e8', (44, 39), (42, 40), radius_x=19, sweep=False)
        self.add_line('sym-e9', (42, 40), (24, 40))
        self.add_line('sym-e10', (24, 8), (6, 8))
        self.add_arc('sym-e11', (6, 8), (4, 10), radius_x=2, sweep=False)
        self.add_line('sym-e13', (4, 10), (4, 39))
        self.add_line('sym-e14', (24, 8), (42, 8))
        self.add_arc('sym-e15', (42, 8), (44, 10), radius_x=2)
        self.add_line('sym-e17', (44, 10), (44, 39))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11', 'sym-e13')
        self.add_contour('sym-c2', 'sym-e14', 'sym-e15', 'sym-e17')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
