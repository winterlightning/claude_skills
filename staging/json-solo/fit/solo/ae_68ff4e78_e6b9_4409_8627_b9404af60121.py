"""Ae (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68ff4e78-e6b9-4409-8627-b9404af60121'
SOURCE_PATH = 'icons-json/symbol/Ae_68ff4e78-e6b9-4409-8627-b9404af60121.json'
AUTHOR = 'json_to_solo'

class AeSymbol(Solo48):
    icon_id = 'ae-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ae', 'symbol')

    def build(self):
        self.add_line('e0', (22, 40), (15, 10))
        self.add_line('e1', (11, 9), (4, 40))
        self.add_line('e2', (7, 29), (19, 29))
        self.add_line('e3-1', (15, 10), (13, 8))
        self.add_line('e3-2', (13, 8), (11, 9))
        self.add_arc('e4-1', (32, 30), (42, 30), radius_x=29, sweep=False)
        self.add_arc('e4-2', (42, 30), (44, 26), radius_x=5, sweep=False)
        self.add_arc('e4-3', (44, 26), (40, 20), radius_x=7, sweep=False)
        self.add_arc('e4-4', (40, 20), (32, 27), radius_x=7, sweep=False)
        self.add_arc('e4-5', (32, 27), (34, 38), radius_x=15, sweep=False)
        self.add_arc('e4-6', (34, 38), (35, 39), radius_x=5, sweep=False)
        self.add_line('e4-7', (35, 39), (39, 40))
        self.add_line('e4-8', (39, 40), (40, 40))
        self.add_arc('e4-9', (40, 40), (44, 36), radius_x=4, sweep=False)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e4-8', 'e4-9')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
