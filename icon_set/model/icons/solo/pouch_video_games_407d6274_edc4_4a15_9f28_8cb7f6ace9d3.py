"""Pouch (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '407d6274-edc4-4a15-9f28-8cb7f6ace9d3'
SOURCE_PATH = 'icons-json/video-games/pouch_407d6274-edc4-4a15-9f28-8cb7f6ace9d3.json'
AUTHOR = 'gpt-6'

class PouchVideoGames(Solo48):
    icon_id = 'pouch-video-games'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('pouch', 'video-games')

    def build(self):
        self.add_line('sym-e0', (24, 13), (29, 13))
        self.add_arc('sym-e2', (29, 13), (33, 16), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_arc('sym-e3', (33, 16), (40, 32), radius_x=25, radius_y=25, large_arc=False, sweep=True)
        self.add_arc('sym-e4', (40, 32), (40, 33), radius_x=34, radius_y=34, large_arc=False, sweep=False)
        self.add_line('sym-e5', (40, 33), (40, 34))
        self.add_arc('sym-e6', (40, 34), (36, 42), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('sym-e7', (36, 42), (30, 44), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('sym-e8', (30, 44), (18, 44))
        self.add_arc('sym-e14', (18, 44), (12, 42), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('sym-e15', (12, 42), (8, 34), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('sym-e16', (8, 34), (8, 32))
        self.add_arc('sym-e18', (8, 32), (15, 16), radius_x=26, radius_y=26, large_arc=False, sweep=True)
        self.add_arc('sym-e19', (15, 16), (19, 13), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('sym-e20', (19, 13), (24, 13))
        self.add_line('sym-e22', (27, 15), (25, 13))
        self.add_arc('sym-e23', (29, 13), (32, 7), radius_x=25, radius_y=25, large_arc=False, sweep=False)
        self.add_arc('sym-e24', (32, 7), (30, 4), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e25', (30, 4), (18, 4))
        self.add_arc('sym-e31', (18, 4), (16, 7), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('sym-e32', (16, 7), (19, 13), radius_x=25, radius_y=25, large_arc=False, sweep=False)
        self.add_line('sym-e33', (21, 15), (23, 13))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e20', closed=True)
        self.add_contour('sym-c1', 'sym-e22', closed=False)
        self.add_contour('sym-c2', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e31', 'sym-e32', closed=False)
        self.add_contour('sym-c3', 'sym-e33', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
