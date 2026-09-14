"""Math symbol (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da4118b4-4da8-5af9-a462-dcda26157ef0'
SOURCE_PATH = 'icons-json/interface-essential/math symbol_da4118b4-4da8-5af9-a462-dcda26157ef0.json'
AUTHOR = 'json_to_solo'

class MathSymbol(Solo48):
    icon_id = 'math-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('math', 'symbol', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 4), (24, 35))
        self.add_line('e1', (8, 19), (40, 19))
        self.add_line('e2', (8, 44), (40, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
