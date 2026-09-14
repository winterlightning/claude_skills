"""Corn (food), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dfc9df01-8144-40e0-b66d-be471956d900'
SOURCE_PATH = 'icons-json/food/corn_dfc9df01-8144-40e0-b66d-be471956d900.json'
AUTHOR = 'json_to_solo'

class CornFood(Solo48):
    icon_id = 'corn-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('corn', 'food')

    def build(self):
        self.add_line('e0', (38, 27), (36, 35))
        self.add_line('e1', (18, 27), (15, 24))
        self.add_line('e2', (10, 27), (12, 35))
        self.add_line('e3', (16, 25), (17, 10))
        self.add_line('e4', (31, 10), (32, 25))
        self.add_bezier('e5', (32, 25), ((33.88, 23.864), (35.77, 22.618), (37.95, 22.018)), ((38.275, 21.929), (40, 21.584), (40, 21.651)), ((40, 21.652), (40, 21.653), (40, 21.655)), ((39.73, 22.218), (39.46, 22.773), (39.19, 23.336)), ((38.68, 24.391), (38.27, 25.882), (38, 27)))
        self.add_bezier('e6', (36, 35), ((35.1, 38.7), (32.85, 41.964), (28.85, 43.427)), ((28.14, 43.682), (27.24, 44), (26.47, 44)), ((24.65, 44), (22.82, 44), (21, 44)))
        self.add_bezier('e7', (32, 25), ((28.45, 27.645), (25, 30.136), (23, 34)), ((21.39, 37.109), (21.02, 40.609), (21, 44)))
        self.add_bezier('e8', (23, 34), ((21.7, 31.4), (20.25, 29.045), (18, 27)))
        self.add_bezier('e9', (15, 24), ((13.92, 23.018), (11.32, 22.155), (9.82, 21.891)), ((9.61, 21.864), (9.4, 21.836), (9.19, 21.809)), ((8.79, 21.764), (8.4, 21.709), (8, 21.664)), ((8.004, 21.672), (8, 21.68), (8, 21.689)), ((8, 22.216), (8.524, 22.736), (8.77, 23.264)), ((8.79, 23.282), (8.8, 23.3), (8.81, 23.327)), ((9.33, 24.391), (9.72, 25.864), (10, 27)))
        self.add_bezier('e10', (12, 35), ((13.24, 40.073), (15.34, 42.745), (21, 44)))
        self.add_bezier('e11', (17, 10), ((17.19, 7.173), (20.1, 4.018), (23.41, 4.018)), ((23.548, 4.018), (23.686, 4), (23.823, 4)), ((23.826, 4), (23.828, 4), (23.83, 4)), ((24.04, 4), (24.25, 4.018), (24.46, 4.018)), ((27.82, 4.018), (30.8, 7.109), (31, 10)))
        self.add_contour('c0', 'e5', 'e0', 'e6')
        self.add_contour('c1', 'e7')
        self.add_contour('c2', 'e8', 'e1', 'e9', 'e2', 'e10')
        self.add_contour('c3', 'e3', 'e11', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c2')
