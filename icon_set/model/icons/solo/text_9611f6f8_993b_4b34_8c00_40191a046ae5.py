"""Text (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9611f6f8-993b-4b34-8c00-40191a046ae5'
SOURCE_PATH = 'icons-json/symbol/text_9611f6f8-993b-4b34-8c00-40191a046ae5.json'
AUTHOR = 'json_to_solo'

class Text(Solo48):
    icon_id = 'text'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('text', 'symbol')

    def build(self):
        self.add_line('e0', (8, 11), (8, 4))
        self.add_line('e1', (8, 4), (24, 4))
        self.add_line('e2', (19, 44), (24, 44))
        self.add_line('e3', (29, 44), (24, 44))
        self.add_line('e4', (40, 11), (40, 4))
        self.add_line('e5', (40, 4), (24, 4))
        self.add_line('e6', (24, 4), (24, 44))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4', 'e5')
        self.add_contour('c4', 'e6')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
