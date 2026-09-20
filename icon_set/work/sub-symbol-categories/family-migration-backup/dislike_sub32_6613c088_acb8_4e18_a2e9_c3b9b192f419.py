"""Independent 32px profile of dislike.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6613c088-acb8-4e18-a2e9-c3b9b192f419'
SOURCE_PATH = 'pictographic-primitives/rating/dislike_6613c088-acb8-4e18-a2e9-c3b9b192f419.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6613c088-acb8-4e18-a2e9-c3b9b192f419', 'pictographic-primitives/rating/dislike_6613c088-acb8-4e18-a2e9-c3b9b192f419.svg'),)
PROFILE_SOURCE_KEYS = ('solo/dislike',)
SOLO_SOURCE_ICON_IDS = ('dislike',)
REFERENCE_EXPORT_SHA256 = '9773e56495ae5ced76cc481466088a7f10096fd692871b1e227b6eb35b600cc1'

class Drawing(Sub32):
    icon_id = 'dislike-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'rating'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (21, 2))
        self.add_bezier('p1-r1-2', (21, 2), ((25, 2), (26, 4), (27, 7)))
        self.add_bezier('p1-r1-3', (27, 7), ((28, 10), (30, 12), (30, 14)))
        self.add_bezier('p1-r1-4', (30, 14), ((30, 17), (28, 18), (26, 18)))
        self.add_line('p1-r1-5', (26, 18), (18, 18))
        self.add_bezier('p1-r1-6', (18, 18), ((18, 20), (21, 22), (21, 25)))
        self.add_bezier('p1-r1-7', (21, 25), ((21, 27), (19, 30), (18, 30)))
        self.add_bezier('p1-r1-8', (18, 30), ((16, 30), (13, 23), (11, 21)))
        self.add_bezier('p1-r1-9', (11, 21), ((8, 18), (5, 18), (2, 18)))
        self.add_line('p1-r1-10', (2, 18), (2, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
