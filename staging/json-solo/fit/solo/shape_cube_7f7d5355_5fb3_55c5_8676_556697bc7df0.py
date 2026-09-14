"""Shape cube (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f7d5355-5fb3-55c5-8676-556697bc7df0'
SOURCE_PATH = 'icons-json/design/shape cube_7f7d5355-5fb3-55c5-8676-556697bc7df0.json'
AUTHOR = 'json_to_solo'

class ShapeCubeDesign(Solo48):
    icon_id = 'shape-cube-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('shape', 'cube', 'design')

    def build(self):
        self.add_line('e0', (42, 6), (15, 6))
        self.add_line('e1', (14, 7), (6, 15))
        self.add_line('e2', (42, 6), (42, 33))
        self.add_line('e3', (42, 33), (33, 42))
        self.add_line('e4', (42, 6), (33, 16))
        self.add_line('e5', (33, 16), (6, 16))
        self.add_line('e6', (6, 16), (6, 42))
        self.add_line('e7', (6, 42), (33, 42))
        self.add_line('e8', (33, 16), (33, 42))
        self.add_line('e9', (15, 6), (14, 7))
        self.add_contour('c0', 'e0', 'e9', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5', 'e6', 'e7')
        self.add_contour('c4', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
