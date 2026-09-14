"""Time clock three (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e70b94d1-fd6b-4ec0-9e72-601ea85a80b4'
SOURCE_PATH = 'icons-json/interface-essential/time clock three_e70b94d1-fd6b-4ec0-9e72-601ea85a80b4.json'
AUTHOR = 'json_to_solo'

class TimeClockThreeInterfaceEssential(Solo48):
    icon_id = 'time-clock-three-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('time', 'clock', 'three', 'interface-essential')

    def build(self):
        self.add_line('e0', (12, 13), (13, 15))
        self.add_line('e1', (6, 25), (9, 25))
        self.add_line('e2', (12, 36), (13, 35))
        self.add_line('e3', (34, 35), (35, 36))
        self.add_line('e4', (24, 42), (24, 39))
        self.add_line('e5', (42, 25), (24, 25))
        self.add_line('e6', (24, 25), (24, 6))
        self.add_arc('e7-1', (24, 6), (42, 24), radius_x=18)
        self.add_line('e7-2', (42, 24), (42, 25))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e7-1', 'e7-2', 'e5', 'e6', closed=True)
