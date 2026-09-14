"""Arrow thick bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6e16665-69b0-50f4-bc4c-144edfd6fffb'
SOURCE_PATH = 'icons-json/arrows/arrow thick bottom_d6e16665-69b0-50f4-bc4c-144edfd6fffb.json'
AUTHOR = 'json_to_solo'

class ArrowThickBottom(Solo48):
    icon_id = 'arrow-thick-bottom'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (6, 25), (24, 42))
        self.add_line('e1', (42, 25), (24, 42))
        self.add_line('e2', (24, 42), (24, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
