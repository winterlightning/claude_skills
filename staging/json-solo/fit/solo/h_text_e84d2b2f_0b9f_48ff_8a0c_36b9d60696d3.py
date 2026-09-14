"""H (text) (text), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e84d2b2f-0b9f-48ff-8a0c-36b9d60696d3'
SOURCE_PATH = 'icons-json/text/h (text)_e84d2b2f-0b9f-48ff-8a0c-36b9d60696d3.json'
AUTHOR = 'json_to_solo'

class HTextText(Solo48):
    icon_id = 'h-text-text'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('h', 'text')

    def build(self):
        self.add_line('e0', (8, 4), (8, 44))
        self.add_line('e1', (40, 24), (8, 24))
        self.add_line('e2', (40, 44), (40, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c0')
