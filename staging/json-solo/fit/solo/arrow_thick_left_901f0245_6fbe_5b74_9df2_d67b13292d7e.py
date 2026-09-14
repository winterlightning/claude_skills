"""Arrow thick left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '901f0245-6fbe-5b74-9df2-d67b13292d7e'
SOURCE_PATH = 'icons-json/arrows/arrow thick left_901f0245-6fbe-5b74-9df2-d67b13292d7e.json'
AUTHOR = 'json_to_solo'

class ArrowThickLeft901f0245(Solo48):
    icon_id = 'arrow-thick-left-901f0245'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (23, 6), (6, 24))
        self.add_line('e1', (23, 42), (6, 24))
        self.add_line('e2', (6, 24), (42, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
