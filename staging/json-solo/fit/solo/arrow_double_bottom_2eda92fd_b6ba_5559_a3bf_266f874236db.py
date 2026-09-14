"""Arrow double bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2eda92fd-b6ba-5559-a3bf-266f874236db'
SOURCE_PATH = 'icons-json/arrows/arrow double bottom_2eda92fd-b6ba-5559-a3bf-266f874236db.json'
AUTHOR = 'json_to_solo'

class ArrowDoubleBottomArrows(Solo48):
    icon_id = 'arrow-double-bottom-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'double', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (9, 29), (24, 44))
        self.add_line('e1', (24, 44), (40, 28))
        self.add_line('e2', (8, 4), (24, 20))
        self.add_line('e3', (24, 20), (40, 4))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
