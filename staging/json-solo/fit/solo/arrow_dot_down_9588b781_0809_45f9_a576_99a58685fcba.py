"""Arrow dot down (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9588b781-0809-45f9-a576-99a58685fcba'
SOURCE_PATH = 'icons-json/arrows/arrow dot down_9588b781-0809-45f9-a576-99a58685fcba.json'
AUTHOR = 'json_to_solo'

class ArrowDotDownArrows(Solo48):
    icon_id = 'arrow-dot-down-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'dot', 'down', 'arrows')

    def build(self):
        self.add_line('e0', (24, 32), (24, 44))
        self.add_line('e1', (24, 44), (40, 37))
        self.add_line('e2', (24, 44), (8, 37))
        self.add_line('e3', (24, 24), (24, 19))
        self.add_line('e4', (24, 10), (24, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
