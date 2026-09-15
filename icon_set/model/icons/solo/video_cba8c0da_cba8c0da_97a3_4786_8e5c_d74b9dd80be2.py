"""Video (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cba8c0da-97a3-4786-8e5c-d74b9dd80be2'
SOURCE_PATH = 'icons-json/symbol/video_cba8c0da-97a3-4786-8e5c-d74b9dd80be2.json'
AUTHOR = 'gpt-6'

class VideoCba8c0da(Solo48):
    icon_id = 'video-cba8c0da'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('video', 'symbol')

    def build(self):
        self.add_line('sym-e0', (33, 19), (33, 29))
        self.add_line('sym-e1', (33, 29), (44, 39))
        self.add_line('sym-e2', (44, 39), (44, 9))
        self.add_line('sym-e4', (44, 9), (33, 19))
        self.add_line('sym-e5', (33, 19), (33, 13))
        self.add_line('sym-e6', (33, 13), (31, 8))
        self.add_line('sym-e7', (31, 8), (8, 8))
        self.add_arc('sym-e10', (8, 8), (4, 13), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('sym-e11', (4, 13), (4, 35))
        self.add_arc('sym-e13', (4, 35), (8, 40), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('sym-e14', (8, 40), (31, 40))
        self.add_line('sym-e17', (31, 40), (33, 35))
        self.add_line('sym-e18', (33, 35), (33, 29))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e17', 'sym-e18', closed=False)
