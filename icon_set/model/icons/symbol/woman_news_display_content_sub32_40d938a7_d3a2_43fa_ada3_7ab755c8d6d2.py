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
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'users'
    categories = ('users', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 9), (24, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (24, 9), (16, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (10, 27), (30, 27), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 5), (8, 5))
        self.add_line('p3-r1-2', (8, 5), (8, 13))
        self.add_line('p3-r1-3', (8, 13), (2, 13))
        self.add_line('p3-r1-4', (2, 13), (2, 5))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (16, 9), (15, 14))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (24, 9), (26, 14))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-1', 'p5-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-2', 'p5-r1-1')
