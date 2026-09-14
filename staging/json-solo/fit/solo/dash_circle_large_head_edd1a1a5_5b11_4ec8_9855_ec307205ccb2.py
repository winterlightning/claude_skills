"""Dash circle large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'edd1a1a5-5b11-4ec8-9855-ec307205ccb2'
SOURCE_PATH = 'icons-json/arrows/dash circle large head_edd1a1a5-5b11-4ec8-9855-ec307205ccb2.json'
AUTHOR = 'json_to_solo'

class DashCircleLargeHeadArrows(Solo48):
    icon_id = 'dash-circle-large-head-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('dash', 'circle', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (17, 32), (10, 27))
        self.add_line('e1', (4, 32), (9, 28))
        self.add_line('e2', (9, 28), (10, 27))
        self.add_arc('e3-1', (9, 22), (26, 8), radius_x=18)
        self.add_line('e3-2', (26, 8), (35, 10))
        self.add_arc('e3-3', (35, 10), (40, 14), radius_x=18)
        self.add_line('e3-4', (40, 14), (43, 18))
        self.add_line('e3-5', (43, 18), (44, 24))
        self.add_arc('e3-6', (44, 24), (39, 35), radius_x=15)
        self.add_arc('e3-7', (39, 35), (26, 40), radius_x=20)
        self.add_line('e3-8', (26, 40), (17, 38))
        self.add_arc('e3-9', (17, 38), (11, 33), radius_x=12)
        self.add_arc('e3-10', (11, 33), (10, 27), radius_x=9)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e3-10')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
