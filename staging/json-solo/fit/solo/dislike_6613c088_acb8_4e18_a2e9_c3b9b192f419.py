"""Dislike (rating), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6613c088-acb8-4e18-a2e9-c3b9b192f419'
SOURCE_PATH = 'icons-json/rating/dislike_6613c088-acb8-4e18-a2e9-c3b9b192f419.json'
AUTHOR = 'json_to_solo'

class DislikeRating(Solo48):
    icon_id = 'dislike-rating'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rating'
    aliases = ()
    keywords = ('dislike', 'rating')

    def build(self):
        self.add_line('e0', (12, 8), (17, 7))
        self.add_line('e1', (19, 6), (30, 6))
        self.add_line('e2', (39, 13), (41, 20))
        self.add_line('e3', (38, 26), (26, 27))
        self.add_line('e4', (26, 27), (29, 33))
        self.add_line('e5', (24, 40), (17, 30))
        self.add_line('e6', (6, 26), (6, 7))
        self.add_arc('e7', (6, 8), (12, 8), radius_x=15, sweep=False)
        self.add_arc('e8', (17, 7), (19, 6), radius_x=8, sweep=False)
        self.add_line('e9-1', (30, 6), (35, 7))
        self.add_arc('e9-2', (35, 7), (39, 13), radius_x=10)
        self.add_arc('e10-1', (41, 20), (42, 23), radius_x=8)
        self.add_arc('e10-2', (42, 23), (38, 26), radius_x=4)
        self.add_arc('e11-1', (29, 33), (27, 42), radius_x=7)
        self.add_line('e11-2', (27, 42), (24, 40))
        self.add_arc('e12', (17, 30), (6, 25), radius_x=10, sweep=False)
        self.add_contour('c0', 'e7', 'e0', 'e8', 'e1', 'e9-1', 'e9-2', 'e2', 'e10-1', 'e10-2', 'e3', 'e4', 'e11-1', 'e11-2', 'e5', 'e12')
        self.add_contour('c1', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
