"""Arrow thick 3 bottom left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ddd7ea21-d806-5134-a35f-80d2eb3aa660'
SOURCE_PATH = 'icons-json/arrows/arrow thick 3 bottom left_ddd7ea21-d806-5134-a35f-80d2eb3aa660.json'
AUTHOR = 'json_to_solo'

class ArrowThick3BottomLeft(Solo48):
    icon_id = 'arrow-thick-3-bottom-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'bottom', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (21, 33), (40, 14))
        self.add_line('e1', (35, 8), (15, 26))
        self.add_line('e2', (15, 26), (15, 12))
        self.add_line('e3', (6, 12), (6, 42))
        self.add_line('e4', (6, 42), (34, 42))
        self.add_line('e5', (36, 33), (21, 33))
        self.add_arc('e6-1', (40, 14), (42, 11), radius_x=5, sweep=False)
        self.add_arc('e6-2', (42, 11), (41, 8), radius_x=5, sweep=False)
        self.add_arc('e6-3', (41, 8), (38, 6), radius_x=4, sweep=False)
        self.add_arc('e6-4', (38, 6), (35, 8), radius_x=5, sweep=False)
        self.add_arc('e7-1', (15, 12), (14, 8), radius_x=5, sweep=False)
        self.add_line('e7-2', (14, 8), (10, 6))
        self.add_line('e7-3', (10, 6), (7, 8))
        self.add_line('e7-4', (7, 8), (6, 11))
        self.add_line('e7-5', (6, 11), (6, 12))
        self.add_line('e8-1', (34, 42), (40, 41))
        self.add_line('e8-2', (40, 41), (42, 38))
        self.add_arc('e8-3', (42, 38), (36, 33), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e1', 'e2', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e3', 'e4', 'e8-1', 'e8-2', 'e8-3', 'e5', closed=True)
