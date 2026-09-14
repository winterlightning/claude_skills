"""Move right 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8e61c84-2e10-4e16-b762-cf78ea0473ae'
SOURCE_PATH = 'icons-json/interface-essential/move right 1_c8e61c84-2e10-4e16-b762-cf78ea0473ae.json'
AUTHOR = 'json_to_solo'

class MoveRight1C8e61c84(Solo48):
    icon_id = 'move-right-1-c8e61c84'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('move', 'right', 'interface-essential')

    def build(self):
        self.add_line('e0', (39, 19), (44, 24))
        self.add_line('e1', (25, 24), (44, 24))
        self.add_line('e2', (39, 29), (44, 24))
        self.add_line('e3', (16, 8), (6, 8))
        self.add_line('e4', (4, 10), (4, 38))
        self.add_line('e5', (6, 40), (16, 40))
        self.add_line('e6', (18, 38), (18, 10))
        self.add_bezier('e7', (6, 8), ((5.964, 8), (5.755, 8.008), (5.718, 8.008)), ((4.673, 8.008), (4.3, 9.309), (4, 10)))
        self.add_bezier('e8', (4, 38), ((4.527, 39.145), (4.773, 39.503), (6, 40)))
        self.add_bezier('e9', (16, 40), ((17.227, 39.469), (17.445, 39.12), (18, 38)))
        self.add_bezier('e10', (18, 10), ((17.491, 9.006), (17.136, 8.438), (16, 8)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', 'e6', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
