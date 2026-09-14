"""Shape triangle (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70d03d11-1d6e-5211-ac36-868a3ce6aa14'
SOURCE_PATH = 'icons-json/design/shape triangle_70d03d11-1d6e-5211-ac36-868a3ce6aa14.json'
AUTHOR = 'json_to_solo'

class ShapeTriangleDesign(Solo48):
    icon_id = 'shape-triangle-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('shape', 'triangle', 'design')

    def build(self):
        self.add_line('e0', (6, 40), (24, 6))
        self.add_line('e1', (24, 6), (42, 40))
        self.add_line('e2-1', (42, 40), (23, 42))
        self.add_line('e2-2', (23, 42), (6, 40))
        self.add_contour('c0', 'e2-1', 'e2-2', 'e0', 'e1', closed=True)
