"""Square wireframe 3d (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c42cbe7-b946-5607-a8e7-36485a8c3e5b'
SOURCE_PATH = 'icons-json/design/square wireframe 3d_0c42cbe7-b946-5607-a8e7-36485a8c3e5b.json'
AUTHOR = 'json_to_solo'

class SquareWireframe3dDesign(Solo48):
    icon_id = 'square-wireframe-3d-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('square', 'wireframe', '3d', 'design')

    def build(self):
        self.add_line('e0', (24, 44), (40, 34))
        self.add_line('e1', (40, 34), (40, 14))
        self.add_line('e2', (40, 14), (24, 24))
        self.add_line('e3', (24, 24), (8, 14))
        self.add_line('e4', (24, 24), (24, 44))
        self.add_line('e5', (24, 44), (8, 34))
        self.add_line('e6', (8, 34), (8, 14))
        self.add_line('e7', (8, 14), (24, 4))
        self.add_line('e8', (24, 4), (40, 14))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e5', 'e6')
        self.add_contour('c2', 'e7', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
