"""Explosion sound effect text (video-games), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f2ba451-650e-406e-a2e4-faf0686c7ce1'
SOURCE_PATH = 'icons-json/video-games/explosion sound effect text_5f2ba451-650e-406e-a2e4-faf0686c7ce1.json'
AUTHOR = 'json_to_solo'

class ExplosionSoundEffectTextVideoGames(Solo48):
    icon_id = 'explosion-sound-effect-text-video-games'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('explosion', 'sound', 'effect', 'text', 'video-games')

    def build(self):
        self.add_line('e0', (17, 39), (6, 23))
        self.add_line('e1', (6, 23), (15, 26))
        self.add_line('e2', (15, 26), (13, 14))
        self.add_line('e3', (13, 14), (19, 19))
        self.add_line('e4', (19, 19), (23, 6))
        self.add_line('e5', (23, 6), (28, 23))
        self.add_line('e6', (28, 23), (39, 18))
        self.add_line('e7', (39, 18), (33, 31))
        self.add_line('e8', (33, 31), (42, 31))
        self.add_line('e9', (42, 31), (28, 42))
        self.add_line('e10', (11, 42), (37, 42))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9')
        self.add_contour('c1', 'e10')
        self.relate('connect', 'c0', 'c1')
