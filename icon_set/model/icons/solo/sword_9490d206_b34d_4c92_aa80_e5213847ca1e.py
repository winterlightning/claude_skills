"""Sword (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9490d206-b34d-4c92-aa80-e5213847ca1e'
SOURCE_PATH = 'pictographic-primitives/video-games/sword_9490d206-b34d-4c92-aa80-e5213847ca1e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Sword(Solo48):
    icon_id = 'sword'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('video-games', 'state')
    aliases = ()
    keywords = ('sword', 'video-games')

    def build(self):
        self.add_line('e0', (42, 42), (31, 31))
        self.add_line('e1', (40, 22), (22, 40))
        self.add_line('e2', (34, 27), (19, 9))
        self.add_line('e3', (18, 8), (6, 6))
        self.add_line('e4', (6, 6), (8, 18))
        self.add_line('e5', (8, 19), (28, 34))
        self.add_line('e6', (19, 9), (18, 8))
        self.add_line('e7', (8, 18), (8, 19))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6', 'e3', 'e4', 'e7', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c1')
