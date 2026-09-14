"""Pin (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76f7fdb5-5122-45e4-a53b-be1029308735'
SOURCE_PATH = 'icons-json/interface-essential/pin_76f7fdb5-5122-45e4-a53b-be1029308735.json'
AUTHOR = 'json_to_solo'

class Pin76f7fdb5(Solo48):
    icon_id = 'pin-76f7fdb5'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('pin', 'interface-essential')

    def build(self):
        self.add_line('e0', (20, 39), (15, 33))
        self.add_line('e1', (36, 29), (31, 36))
        self.add_line('e2', (30, 37), (24, 44))
        self.add_line('e3', (24, 44), (22, 42))
        self.add_arc('e4-top', (18, 19), (30, 19), radius_x=6, radius_y=5)
        self.add_arc('e4-bottom', (30, 19), (18, 19), radius_x=6, radius_y=5)
        self.add_arc('e5', (22, 42), (20, 39), radius_x=79, sweep=False)
        self.add_arc('e6-1', (15, 33), (8, 19), radius_x=21)
        self.add_arc('e6-2', (8, 19), (9, 14), radius_x=13)
        self.add_arc('e6-3', (9, 14), (13, 8), radius_x=15)
        self.add_arc('e6-4', (13, 8), (18, 5), radius_x=17)
        self.add_line('e6-5', (18, 5), (24, 4))
        self.add_line('e6-6', (24, 4), (32, 6))
        self.add_arc('e6-7', (32, 6), (40, 19), radius_x=15)
        self.add_arc('e6-8', (40, 19), (36, 29), radius_x=15)
        self.add_line('e7', (31, 36), (30, 37))
        self.add_contour('c0', 'e5', 'e0', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7', 'e6-8', 'e1', 'e7', 'e2', 'e3', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
