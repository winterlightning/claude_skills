"""Polygon frame (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c37f3ca8-548a-50a7-a9d2-e4ef9b849e3d'
SOURCE_PATH = 'icons-json/design/polygon frame_c37f3ca8-548a-50a7-a9d2-e4ef9b849e3d.json'
AUTHOR = 'json_to_solo'

class PolygonFrameDesign(Solo48):
    icon_id = 'polygon-frame-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('polygon', 'frame', 'design')

    def build(self):
        self.add_line('e0', (35, 40), (13, 40))
        self.add_line('e1', (35, 8), (13, 8))
        self.add_line('e2', (35, 40), (24, 24))
        self.add_line('e3', (24, 24), (35, 8))
        self.add_line('e4', (35, 8), (44, 24))
        self.add_line('e5', (44, 24), (35, 40))
        self.add_line('e6', (24, 24), (13, 40))
        self.add_line('e7', (13, 40), (4, 24))
        self.add_line('e8', (4, 24), (13, 8))
        self.add_line('e9', (13, 8), (24, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e5', closed=True)
        self.add_contour('c3', 'e6', 'e7', 'e8', 'e9', closed=True)
        self.relate('connect', 'c2', 'c3')
