"""Plus math symbol circle (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0bba548-63cf-4a5b-979d-41ee0f279414'
SOURCE_PATH = 'icons-json/interface-essential/plus math symbol circle_b0bba548-63cf-4a5b-979d-41ee0f279414.json'
AUTHOR = 'json_to_solo'

class PlusMathSymbolCircleInterfaceEssential(Solo48):
    icon_id = 'plus-math-symbol-circle-interface-essential'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('plus', 'math', 'symbol', 'circle', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 13), (24, 24))
        self.add_line('e1', (14, 24), (24, 24))
        self.add_line('e2', (24, 34), (24, 24))
        self.add_line('e3', (34, 24), (24, 24))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
