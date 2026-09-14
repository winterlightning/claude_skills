"""Microphone (audio), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70c2117f-0d53-445a-80cb-9c38d8a76797'
SOURCE_PATH = 'icons-json/audio/microphone_70c2117f-0d53-445a-80cb-9c38d8a76797.json'
AUTHOR = 'json_to_solo'

class Microphone70c2117f(Solo48):
    icon_id = 'microphone-70c2117f'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'audio')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 36))
        self.add_line('sym-e1', (24, 36), (25, 36))
        self.add_line('sym-e4', (25, 36), (24, 36))
        self.add_arc('sym-e5', (24, 36), (23, 36), radius_x=26, sweep=False)
        self.add_arc('sym-e8', (23, 36), (24, 36), radius_x=26, sweep=False)
        self.add_arc('sym-e9', (25, 36), (39, 26), radius_x=15, sweep=False)
        self.add_line('sym-e10', (39, 26), (40, 23))
        self.add_line('sym-e11', (40, 23), (40, 22))
        self.add_line('sym-e13-1', (24, 4), (28, 5))
        self.add_arc('sym-e13-2', (28, 5), (32, 10), radius_x=7)
        self.add_arc('sym-e14', (32, 10), (32, 12), radius_x=9, sweep=False)
        self.add_line('sym-e15', (32, 12), (32, 22))
        self.add_arc('sym-e16', (32, 22), (31, 24), radius_x=11)
        self.add_arc('sym-e17', (31, 24), (24, 29), radius_x=7)
        self.add_arc('sym-e18', (24, 29), (17, 24), radius_x=7)
        self.add_arc('sym-e19', (17, 24), (16, 22), radius_x=11)
        self.add_line('sym-e20', (16, 22), (16, 12))
        self.add_line('sym-e21', (16, 12), (16, 10))
        self.add_arc('sym-e22-1', (16, 10), (20, 5), radius_x=7)
        self.add_line('sym-e22-2', (20, 5), (24, 4))
        self.add_arc('sym-e24', (23, 36), (9, 26), radius_x=15)
        self.add_line('sym-e25', (9, 26), (8, 23))
        self.add_line('sym-e26', (8, 23), (8, 22))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e4', 'sym-e5', 'sym-e8')
        self.add_contour('sym-c1', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c2', 'sym-e13-1', 'sym-e13-2', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22-1', 'sym-e22-2', closed=True)
        self.add_contour('sym-c3', 'sym-e24', 'sym-e25', 'sym-e26')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
