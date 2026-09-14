"""Arrow corner bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd850060-547e-5eb4-96ec-5dd3a191fde4'
SOURCE_PATH = 'icons-json/arrows/arrow corner bottom_cd850060-547e-5eb4-96ec-5dd3a191fde4.json'
AUTHOR = 'json_to_solo'

class ArrowCornerBottom(Solo48):
    icon_id = 'arrow-corner-bottom'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'corner', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (4, 40), (44, 40))
        self.add_line('e1', (44, 40), (44, 8))
        self.add_contour('c0', 'e0', 'e1')
