"""Barrier (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80d907cf-11f8-4104-a791-525bc0837b34'
SOURCE_PATH = 'icons-json/symbol/barrier_80d907cf-11f8-4104-a791-525bc0837b34.json'
AUTHOR = 'json_to_solo'

class BarrierSymbol(Solo48):
    icon_id = 'barrier-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('barrier', 'symbol')

    def build(self):
        self.add_line('e0', (44, 16), (44, 27))
        self.add_line('e1', (44, 27), (4, 27))
        self.add_line('e2', (4, 27), (4, 16))
        self.add_line('e3', (4, 16), (44, 16))
        self.add_line('e4', (39, 16), (27, 27))
        self.add_line('e5', (21, 16), (9, 27))
        self.add_line('e6', (9, 27), (9, 40))
        self.add_line('e7', (39, 40), (39, 27))
        self.add_dot('e8', (11, 8))
        self.add_dot('e9', (37, 8))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5', 'e6')
        self.add_contour('c3', 'e7')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'c0')
