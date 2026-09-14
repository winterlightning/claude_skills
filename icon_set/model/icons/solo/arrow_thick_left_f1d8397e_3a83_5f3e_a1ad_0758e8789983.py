"""Arrow thick left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1d8397e-3a83-5f3e-a1ad-0758e8789983'
SOURCE_PATH = 'icons-json/arrows/arrow thick left_f1d8397e-3a83-5f3e-a1ad-0758e8789983.json'
AUTHOR = 'json_to_solo'

class ArrowThickLeftF1d8397e(Solo48):
    icon_id = 'arrow-thick-left-f1d8397e'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (19, 8), (4, 24))
        self.add_line('e1', (19, 40), (4, 24))
        self.add_line('e2', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
