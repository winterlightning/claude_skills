"""Time stopwatch half (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91cc612c-2da3-5c85-8791-ab1cd23dc432'
SOURCE_PATH = 'icons-json/interface-essential/time stopwatch half_91cc612c-2da3-5c85-8791-ab1cd23dc432.json'
AUTHOR = 'json_to_solo'

class TimeStopwatchHalfInterfaceEssential(Solo48):
    icon_id = 'time-stopwatch-half-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('time', 'stopwatch', 'half', 'interface-essential')

    def build(self):
        self.add_line('e0', (23, 44), (23, 4))
        self.add_line('e1', (20, 4), (27, 4))
        self.add_line('e2', (40, 14), (36, 19))
        self.add_line('e3', (37, 11), (40, 14))
        self.add_arc('e4-top', (8, 28), (38, 28), radius_x=15, radius_y=16)
        self.add_arc('e4-bottom', (38, 28), (8, 28), radius_x=15, radius_y=16)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'e4')
