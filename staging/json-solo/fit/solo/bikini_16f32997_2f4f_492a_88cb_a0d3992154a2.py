"""Bikini (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '16f32997-2f4f-492a-88cb-a0d3992154a2'
SOURCE_PATH = 'icons-json/symbol/bikini_16f32997-2f4f-492a-88cb-a0d3992154a2.json'
AUTHOR = 'json_to_solo'

class BikiniSymbol(Solo48):
    icon_id = 'bikini-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bikini', 'symbol')

    def build(self):
        self.add_line('e0', (22, 11), (17, 16))
        self.add_line('e1', (24, 9), (31, 16))
        self.add_line('e2', (36, 22), (40, 27))
        self.add_line('e3', (26, 39), (22, 39))
        self.add_arc('e4-1', (17, 8), (20, 6), radius_x=4)
        self.add_line('e4-2', (20, 6), (24, 9))
        self.add_line('e4-3', (24, 9), (22, 11))
        self.add_line('e5', (17, 16), (11, 24))
        self.add_arc('e6', (11, 24), (22, 39), radius_x=20)
        self.add_arc('e7-1', (11, 24), (6, 35), radius_x=17, sweep=False)
        self.add_arc('e7-2', (6, 35), (13, 42), radius_x=7, sweep=False)
        self.add_line('e7-3', (13, 42), (22, 39))
        self.add_arc('e8-1', (31, 8), (28, 6), radius_x=4, sweep=False)
        self.add_line('e8-2', (28, 6), (24, 9))
        self.add_arc('e9', (31, 16), (36, 22), radius_x=35)
        self.add_line('e10-1', (40, 27), (42, 35))
        self.add_arc('e10-2', (42, 35), (35, 42), radius_x=7)
        self.add_line('e10-3', (35, 42), (30, 41))
        self.add_line('e10-4', (30, 41), (26, 39))
        self.add_arc('e11', (38, 25), (26, 39), radius_x=19, sweep=False)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e0', 'e5')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e7-1', 'e7-2', 'e7-3')
        self.add_contour('c3', 'e8-1', 'e8-2', 'e1', 'e9', 'e2', 'e10-1', 'e10-2', 'e10-3', 'e10-4')
        self.add_contour('c4', 'e11', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c4', 'c3')
