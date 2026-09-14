"""Number (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1edccb27-38c1-5d49-b045-3faf028ee95b'
SOURCE_PATH = 'icons-json/interface-essential/number_1edccb27-38c1-5d49-b045-3faf028ee95b.json'
AUTHOR = 'json_to_solo'

class NumberInterfaceEssential(Solo48):
    icon_id = 'number-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('number', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 44), (18, 44))
        self.add_line('e1', (37, 35), (34, 35))
        self.add_line('e2', (19, 7), (24, 4))
        self.add_line('e3', (24, 4), (24, 20))
        self.add_line('e4', (19, 20), (29, 20))
        self.add_bezier('e5', (8, 30), ((8.61, 28.436), (9.61, 27.418), (11.46, 26.855)), ((14.65, 25.864), (17.93, 28.273), (17.57, 31.309)), ((17.3, 33.555), (15.44, 35.118), (13.81, 36.636)), ((12.06, 38.264), (9.9, 39.9), (8.74, 41.964)), ((8.39, 42.591), (8.22, 43.327), (8, 44)))
        self.add_bezier('e6', (30, 29), ((30.21, 28.455), (30.36, 28.364), (30.72, 27.873)), ((33.41, 24.209), (40, 26.964), (39.69, 31.382)), ((39.47, 32.918), (38.16, 34), (37, 35)))
        self.add_bezier('e7', (37, 35), ((38.49, 36.027), (39.99, 36.845), (39.99, 38.718)), ((39.99, 39.022), (40, 39.327), (40, 39.622)), ((40, 39.627), (40, 39.632), (40, 39.636)), ((40, 39.827), (39.98, 40.018), (39.98, 40.2)), ((39.98, 41.991), (37.92, 43.991), (35.93, 43.991)), ((35.85, 44), (35.78, 44), (35.7, 44)), ((35.56, 43.991), (35.41, 43.991), (35.26, 43.982)), ((33.04, 43.982), (31.02, 41.573), (30, 40)))
        self.add_contour('c0', 'e5', 'e0')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('c3', 'e1')
        self.add_contour('c4', 'e2', 'e3')
        self.add_contour('c5', 'e4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c4', 'c5')
