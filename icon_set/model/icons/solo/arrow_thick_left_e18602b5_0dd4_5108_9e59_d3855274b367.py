"""Arrow thick left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e18602b5-0dd4-5108-9e59-d3855274b367'
SOURCE_PATH = 'icons-json/arrows/arrow thick left_e18602b5-0dd4-5108-9e59-d3855274b367.json'
AUTHOR = 'json_to_solo'

class ArrowThickLeftE18602b5(Solo48):
    icon_id = 'arrow-thick-left-e18602b5'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (22, 6), (6, 24))
        self.add_line('e1', (6, 24), (42, 24))
        self.add_line('e2', (23, 42), (6, 24))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
