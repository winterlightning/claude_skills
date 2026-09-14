"""Microphone podcast (audio), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b07660f9-f5a9-58bd-bb19-abd1d2970779'
SOURCE_PATH = 'icons-json/audio/microphone podcast_b07660f9-f5a9-58bd-bb19-abd1d2970779.json'
AUTHOR = 'json_to_solo'

class MicrophonePodcast(Solo48):
    icon_id = 'microphone-podcast'
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
        self.add_arc('e7-1', (15, 20), (25, 27), radius_x=8, sweep=False)
        self.add_arc('e7-2', (25, 27), (33, 20), radius_x=8, sweep=False)
        self.add_arc('e8-1', (33, 13), (24, 4), radius_x=9, sweep=False)
        self.add_line('e8-2', (24, 4), (18, 6))
        self.add_arc('e8-3', (18, 6), (15, 11), radius_x=8, sweep=False)
        self.add_arc('e9-1', (40, 22), (29, 35), radius_x=14)
        self.add_arc('e9-2', (29, 35), (12, 31), radius_x=17)
        self.add_arc('e9-3', (12, 31), (9, 27), radius_x=14)
        self.add_line('e9-4', (9, 27), (8, 18))
        self.add_contour('c0', 'e0', 'e1', 'e7-1', 'e7-2', 'e2', 'e8-1', 'e8-2', 'e8-3', 'e3')
        self.add_contour('c1', 'e4', 'e9-1', 'e9-2', 'e9-3', 'e9-4')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e6')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c3')
