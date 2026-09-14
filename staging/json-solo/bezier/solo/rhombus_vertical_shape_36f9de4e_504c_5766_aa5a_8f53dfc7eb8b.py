"""Rhombus vertical shape (design), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36f9de4e-504c-5766-aa5a-8f53dfc7eb8b'
SOURCE_PATH = 'icons-json/design/rhombus vertical shape_36f9de4e-504c-5766-aa5a-8f53dfc7eb8b.json'
AUTHOR = 'json_to_solo'

class RhombusVerticalShapeDesign(Solo48):
    icon_id = 'rhombus-vertical-shape-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rhombus', 'vertical', 'shape', 'design')

    def build(self):
        self.add_line('e0', (22, 42), (10, 28))
        self.add_line('e1', (8, 23), (20, 8))
        self.add_line('e2', (26, 7), (40, 23))
        self.add_line('e3', (40, 25), (25, 44))
        self.add_bezier('e4', (25, 44), ((24.69, 44), (24.37, 44), (24.06, 44)), ((23.21, 44), (22.43, 42.518), (22, 42)))
        self.add_bezier('e5', (10, 28), ((9.63, 27.545), (8.01, 25.336), (8.01, 24.745)), ((8.01, 24.682), (8, 24.618), (8, 24.564)), ((8, 24.464), (8, 24.364), (8, 24.264)), ((8, 24.073), (8, 23.882), (8, 23.7)), ((8, 23.491), (8, 23.2), (8, 23)))
        self.add_bezier('e6', (20, 8), ((20.22, 7.709), (23.12, 4), (23.58, 4)), ((23.585, 4), (23.591, 4), (23.597, 4)), ((23.976, 4), (25.715, 6.669), (26, 7)))
        self.add_bezier('e7', (40, 23), ((40, 23.218), (40, 23.527), (40, 23.745)), ((40, 23.918), (39.99, 24.082), (39.99, 24.255)), ((39.99, 24.327), (40, 24.4), (40, 24.482)), ((40, 24.618), (40, 24.855), (40, 25)))
        self.add_contour('c0', 'e4', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', closed=True)
