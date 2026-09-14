"""Arrow button right 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51d9ca4f-68bd-5384-b189-4bd7ab489121'
SOURCE_PATH = 'icons-json/arrows/arrow button right 1_51d9ca4f-68bd-5384-b189-4bd7ab489121.json'
AUTHOR = 'json_to_solo'

class ArrowButtonRight1(Solo48):
    icon_id = 'arrow-button-right-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'button', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (8, 4), (40, 23))
        self.add_line('e1', (38, 25), (8, 44))
        self.add_arc('e2', (40, 23), (38, 25), radius_x=2)
        self.add_contour('c0', 'e0', 'e2', 'e1')
