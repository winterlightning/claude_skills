"""Arrow thick right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9652b24b-db39-57be-aeab-25fe6153652b'
SOURCE_PATH = 'icons-json/arrows/arrow thick right_9652b24b-db39-57be-aeab-25fe6153652b.json'
AUTHOR = 'json_to_solo'

class ArrowThickRightArrows(Solo48):
    icon_id = 'arrow-thick-right-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (25, 42), (42, 24))
        self.add_line('e1', (25, 6), (42, 24))
        self.add_line('e2', (42, 24), (6, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
