"""Martial arts sword fencing (sports), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a998291b-f3d0-53ea-ba75-ad630276a239'
SOURCE_PATH = 'pictographic-primitives/sports/martial arts sword fencing_a998291b-f3d0-53ea-ba75-ad630276a239.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MartialArtsSwordFencing(Solo48):
    icon_id = 'martial-arts-sword-fencing'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases = ()
    keywords = ('martial', 'arts', 'sword', 'fencing', 'sports')

    def build(self):
        self.add_line('e0', (44, 8), (7, 40))
        self.add_line('e1', (4, 8), (41, 40))
        self.add_line('e2', (12, 30), (19, 36))
        self.add_line('e3', (29, 36), (36, 30))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
