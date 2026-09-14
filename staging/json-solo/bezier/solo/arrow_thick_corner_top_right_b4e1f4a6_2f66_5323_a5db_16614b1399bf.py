"""Arrow thick corner top right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4e1f4a6-2f66-5323-a5db-16614b1399bf'
SOURCE_PATH = 'icons-json/arrows/arrow thick corner top right_b4e1f4a6-2f66-5323-a5db-16614b1399bf.json'
AUTHOR = 'json_to_solo'

class ArrowThickCornerTopRightArrows(Solo48):
    icon_id = 'arrow-thick-corner-top-right-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'corner', 'top', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (15, 6), (24, 14))
        self.add_line('e1', (24, 14), (6, 32))
        self.add_line('e2', (6, 32), (16, 42))
        self.add_line('e3', (16, 42), (34, 24))
        self.add_line('e4', (34, 24), (42, 32))
        self.add_line('e5', (42, 32), (42, 6))
        self.add_line('e6', (42, 6), (15, 6))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', closed=True)
