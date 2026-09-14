"""Pi math symbol (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '680e723c-ddfa-53c3-83db-849e585cc800'
SOURCE_PATH = 'icons-json/interface-essential/pi math symbol_680e723c-ddfa-53c3-83db-849e585cc800.json'
AUTHOR = 'json_to_solo'

class PiMathSymbolInterfaceEssential(Solo48):
    icon_id = 'pi-math-symbol-interface-essential'
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
        self.add_bezier('e4', (43, 37), ((41.991, 38.802), (40.591, 39.983), (38.209, 39.983)), ((38, 39.983), (37.791, 40), (37.591, 40)), ((37.382, 40), (37.173, 39.992), (36.964, 39.992)), ((36.509, 39.992), (35.964, 39.789), (35.545, 39.646)), ((32.145, 38.476), (32.036, 34.779), (32, 32)))
        self.add_contour('c0', 'e4', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c1')
