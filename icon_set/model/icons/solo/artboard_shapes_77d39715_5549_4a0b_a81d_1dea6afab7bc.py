"""Artboard shapes (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77d39715-5549-4a0b-a81d-1dea6afab7bc'
SOURCE_PATH = 'icons-json/design/artboard shapes_77d39715-5549-4a0b-a81d-1dea6afab7bc.json'
AUTHOR = 'json_to_solo'

class ArtboardShapes(Solo48):
    icon_id = 'artboard-shapes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('artboard', 'shapes', 'design')

    def build(self):
        self.add_line('e0', (26, 15), (26, 6))
        self.add_line('e1', (26, 6), (6, 6))
        self.add_line('e2', (6, 6), (6, 33))
        self.add_line('e3', (6, 33), (18, 33))
        self.add_line('e4', (18, 15), (18, 32))
        self.add_line('e5', (18, 32), (18, 42))
        self.add_line('e6', (19, 42), (37, 42))
        self.add_line('e7', (42, 35), (42, 18))
        self.add_line('e8', (41, 15), (18, 15))
        self.add_arc('e9', (18, 42), (19, 42), radius_x=26)
        self.add_arc('e10-1', (37, 42), (41, 42), radius_x=64)
        self.add_line('e10-2', (41, 42), (42, 36))
        self.add_arc('e10-3', (42, 36), (42, 35), radius_x=37)
        self.add_arc('e11', (42, 18), (41, 15), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e5', 'e9', 'e6', 'e10-1', 'e10-2', 'e10-3', 'e7', 'e11', 'e8', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
