"""Arrow thick left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04e5d318-5e49-504c-8b60-1ac19500e1d2'
SOURCE_PATH = 'icons-json/arrows/arrow thick left_04e5d318-5e49-504c-8b60-1ac19500e1d2.json'
AUTHOR = 'json_to_solo'

class ArrowThickLeft(Solo48):
    icon_id = 'arrow-thick-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (24, 15), (16, 24))
        self.add_line('e1', (16, 24), (34, 24))
        self.add_line('e2', (16, 24), (24, 32))
        self.add_line('e3', (40, 42), (8, 42))
        self.add_line('e4', (6, 40), (6, 8))
        self.add_line('e5', (8, 6), (40, 6))
        self.add_line('e6', (42, 9), (42, 40))
        self.add_arc('e7', (8, 42), (6, 40), radius_x=2)
        self.add_arc('e8', (6, 8), (8, 6), radius_x=2)
        self.add_arc('e9-1', (40, 6), (42, 8), radius_x=2)
        self.add_line('e9-2', (42, 8), (42, 9))
        self.add_arc('e10', (42, 40), (40, 42), radius_x=2)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9-1', 'e9-2', 'e6', 'e10', closed=True)
