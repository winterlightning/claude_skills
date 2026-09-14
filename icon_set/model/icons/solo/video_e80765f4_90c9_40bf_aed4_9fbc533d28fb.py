"""Video (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e80765f4-90c9-40bf-aed4-9fbc533d28fb'
SOURCE_PATH = 'icons-json/symbol/video_e80765f4-90c9-40bf-aed4-9fbc533d28fb.json'
AUTHOR = 'json_to_solo'

class VideoE80765f4(Solo48):
    icon_id = 'video-e80765f4'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('video', 'symbol')

    def build(self):
        self.add_line('e0', (33, 19), (44, 13))
        self.add_line('e1', (44, 13), (44, 35))
        self.add_line('e2', (44, 35), (33, 29))
        self.add_line('e3', (29, 40), (9, 40))
        self.add_line('e4', (4, 33), (4, 15))
        self.add_line('e5', (10, 8), (28, 8))
        self.add_line('e6', (33, 14), (33, 29))
        self.add_arc('e7', (33, 29), (29, 40), radius_x=10)
        self.add_arc('e8-1', (9, 40), (5, 37), radius_x=5)
        self.add_arc('e8-2', (5, 37), (4, 34), radius_x=8)
        self.add_line('e8-3', (4, 34), (4, 33))
        self.add_arc('e9-1', (4, 15), (5, 11), radius_x=9)
        self.add_arc('e9-2', (5, 11), (9, 8), radius_x=5)
        self.add_line('e9-3', (9, 8), (10, 8))
        self.add_arc('e10', (28, 8), (33, 14), radius_x=6)
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e7', 'e3', 'e8-1', 'e8-2', 'e8-3', 'e4', 'e9-1', 'e9-2', 'e9-3', 'e5', 'e10', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
