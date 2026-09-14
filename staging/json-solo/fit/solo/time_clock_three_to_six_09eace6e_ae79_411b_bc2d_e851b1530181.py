"""Time clock three to six (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09eace6e-ae79-411b-bc2d-e851b1530181'
SOURCE_PATH = 'icons-json/interface-essential/time clock three to six_09eace6e-ae79-411b-bc2d-e851b1530181.json'
AUTHOR = 'json_to_solo'

class TimeClockThreeToSix09eace6e(Solo48):
    icon_id = 'time-clock-three-to-six-09eace6e'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('time', 'clock', 'three', 'to', 'six', 'interface-essential')

    def build(self):
        self.add_line('e0', (36, 23), (24, 23))
        self.add_line('e1', (24, 23), (24, 34))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
