"""Arrow left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9626ad56-bad2-531b-89eb-4b608917010a'
SOURCE_PATH = 'icons-json/arrows/arrow left_9626ad56-bad2-531b-89eb-4b608917010a.json'
AUTHOR = 'json_to_solo'

class ArrowLeft(Solo48):
    icon_id = 'arrow-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (14, 8), (4, 24))
        self.add_line('e1', (14, 40), (4, 24))
        self.add_line('e2', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
