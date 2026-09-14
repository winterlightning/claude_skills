"""Arrow thick top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f98a269-9d67-5a45-af68-1f107195bcf0'
SOURCE_PATH = 'icons-json/arrows/arrow thick top_3f98a269-9d67-5a45-af68-1f107195bcf0.json'
AUTHOR = 'json_to_solo'

class ArrowThickTop(Solo48):
    icon_id = 'arrow-thick-top'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (42, 23), (24, 6))
        self.add_line('e1', (6, 23), (24, 6))
        self.add_line('e2', (24, 6), (24, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
