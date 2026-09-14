"""Arrow left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca929b9e-035f-546c-b0cd-d1304977d057'
SOURCE_PATH = 'icons-json/arrows/arrow left_ca929b9e-035f-546c-b0cd-d1304977d057.json'
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
        self.add_line('e0', (19, 8), (4, 24))
        self.add_line('e1', (4, 24), (19, 40))
        self.add_line('e2', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
