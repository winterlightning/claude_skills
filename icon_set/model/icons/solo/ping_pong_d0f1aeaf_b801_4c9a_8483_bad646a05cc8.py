"""Ping pong (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd0f1aeaf-b801-4c9a-8483-bad646a05cc8'
SOURCE_PATH = 'pictographic-primitives/video-games/ping pong_d0f1aeaf-b801-4c9a-8483-bad646a05cc8.svg'
AUTHOR = 'gpt-6'

class PingPong(Solo48):
    icon_id = 'ping-pong'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('ping', 'pong', 'video-games')

    def build(self):
        self.add_line('sym-e0', (24, 42), (24, 6))
        self.add_line('sym-e1', (24, 6), (40, 6))
        self.add_arc('sym-e2', (40, 6), (42, 8), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e3', (42, 8), (42, 40))
        self.add_arc('sym-e4', (42, 40), (40, 42), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e5', (40, 42), (8, 42))
        self.add_arc('sym-e7', (8, 42), (6, 40), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e8', (6, 40), (6, 8))
        self.add_arc('sym-e9', (6, 8), (8, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('sym-e10', (8, 6), (24, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', closed=False)
