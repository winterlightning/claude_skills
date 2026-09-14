"""Arrow thick corner 1 top left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '349b52ac-f996-5d80-a4a9-d35751fe8135'
SOURCE_PATH = 'icons-json/arrows/arrow thick corner 1 top left_349b52ac-f996-5d80-a4a9-d35751fe8135.json'
AUTHOR = 'json_to_solo'

class ArrowThickCorner1TopLeftArrows(Solo48):
    icon_id = 'arrow-thick-corner-1-top-left-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'corner', 'top', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (38, 6), (6, 6))
        self.add_line('e1', (6, 6), (6, 40))
        self.add_line('e2', (18, 18), (42, 42))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
