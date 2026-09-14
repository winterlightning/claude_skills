"""Cube shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b521cdf9-562a-4900-a31d-1736379a2d98'
SOURCE_PATH = 'icons-json/design/cube shape_b521cdf9-562a-4900-a31d-1736379a2d98.json'
AUTHOR = 'json_to_solo'

class CubeShapeDesign(Solo48):
    icon_id = 'cube-shape-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('cube', 'shape', 'design')

    def build(self):
        self.add_line('e0', (40, 14), (40, 34))
        self.add_line('e1', (40, 34), (24, 44))
        self.add_line('e2', (40, 14), (24, 24))
        self.add_line('e3', (40, 14), (24, 4))
        self.add_line('e4', (23, 4), (8, 14))
        self.add_line('e5', (24, 44), (24, 24))
        self.add_line('e6', (24, 44), (8, 34))
        self.add_line('e7', (8, 34), (8, 14))
        self.add_line('e8', (24, 24), (8, 14))
        self.add_arc('e9', (24, 4), (23, 4), radius_x=70)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e9', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6', 'e7')
        self.add_contour('c5', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
