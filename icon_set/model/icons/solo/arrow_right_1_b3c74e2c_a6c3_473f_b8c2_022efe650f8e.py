"""Arrow right 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3c74e2c-a6c3-473f-b8c2-022efe650f8e'
SOURCE_PATH = 'icons-json/arrows/arrow right 1_b3c74e2c-a6c3-473f-b8c2-022efe650f8e.json'
AUTHOR = 'json_to_solo'

class ArrowRight1(Solo48):
    icon_id = 'arrow-right-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (8, 4), (40, 23))
        self.add_line('e1', (38, 25), (8, 44))
        self.add_arc('e2', (40, 23), (38, 25), radius_x=2)
        self.add_contour('c0', 'e0', 'e2', 'e1')
