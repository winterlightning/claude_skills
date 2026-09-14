"""Tank top (clothes), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39361dc4-7a27-511a-8675-7fff10adc8f5'
SOURCE_PATH = 'icons-json/clothes/tank top_39361dc4-7a27-511a-8675-7fff10adc8f5.json'
AUTHOR = 'json_to_solo'

class TankTopClothes(Solo48):
    icon_id = 'tank-top-clothes'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('tank', 'top', 'clothes')

    def build(self):
        self.add_line('e0', (36, 4), (36, 9))
        self.add_line('e1', (39, 31), (40, 40))
        self.add_line('e2', (8, 39), (9, 31))
        self.add_line('e3', (9, 31), (9, 28))
        self.add_line('e4', (9, 28), (8, 19))
        self.add_line('e5', (33, 4), (36, 4))
        self.add_arc('e6-1', (36, 9), (40, 17), radius_x=9, sweep=False)
        self.add_arc('e6-2', (40, 17), (39, 31), radius_x=49, sweep=False)
        self.add_line('e7-1', (40, 40), (40, 42))
        self.add_arc('e7-2', (40, 42), (38, 43), radius_x=3)
        self.add_line('e7-3', (38, 43), (24, 44))
        self.add_line('e7-4', (24, 44), (10, 43))
        self.add_arc('e7-5', (10, 43), (8, 42), radius_x=3)
        self.add_line('e7-6', (8, 42), (8, 40))
        self.add_line('e7-7', (8, 40), (8, 39))
        self.add_line('e8-1', (8, 19), (8, 17))
        self.add_line('e8-2', (8, 17), (11, 13))
        self.add_line('e8-3', (11, 13), (13, 4))
        self.add_arc('e8-4', (13, 4), (14, 4), radius_x=19, sweep=False)
        self.add_line('e8-5', (14, 4), (16, 5))
        self.add_line('e8-6', (16, 5), (18, 12))
        self.add_arc('e8-7', (18, 12), (23, 15), radius_x=6, sweep=False)
        self.add_arc('e8-8', (23, 15), (30, 12), radius_x=7, sweep=False)
        self.add_line('e8-9', (30, 12), (33, 4))
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e7-6', 'e7-7', 'e2', 'e3', 'e4', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e8-5', 'e8-6', 'e8-7', 'e8-8', 'e8-9', 'e5', closed=True)
