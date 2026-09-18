"""Independent 32px profile of deer-head.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7bd92a94-e5b9-4c86-b41a-4bdf016eba52'
SOURCE_PATH = 'pictographic-primitives/animals/deer_7bd92a94-e5b9-4c86-b41a-4bdf016eba52.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7bd92a94-e5b9-4c86-b41a-4bdf016eba52', 'pictographic-primitives/animals/deer_7bd92a94-e5b9-4c86-b41a-4bdf016eba52.svg'),)
PROFILE_SOURCE_KEYS = ('solo/deer-head',)
SOLO_SOURCE_ICON_IDS = ('deer-head',)
REFERENCE_EXPORT_SHA256 = '50d4feb9e55fce991f58a8582542d6e3569d9a6a11e9a2c49c5b203354efda9a'

class Drawing(Sub32):
    icon_id = 'deer-head-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'nature/animals'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 14), (21, 14))
        self.add_line('p1-r1-2', (21, 14), (20, 26))
        self.add_arc('p1-r1-3', (20, 26), (12, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (12, 26), (11, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (11, 14), (2, 7))
        self.add_line('p2-r1-2', (2, 7), (2, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 7), (11, 4))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (21, 14), (30, 7))
        self.add_line('p4-r1-2', (30, 7), (30, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (30, 7), (21, 4))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p4-r1-1')
        self.relate("connect", 'p1-r1-2', 'p4-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-2', 'p5-r1-1')
