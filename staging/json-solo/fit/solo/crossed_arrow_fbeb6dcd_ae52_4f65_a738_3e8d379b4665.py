"""Crossed arrow (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fbeb6dcd-ae52-4f65-a738-3e8d379b4665'
SOURCE_PATH = 'icons-json/symbol/crossed arrow_fbeb6dcd-ae52-4f65-a738-3e8d379b4665.json'
AUTHOR = 'json_to_solo'

class CrossedArrowSymbol(Solo48):
    icon_id = 'crossed-arrow-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('crossed', 'arrow', 'symbol')

    def build(self):
        self.add_line('e0', (15, 33), (34, 13))
        self.add_line('e1', (33, 33), (14, 13))
        self.add_line('e2', (37, 32), (33, 33))
        self.add_line('e3', (29, 8), (42, 6))
        self.add_line('e4', (42, 6), (40, 18))
        self.add_line('e5', (40, 18), (29, 8))
        self.add_line('e6', (19, 8), (6, 6))
        self.add_line('e7', (6, 6), (8, 18))
        self.add_line('e8', (19, 8), (8, 18))
        self.add_arc('e9', (6, 37), (15, 33), radius_x=6)
        self.add_arc('e10', (11, 42), (15, 33), radius_x=6, sweep=False)
        self.add_arc('e11', (36, 42), (33, 33), radius_x=6)
        self.add_arc('e12', (42, 36), (37, 32), radius_x=9, sweep=False)
        self.add_contour('c0', 'e9', 'e0')
        self.add_contour('c1', 'e10')
        self.add_contour('c2', 'e11', 'e1')
        self.add_contour('c3', 'e12', 'e2')
        self.add_contour('c4', 'e3', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6', 'e7')
        self.add_contour('c7', 'e8')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c2', 'c7')
