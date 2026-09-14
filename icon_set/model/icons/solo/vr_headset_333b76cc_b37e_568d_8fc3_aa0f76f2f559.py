"""Vr headset (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '333b76cc-b37e-568d-8fc3-aa0f76f2f559'
SOURCE_PATH = 'icons-json/video-games/vr headset_333b76cc-b37e-568d-8fc3-aa0f76f2f559.json'
AUTHOR = 'json_to_solo'

class VrHeadset(Solo48):
    icon_id = 'vr-headset'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('vr', 'headset', 'video-games')

    def build(self):
        self.add_line('e0', (13, 42), (13, 36))
        self.add_line('e1', (12, 33), (8, 29))
        self.add_line('e2', (22, 17), (6, 17))
        self.add_line('e3', (37, 23), (39, 30))
        self.add_line('e4', (39, 30), (35, 31))
        self.add_line('e5', (35, 31), (35, 35))
        self.add_line('e6', (28, 38), (28, 42))
        self.add_line('e7', (40, 23), (27, 23))
        self.add_line('e8', (27, 12), (40, 12))
        self.add_line('e9', (42, 13), (42, 22))
        self.add_arc('e10-1', (35, 12), (27, 7), radius_x=19, sweep=False)
        self.add_line('e10-2', (27, 7), (21, 6))
        self.add_arc('e10-3', (21, 6), (6, 17), radius_x=16, sweep=False)
        self.add_line('e10-4', (6, 17), (6, 18))
        self.add_line('e11', (13, 36), (12, 33))
        self.add_line('e12-1', (8, 29), (6, 23))
        self.add_line('e12-2', (6, 23), (6, 18))
        self.add_arc('e13', (35, 35), (28, 38), radius_x=5)
        self.add_arc('e14-1', (27, 23), (22, 17), radius_x=5)
        self.add_arc('e14-2', (22, 17), (27, 12), radius_x=5)
        self.add_line('e15', (40, 12), (42, 13))
        self.add_line('e16', (42, 22), (40, 23))
        self.add_contour('c0', 'e10-1', 'e10-2', 'e10-3', 'e10-4')
        self.add_contour('c1', 'e0', 'e11', 'e1', 'e12-1', 'e12-2')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5', 'e13', 'e6')
        self.add_contour('c4', 'e7', 'e14-1', 'e14-2', 'e8', 'e15', 'e9', 'e16', closed=True)
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c0')
        self.relate('connect', 'c3', 'c4')
