"""Batch-04/cd broken (computers), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35902389-7674-5992-88ac-62b704c11f7f'
SOURCE_PATH = 'icons-json/computers/batch-04/cd broken_35902389-7674-5992-88ac-62b704c11f7f.json'
AUTHOR = 'json_to_solo'

class Batch04CdBroken(Solo48):
    icon_id = 'batch-04-cd-broken'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'cd', 'broken', 'computers')

    def build(self):
        self.add_line('e0', (28, 7), (21, 19))
        self.add_line('e1', (21, 19), (31, 17))
        self.add_line('e2', (31, 17), (19, 31))
        self.add_bezier('e3', (22, 6), ((21.902, 6), (22.175, 6.008), (22.077, 6.016)), ((20.801, 6.016), (19.426, 6.319), (18.207, 6.679)), ((11.253, 8.725), (6.008, 15.483), (6.008, 22.814)), ((6.008, 22.999), (6, 23.184), (6, 23.362)), ((6, 23.364), (6, 23.367), (6, 23.37)), ((6, 23.73), (6.016, 24.09), (6.016, 24.442)), ((6.016, 32.91), (12.824, 40.519), (21.104, 41.755)), ((21.807, 41.861), (22.552, 42), (23.264, 42)), ((23.266, 42), (23.269, 42), (23.271, 42)), ((23.432, 42), (23.593, 41.992), (23.755, 41.992)), ((33.605, 41.992), (41.984, 33.982), (41.984, 24.008)), ((41.984, 23.823), (42, 23.646), (42, 23.461)), ((42, 23.458), (42, 23.455), (42, 23.452)), ((41.992, 23.337), (41.992, 23.223), (41.984, 23.108)), ((41.984, 17.258), (38.457, 10.999), (33.237, 8.307)), ((32.329, 7.833), (29.703, 6.646), (28.778, 6.646)), ((28.508, 6.638), (28.237, 6.959), (28, 7)))
        self.add_bezier('e4', (19, 31), ((22.24, 30.092), (25.104, 29.825), (28, 28)))
        self.add_contour('c0', 'e3', 'e0', 'e1', 'e2', 'e4')
