"""Independent 32px profile of woman-news-display-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '40d938a7-d3a2-43fa-ada3-7ab755c8d6d2'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/40d938a7-d3a2-43fa-ada3-7ab755c8d6d2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('40d938a7-d3a2-43fa-ada3-7ab755c8d6d2', 'icon_set/dist/gallery/combination-originals/40d938a7-d3a2-43fa-ada3-7ab755c8d6d2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/woman-news-display-content',)
SOLO_SOURCE_ICON_IDS = ('woman-news-display-content',)
REFERENCE_EXPORT_SHA256 = 'eb97162081ad5d577a4c763d2e75592fac245fcde28503961eea58f5af8b5be3'

class Drawing(Sub32):
    icon_id = 'woman-news-display-content-sub32'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'users'
    categories = ('users', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Adopted from the production stroke edit (Browser Edit by hina).
        self.add_arc('p1-r1-1', (20, 10), (28, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (28, 10), (20, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-1', (19, 26), (29, 26), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p3-r1-1', (2, 11), (10, 11))
        self.add_line('p3-r1-2', (10, 11), (10, 19))
        self.add_line('p3-r1-3', (10, 19), (2, 19))
        self.add_line('p3-r1-4', (2, 19), (2, 11))
        self.add_line('p4-r1-1', (20, 10), (18, 14))
        self.add_line('p5-r1-1', (28, 10), (30, 13))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-1', 'p5-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p5-r1-1')
