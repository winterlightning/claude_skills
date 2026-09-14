"""Dash fast up large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef45cf2e-5e94-4067-a4b1-6061831c3128'
SOURCE_PATH = 'icons-json/arrows/dash fast up large head_ef45cf2e-5e94-4067-a4b1-6061831c3128.json'
AUTHOR = 'json_to_solo'

class DashFastUpLargeHeadArrows(Solo48):
    icon_id = 'dash-fast-up-large-head-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('dash', 'fast', 'up', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (34, 14), (40, 8))
        self.add_line('e1', (39, 10), (40, 8))
        self.add_line('e2', (44, 17), (40, 8))
        self.add_line('e3', (4, 40), (9, 40))
        self.add_line('e4', (14, 40), (19, 40))
        self.add_arc('e5', (24, 39), (39, 10), radius_x=30, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e5', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
