"""Arrow zigzag left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c36e454-7588-58d7-b2b0-f046314843ba'
SOURCE_PATH = 'icons-json/interface-essential/arrow zigzag left_3c36e454-7588-58d7-b2b0-f046314843ba.json'
AUTHOR = 'json_to_solo'

class ArrowZigzagLeftInterfaceEssential(Solo48):
    icon_id = 'arrow-zigzag-left-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('arrow', 'zigzag', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (44, 29), (31, 29))
        self.add_line('e1', (31, 29), (31, 40))
        self.add_line('e2', (31, 40), (44, 29))
        self.add_line('e3', (44, 29), (44, 19))
        self.add_line('e4', (44, 19), (4, 19))
        self.add_line('e5', (16, 8), (4, 19))
        self.add_line('e6', (4, 19), (16, 29))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('c1', 'e3', 'e4')
        self.add_contour('c2', 'e5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
