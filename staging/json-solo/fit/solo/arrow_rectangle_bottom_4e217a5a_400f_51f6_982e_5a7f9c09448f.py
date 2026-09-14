"""Arrow rectangle bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e217a5a-400f-51f6-982e-5a7f9c09448f'
SOURCE_PATH = 'icons-json/arrows/arrow rectangle bottom_4e217a5a-400f-51f6-982e-5a7f9c09448f.json'
AUTHOR = 'json_to_solo'

class ArrowRectangleBottomArrows(Solo48):
    icon_id = 'arrow-rectangle-bottom-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'rectangle', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (16, 22), (24, 30))
        self.add_line('e1', (24, 30), (33, 22))
        self.add_line('e2', (42, 13), (42, 35))
        self.add_line('e3', (33, 42), (13, 42))
        self.add_line('e4', (6, 33), (6, 11))
        self.add_line('e5', (13, 6), (38, 6))
        self.add_line('e6-1', (42, 35), (41, 39))
        self.add_arc('e6-2', (41, 39), (39, 41), radius_x=6)
        self.add_line('e6-3', (39, 41), (33, 42))
        self.add_line('e7-1', (13, 42), (8, 40))
        self.add_arc('e7-2', (8, 40), (6, 36), radius_x=7)
        self.add_line('e7-3', (6, 36), (6, 33))
        self.add_arc('e8-1', (6, 11), (8, 7), radius_x=5)
        self.add_line('e8-2', (8, 7), (12, 6))
        self.add_line('e8-3', (12, 6), (13, 6))
        self.add_line('e9-1', (38, 6), (41, 7))
        self.add_line('e9-2', (41, 7), (42, 9))
        self.add_arc('e9-3', (42, 9), (42, 12), radius_x=27, sweep=False)
        self.add_line('e9-4', (42, 12), (42, 13))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e3', 'e7-1', 'e7-2', 'e7-3', 'e4', 'e8-1', 'e8-2', 'e8-3', 'e5', 'e9-1', 'e9-2', 'e9-3', 'e9-4', closed=True)
