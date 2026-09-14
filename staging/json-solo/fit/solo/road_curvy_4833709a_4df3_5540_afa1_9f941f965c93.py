"""Road curvy (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4833709a-4df3-5540-afa1-9f941f965c93'
SOURCE_PATH = 'icons-json/transportation/road curvy_4833709a-4df3-5540-afa1-9f941f965c93.json'
AUTHOR = 'json_to_solo'

class RoadCurvyTransportation(Solo48):
    icon_id = 'road-curvy-transportation'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('road', 'curvy', 'transportation')

    def build(self):
        self.add_line('e0', (33, 9), (38, 4))
        self.add_line('e1', (38, 4), (32, 5))
        self.add_line('e2', (13, 41), (8, 44))
        self.add_arc('e3-1', (37, 44), (40, 35), radius_x=18, sweep=False)
        self.add_line('e3-2', (40, 35), (39, 29))
        self.add_arc('e3-3', (39, 29), (36, 25), radius_x=15, sweep=False)
        self.add_arc('e3-4', (36, 25), (29, 16), radius_x=13)
        self.add_arc('e3-5', (29, 16), (33, 9), radius_x=10)
        self.add_arc('e4-1', (32, 5), (16, 16), radius_x=21, sweep=False)
        self.add_arc('e4-2', (16, 16), (16, 20), radius_x=6, sweep=False)
        self.add_arc('e4-3', (16, 20), (21, 31), radius_x=17)
        self.add_arc('e4-4', (21, 31), (13, 41), radius_x=16)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e0', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e2')
