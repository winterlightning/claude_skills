"""Footwear sock (clothes), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b273457-d5cd-507b-9092-a6e989db84d5'
SOURCE_PATH = 'icons-json/clothes/footwear sock_9b273457-d5cd-507b-9092-a6e989db84d5.json'
AUTHOR = 'json_to_solo'

class FootwearSockClothes(Solo48):
    icon_id = 'footwear-sock-clothes'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('footwear', 'sock', 'clothes')

    def build(self):
        self.add_line('e0', (26, 4), (26, 16))
        self.add_line('e1', (27, 21), (32, 32))
        self.add_line('e2', (33, 44), (31, 44))
        self.add_line('e3', (16, 31), (11, 29))
        self.add_line('e4', (11, 13), (11, 4))
        self.add_line('e5', (11, 4), (26, 4))
        self.add_line('e6', (26, 16), (27, 21))
        self.add_line('e7-1', (32, 32), (40, 39))
        self.add_line('e7-2', (40, 39), (39, 42))
        self.add_arc('e7-3', (39, 42), (36, 44), radius_x=4)
        self.add_line('e7-4', (36, 44), (33, 44))
        self.add_arc('e8-1', (31, 44), (25, 42), radius_x=11)
        self.add_line('e8-2', (25, 42), (16, 31))
        self.add_line('e9-1', (11, 29), (9, 27))
        self.add_line('e9-2', (9, 27), (8, 23))
        self.add_line('e9-3', (8, 23), (11, 13))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e2', 'e8-1', 'e8-2', 'e3', 'e9-1', 'e9-2', 'e9-3', 'e4', 'e5', closed=True)
