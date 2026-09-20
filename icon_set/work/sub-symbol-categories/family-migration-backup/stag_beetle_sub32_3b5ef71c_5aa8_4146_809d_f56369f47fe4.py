"""Independent 32px profile of stag-beetle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3b5ef71c-5aa8-4146-809d-f56369f47fe4'
SOURCE_PATH = 'pictographic-primitives/animals/insect_3b5ef71c-5aa8-4146-809d-f56369f47fe4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3b5ef71c-5aa8-4146-809d-f56369f47fe4', 'pictographic-primitives/animals/insect_3b5ef71c-5aa8-4146-809d-f56369f47fe4.svg'),)
PROFILE_SOURCE_KEYS = ('solo/stag-beetle',)
SOLO_SOURCE_ICON_IDS = ('stag-beetle',)
REFERENCE_EXPORT_SHA256 = '20cc78faefe7f830dbe0f22f4824f5099573569ddd67cb658388eb475e5b290b'

class Drawing(Sub32):
    icon_id = 'stag-beetle-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'animals'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (8, 22), ((4, 22), (2, 19), (2, 16)))
        self.add_bezier('p1-r1-2', (2, 16), ((2, 13), (4, 10), (8, 10)))
        self.add_line('p1-r1-3', (8, 10), (19, 10))
        self.add_line('p1-r1-4', (19, 10), (19, 22))
        self.add_line('p1-r1-5', (19, 22), (16, 22))
        self.add_line('p1-r1-6', (16, 22), (9, 22))
        self.add_line('p1-r1-7', (9, 22), (8, 22))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_bezier('p2-r1-1', (19, 10), ((19, 7), (22, 5), (26, 5)))
        self.add_bezier('p2-r1-2', (26, 5), ((26, 6), (25, 7), (25, 8)))
        self.add_bezier('p2-r1-3', (25, 8), ((25, 9), (25, 9), (26, 10)))
        self.add_bezier('p2-r1-4', (26, 10), ((26, 11), (28, 13), (30, 13)))
        self.add_bezier('p2-r1-5', (30, 13), ((30, 17), (27, 20), (23, 22)))
        self.add_line('p2-r1-6', (23, 22), (19, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_arc('p3-r1-1', (9, 22), (6, 27), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_bezier('p4-r1-1', (23, 22), ((23, 24), (24, 26), (26, 27)))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-6')
        self.relate("connect", 'p1-r1-5', 'p2-r1-6')
        self.relate("connect", 'p1-r1-6', 'p3-r1-1')
        self.relate("connect", 'p1-r1-7', 'p3-r1-1')
        self.relate("connect", 'p2-r1-5', 'p4-r1-1')
        self.relate("connect", 'p2-r1-6', 'p4-r1-1')
