"""Microphone 2 (audio), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '769c5a53-6176-5bd7-997c-0f360bbc131b'
SOURCE_PATH = 'icons-json/audio/microphone 2_769c5a53-6176-5bd7-997c-0f360bbc131b.json'
AUTHOR = 'json_to_solo'

class Microphone2Audio(Solo48):
    icon_id = 'microphone-2-audio'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'audio')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 33))
        self.add_arc('sym-e1', (24, 33), (8, 21), radius_x=15)
        self.add_line('sym-e2', (8, 21), (8, 20))
        self.add_line('sym-e3', (17, 44), (24, 44))
        self.add_line('sym-e4', (24, 44), (31, 44))
        self.add_arc('sym-e5', (15, 19), (17, 23), radius_x=6, sweep=False)
        self.add_arc('sym-e6', (17, 23), (24, 26), radius_x=9, sweep=False)
        self.add_arc('sym-e7', (24, 26), (31, 23), radius_x=9, sweep=False)
        self.add_line('sym-e8', (31, 23), (33, 19))
        self.add_line('sym-e9', (33, 19), (33, 10))
        self.add_line('sym-e10-1', (33, 10), (30, 6))
        self.add_arc('sym-e10-2', (30, 6), (25, 4), radius_x=8, sweep=False)
        self.add_arc('sym-e11', (25, 4), (24, 4), radius_x=76)
        self.add_arc('sym-e14', (24, 4), (23, 4), radius_x=69)
        self.add_arc('sym-e15-1', (23, 4), (18, 6), radius_x=8, sweep=False)
        self.add_arc('sym-e15-2', (18, 6), (15, 10), radius_x=6, sweep=False)
        self.add_line('sym-e16', (15, 10), (15, 19))
        self.add_line('sym-e17', (40, 20), (40, 21))
        self.add_arc('sym-e18', (40, 21), (24, 33), radius_x=15)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10-1', 'sym-e10-2', 'sym-e11', 'sym-e14', 'sym-e15-1', 'sym-e15-2', 'sym-e16', closed=True)
        self.add_contour('sym-c3', 'sym-e17', 'sym-e18')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
