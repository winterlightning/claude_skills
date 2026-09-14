"""Arrow rectangle top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4968e7eb-0c17-5914-a579-92bd1c46e9f0'
SOURCE_PATH = 'icons-json/arrows/arrow rectangle top_4968e7eb-0c17-5914-a579-92bd1c46e9f0.json'
AUTHOR = 'json_to_solo'

class ArrowRectangleTop(Solo48):
    icon_id = 'arrow-rectangle-top'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'rectangle', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (32, 26), (24, 18))
        self.add_line('e1', (24, 18), (15, 26))
        self.add_line('e2', (6, 35), (6, 13))
        self.add_line('e3', (15, 6), (35, 6))
        self.add_line('e4', (42, 15), (42, 37))
        self.add_line('e5', (35, 42), (10, 42))
        self.add_line('e6-1', (6, 13), (7, 9))
        self.add_arc('e6-2', (7, 9), (9, 7), radius_x=6)
        self.add_line('e6-3', (9, 7), (15, 6))
        self.add_line('e7-1', (35, 6), (40, 8))
        self.add_arc('e7-2', (40, 8), (42, 12), radius_x=7)
        self.add_line('e7-3', (42, 12), (42, 15))
        self.add_arc('e8-1', (42, 37), (40, 41), radius_x=5)
        self.add_line('e8-2', (40, 41), (36, 42))
        self.add_line('e8-3', (36, 42), (35, 42))
        self.add_line('e9-1', (10, 42), (7, 41))
        self.add_arc('e9-2', (7, 41), (6, 39), radius_x=4)
        self.add_line('e9-3', (6, 39), (6, 37))
        self.add_line('e9-4', (6, 37), (6, 35))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e3', 'e7-1', 'e7-2', 'e7-3', 'e4', 'e8-1', 'e8-2', 'e8-3', 'e5', 'e9-1', 'e9-2', 'e9-3', 'e9-4', closed=True)
