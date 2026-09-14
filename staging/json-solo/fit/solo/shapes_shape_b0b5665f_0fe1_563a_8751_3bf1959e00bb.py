"""Shapes shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0b5665f-0fe1-563a-8751-3bf1959e00bb'
SOURCE_PATH = 'icons-json/design/shapes shape_b0b5665f-0fe1-563a-8751-3bf1959e00bb.json'
AUTHOR = 'json_to_solo'

class ShapesShapeDesign(Solo48):
    icon_id = 'shapes-shape-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('shapes', 'shape', 'design')

    def build(self):
        self.add_line('e0', (42, 20), (20, 20))
        self.add_line('e1', (20, 20), (20, 42))
        self.add_line('e2', (20, 42), (42, 42))
        self.add_line('e3', (42, 42), (42, 20))
        self.add_arc('e4-1', (20, 31), (6, 19), radius_x=13)
        self.add_line('e4-2', (6, 19), (8, 12))
        self.add_arc('e4-3', (8, 12), (18, 6), radius_x=12)
        self.add_line('e4-4', (18, 6), (25, 8))
        self.add_arc('e4-5', (25, 8), (29, 12), radius_x=12)
        self.add_line('e4-6', (29, 12), (31, 20))
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6')
        self.add_contour('c1', 'e0', 'e1', 'e2', 'e3', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
