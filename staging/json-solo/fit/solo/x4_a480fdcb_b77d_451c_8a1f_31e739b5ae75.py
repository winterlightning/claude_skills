"""X4 (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a480fdcb-b77d-451c-8a1f-31e739b5ae75'
SOURCE_PATH = 'icons-json/symbol/X4_a480fdcb-b77d-451c-8a1f-31e739b5ae75.json'
AUTHOR = 'json_to_solo'

class X4Symbol(Solo48):
    icon_id = 'x4-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('x4', 'symbol')

    def build(self):
        self.add_line('e0', (19, 9), (4, 40))
        self.add_line('e1', (4, 8), (19, 40))
        self.add_line('e2', (41, 40), (41, 8))
        self.add_line('e3', (41, 8), (30, 29))
        self.add_line('e4', (30, 29), (44, 29))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e3', 'e4')
