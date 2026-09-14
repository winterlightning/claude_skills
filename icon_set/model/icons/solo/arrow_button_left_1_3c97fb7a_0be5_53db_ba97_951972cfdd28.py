"""Arrow button left 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c97fb7a-0be5-53db-ba97-951972cfdd28'
SOURCE_PATH = 'icons-json/arrows/arrow button left 1_3c97fb7a-0be5-53db-ba97-951972cfdd28.json'
AUTHOR = 'json_to_solo'

class ArrowButtonLeft1(Solo48):
    icon_id = 'arrow-button-left-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'button', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (40, 44), (8, 25))
        self.add_line('e1', (10, 23), (40, 4))
        self.add_arc('e2', (8, 25), (10, 23), radius_x=2)
        self.add_contour('c0', 'e0', 'e2', 'e1')
