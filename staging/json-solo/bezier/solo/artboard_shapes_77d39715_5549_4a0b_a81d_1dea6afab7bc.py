"""Artboard shapes (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77d39715-5549-4a0b-a81d-1dea6afab7bc'
SOURCE_PATH = 'icons-json/design/artboard shapes_77d39715-5549-4a0b-a81d-1dea6afab7bc.json'
AUTHOR = 'json_to_solo'

class ArtboardShapesDesign(Solo48):
    icon_id = 'artboard-shapes-design'
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
        self.add_bezier('e9', (18, 42), ((18.27, 42), (18.73, 42), (19, 42)))
        self.add_bezier('e10', (37, 42), ((37.761, 42), (38.621, 41.984), (39.382, 41.984)), ((39.652, 41.984), (41.517, 41.967), (41.714, 41.787)), ((41.885, 41.624), (41.984, 37.713), (41.984, 37.459)), ((41.984, 36.944), (42, 36.42), (42, 35.905)), ((42, 35.757), (42, 35.147), (42, 35)))
        self.add_bezier('e11', (42, 18), ((42, 17.885), (42, 18.035), (42, 17.921)), ((42, 16.849), (41.532, 15.9), (41, 15)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e5', 'e9', 'e6', 'e10', 'e7', 'e11', 'e8', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
