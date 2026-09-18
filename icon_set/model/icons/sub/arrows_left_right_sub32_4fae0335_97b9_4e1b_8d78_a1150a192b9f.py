"""Independent 32px profile of arrows-left-right.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4fae0335-97b9-4e1b-8d78-a1150a192b9f'
SOURCE_PATH = 'pictographic-primitives/symbol/arrows left right_4fae0335-97b9-4e1b-8d78-a1150a192b9f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4fae0335-97b9-4e1b-8d78-a1150a192b9f', 'pictographic-primitives/symbol/arrows left right_4fae0335-97b9-4e1b-8d78-a1150a192b9f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrows-left-right',)
SOLO_SOURCE_ICON_IDS = ('arrows-left-right',)
REFERENCE_EXPORT_SHA256 = 'a963148568cf166ff6723bc219bc565e68b1725de0fa45d129a2216a630a8cbf'

class Drawing(Sub32):
    icon_id = 'arrows-left-right-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 7), (10, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (10, 2), (10, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (10, 2), (17, 7))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (22, 13), (22, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (22, 30), (15, 25))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (22, 30), (27, 25))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-1', 'p6-r1-1')
        self.relate("connect", 'p5-r1-1', 'p6-r1-1')
