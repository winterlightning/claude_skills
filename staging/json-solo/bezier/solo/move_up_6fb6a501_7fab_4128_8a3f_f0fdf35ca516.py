"""Move up (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6fb6a501-7fab-4128-8a3f-f0fdf35ca516'
SOURCE_PATH = 'icons-json/interface-essential/move up_6fb6a501-7fab-4128-8a3f-f0fdf35ca516.json'
AUTHOR = 'json_to_solo'

class MoveUpInterfaceEssential(Solo48):
    icon_id = 'move-up-interface-essential'
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
        self.add_bezier('e7', (8, 42), ((8.093, 42.2), (8.017, 42.436), (8.101, 42.645)), ((8.413, 43.427), (9.36, 43.691), (10, 44)))
        self.add_bezier('e8', (38, 44), ((38.042, 43.991), (38.4, 43.991), (38.442, 43.982)), ((38.998, 43.982), (39.672, 43.209), (39.882, 42.718)), ((39.949, 42.555), (39.941, 42.164), (40, 42)))
        self.add_bezier('e9', (40, 34), ((40, 33.845), (39.992, 33.7), (39.992, 33.545)), ((39.992, 32.855), (39.387, 32.409), (39, 32)))
        self.add_bezier('e10', (9, 32), ((8.604, 32.445), (8.008, 32.973), (8.008, 33.691)), ((8, 33.745), (8, 33.791), (8, 33.845)), ((8, 33.9), (8, 33.945), (8, 34)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', 'e6', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
