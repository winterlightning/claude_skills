"""Move up (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6fb6a501-7fab-4128-8a3f-f0fdf35ca516'
SOURCE_PATH = 'icons-json/interface-essential/move up_6fb6a501-7fab-4128-8a3f-f0fdf35ca516.json'
AUTHOR = 'json_to_solo'

class MoveUp(Solo48):
    icon_id = 'move-up'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('move', 'up', 'interface-essential')

    def build(self):
        self.add_line('e0', (18, 10), (24, 4))
        self.add_line('e1', (24, 24), (24, 4))
        self.add_line('e2', (30, 10), (24, 4))
        self.add_line('e3', (8, 34), (8, 42))
        self.add_line('e4', (10, 44), (38, 44))
        self.add_line('e5', (40, 42), (40, 34))
        self.add_line('e6', (39, 32), (9, 32))
        self.add_arc('e7', (8, 42), (10, 44), radius_x=2, sweep=False)
        self.add_arc('e8', (38, 44), (40, 42), radius_x=2, sweep=False)
        self.add_line('e9', (40, 34), (39, 32))
        self.add_line('e10', (9, 32), (8, 34))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', 'e6', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
