"""Arrow dot up (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76c32561-c42c-4de0-b32b-c4e51a1e90ca'
SOURCE_PATH = 'icons-json/arrows/arrow dot up_76c32561-c42c-4de0-b32b-c4e51a1e90ca.json'
AUTHOR = 'json_to_solo'

class ArrowDotUp(Solo48):
    icon_id = 'arrow-dot-up'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'dot', 'up', 'arrows')

    def build(self):
        self.add_line('e0', (24, 16), (24, 4))
        self.add_line('e1', (24, 4), (8, 11))
        self.add_line('e2', (24, 4), (40, 11))
        self.add_line('e3', (24, 24), (24, 29))
        self.add_line('e4', (24, 38), (24, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
