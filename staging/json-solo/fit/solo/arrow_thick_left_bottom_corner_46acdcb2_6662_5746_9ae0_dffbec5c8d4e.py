"""Arrow thick left bottom corner (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46acdcb2-6662-5746-9ae0-dffbec5c8d4e'
SOURCE_PATH = 'icons-json/arrows/arrow thick left bottom corner_46acdcb2-6662-5746-9ae0-dffbec5c8d4e.json'
AUTHOR = 'json_to_solo'

class ArrowThickLeftBottomCorner46acdcb2(Solo48):
    icon_id = 'arrow-thick-left-bottom-corner-46acdcb2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'left', 'bottom', 'corner', 'arrows')

    def build(self):
        self.add_line('e0', (32, 14), (17, 30))
        self.add_line('e1', (17, 30), (31, 30))
        self.add_line('e2', (17, 30), (17, 16))
        self.add_line('e3', (6, 39), (6, 8))
        self.add_line('e4', (8, 6), (40, 6))
        self.add_line('e5', (42, 8), (42, 40))
        self.add_line('e6', (41, 42), (8, 42))
        self.add_line('e7-1', (8, 42), (6, 41))
        self.add_line('e7-2', (6, 41), (6, 39))
        self.add_arc('e8', (6, 8), (8, 6), radius_x=2)
        self.add_arc('e9', (40, 6), (42, 8), radius_x=2)
        self.add_line('e10', (42, 40), (41, 42))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e7-1', 'e7-2', 'e3', 'e8', 'e4', 'e9', 'e5', 'e10', 'e6', closed=True)
