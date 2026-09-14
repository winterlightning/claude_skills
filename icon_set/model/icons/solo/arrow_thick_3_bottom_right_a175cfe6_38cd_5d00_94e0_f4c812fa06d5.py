"""Arrow thick 3 bottom right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a175cfe6-38cd-5d00-94e0-f4c812fa06d5'
SOURCE_PATH = 'icons-json/arrows/arrow thick 3 bottom right_a175cfe6-38cd-5d00-94e0-f4c812fa06d5.json'
AUTHOR = 'json_to_solo'

class ArrowThick3BottomRight(Solo48):
    icon_id = 'arrow-thick-3-bottom-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'bottom', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (8, 13), (26, 33))
        self.add_line('e1', (26, 33), (12, 33))
        self.add_line('e2', (12, 42), (42, 42))
        self.add_line('e3', (42, 42), (42, 14))
        self.add_line('e4', (33, 12), (33, 27))
        self.add_line('e5', (33, 27), (14, 8))
        self.add_arc('e6-1', (14, 8), (11, 6), radius_x=4, sweep=False)
        self.add_arc('e6-2', (11, 6), (8, 7), radius_x=5, sweep=False)
        self.add_arc('e6-3', (8, 7), (6, 10), radius_x=4, sweep=False)
        self.add_arc('e6-4', (6, 10), (8, 13), radius_x=5, sweep=False)
        self.add_arc('e7-1', (12, 33), (8, 34), radius_x=5, sweep=False)
        self.add_line('e7-2', (8, 34), (6, 38))
        self.add_arc('e7-3', (6, 38), (8, 41), radius_x=4)
        self.add_line('e7-4', (8, 41), (12, 42))
        self.add_line('e8-1', (42, 14), (41, 8))
        self.add_line('e8-2', (41, 8), (38, 6))
        self.add_arc('e8-3', (38, 6), (33, 12), radius_x=6, sweep=False)
        self.add_contour('c0', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e0', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e2', 'e3', 'e8-1', 'e8-2', 'e8-3', 'e4', 'e5', closed=True)
