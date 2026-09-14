"""Arrow thick corner 2 bottom right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af004c24-a3a7-5d9e-b25b-73e93acc2aba'
SOURCE_PATH = 'icons-json/arrows/arrow thick corner 2 bottom right_af004c24-a3a7-5d9e-b25b-73e93acc2aba.json'
AUTHOR = 'json_to_solo'

class ArrowThickCorner2BottomRight(Solo48):
    icon_id = 'arrow-thick-corner-2-bottom-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'corner', 'bottom', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (6, 6), (42, 42))
        self.add_line('e1', (42, 42), (6, 42))
        self.add_line('e2', (42, 42), (42, 6))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
