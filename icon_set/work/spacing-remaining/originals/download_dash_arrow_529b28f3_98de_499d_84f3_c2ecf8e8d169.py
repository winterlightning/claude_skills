"""Download dash arrow (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '529b28f3-98de-499d-84f3-c2ecf8e8d169'
SOURCE_PATH = 'icons-json/arrows/download dash arrow_529b28f3-98de-499d-84f3-c2ecf8e8d169.json'
AUTHOR = 'json_to_solo'

class DownloadDashArrow(Solo48):
    icon_id = 'download-dash-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('download', 'dash', 'arrow', 'arrows')

    def build(self):
        self.add_line('e0', (24, 33), (24, 36))
        self.add_line('e1', (24, 36), (22, 34))
        self.add_line('e2', (24, 36), (26, 34))
        self.add_line('e3', (24, 26), (24, 29))
        self.add_line('e4', (24, 19), (24, 21))
        self.add_line('e5', (24, 11), (24, 14))
        self.add_line('e6', (24, 4), (24, 7))
        self.add_line('e7', (17, 29), (19, 31))
        self.add_line('e8', (30, 30), (28, 32))
        self.add_line('e9', (12, 25), (14, 27))
        self.add_line('e10', (35, 25), (33, 27))
        self.add_line('e11', (8, 44), (40, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.add_contour('c9', 'e9')
        self.add_contour('c10', 'e10')
        self.add_contour('c11', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
