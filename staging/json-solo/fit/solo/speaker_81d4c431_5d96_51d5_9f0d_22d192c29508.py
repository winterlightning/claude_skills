"""Speaker (audio), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81d4c431-5d96-51d5-9f0d-22d192c29508'
SOURCE_PATH = 'icons-json/audio/speaker_81d4c431-5d96-51d5-9f0d-22d192c29508.json'
AUTHOR = 'json_to_solo'

class SpeakerAudio(Solo48):
    icon_id = 'speaker-audio'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('speaker', 'audio')

    def build(self):
        self.add_line('e0', (9, 34), (8, 35))
        self.add_line('e1', (35, 39), (36, 40))
        self.add_line('e2', (40, 14), (40, 13))
        self.add_arc('e3-top', (17, 24), (31, 24), radius_x=7)
        self.add_arc('e3-bottom', (31, 24), (17, 24), radius_x=7)
        self.add_arc('e4-1', (8, 35), (10, 40), radius_x=3, sweep=False)
        self.add_arc('e4-2', (10, 40), (13, 39), radius_x=3, sweep=False)
        self.add_line('e4-3', (13, 39), (24, 42))
        self.add_line('e4-4', (24, 42), (35, 39))
        self.add_arc('e5-1', (36, 40), (40, 40), radius_x=3, sweep=False)
        self.add_arc('e5-2', (40, 40), (39, 34), radius_x=4, sweep=False)
        self.add_line('e5-3', (39, 34), (41, 30))
        self.add_line('e5-4', (41, 30), (42, 24))
        self.add_line('e5-5', (42, 24), (40, 14))
        self.add_line('e6-1', (40, 13), (40, 10))
        self.add_arc('e6-2', (40, 10), (37, 9), radius_x=3, sweep=False)
        self.add_arc('e6-3', (37, 9), (33, 8), radius_x=3)
        self.add_line('e6-4', (33, 8), (24, 6))
        self.add_line('e6-5', (24, 6), (13, 9))
        self.add_arc('e6-6', (13, 9), (8, 9), radius_x=4, sweep=False)
        self.add_arc('e6-7', (8, 9), (9, 14), radius_x=4, sweep=False)
        self.add_arc('e6-8', (9, 14), (7, 18), radius_x=19, sweep=False)
        self.add_arc('e6-9', (7, 18), (6, 24), radius_x=19, sweep=False)
        self.add_line('e6-10', (6, 24), (9, 35))
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7', 'e6-8', 'e6-9', 'e6-10')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
