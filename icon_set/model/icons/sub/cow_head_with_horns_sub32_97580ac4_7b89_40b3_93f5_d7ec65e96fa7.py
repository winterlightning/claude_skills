"""Independent 32px profile of cow-head-with-horns.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '97580ac4-7b89-40b3-93f5-d7ec65e96fa7'
SOURCE_PATH = 'pictographic-primitives/animals/cow_97580ac4-7b89-40b3-93f5-d7ec65e96fa7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('97580ac4-7b89-40b3-93f5-d7ec65e96fa7', 'pictographic-primitives/animals/cow_97580ac4-7b89-40b3-93f5-d7ec65e96fa7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cow-head-with-horns',)
SOLO_SOURCE_ICON_IDS = ('cow-head-with-horns',)
REFERENCE_EXPORT_SHA256 = '8495158b044a97fd4c607930f371f3df224cdb63e4843144d33cb1fb63f11232'

class Drawing(Sub32):
    icon_id = 'cow-head-with-horns-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'animals'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (8, 10), (16, 4), radius_x=8, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 4), (24, 10), radius_x=8, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (8, 10), (10, 23))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (24, 10), (22, 23))
        self.add_arc('p3-r1-2', (22, 23), (10, 23), radius_x=6, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (10, 23), (22, 23), radius_x=6, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (16, 4), (2, 2), radius_x=15, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_arc('p6-r1-1', (8, 10), (2, 18), radius_x=9, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_arc('p7-r1-1', (16, 4), (30, 2), radius_x=15, radius_y=5, large_arc=False, sweep=False)
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_arc('p8-r1-1', (24, 10), (30, 18), radius_x=9, radius_y=8, large_arc=False, sweep=False)
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p5-r1-1')
        self.relate("connect", 'p1-r1-1', 'p6-r1-1')
        self.relate("connect", 'p1-r1-1', 'p7-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p5-r1-1')
        self.relate("connect", 'p1-r1-2', 'p7-r1-1')
        self.relate("connect", 'p1-r1-2', 'p8-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p6-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p8-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p5-r1-1', 'p7-r1-1')
