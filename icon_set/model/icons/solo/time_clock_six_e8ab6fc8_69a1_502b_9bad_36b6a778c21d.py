"""Time clock six (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e8ab6fc8-69a1-502b-9bad-36b6a778c21d'
SOURCE_PATH = 'icons-json/interface-essential/time clock six_e8ab6fc8-69a1-502b-9bad-36b6a778c21d.json'
AUTHOR = 'gpt-6'

class TimeClockSix(Solo48):
    icon_id = 'time-clock-six'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('time', 'clock', 'six', 'interface-essential')

    def build(self):
        self.add_line('e0', (25, 42), (25, 6))
        self.add_line('e1', (13, 33), (11, 36))
        self.add_line('e2', (6, 24), (10, 24))
        self.add_line('e3', (13, 15), (11, 12))
        self.add_line('e4', (35, 14), (37, 12))
        self.add_line('e5', (39, 24), (42, 24))
        self.add_line('e6', (35, 33), (37, 35))
        self.add_line('e7-1', (25, 6), (16, 8))
        self.add_arc('e7-2', (16, 8), (10, 13), radius_x=17, radius_y=17, large_arc=False, sweep=False)
        self.add_arc('e7-3', (10, 13), (6, 24), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_arc('e7-4', (6, 24), (14, 39), radius_x=19, radius_y=19, large_arc=False, sweep=False)
        self.add_line('e7-5', (14, 39), (18, 41))
        self.add_line('e7-6', (18, 41), (25, 42))
        self.add_contour('c0', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e7-6', 'e0', closed=True)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', closed=False)
        self.add_contour('c3', 'e3', closed=False)
        self.add_contour('c4', 'e4', closed=False)
        self.add_contour('c5', 'e5', closed=False)
        self.add_contour('c6', 'e6', closed=False)
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'c0')
