"""Left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e7d5eb7-d8b8-5f42-8456-a7d8ce8a9c6d'
SOURCE_PATH = 'icons-json/arrows/left_2e7d5eb7-d8b8-5f42-8456-a7d8ce8a9c6d.json'
AUTHOR = 'json_to_solo'

class Left2e7d5eb7(Solo48):
    icon_id = 'left-2e7d5eb7'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('left', 'arrows')

    def build(self):
        self.add_line('e0', (8, 24), (40, 44))
        self.add_line('e1', (40, 44), (40, 4))
        self.add_line('e2', (40, 4), (14, 20))
        self.add_line('e3', (14, 20), (8, 24))
        self.add_contour('c0', 'e3', 'e0', 'e1', 'e2', closed=True)
