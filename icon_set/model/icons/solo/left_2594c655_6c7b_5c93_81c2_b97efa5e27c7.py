"""Left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2594c655-6c7b-5c93-81c2-b97efa5e27c7'
SOURCE_PATH = 'icons-json/arrows/left_2594c655-6c7b-5c93-81c2-b97efa5e27c7.json'
AUTHOR = 'json_to_solo'

class Left(Solo48):
    icon_id = 'left'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('left', 'arrows')

    def build(self):
        self.add_line('e0', (40, 4), (8, 24))
        self.add_line('e1', (8, 24), (40, 44))
        self.add_contour('c0', 'e0', 'e1')
