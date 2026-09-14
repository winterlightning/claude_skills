"""Time clock nine (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cba1d48c-2f8c-4f0c-ae87-fd2604853f59'
SOURCE_PATH = 'icons-json/interface-essential/time clock nine_cba1d48c-2f8c-4f0c-ae87-fd2604853f59.json'
AUTHOR = 'json_to_solo'

class TimeClockNineInterfaceEssential(Solo48):
    icon_id = 'time-clock-nine-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('time', 'clock', 'nine', 'interface-essential')

    def build(self):
        self.add_line('e0', (38, 23), (42, 23))
        self.add_line('e1', (24, 38), (24, 42))
        self.add_line('e2', (14, 35), (12, 37))
        self.add_line('e3', (24, 6), (24, 23))
        self.add_line('e4', (24, 23), (6, 23))
        self.add_arc('e5-1', (42, 23), (25, 6), radius_x=18, sweep=False)
        self.add_arc('e5-2', (25, 6), (24, 6), radius_x=51)
        self.add_line('e6-1', (6, 23), (7, 30))
        self.add_arc('e6-2', (7, 30), (10, 35), radius_x=23, sweep=False)
        self.add_arc('e6-3', (10, 35), (23, 42), radius_x=16, sweep=False)
        self.add_arc('e6-4', (23, 42), (24, 42), radius_x=27)
        self.add_line('e7-1', (42, 23), (40, 32))
        self.add_arc('e7-2', (40, 32), (39, 34), radius_x=19)
        self.add_arc('e7-3', (39, 34), (25, 42), radius_x=18)
        self.add_arc('e7-4', (25, 42), (24, 42), radius_x=29, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e5-1', 'e5-2', 'e3', 'e4', 'e6-1', 'e6-2', 'e6-3', 'e6-4')
        self.add_contour('c4', 'e7-1', 'e7-2', 'e7-3', 'e7-4')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c3')
