"""Video (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77cac2c6-9ef1-4a3f-85bf-963aeda09df3'
SOURCE_PATH = 'icons-json/symbol/video_77cac2c6-9ef1-4a3f-85bf-963aeda09df3.json'
AUTHOR = 'json_to_solo'

class Video77cac2c6(Solo48):
    icon_id = 'video-77cac2c6'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('video', 'symbol')

    def build(self):
        self.add_line('e0', (33, 26), (44, 34))
        self.add_line('e1', (44, 34), (44, 15))
        self.add_line('e2', (44, 15), (33, 23))
        self.add_line('e3', (9, 40), (31, 40))
        self.add_line('e4', (33, 35), (33, 12))
        self.add_line('e5', (29, 8), (8, 8))
        self.add_line('e6', (4, 13), (4, 36))
        self.add_arc('e7-1', (4, 36), (8, 40), radius_x=4, sweep=False)
        self.add_arc('e7-2', (8, 40), (9, 40), radius_x=20)
        self.add_arc('e8', (31, 40), (33, 35), radius_x=4, sweep=False)
        self.add_arc('e9-1', (33, 12), (30, 8), radius_x=4, sweep=False)
        self.add_arc('e9-2', (30, 8), (29, 8), radius_x=59)
        self.add_line('e10-1', (8, 8), (5, 9))
        self.add_line('e10-2', (5, 9), (4, 13))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e7-1', 'e7-2', 'e3', 'e8', 'e4', 'e9-1', 'e9-2', 'e5', 'e10-1', 'e10-2', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
