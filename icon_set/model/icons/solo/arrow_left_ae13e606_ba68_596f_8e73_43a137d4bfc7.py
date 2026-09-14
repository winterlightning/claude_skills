"""Arrow left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae13e606-ba68-596f-8e73-43a137d4bfc7'
SOURCE_PATH = 'icons-json/arrows/arrow left_ae13e606-ba68-596f-8e73-43a137d4bfc7.json'
AUTHOR = 'json_to_solo'

class ArrowLeftAe13e606(Solo48):
    icon_id = 'arrow-left-ae13e606'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (23, 8), (4, 24))
        self.add_line('e1', (22, 40), (4, 24))
        self.add_line('e2', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
