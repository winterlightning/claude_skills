"""Arrow thick corner 1 bottom right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f66c9d61-89e3-59c1-8498-568adf181fd1'
SOURCE_PATH = 'icons-json/arrows/arrow thick corner 1 bottom right_f66c9d61-89e3-59c1-8498-568adf181fd1.json'
AUTHOR = 'json_to_solo'

class ArrowThickCorner1BottomRightArrows(Solo48):
    icon_id = 'arrow-thick-corner-1-bottom-right-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'corner', 'bottom', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (10, 42), (42, 42))
        self.add_line('e1', (42, 42), (42, 8))
        self.add_line('e2', (30, 30), (6, 6))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
