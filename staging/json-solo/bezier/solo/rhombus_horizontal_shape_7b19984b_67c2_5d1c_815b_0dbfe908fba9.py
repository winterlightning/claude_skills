"""Rhombus horizontal shape (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b19984b-67c2-5d1c-815b-0dbfe908fba9'
SOURCE_PATH = 'icons-json/design/rhombus horizontal shape_7b19984b-67c2-5d1c-815b-0dbfe908fba9.json'
AUTHOR = 'json_to_solo'

class RhombusHorizontalShapeDesign(Solo48):
    icon_id = 'rhombus-horizontal-shape-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rhombus', 'horizontal', 'shape', 'design')

    def build(self):
        self.add_line('e0', (8, 20), (22, 9))
        self.add_line('e1', (25, 8), (43, 22))
        self.add_line('e2', (42, 27), (26, 39))
        self.add_line('e3', (21, 38), (4, 25))
        self.add_bezier('e4', (22, 9), ((22.355, 8.73), (23.018, 8.01), (23.5, 8.01)), ((23.564, 8.01), (23.627, 8.01), (23.7, 8)), ((23.764, 8.01), (23.836, 8.01), (23.9, 8.01)), ((24.036, 8.01), (24.173, 8.01), (24.309, 8)), ((24.373, 8), (24.445, 8), (24.509, 8)), ((24.645, 8), (24.864, 8), (25, 8)))
        self.add_bezier('e5', (43, 22), ((43.455, 22.35), (43.991, 22.79), (43.991, 23.45)), ((43.991, 23.568), (44, 23.686), (44, 23.804)), ((44, 23.806), (44, 23.808), (44, 23.81)), ((44, 23.93), (43.991, 24.05), (43.991, 24.17)), ((43.991, 25.58), (42.964, 26.29), (42, 27)))
        self.add_bezier('e6', (26, 39), ((25.582, 39.31), (24.809, 40), (24.273, 40)), ((24.272, 40), (24.271, 40), (24.27, 40)), ((24.216, 40), (24.154, 39.99), (24.1, 39.99)), ((23.373, 39.99), (21.6, 38.45), (21, 38)))
        self.add_bezier('e7', (4, 25), ((4, 24.83), (4, 24.65), (4, 24.48)), ((4, 22.78), (6.909, 20.82), (8, 20)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2', 'e6', 'e3', 'e7', closed=True)
