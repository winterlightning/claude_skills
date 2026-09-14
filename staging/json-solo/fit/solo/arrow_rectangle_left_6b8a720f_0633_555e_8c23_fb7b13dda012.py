"""Arrow rectangle left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b8a720f-0633-555e-8c23-fb7b13dda012'
SOURCE_PATH = 'icons-json/arrows/arrow rectangle left_6b8a720f-0633-555e-8c23-fb7b13dda012.json'
AUTHOR = 'json_to_solo'

class ArrowRectangleLeft6b8a720f(Solo48):
    icon_id = 'arrow-rectangle-left-6b8a720f'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'rectangle', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (26, 16), (18, 24))
        self.add_line('e1', (18, 24), (26, 33))
        self.add_line('e2', (35, 42), (13, 42))
        self.add_line('e3', (6, 33), (6, 13))
        self.add_line('e4', (15, 6), (37, 6))
        self.add_line('e5', (42, 13), (42, 38))
        self.add_line('e6-1', (13, 42), (9, 41))
        self.add_arc('e6-2', (9, 41), (7, 39), radius_x=6)
        self.add_line('e6-3', (7, 39), (6, 33))
        self.add_line('e7-1', (6, 13), (8, 8))
        self.add_arc('e7-2', (8, 8), (12, 6), radius_x=7)
        self.add_line('e7-3', (12, 6), (15, 6))
        self.add_arc('e8-1', (37, 6), (41, 8), radius_x=5)
        self.add_line('e8-2', (41, 8), (42, 12))
        self.add_arc('e8-3', (42, 12), (42, 13), radius_x=23, sweep=False)
        self.add_line('e9-1', (42, 38), (41, 41))
        self.add_line('e9-2', (41, 41), (39, 42))
        self.add_line('e9-3', (39, 42), (36, 42))
        self.add_line('e9-4', (36, 42), (35, 42))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e3', 'e7-1', 'e7-2', 'e7-3', 'e4', 'e8-1', 'e8-2', 'e8-3', 'e5', 'e9-1', 'e9-2', 'e9-3', 'e9-4', closed=True)
