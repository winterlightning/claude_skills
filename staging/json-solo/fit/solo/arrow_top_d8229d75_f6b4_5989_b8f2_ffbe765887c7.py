"""Arrow top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8229d75-f6b4-5989-b8f2-ffbe765887c7'
SOURCE_PATH = 'icons-json/arrows/arrow top_d8229d75-f6b4-5989-b8f2-ffbe765887c7.json'
AUTHOR = 'json_to_solo'

class ArrowTopArrows(Solo48):
    icon_id = 'arrow-top-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (40, 23), (24, 4))
        self.add_line('e1', (8, 22), (24, 4))
        self.add_line('e2', (24, 4), (24, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
