"""Independent 32px profile of cat-head.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0da7dd89-02ff-406b-bac6-3026293829ce'
SOURCE_PATH = 'pictographic-primitives/pets/cat head_0da7dd89-02ff-406b-bac6-3026293829ce.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0da7dd89-02ff-406b-bac6-3026293829ce', 'pictographic-primitives/pets/cat head_0da7dd89-02ff-406b-bac6-3026293829ce.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cat-head',)
SOLO_SOURCE_ICON_IDS = ('cat-head',)
REFERENCE_EXPORT_SHA256 = '577352f01f05ae9641d8c517ebc8e1e13660fdf78a365f90136ccb66fd59f251'

class Drawing(Sub32):
    icon_id = 'cat-head-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'pets'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (11, 7), ((13, 7), (14, 6), (16, 6)))
        self.add_bezier('p1-r1-2', (16, 6), ((18, 6), (19, 7), (21, 7)))
        self.add_bezier('p1-r1-3', (21, 7), ((24, 4), (26, 2), (28, 2)))
        self.add_bezier('p1-r1-4', (28, 2), ((29, 3), (29, 5), (29, 7)))
        self.add_bezier('p1-r1-5', (29, 7), ((29, 9), (29, 12), (28, 13)))
        self.add_bezier('p1-r1-6', (28, 13), ((29, 14), (30, 16), (30, 18)))
        self.add_bezier('p1-r1-7', (30, 18), ((30, 25), (24, 30), (16, 30)))
        self.add_bezier('p1-r1-8', (16, 30), ((8, 30), (2, 25), (2, 18)))
        self.add_bezier('p1-r1-9', (2, 18), ((2, 16), (3, 14), (4, 13)))
        self.add_bezier('p1-r1-10', (4, 13), ((3, 12), (3, 9), (3, 7)))
        self.add_bezier('p1-r1-11', (3, 7), ((3, 5), (3, 3), (4, 2)))
        self.add_bezier('p1-r1-12', (4, 2), ((6, 2), (8, 4), (11, 7)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (10, 14), (10, 14))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (22, 14), (22, 14))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (11, 21), (16, 21), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=False)
        self.add_arc('p4-r1-2', (16, 21), (21, 21), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (16, 19), (16, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-2', 'p5-r1-1')
