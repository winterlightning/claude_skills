"""Button syncing (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '18f9d573-e7b3-5500-9011-0bd7ffb6dcc0'
SOURCE_PATH = 'icons-json/interface-essential/button syncing_18f9d573-e7b3-5500-9011-0bd7ffb6dcc0.json'
AUTHOR = 'json_to_solo'

class ButtonSyncingInterfaceEssential(Solo48):
    icon_id = 'button-syncing-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('button', 'syncing', 'interface-essential')

    def build(self):
        self.add_line('e0', (31, 4), (35, 10))
        self.add_line('e1', (35, 10), (29, 11))
        self.add_line('e2', (17, 40), (13, 38))
        self.add_line('e3', (19, 37), (13, 38))
        self.add_line('e4', (13, 38), (17, 44))
        self.add_bezier('e5', (10, 31), ((9.175, 28.745), (8.008, 26.5), (8.008, 24.045)), ((8.008, 23.902), (8, 23.768), (8, 23.634)), ((8, 23.632), (8, 23.629), (8, 23.627)), ((8, 23.418), (8.017, 23.209), (8.017, 23)), ((8.017, 21.527), (8.387, 19.973), (8.775, 18.573)), ((10.914, 10.882), (17.272, 5.927), (24.707, 6.364)), ((28.379, 6.582), (31.766, 8.318), (35, 10)))
        self.add_bezier('e6', (38, 17), ((38.851, 19.218), (39.983, 21.427), (39.983, 23.864)), ((39.983, 24.073), (40, 24.273), (40, 24.482)), ((40, 24.485), (40, 24.488), (40, 24.492)), ((40, 24.697), (39.992, 24.903), (39.992, 25.1)), ((39.992, 26.809), (39.545, 28.636), (39.023, 30.236)), ((36.581, 37.755), (29.718, 42.755), (22.307, 41.891)), ((20.573, 41.691), (18.507, 40.973), (17, 40)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e5', 'e1')
        self.add_contour('c2', 'e6', 'e2')
        self.add_contour('c3', 'e3', 'e4')
        self.relate('connect', 'c2', 'c3')
