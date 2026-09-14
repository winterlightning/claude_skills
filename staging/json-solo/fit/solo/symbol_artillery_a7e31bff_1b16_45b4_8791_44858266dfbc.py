"""Symbol artillery (war), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7e31bff-1b16-45b4-8791-44858266dfbc'
SOURCE_PATH = 'icons-json/war/symbol artillery_a7e31bff-1b16-45b4-8791-44858266dfbc.json'
AUTHOR = 'json_to_solo'

class SymbolArtilleryWar(Solo48):
    icon_id = 'symbol-artillery-war'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('symbol', 'artillery', 'war')

    def build(self):
        self.add_line('e0', (24, 4), (24, 14))
        self.add_line('e1', (9, 25), (9, 36))
        self.add_line('e2', (39, 36), (39, 25))
        self.add_line('e3', (8, 12), (8, 4))
        self.add_line('e4', (8, 4), (24, 14))
        self.add_line('e5', (24, 17), (24, 14))
        self.add_line('e6', (24, 14), (30, 10))
        self.add_line('e7', (30, 10), (40, 4))
        self.add_line('e8', (40, 4), (40, 13))
        self.add_arc('e9', (15, 19), (9, 25), radius_x=10, sweep=False)
        self.add_arc('e10-1', (9, 36), (15, 42), radius_x=8, sweep=False)
        self.add_line('e10-2', (15, 42), (24, 44))
        self.add_line('e10-3', (24, 44), (33, 42))
        self.add_arc('e10-4', (33, 42), (39, 36), radius_x=9, sweep=False)
        self.add_arc('e11', (39, 25), (33, 19), radius_x=9, sweep=False)
        self.add_arc('e12', (15, 19), (24, 17), radius_x=28)
        self.add_arc('e13', (15, 19), (8, 12), radius_x=13)
        self.add_arc('e14', (24, 17), (33, 19), radius_x=28)
        self.add_arc('e15', (40, 13), (33, 19), radius_x=14)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e9', 'e1', 'e10-1', 'e10-2', 'e10-3', 'e10-4', 'e2', 'e11')
        self.add_contour('c2', 'e12')
        self.add_contour('c3', 'e13', 'e3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e14')
        self.add_contour('c6', 'e6', 'e7', 'e8', 'e15')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
