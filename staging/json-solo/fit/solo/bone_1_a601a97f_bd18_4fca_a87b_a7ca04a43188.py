"""Bone 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a601a97f-bd18-4fca-a87b-a7ca04a43188'
SOURCE_PATH = 'icons-json/symbol/bone 1_a601a97f-bd18-4fca-a87b-a7ca04a43188.json'
AUTHOR = 'json_to_solo'

class Bone1Symbol(Solo48):
    icon_id = 'bone-1-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bone', 'symbol')

    def build(self):
        self.add_line('e0', (33, 26), (17, 31))
        self.add_line('e1', (15, 22), (31, 17))
        self.add_arc('e2-1', (31, 17), (36, 8), radius_x=7)
        self.add_arc('e2-2', (36, 8), (42, 14), radius_x=6)
        self.add_arc('e2-3', (42, 14), (41, 19), radius_x=7)
        self.add_arc('e2-4', (41, 19), (44, 24), radius_x=8)
        self.add_arc('e2-5', (44, 24), (44, 26), radius_x=11, sweep=False)
        self.add_arc('e2-6', (44, 26), (39, 32), radius_x=7)
        self.add_arc('e2-7', (39, 32), (33, 26), radius_x=6)
        self.add_arc('e3-1', (17, 31), (11, 40), radius_x=7)
        self.add_arc('e3-2', (11, 40), (6, 35), radius_x=6)
        self.add_arc('e3-3', (6, 35), (7, 29), radius_x=8)
        self.add_arc('e3-4', (7, 29), (4, 23), radius_x=8)
        self.add_line('e3-5', (4, 23), (5, 19))
        self.add_arc('e3-6', (5, 19), (9, 16), radius_x=5)
        self.add_arc('e3-7', (9, 16), (15, 22), radius_x=6)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e1', closed=True)
