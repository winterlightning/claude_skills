"""Steady down large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17a4f3a7-12ec-4175-acb5-bbb0c55593a0'
SOURCE_PATH = 'icons-json/arrows/steady down large head_17a4f3a7-12ec-4175-acb5-bbb0c55593a0.json'
AUTHOR = 'json_to_solo'

class SteadyDownLargeHeadArrows(Solo48):
    icon_id = 'steady-down-large-head-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('steady', 'down', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (8, 27), (18, 27))
        self.add_line('e1', (14, 39), (18, 44))
        self.add_line('e2', (23, 39), (18, 44))
        self.add_line('e3', (18, 27), (18, 14))
        self.add_line('e4', (31, 27), (18, 27))
        self.add_line('e5', (18, 27), (18, 44))
        self.add_arc('e6-1', (18, 14), (29, 4), radius_x=12)
        self.add_arc('e6-2', (29, 4), (40, 15), radius_x=11)
        self.add_line('e6-3', (40, 15), (38, 22))
        self.add_arc('e6-4', (38, 22), (31, 27), radius_x=10)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e4', closed=True)
        self.add_contour('c4', 'e5')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
