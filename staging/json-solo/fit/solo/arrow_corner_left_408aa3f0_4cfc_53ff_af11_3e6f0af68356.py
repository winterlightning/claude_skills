"""Arrow corner left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '408aa3f0-4cfc-53ff-af11-3e6f0af68356'
SOURCE_PATH = 'icons-json/arrows/arrow corner left_408aa3f0-4cfc-53ff-af11-3e6f0af68356.json'
AUTHOR = 'json_to_solo'

class ArrowCornerLeft408aa3f0(Solo48):
    icon_id = 'arrow-corner-left-408aa3f0'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'corner', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (8, 4), (8, 44))
        self.add_line('e1', (8, 44), (40, 44))
        self.add_contour('c0', 'e0', 'e1')
