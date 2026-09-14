"""Move bottom 1 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb826cae-cfc3-5b67-946a-41341bfb7494'
SOURCE_PATH = 'icons-json/arrows/move bottom 1_fb826cae-cfc3-5b67-946a-41341bfb7494.json'
AUTHOR = 'json_to_solo'

class MoveBottom1Arrows(Solo48):
    icon_id = 'move-bottom-1-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('move', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (40, 44), (8, 44))
        self.add_line('e1', (14, 22), (24, 33))
        self.add_line('e2', (24, 33), (24, 4))
        self.add_line('e3', (24, 33), (34, 22))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3')
