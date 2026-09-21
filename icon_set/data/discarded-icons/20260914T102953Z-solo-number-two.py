"""Number two (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2abedf3-2a42-56f7-a5ac-9583b3bda173'
SOURCE_PATH = 'icons-json/interface-essential/number two_b2abedf3-2a42-56f7-a5ac-9583b3bda173.json'
AUTHOR = 'json_to_solo'

class NumberTwo(Solo48):
    icon_id = 'number-two'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('number', 'two', 'interface-essential')

    def build(self):
        self.add_line('e0', (34, 24), (8, 44))
        self.add_line('e1', (8, 44), (40, 44))
        self.add_line('e2-1', (9, 11), (16, 6))
        self.add_line('e2-2', (16, 6), (25, 4))
        self.add_arc('e2-3', (25, 4), (35, 7), radius_x=19)
        self.add_arc('e2-4', (35, 7), (39, 15), radius_x=8)
        self.add_arc('e2-5', (39, 15), (34, 24), radius_x=15)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e0', 'e1')
