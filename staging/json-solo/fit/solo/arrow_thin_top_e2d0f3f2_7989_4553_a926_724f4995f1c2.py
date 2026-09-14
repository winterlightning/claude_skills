"""Arrow thin top (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2d0f3f2-7989-4553-a926-724f4995f1c2'
SOURCE_PATH = 'icons-json/symbol/arrow thin top_e2d0f3f2-7989-4553-a926-724f4995f1c2.json'
AUTHOR = 'json_to_solo'

class ArrowThinTopE2d0f3f2(Solo48):
    icon_id = 'arrow-thin-top-e2d0f3f2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('arrow', 'thin', 'top', 'symbol')

    def build(self):
        self.add_line('e0', (40, 23), (24, 4))
        self.add_line('e1', (8, 22), (24, 4))
        self.add_line('e2', (24, 44), (24, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
