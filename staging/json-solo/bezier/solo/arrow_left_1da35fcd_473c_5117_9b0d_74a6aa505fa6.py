"""Arrow left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1da35fcd-473c-5117-9b0d-74a6aa505fa6'
SOURCE_PATH = 'icons-json/arrows/arrow left_1da35fcd-473c-5117-9b0d-74a6aa505fa6.json'
AUTHOR = 'json_to_solo'

class ArrowLeft(Solo48):
    icon_id = 'arrow-left'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (40, 4), (8, 24))
        self.add_line('e1', (8, 24), (40, 44))
        self.add_contour('c0', 'e0', 'e1')
