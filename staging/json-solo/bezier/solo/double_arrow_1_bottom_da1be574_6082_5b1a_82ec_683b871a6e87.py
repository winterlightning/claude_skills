"""Double arrow 1 bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da1be574-6082-5b1a-82ec-683b871a6e87'
SOURCE_PATH = 'icons-json/arrows/double arrow 1 bottom_da1be574-6082-5b1a-82ec-683b871a6e87.json'
AUTHOR = 'json_to_solo'

class DoubleArrow1BottomArrows(Solo48):
    icon_id = 'double-arrow-1-bottom-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'bottom', 'arrows')

    def build(self):
        self.add_line('sym-e0', (42, 23), (24, 42))
        self.add_line('sym-e1', (24, 42), (6, 23))
        self.add_line('sym-e2', (42, 6), (24, 25))
        self.add_line('sym-e3', (24, 25), (6, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
