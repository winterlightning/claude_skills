"""Microphone (audio), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e543cdc-214f-483d-bf63-44eeef6a18ba'
SOURCE_PATH = 'icons-json/audio/microphone_3e543cdc-214f-483d-bf63-44eeef6a18ba.json'
AUTHOR = 'json_to_solo'

class Microphone(Solo48):
    icon_id = 'microphone'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'audio')

    def build(self):
        self.add_arc('sym-e0', (40, 24), (40, 25), radius_x=28, sweep=False)
        self.add_arc('sym-e1', (40, 25), (39, 30), radius_x=10, sweep=False)
        self.add_arc('sym-e2', (39, 30), (24, 38), radius_x=17)
        self.add_arc('sym-e3', (24, 38), (9, 30), radius_x=17)
        self.add_arc('sym-e4', (9, 30), (8, 25), radius_x=10, sweep=False)
        self.add_line('sym-e5', (8, 25), (8, 24))
        self.add_line('sym-e6', (24, 38), (24, 44))
        self.add_line('sym-e7', (16, 19), (16, 10))
        self.add_arc('sym-e8', (16, 10), (16, 9), radius_x=4, sweep=False)
        self.add_arc('sym-e9', (16, 9), (24, 4), radius_x=9)
        self.add_arc('sym-e12', (24, 4), (32, 9), radius_x=9)
        self.add_arc('sym-e13', (32, 9), (32, 10), radius_x=4, sweep=False)
        self.add_line('sym-e14', (32, 10), (32, 19))
        self.add_arc('sym-e15', (32, 19), (25, 26), radius_x=7)
        self.add_line('sym-e16', (25, 26), (24, 26))
        self.add_line('sym-e17', (24, 26), (23, 26))
        self.add_arc('sym-e18', (23, 26), (16, 19), radius_x=7)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
