"""Mood happy (rating), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a1975b4-7584-576b-b4b1-f9e4af45a884'
SOURCE_PATH = 'pictographic-primitives/rating/mood happy_3a1975b4-7584-576b-b4b1-f9e4af45a884.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MoodHappy(Solo48):
    icon_id = 'mood-happy'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rating'
    categories = ('rating', 'primitives')
    aliases = ()
    keywords = ('mood', 'happy', 'rating')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_line('sym-e2', (18, 19), (18, 21))
        self.add_arc('sym-e3', (17, 30), (24, 34), radius_x=8, sweep=False)
        self.add_arc('sym-e4', (24, 34), (31, 30), radius_x=8, sweep=False)
        self.add_line('sym-e5', (30, 19), (30, 21))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5')
