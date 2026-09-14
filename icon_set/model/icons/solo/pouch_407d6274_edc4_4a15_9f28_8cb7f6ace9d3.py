"""Pouch (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '407d6274-edc4-4a15-9f28-8cb7f6ace9d3'
SOURCE_PATH = 'icons-json/video-games/pouch_407d6274-edc4-4a15-9f28-8cb7f6ace9d3.json'
AUTHOR = 'json_to_solo'

class PouchVideoGames(Solo48):
    icon_id = 'pouch-video-games'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('pouch', 'video-games')

    def build(self):
        self.add_line('sym-e0', (24, 13), (25, 13))
        self.add_line('sym-e1', (25, 13), (29, 13))
        self.add_arc('sym-e2', (29, 13), (33, 16), radius_x=17)
        self.add_arc('sym-e3', (33, 16), (40, 32), radius_x=25)
        self.add_arc('sym-e4', (40, 32), (40, 33), radius_x=34, sweep=False)
        self.add_line('sym-e5', (40, 33), (40, 34))
        self.add_arc('sym-e6', (40, 34), (36, 42), radius_x=11)
        self.add_arc('sym-e7', (36, 42), (30, 44), radius_x=10)
        self.add_line('sym-e8', (30, 44), (29, 44))
        self.add_line('sym-e9', (29, 44), (28, 44))
        self.add_line('sym-e10', (28, 44), (24, 44))
        self.add_line('sym-e11', (24, 44), (20, 44))
        self.add_line('sym-e12', (20, 44), (19, 44))
        self.add_line('sym-e13', (19, 44), (18, 44))
        self.add_arc('sym-e14', (18, 44), (12, 42), radius_x=10)
        self.add_arc('sym-e15', (12, 42), (8, 34), radius_x=11)
        self.add_line('sym-e16', (8, 34), (8, 33))
        self.add_line('sym-e17', (8, 33), (8, 32))
        self.add_arc('sym-e18', (8, 32), (15, 16), radius_x=26)
        self.add_arc('sym-e19', (15, 16), (19, 13), radius_x=18)
        self.add_line('sym-e20', (19, 13), (23, 13))
        self.add_line('sym-e21', (23, 13), (24, 13))
        self.add_line('sym-e22', (27, 15), (25, 13))
        self.add_arc('sym-e23', (29, 13), (32, 7), radius_x=25, sweep=False)
        self.add_arc('sym-e24', (32, 7), (30, 4), radius_x=3, sweep=False)
        self.add_line('sym-e25', (30, 4), (29, 4))
        self.add_line('sym-e26', (29, 4), (27, 4))
        self.add_line('sym-e27', (27, 4), (24, 4))
        self.add_line('sym-e28', (24, 4), (21, 4))
        self.add_line('sym-e29', (21, 4), (19, 4))
        self.add_line('sym-e30', (19, 4), (18, 4))
        self.add_arc('sym-e31', (18, 4), (16, 7), radius_x=3, sweep=False)
        self.add_arc('sym-e32', (16, 7), (19, 13), radius_x=25, sweep=False)
        self.add_line('sym-e33', (21, 15), (23, 13))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
        self.add_contour('sym-c1', 'sym-e22')
        self.add_contour('sym-c2', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32')
        self.add_contour('sym-c3', 'sym-e33')
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
