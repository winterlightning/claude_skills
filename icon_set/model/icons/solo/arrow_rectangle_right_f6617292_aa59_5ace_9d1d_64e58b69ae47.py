"""Arrow rectangle right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f6617292-aa59-5ace-9d1d-64e58b69ae47'
SOURCE_PATH = 'icons-json/arrows/arrow rectangle right_f6617292-aa59-5ace-9d1d-64e58b69ae47.json'
AUTHOR = 'json_to_solo'

class ArrowRectangleRight(Solo48):
    icon_id = 'arrow-rectangle-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'rectangle', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (22, 32), (30, 24))
        self.add_line('e1', (30, 24), (22, 15))
        self.add_line('e2', (13, 6), (35, 6))
        self.add_line('e3', (42, 15), (42, 35))
        self.add_line('e4', (33, 42), (11, 42))
        self.add_line('e5', (6, 35), (6, 10))
        self.add_line('e6-1', (35, 6), (39, 7))
        self.add_arc('e6-2', (39, 7), (41, 9), radius_x=6)
        self.add_line('e6-3', (41, 9), (42, 15))
        self.add_line('e7-1', (42, 35), (40, 40))
        self.add_arc('e7-2', (40, 40), (36, 42), radius_x=7)
        self.add_line('e7-3', (36, 42), (33, 42))
        self.add_arc('e8-1', (11, 42), (7, 40), radius_x=5)
        self.add_line('e8-2', (7, 40), (6, 36))
        self.add_line('e8-3', (6, 36), (6, 35))
        self.add_line('e9-1', (6, 10), (7, 7))
        self.add_line('e9-2', (7, 7), (9, 6))
        self.add_arc('e9-3', (9, 6), (11, 6), radius_x=20, sweep=False)
        self.add_line('e9-4', (11, 6), (13, 6))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e3', 'e7-1', 'e7-2', 'e7-3', 'e4', 'e8-1', 'e8-2', 'e8-3', 'e5', 'e9-1', 'e9-2', 'e9-3', 'e9-4', closed=True)
