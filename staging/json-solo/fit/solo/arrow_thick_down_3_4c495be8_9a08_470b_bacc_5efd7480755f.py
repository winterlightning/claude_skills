"""Arrow thick down 3 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c495be8-9a08-470b-bacc-5efd7480755f'
SOURCE_PATH = 'icons-json/arrows/arrow thick down 3_4c495be8-9a08-470b-bacc-5efd7480755f.json'
AUTHOR = 'json_to_solo'

class ArrowThickDown3Arrows(Solo48):
    icon_id = 'arrow-thick-down-3-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'down', 'arrows')

    def build(self):
        self.add_line('e0', (28, 27), (36, 19))
        self.add_line('e1', (37, 18), (42, 23))
        self.add_line('e2', (42, 25), (25, 41))
        self.add_line('e3', (23, 42), (6, 24))
        self.add_line('e4', (6, 23), (10, 19))
        self.add_line('e5', (12, 19), (18, 26))
        self.add_line('e6', (19, 26), (19, 6))
        self.add_line('e7', (19, 6), (28, 6))
        self.add_line('e8', (28, 6), (28, 27))
        self.add_arc('e9', (36, 19), (37, 18), radius_x=31)
        self.add_arc('e10', (42, 23), (42, 25), radius_x=28, sweep=False)
        self.add_line('e11', (25, 41), (23, 42))
        self.add_line('e12', (6, 24), (6, 23))
        self.add_line('e13', (10, 19), (12, 19))
        self.add_line('e14', (18, 26), (19, 26))
        self.add_contour('c0', 'e0', 'e9', 'e1', 'e10', 'e2', 'e11', 'e3', 'e12', 'e4', 'e13', 'e5', 'e14', 'e6', 'e7', 'e8', closed=True)
