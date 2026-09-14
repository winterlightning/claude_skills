"""Music sound (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd924d40c-7b79-5735-8f6d-9d6949cbf2eb'
SOURCE_PATH = 'icons-json/audio/music sound_d924d40c-7b79-5735-8f6d-9d6949cbf2eb.json'
AUTHOR = 'json_to_solo'

class MusicSoundAudio(Solo48):
    icon_id = 'music-sound-audio'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('music', 'sound', 'audio')

    def build(self):
        self.add_line('e0', (24, 44), (24, 4))
        self.add_line('e1', (16, 10), (16, 38))
        self.add_line('e2', (32, 34), (32, 14))
        self.add_line('e3', (8, 30), (8, 18))
        self.add_line('e4', (40, 27), (40, 22))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
