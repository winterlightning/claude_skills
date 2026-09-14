"""Paddle board (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97cda55a-4e3a-4bc4-b593-5316283a391c'
SOURCE_PATH = 'icons-json/outdoors/paddle board_97cda55a-4e3a-4bc4-b593-5316283a391c.json'
AUTHOR = 'json_to_solo'

class PaddleBoard(Solo48):
    icon_id = 'paddle-board'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('paddle', 'board', 'outdoors')

    def build(self):
        self.add_line('e0', (32, 4), (35, 4))
        self.add_line('e1', (38, 4), (35, 4))
        self.add_line('e2', (35, 29), (35, 4))
        self.add_line('e3', (16, 4), (15, 6))
        self.add_line('e4', (14, 44), (19, 44))
        self.add_arc('e5-1', (35, 29), (30, 40), radius_x=18, sweep=False)
        self.add_arc('e5-2', (30, 40), (34, 44), radius_x=4, sweep=False)
        self.add_line('e5-3', (34, 44), (39, 43))
        self.add_line('e5-4', (39, 43), (40, 41))
        self.add_arc('e5-5', (40, 41), (35, 29), radius_x=17, sweep=False)
        self.add_arc('e6-1', (15, 6), (10, 14), radius_x=29, sweep=False)
        self.add_line('e6-2', (10, 14), (8, 26))
        self.add_line('e6-3', (8, 26), (9, 34))
        self.add_arc('e6-4', (9, 34), (14, 44), radius_x=12, sweep=False)
        self.add_arc('e7-1', (19, 44), (24, 36), radius_x=10, sweep=False)
        self.add_arc('e7-2', (24, 36), (24, 15), radius_x=34, sweep=False)
        self.add_arc('e7-3', (24, 15), (16, 4), radius_x=13, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', closed=True)
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e4', 'e7-1', 'e7-2', 'e7-3', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
