"""Vr headset (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '427e8988-7e0f-4f0e-930b-42ce7a00bd27'
SOURCE_PATH = 'icons-json/video-games/vr headset_427e8988-7e0f-4f0e-930b-42ce7a00bd27.json'
AUTHOR = 'json_to_solo'

class VrHeadsetVideoGames(Solo48):
    icon_id = 'vr-headset-video-games'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('vr', 'headset', 'video-games')

    def build(self):
        self.add_line('sym-e0', (24, 8), (29, 8))
        self.add_arc('sym-e1', (29, 8), (31, 8), radius_x=58, sweep=False)
        self.add_line('sym-e2', (31, 8), (35, 9))
        self.add_arc('sym-e3', (35, 9), (39, 11), radius_x=11)
        self.add_arc('sym-e4-1', (39, 11), (43, 17), radius_x=12)
        self.add_line('sym-e4-2', (43, 17), (44, 25))
        self.add_arc('sym-e6', (44, 25), (44, 26), radius_x=30, sweep=False)
        self.add_line('sym-e7-1', (44, 26), (42, 36))
        self.add_arc('sym-e7-2', (42, 36), (37, 40), radius_x=7)
        self.add_line('sym-e9', (37, 40), (36, 40))
        self.add_arc('sym-e10-1', (36, 40), (27, 30), radius_x=19)
        self.add_arc('sym-e10-2', (27, 30), (24, 29), radius_x=3, sweep=False)
        self.add_arc('sym-e13-1', (24, 29), (21, 30), radius_x=3, sweep=False)
        self.add_arc('sym-e13-2', (21, 30), (12, 40), radius_x=19)
        self.add_line('sym-e14', (12, 40), (11, 40))
        self.add_arc('sym-e16-1', (11, 40), (6, 36), radius_x=7)
        self.add_line('sym-e16-2', (6, 36), (4, 26))
        self.add_line('sym-e17', (4, 26), (4, 25))
        self.add_line('sym-e19-1', (4, 25), (5, 17))
        self.add_arc('sym-e19-2', (5, 17), (9, 11), radius_x=12)
        self.add_arc('sym-e20', (9, 11), (13, 9), radius_x=11)
        self.add_line('sym-e21', (13, 9), (17, 8))
        self.add_line('sym-e22-1', (17, 8), (18, 8))
        self.add_line('sym-e22-2', (18, 8), (19, 8))
        self.add_line('sym-e23', (19, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4-1', 'sym-e4-2', 'sym-e6', 'sym-e7-1', 'sym-e7-2', 'sym-e9', 'sym-e10-1', 'sym-e10-2', 'sym-e13-1', 'sym-e13-2', 'sym-e14', 'sym-e16-1', 'sym-e16-2', 'sym-e17', 'sym-e19-1', 'sym-e19-2', 'sym-e20', 'sym-e21', 'sym-e22-1', 'sym-e22-2', 'sym-e23', closed=True)
