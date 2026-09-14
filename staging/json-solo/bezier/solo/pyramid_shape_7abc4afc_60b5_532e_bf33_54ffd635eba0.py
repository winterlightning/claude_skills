"""Pyramid shape (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7abc4afc-60b5-532e-bf33-54ffd635eba0'
SOURCE_PATH = 'icons-json/design/pyramid shape_7abc4afc-60b5-532e-bf33-54ffd635eba0.json'
AUTHOR = 'json_to_solo'

class PyramidShapeDesign(Solo48):
    icon_id = 'pyramid-shape-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pyramid', 'shape', 'design')

    def build(self):
        self.add_line('e0', (24, 6), (42, 33))
        self.add_line('e1', (42, 33), (24, 42))
        self.add_line('e2', (24, 42), (6, 33))
        self.add_line('e3', (6, 33), (24, 6))
        self.add_line('e4', (24, 6), (24, 42))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
