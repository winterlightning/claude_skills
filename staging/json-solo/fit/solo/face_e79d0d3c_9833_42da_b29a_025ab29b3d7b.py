"""Face (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e79d0d3c-9833-42da-b29a-025ab29b3d7b'
SOURCE_PATH = 'icons-json/symbol/face_e79d0d3c-9833-42da-b29a-025ab29b3d7b.json'
AUTHOR = 'json_to_solo'

class FaceSymbol(Solo48):
    icon_id = 'face-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('face', 'symbol')

    def build(self):
        self.add_line('e0', (9, 20), (5, 20))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e2-1', (43, 19), (24, 12), radius_x=17)
        self.add_arc('e2-2', (24, 12), (9, 20), radius_x=22)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e0')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.relate('connect', 'c0', 'e1')
        self.relate('connect', 'c0', 'e1')
