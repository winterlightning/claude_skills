"""Arrow corner right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f974b62e-0d33-55cb-be2b-f88ed0faccf9'
SOURCE_PATH = 'icons-json/arrows/arrow corner right_f974b62e-0d33-55cb-be2b-f88ed0faccf9.json'
AUTHOR = 'json_to_solo'

class ArrowCornerRightArrows(Solo48):
    icon_id = 'arrow-corner-right-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'corner', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (40, 44), (40, 4))
        self.add_line('e1', (40, 4), (8, 4))
        self.add_contour('c0', 'e0', 'e1')
