"""Charging (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'adb38709-2d40-4069-b4f6-36531140d2ed'
SOURCE_PATH = 'icons-json/symbol/charging_adb38709-2d40-4069-b4f6-36531140d2ed.json'
AUTHOR = 'json_to_solo'

class Charging(Solo48):
    icon_id = 'charging'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('charging', 'symbol')

    def build(self):
        self.add_line('e0', (8, 27), (8, 40))
        self.add_line('e1', (12, 44), (36, 44))
        self.add_line('e2', (40, 40), (40, 27))
        self.add_line('e3', (8, 27), (40, 27))
        self.add_line('e4', (8, 27), (8, 13))
        self.add_line('e5', (18, 9), (18, 4))
        self.add_line('e6', (18, 4), (30, 4))
        self.add_line('e7', (30, 4), (30, 9))
        self.add_line('e8', (40, 12), (40, 27))
        self.add_arc('e9', (8, 40), (12, 44), radius_x=5, sweep=False)
        self.add_arc('e10', (36, 44), (40, 40), radius_x=4, sweep=False)
        self.add_arc('e11-1', (8, 13), (10, 10), radius_x=4)
        self.add_line('e11-2', (10, 10), (18, 9))
        self.add_arc('e12-1', (30, 9), (40, 11), radius_x=12)
        self.add_line('e12-2', (40, 11), (40, 12))
        self.add_contour('c0', 'e0', 'e9', 'e1', 'e10', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e11-1', 'e11-2', 'e5', 'e6', 'e7', 'e12-1', 'e12-2', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
