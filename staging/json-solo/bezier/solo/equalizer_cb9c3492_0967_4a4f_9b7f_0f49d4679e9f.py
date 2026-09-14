"""Equalizer (audio), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb9c3492-0967-4a4f-9b7f-0f49d4679e9f'
SOURCE_PATH = 'icons-json/audio/equalizer_cb9c3492-0967-4a4f-9b7f-0f49d4679e9f.json'
AUTHOR = 'json_to_solo'

class Equalizer(Solo48):
    icon_id = 'equalizer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('equalizer', 'audio')

    def build(self):
        self.add_line('e0', (42, 6), (42, 42))
        self.add_line('e1', (18, 11), (18, 37))
        self.add_line('e2', (30, 31), (30, 17))
        self.add_line('e3', (6, 29), (6, 21))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
