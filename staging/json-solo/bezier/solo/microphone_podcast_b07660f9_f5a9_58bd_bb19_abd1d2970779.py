"""Microphone podcast (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b07660f9-f5a9-58bd-bb19-abd1d2970779'
SOURCE_PATH = 'icons-json/audio/microphone podcast_b07660f9-f5a9-58bd-bb19-abd1d2970779.json'
AUTHOR = 'json_to_solo'

class MicrophonePodcastAudio(Solo48):
    icon_id = 'microphone-podcast-audio'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'podcast', 'audio')

    def build(self):
        self.add_line('e0', (18, 16), (15, 16))
        self.add_line('e1', (15, 16), (15, 20))
        self.add_line('e2', (33, 20), (33, 13))
        self.add_line('e3', (15, 11), (15, 16))
        self.add_line('e4', (40, 19), (40, 22))
        self.add_line('e5', (24, 36), (24, 44))
        self.add_line('e6', (14, 44), (34, 44))
        self.add_bezier('e7', (15, 20), ((15, 21.1), (15.59, 22.691), (16.23, 23.591)), ((19.75, 28.527), (28.3, 28.291), (31.73, 23.427)), ((32.31, 22.609), (33, 21), (33, 20)))
        self.add_bezier('e8', (33, 13), ((33, 11.964), (33.1, 10.918), (32.74, 9.909)), ((31.59, 6.655), (28.24, 4.009), (24.35, 4.009)), ((24.193, 4.009), (24.045, 4), (23.887, 4)), ((23.885, 4), (23.883, 4), (23.88, 4)), ((23.72, 4), (23.57, 4.009), (23.41, 4.009)), ((19.47, 4.009), (15, 7.327), (15, 11)))
        self.add_bezier('e9', (40, 22), ((39.99, 22.082), (39.99, 22.345), (39.98, 22.427)), ((39.98, 29.918), (31.75, 35.627), (24, 35.818)), ((17.63, 35.973), (10.74, 31.536), (8.68, 26.109)), ((8, 23.582), (8.06, 20.673), (8.02, 18.045)), ((8.01, 17.909), (8.01, 18.136), (8, 18)))
        self.add_contour('c0', 'e0', 'e1', 'e7', 'e2', 'e8', 'e3')
        self.add_contour('c1', 'e4', 'e9')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e6')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c3')
