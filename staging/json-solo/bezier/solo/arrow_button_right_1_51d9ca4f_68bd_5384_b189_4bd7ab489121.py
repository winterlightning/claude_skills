"""Arrow button right 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51d9ca4f-68bd-5384-b189-4bd7ab489121'
SOURCE_PATH = 'icons-json/arrows/arrow button right 1_51d9ca4f-68bd-5384-b189-4bd7ab489121.json'
AUTHOR = 'json_to_solo'

class ArrowButtonRight1Arrows(Solo48):
    icon_id = 'arrow-button-right-1-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'button', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (8, 4), (40, 23))
        self.add_line('e1', (38, 25), (8, 44))
        self.add_bezier('e2', (40, 23), ((40, 23.164), (40, 23.427), (40, 23.591)), ((40, 24.373), (38.8, 24.5), (38, 25)))
        self.add_contour('c0', 'e0', 'e2', 'e1')
