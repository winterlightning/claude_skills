"""Arrow zigzag right (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a44f550-0563-553e-9444-c610f0f7f03a'
SOURCE_PATH = 'icons-json/interface-essential/arrow zigzag right_4a44f550-0563-553e-9444-c610f0f7f03a.json'
AUTHOR = 'json_to_solo'

class ArrowZigzagRight(Solo48):
    icon_id = 'arrow-zigzag-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('arrow', 'zigzag', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 19), (17, 19))
        self.add_line('e1', (17, 19), (17, 8))
        self.add_line('e2', (17, 8), (4, 19))
        self.add_line('e3', (4, 19), (4, 30))
        self.add_line('e4', (4, 30), (44, 30))
        self.add_line('e5', (32, 40), (44, 30))
        self.add_line('e6', (44, 30), (32, 19))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('c1', 'e3', 'e4')
        self.add_contour('c2', 'e5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
