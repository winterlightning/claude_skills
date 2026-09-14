"""Microphone karaoke (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ae391a9-9356-50c7-bd0a-64b441bf643b'
SOURCE_PATH = 'icons-json/audio/microphone karaoke_5ae391a9-9356-50c7-bd0a-64b441bf643b.json'
AUTHOR = 'json_to_solo'

class MicrophoneKaraokeAudio(Solo48):
    icon_id = 'microphone-karaoke-audio'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'karaoke', 'audio')

    def build(self):
        self.add_line('e0', (21, 15), (10, 32))
        self.add_line('e1', (16, 37), (30, 24))
        self.add_line('e2', (11, 44), (27, 44))
        self.add_arc('e3-top', (22, 14), (40, 14), radius_x=9, radius_y=10)
        self.add_arc('e3-bottom', (40, 14), (22, 14), radius_x=9, radius_y=10)
        self.add_bezier('e4', (10, 32), ((8.594, 34.064), (9.846, 36.291), (11, 38)))
        self.add_bezier('e5', (11, 38), ((12.827, 38.482), (14.476, 38.355), (16, 37)))
        self.add_bezier('e6', (11, 38), ((9.973, 38.736), (8, 39.318), (8, 40.891)), ((8, 40.892), (8, 40.893), (8, 40.894)), ((8, 40.966), (8.008, 41.028), (8.008, 41.091)), ((8.008, 42.718), (9.457, 43.991), (10.888, 43.991)), ((10.964, 43.991), (11.04, 44), (11.116, 44)), ((11.2, 44), (10.916, 44), (11, 44)))
        self.add_contour('c0', 'e0', 'e4')
        self.add_contour('c1', 'e5', 'e1')
        self.add_contour('c2', 'e6', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c1', 'e3')
