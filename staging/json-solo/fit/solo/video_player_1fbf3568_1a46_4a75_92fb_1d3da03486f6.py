"""Video player (video), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fbf3568-1a46-4a75-92fb-1d3da03486f6'
SOURCE_PATH = 'icons-json/video/video player_1fbf3568-1a46-4a75-92fb-1d3da03486f6.json'
AUTHOR = 'json_to_solo'

class VideoPlayerVideo(Solo48):
    icon_id = 'video-player-video'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('video', 'player')

    def build(self):
        self.add_line('e0', (39, 9), (31, 8))
        self.add_line('e1', (4, 28), (5, 36))
        self.add_line('e2', (43, 36), (44, 28))
        self.add_line('e3', (30, 25), (19, 31))
        self.add_line('e4', (19, 31), (19, 17))
        self.add_line('e5', (19, 17), (30, 23))
        self.add_line('e6-1', (31, 8), (19, 8))
        self.add_arc('e6-2', (19, 8), (6, 10), radius_x=44, sweep=False)
        self.add_arc('e6-3', (6, 10), (5, 12), radius_x=3, sweep=False)
        self.add_arc('e6-4', (5, 12), (4, 23), radius_x=79, sweep=False)
        self.add_line('e6-5', (4, 23), (4, 28))
        self.add_arc('e7-1', (5, 36), (10, 39), radius_x=4, sweep=False)
        self.add_arc('e7-2', (10, 39), (22, 40), radius_x=77, sweep=False)
        self.add_line('e7-3', (22, 40), (37, 39))
        self.add_arc('e7-4', (37, 39), (43, 36), radius_x=6, sweep=False)
        self.add_line('e8-1', (44, 28), (43, 12))
        self.add_arc('e8-2', (43, 12), (39, 9), radius_x=3, sweep=False)
        self.add_arc('e11', (30, 23), (30, 25), radius_x=1)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e2', 'e8-1', 'e8-2', closed=True)
        self.add_contour('c1', 'e3', 'e4', 'e5', 'e11', closed=True)
