"""Arrow thick corner bottom right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5b96ef0-c3b6-540c-beca-5397b83627e0'
SOURCE_PATH = 'icons-json/arrows/arrow thick corner bottom right_e5b96ef0-c3b6-540c-beca-5397b83627e0.json'
AUTHOR = 'json_to_solo'

class ArrowThickCornerBottomRight(Solo48):
    icon_id = 'arrow-thick-corner-bottom-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'corner', 'bottom', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (42, 15), (34, 24))
        self.add_line('e1', (34, 24), (16, 6))
        self.add_line('e2', (16, 6), (6, 16))
        self.add_line('e3', (6, 16), (24, 34))
        self.add_line('e4', (24, 34), (16, 42))
        self.add_line('e5', (16, 42), (42, 42))
        self.add_line('e6', (42, 42), (42, 15))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', closed=True)
