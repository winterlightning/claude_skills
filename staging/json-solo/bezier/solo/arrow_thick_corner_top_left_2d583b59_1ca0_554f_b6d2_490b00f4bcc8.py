"""Arrow thick corner top left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d583b59-1ca0-554f-b6d2-490b00f4bcc8'
SOURCE_PATH = 'icons-json/arrows/arrow thick corner top left_2d583b59-1ca0-554f-b6d2-490b00f4bcc8.json'
AUTHOR = 'json_to_solo'

class ArrowThickCornerTopLeftArrows(Solo48):
    icon_id = 'arrow-thick-corner-top-left-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'corner', 'top', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (6, 33), (14, 24))
        self.add_line('e1', (14, 24), (32, 42))
        self.add_line('e2', (32, 42), (42, 32))
        self.add_line('e3', (42, 32), (24, 14))
        self.add_line('e4', (24, 14), (32, 6))
        self.add_line('e5', (32, 6), (6, 6))
        self.add_line('e6', (6, 6), (6, 33))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', closed=True)
