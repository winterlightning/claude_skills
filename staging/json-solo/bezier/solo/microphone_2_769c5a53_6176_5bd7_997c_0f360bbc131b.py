"""Microphone 2 (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e1', (24, 33), ((15.594, 33), (8, 27.245), (8, 21)))
        self.add_bezier('sym-e2', (8, 21), ((8, 20.7), (8, 20.3), (8, 20)))
        self.add_line('sym-e3', (17, 44), (24, 44))
        self.add_line('sym-e4', (24, 44), (31, 44))
        self.add_bezier('sym-e5', (15, 19), ((15, 20.209), (16.188, 21.973), (17, 23)))
        self.add_bezier('sym-e6', (17, 23), ((18.806, 25.259), (21.312, 26), (24, 26)))
        self.add_bezier('sym-e7', (24, 26), ((26.688, 26), (29.194, 25.259), (31, 23)))
        self.add_bezier('sym-e8', (31, 23), ((31.812, 21.973), (33, 20.209), (33, 19)))
        self.add_line('sym-e9', (33, 19), (33, 10))
        self.add_bezier('sym-e10', (33, 10), ((33, 6.955), (29.382, 4), (25, 4)))
        self.add_bezier('sym-e11', (25, 4), ((24.902, 4), (24.098, 4), (24, 4)))
        self.add_bezier('sym-e12', (24, 4), ((23.861, 4.006), (24.139, 4), (24, 4)))
        self.add_bezier('sym-e13', (24, 4), ((23.861, 4), (24.139, 4.006), (24, 4)))
        self.add_bezier('sym-e14', (24, 4), ((23.902, 4), (23.098, 4), (23, 4)))
        self.add_bezier('sym-e15', (23, 4), ((18.618, 4), (15, 6.955), (15, 10)))
        self.add_line('sym-e16', (15, 10), (15, 19))
        self.add_bezier('sym-e17', (40, 20), ((40, 20.3), (40, 20.7), (40, 21)))
        self.add_bezier('sym-e18', (40, 21), ((40, 27.245), (32.406, 33), (24, 33)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', closed=True)
        self.add_contour('sym-c3', 'sym-e17', 'sym-e18')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
