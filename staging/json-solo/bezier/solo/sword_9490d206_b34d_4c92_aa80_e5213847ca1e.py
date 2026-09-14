"""Sword (video-games), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9490d206-b34d-4c92-aa80-e5213847ca1e'
SOURCE_PATH = 'icons-json/video-games/sword_9490d206-b34d-4c92-aa80-e5213847ca1e.json'
AUTHOR = 'json_to_solo'

class SwordVideoGames(Solo48):
    icon_id = 'sword-video-games'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('sword', 'video-games')

    def build(self):
        self.add_line('e0', (42, 42), (31, 31))
        self.add_line('e1', (40, 22), (22, 40))
        self.add_line('e2', (34, 27), (19, 9))
        self.add_line('e3', (18, 8), (6, 6))
        self.add_line('e4', (6, 6), (8, 18))
        self.add_line('e5', (8, 19), (28, 34))
        self.add_bezier('e6', (19, 9), ((18.845, 8.812), (18.845, 8.798), (18.649, 8.651)), ((18.543, 8.569), (18.098, 8.09), (18, 8)))
        self.add_bezier('e7', (8, 18), ((8.27, 18.27), (7.689, 18.763), (8, 19)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6', 'e3', 'e4', 'e7', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c1')
