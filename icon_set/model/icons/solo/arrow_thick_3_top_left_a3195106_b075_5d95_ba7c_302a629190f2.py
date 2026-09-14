"""Arrow thick 3 top left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3195106-b075-5d95-ba7c-302a629190f2'
SOURCE_PATH = 'icons-json/arrows/arrow thick 3 top left_a3195106-b075-5d95-ba7c-302a629190f2.json'
AUTHOR = 'json_to_solo'

class ArrowThick3TopLeft(Solo48):
    icon_id = 'arrow-thick-3-top-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'top', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (15, 21), (34, 40))
        self.add_line('e1', (40, 35), (22, 15))
        self.add_line('e2', (22, 15), (36, 15))
        self.add_line('e3', (36, 6), (6, 6))
        self.add_line('e4', (6, 6), (6, 34))
        self.add_line('e5', (15, 36), (15, 21))
        self.add_arc('e6-1', (34, 40), (37, 42), radius_x=4, sweep=False)
        self.add_arc('e6-2', (37, 42), (40, 41), radius_x=5, sweep=False)
        self.add_arc('e6-3', (40, 41), (42, 38), radius_x=4, sweep=False)
        self.add_arc('e6-4', (42, 38), (40, 35), radius_x=5, sweep=False)
        self.add_arc('e7-1', (36, 15), (40, 14), radius_x=5, sweep=False)
        self.add_line('e7-2', (40, 14), (42, 10))
        self.add_line('e7-3', (42, 10), (40, 7))
        self.add_line('e7-4', (40, 7), (37, 6))
        self.add_line('e7-5', (37, 6), (36, 6))
        self.add_line('e8-1', (6, 34), (7, 40))
        self.add_arc('e8-2', (7, 40), (10, 42), radius_x=5, sweep=False)
        self.add_arc('e8-3', (10, 42), (15, 36), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e1', 'e2', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e3', 'e4', 'e8-1', 'e8-2', 'e8-3', 'e5', closed=True)
