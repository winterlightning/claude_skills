"""Hand down 1 (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce80faa0-dd47-4d1a-9ecb-fb349333dde8'
SOURCE_PATH = 'icons-json/state/hand down 1_ce80faa0-dd47-4d1a-9ecb-fb349333dde8.json'
AUTHOR = 'json_to_solo'

class HandDown1State(Solo48):
    icon_id = 'hand-down-1-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('hand', 'down', 'state')

    def build(self):
        self.add_line('e0', (44, 16), (39, 21))
        self.add_line('e1', (39, 21), (27, 38))
        self.add_line('e2', (23, 40), (15, 40))
        self.add_line('e3', (11, 33), (19, 20))
        self.add_line('e4', (19, 20), (9, 23))
        self.add_line('e5', (4, 23), (4, 21))
        self.add_line('e6', (23, 11), (27, 11))
        self.add_bezier('e7', (27, 38), ((26.464, 38.749), (24.545, 40), (23.564, 40)), ((23.409, 40), (23.155, 40), (23, 40)))
        self.add_bezier('e8', (15, 40), ((14.836, 40), (14.582, 40), (14.418, 40)), ((13.991, 40), (13.455, 39.739), (13.082, 39.554)), ((10.791, 38.425), (9.764, 35.038), (11, 33)))
        self.add_bezier('e9', (9, 23), ((6.936, 23.699), (6.055, 23.547), (4, 23)))
        self.add_bezier('e10', (4, 21), ((4.445, 19.939), (4, 21.735), (4.155, 20.691)), ((4.891, 19.251), (6.427, 18.248), (7.727, 17.263)), ((9.864, 15.621), (12.155, 14.282), (14.555, 12.994)), ((15.573, 12.446), (16.582, 11.857), (17.655, 11.402)), ((19.3, 10.712), (21.182, 10.579), (23, 11)))
        self.add_bezier('e11', (27, 11), ((29.382, 11.547), (32.964, 9.044), (35, 8)))
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2', 'e8', 'e3', 'e4', 'e9', 'e5', 'e10', 'e6', 'e11')
