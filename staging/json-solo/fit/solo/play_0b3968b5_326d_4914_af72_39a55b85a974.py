"""Play (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b3968b5-326d-4914-af72-39a55b85a974'
SOURCE_PATH = 'icons-json/design/play_0b3968b5-326d-4914-af72-39a55b85a974.json'
AUTHOR = 'json_to_solo'

class PlayDesign(Solo48):
    icon_id = 'play-design'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('play', 'design')

    def build(self):
        self.add_line('e0', (42, 23), (38, 26))
        self.add_line('e1', (38, 26), (6, 42))
        self.add_line('e2', (6, 42), (6, 39))
        self.add_line('e3', (6, 39), (6, 13))
        self.add_line('e4', (6, 13), (6, 6))
        self.add_line('e5', (6, 6), (42, 23))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', closed=True)
