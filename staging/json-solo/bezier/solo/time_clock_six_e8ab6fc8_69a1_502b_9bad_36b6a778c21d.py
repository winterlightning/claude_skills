"""Time clock six (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8ab6fc8-69a1-502b-9bad-36b6a778c21d'
SOURCE_PATH = 'icons-json/interface-essential/time clock six_e8ab6fc8-69a1-502b-9bad-36b6a778c21d.json'
AUTHOR = 'json_to_solo'

class TimeClockSixInterfaceEssential(Solo48):
    icon_id = 'time-clock-six-interface-essential'
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
        self.add_bezier('e7', (25, 6), ((24.73, 6), (24.278, 6.016), (24.016, 6.016)), ((19.165, 6.016), (14.182, 8.16), (10.909, 11.727)), ((8.103, 14.787), (6.008, 19.189), (6.008, 23.403)), ((6.008, 23.599), (6, 23.804), (6, 24)), ((6, 24.196), (6.016, 24.401), (6.016, 24.597)), ((6.016, 28.803), (8.111, 33.221), (10.909, 36.273)), ((14.182, 39.856), (19.165, 41.984), (24.016, 41.984)), ((24.286, 41.984), (24.73, 42), (25, 42)))
        self.add_contour('c0', 'e7', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'c0')
