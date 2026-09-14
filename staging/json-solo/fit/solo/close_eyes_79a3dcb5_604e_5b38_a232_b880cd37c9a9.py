"""Close eyes (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79a3dcb5-604e-5b38-a232-b880cd37c9a9'
SOURCE_PATH = 'icons-json/interface-essential/close eyes_79a3dcb5-604e-5b38-a232-b880cd37c9a9.json'
AUTHOR = 'json_to_solo'

class CloseEyesInterfaceEssential(Solo48):
    icon_id = 'close-eyes-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('close', 'eyes', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 34), (11, 28))
        self.add_line('e1', (16, 39), (18, 31))
        self.add_line('e2', (24, 40), (24, 32))
        self.add_line('e3', (31, 31), (33, 39))
        self.add_line('e4', (41, 34), (37, 28))
        self.add_arc('e5-1', (44, 20), (24, 8), radius_x=25, sweep=False)
        self.add_arc('e5-2', (24, 8), (4, 20), radius_x=25, sweep=False)
        self.add_arc('e5-3', (4, 20), (44, 20), radius_x=23, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5-1', 'e5-2', 'e5-3', closed=True)
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
