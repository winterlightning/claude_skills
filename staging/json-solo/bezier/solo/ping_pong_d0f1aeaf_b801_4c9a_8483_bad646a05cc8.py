"""Ping pong (video-games), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0f1aeaf-b801-4c9a-8483-bad646a05cc8'
SOURCE_PATH = 'icons-json/video-games/ping pong_d0f1aeaf-b801-4c9a-8483-bad646a05cc8.json'
AUTHOR = 'json_to_solo'

class PingPongVideoGames(Solo48):
    icon_id = 'ping-pong-video-games'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('ping', 'pong', 'video-games')

    def build(self):
        self.add_line('sym-e0', (24, 42), (24, 6))
        self.add_line('sym-e1', (24, 6), (40, 6))
        self.add_bezier('sym-e2', (40, 6), ((41.055, 6.499), (41.444, 6.904), (42, 8)))
        self.add_line('sym-e3', (42, 8), (42, 40))
        self.add_bezier('sym-e4', (42, 40), ((41.534, 41.055), (40.998, 41.534), (40, 42)))
        self.add_line('sym-e5', (40, 42), (24, 42))
        self.add_line('sym-e6', (24, 42), (8, 42))
        self.add_bezier('sym-e7', (8, 42), ((7.002, 41.534), (6.466, 41.055), (6, 40)))
        self.add_line('sym-e8', (6, 40), (6, 8))
        self.add_bezier('sym-e9', (6, 8), ((6.556, 6.904), (6.945, 6.499), (8, 6)))
        self.add_line('sym-e10', (8, 6), (24, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
