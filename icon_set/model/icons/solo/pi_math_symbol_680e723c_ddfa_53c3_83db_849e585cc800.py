"""Pi math symbol (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '680e723c-ddfa-53c3-83db-849e585cc800'
SOURCE_PATH = 'icons-json/interface-essential/pi math symbol_680e723c-ddfa-53c3-83db-849e585cc800.json'
AUTHOR = 'json_to_solo'

class PiMathSymbol(Solo48):
    icon_id = 'pi-math-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('pi', 'math', 'symbol', 'interface-essential')

    def build(self):
        self.add_line('e0', (32, 32), (32, 29))
        self.add_line('e1', (32, 29), (34, 8))
        self.add_line('e2', (4, 8), (44, 8))
        self.add_line('e3', (9, 40), (15, 8))
        self.add_arc('e4-1', (43, 37), (38, 40), radius_x=6)
        self.add_line('e4-2', (38, 40), (34, 39))
        self.add_line('e4-3', (34, 39), (33, 37))
        self.add_arc('e4-4', (33, 37), (32, 32), radius_x=15)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c1')
