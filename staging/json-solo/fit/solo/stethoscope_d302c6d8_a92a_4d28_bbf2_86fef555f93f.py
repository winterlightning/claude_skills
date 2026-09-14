"""Stethoscope (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd302c6d8-a92a-4d28-bbf2-86fef555f93f'
SOURCE_PATH = 'icons-json/symbol/stethoscope_d302c6d8-a92a-4d28-bbf2-86fef555f93f.json'
AUTHOR = 'json_to_solo'

class StethoscopeSymbol(Solo48):
    icon_id = 'stethoscope-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('stethoscope', 'symbol')

    def build(self):
        self.add_line('e0', (6, 10), (6, 17))
        self.add_line('e1', (27, 9), (27, 17))
        self.add_line('e2', (38, 21), (38, 31))
        self.add_arc('e3-top', (34, 17), (42, 17), radius_x=4)
        self.add_arc('e3-bottom', (42, 17), (34, 17), radius_x=4)
        self.add_arc('e4', (11, 6), (6, 10), radius_x=6, sweep=False)
        self.add_arc('e5', (6, 17), (17, 27), radius_x=11, sweep=False)
        self.add_arc('e6', (22, 6), (27, 9), radius_x=6)
        self.add_arc('e7', (27, 17), (17, 27), radius_x=10)
        self.add_arc('e8-1', (38, 31), (27, 42), radius_x=11)
        self.add_arc('e8-2', (27, 42), (17, 27), radius_x=11)
        self.add_contour('c0', 'e4', 'e0', 'e5')
        self.add_contour('c1', 'e6', 'e1', 'e7')
        self.add_contour('c2', 'e2', 'e8-1', 'e8-2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'e3')
