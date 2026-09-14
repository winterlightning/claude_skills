"""Double arrow top 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f48252b8-8cf1-53e8-9803-326efcd0feb3'
SOURCE_PATH = 'icons-json/arrows/double arrow top 2_f48252b8-8cf1-53e8-9803-326efcd0feb3.json'
AUTHOR = 'json_to_solo'

class DoubleArrowTop2(Solo48):
    icon_id = 'double-arrow-top-2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'top', 'arrows')

    def build(self):
        self.add_line('sym-e0', (24, 22), (21, 24))
        self.add_line('sym-e1', (21, 24), (4, 40))
        self.add_line('sym-e2', (4, 25), (22, 9))
        self.add_arc('sym-e3', (22, 9), (24, 8), radius_x=3)
        self.add_arc('sym-e8', (24, 8), (26, 9), radius_x=3)
        self.add_line('sym-e9', (26, 9), (44, 25))
        self.add_line('sym-e10', (24, 22), (27, 24))
        self.add_line('sym-e11', (27, 24), (44, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10', 'sym-e11')
        self.relate('connect', 'sym-c0', 'sym-c2')
