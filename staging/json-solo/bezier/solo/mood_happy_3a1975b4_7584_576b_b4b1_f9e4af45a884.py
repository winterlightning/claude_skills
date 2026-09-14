"""Mood happy (rating), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3a1975b4-7584-576b-b4b1-f9e4af45a884'
SOURCE_PATH = 'icons-json/rating/mood happy_3a1975b4-7584-576b-b4b1-f9e4af45a884.json'
AUTHOR = 'json_to_solo'

class MoodHappyRating(Solo48):
    icon_id = 'mood-happy-rating'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rating'
    aliases = ()
    keywords = ('mood', 'happy', 'rating')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_line('sym-e2', (18, 19), (18, 21))
        self.add_bezier('sym-e3', (17, 30), ((19.027, 32.709), (21.394, 34.209), (24, 34)))
        self.add_bezier('sym-e4', (24, 34), ((26.606, 34.209), (28.973, 32.709), (31, 30)))
        self.add_line('sym-e5', (30, 19), (30, 21))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5')
