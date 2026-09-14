"""Shape triangle (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e2', (42, 40), ((36.633, 41.898), (30.922, 41.984), (25.235, 41.984)), ((24.638, 41.984), (24.049, 42), (23.452, 42)), ((23.439, 42), (23.427, 42), (23.415, 42)), ((22.633, 42), (21.852, 41.984), (21.063, 41.984)), ((19.745, 41.984), (18.412, 41.845), (17.095, 41.738)), ((13.102, 41.403), (9.772, 41.334), (6, 40)))
        self.add_contour('c0', 'e2', 'e0', 'e1', closed=True)
