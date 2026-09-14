"""Chilli (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8658def3-7931-4cec-bff9-b70a989154e1'
SOURCE_PATH = 'icons-json/symbol/chilli_8658def3-7931-4cec-bff9-b70a989154e1.json'
AUTHOR = 'json_to_solo'

class ChilliSymbol(Solo48):
    icon_id = 'chilli-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('chilli', 'symbol')

    def build(self):
        self.add_line('e0', (31, 19), (26, 23))
        self.add_line('e1', (12, 28), (6, 28))
        self.add_arc('e2-1', (40, 8), (44, 12), radius_x=4)
        self.add_arc('e2-2', (44, 12), (40, 18), radius_x=7)
        self.add_arc('e3', (26, 23), (12, 28), radius_x=22)
        self.add_arc('e4-1', (6, 28), (4, 30), radius_x=2, sweep=False)
        self.add_arc('e4-2', (4, 30), (20, 40), radius_x=18, sweep=False)
        self.add_arc('e4-3', (20, 40), (41, 28), radius_x=25, sweep=False)
        self.add_arc('e4-4', (41, 28), (40, 18), radius_x=7, sweep=False)
        self.add_arc('e4-5', (40, 18), (31, 19), radius_x=8, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2')
        self.add_contour('c1', 'e0', 'e3', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', closed=True)
        self.relate('connect', 'c0', 'c1')
