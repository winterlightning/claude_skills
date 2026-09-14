"""Double arrow 1 top (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd71ba6c-a327-59f2-a1c3-9763b1bfc4dd'
SOURCE_PATH = 'icons-json/arrows/double arrow 1 top_bd71ba6c-a327-59f2-a1c3-9763b1bfc4dd.json'
AUTHOR = 'json_to_solo'

class DoubleArrow1TopArrows(Solo48):
    icon_id = 'double-arrow-1-top-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'top', 'arrows')

    def build(self):
        self.add_line('sym-e0', (6, 25), (24, 6))
        self.add_line('sym-e1', (24, 6), (42, 25))
        self.add_line('sym-e2', (6, 42), (24, 23))
        self.add_line('sym-e3', (24, 23), (42, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
