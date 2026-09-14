"""Split (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5251ba3b-1732-4731-94b1-e6d26d445c61'
SOURCE_PATH = 'icons-json/transportation/split_5251ba3b-1732-4731-94b1-e6d26d445c61.json'
AUTHOR = 'json_to_solo'

class Split(Solo48):
    icon_id = 'split'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('split', 'transportation')

    def build(self):
        self.add_line('e0', (8, 4), (22, 19))
        self.add_line('e1', (22, 19), (24, 21))
        self.add_line('e2', (24, 44), (24, 21))
        self.add_line('e3', (40, 4), (26, 19))
        self.add_line('e4', (26, 19), (24, 21))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
