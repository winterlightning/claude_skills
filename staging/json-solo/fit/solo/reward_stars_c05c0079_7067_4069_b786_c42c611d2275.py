"""Reward stars (rating), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c05c0079-7067-4069-b786-c42c611d2275'
SOURCE_PATH = 'icons-json/rating/reward stars_c05c0079-7067-4069-b786-c42c611d2275.json'
AUTHOR = 'json_to_solo'

class RewardStarsRating(Solo48):
    icon_id = 'reward-stars-rating'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rating'
    aliases = ()
    keywords = ('reward', 'stars', 'rating')

    def build(self):
        self.add_line('e0', (24, 6), (30, 18))
        self.add_line('e1', (30, 18), (42, 20))
        self.add_line('e2', (42, 20), (33, 29))
        self.add_line('e3', (33, 29), (35, 42))
        self.add_line('e4', (35, 42), (24, 35))
        self.add_line('e5', (23, 35), (14, 41))
        self.add_line('e6', (13, 40), (15, 29))
        self.add_line('e7', (15, 28), (6, 20))
        self.add_line('e8', (6, 20), (18, 18))
        self.add_line('e9', (18, 18), (24, 6))
        self.add_line('e10', (24, 35), (23, 35))
        self.add_line('e11-1', (14, 41), (13, 42))
        self.add_line('e11-2', (13, 42), (13, 40))
        self.add_arc('e12', (15, 29), (15, 28), radius_x=1, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e10', 'e5', 'e11-1', 'e11-2', 'e6', 'e12', 'e7', 'e8', 'e9', closed=True)
