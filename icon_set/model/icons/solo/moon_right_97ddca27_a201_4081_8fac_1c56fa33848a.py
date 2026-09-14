"""Moon right (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97ddca27-a201-4081-8fac-1c56fa33848a'
SOURCE_PATH = 'icons-json/symbol/moon right_97ddca27-a201-4081-8fac-1c56fa33848a.json'
AUTHOR = 'json_to_solo'

class MoonRight(Solo48):
    icon_id = 'moon-right'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('moon', 'right', 'symbol')

    def build(self):
        self.add_line('e0', (8, 42), (14, 40))
        self.add_line('e1', (12, 7), (8, 6))
        self.add_arc('e2-1', (8, 6), (18, 4), radius_x=33)
        self.add_arc('e2-2', (18, 4), (31, 8), radius_x=24)
        self.add_arc('e2-3', (31, 8), (40, 23), radius_x=20)
        self.add_arc('e2-4', (40, 23), (40, 26), radius_x=43, sweep=False)
        self.add_arc('e2-5', (40, 26), (38, 32), radius_x=16)
        self.add_arc('e2-6', (38, 32), (27, 42), radius_x=22)
        self.add_arc('e2-7', (27, 42), (18, 44), radius_x=22)
        self.add_arc('e2-8', (18, 44), (8, 42), radius_x=35)
        self.add_arc('e3-1', (14, 40), (25, 21), radius_x=17, sweep=False)
        self.add_arc('e3-2', (25, 21), (12, 7), radius_x=18, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e0', 'e3-1', 'e3-2', 'e1', closed=True)
