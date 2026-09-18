"""Independent 32px profile of minimalist-pig-face-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2878cc5b-7eb0-476d-b3f7-1ad79cba16a4'
SOURCE_PATH = 'pictographic-primitives/state/pig_2878cc5b-7eb0-476d-b3f7-1ad79cba16a4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2878cc5b-7eb0-476d-b3f7-1ad79cba16a4', 'pictographic-primitives/state/pig_2878cc5b-7eb0-476d-b3f7-1ad79cba16a4.svg'),)
PROFILE_SOURCE_KEYS = ('solo/minimalist-pig-face-solo',)
SOLO_SOURCE_ICON_IDS = ('minimalist-pig-face-solo',)
REFERENCE_EXPORT_SHA256 = 'beeafe89b51ab7fabf5e06d610366fe3135b83c447034f4159cab89317bee5b2'

class Drawing(Sub32):
    icon_id = 'minimalist-pig-face-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (8, 5), ((6, 4), (4, 2), (2, 2)))
        self.add_bezier('p1-r1-2', (2, 2), ((2, 8), (4, 11), (5, 14)))
        self.add_bezier('p1-r1-3', (5, 14), ((5, 15), (5, 16), (5, 17)))
        self.add_bezier('p1-r1-4', (5, 17), ((5, 24), (9, 30), (16, 30)))
        self.add_bezier('p1-r1-5', (16, 30), ((23, 30), (27, 24), (27, 17)))
        self.add_bezier('p1-r1-6', (27, 17), ((27, 16), (27, 15), (27, 14)))
        self.add_bezier('p1-r1-7', (27, 14), ((28, 11), (30, 8), (30, 2)))
        self.add_bezier('p1-r1-8', (30, 2), ((28, 2), (26, 4), (24, 5)))
        self.add_bezier('p1-r1-9', (24, 5), ((21, 4), (19, 3), (16, 3)))
        self.add_bezier('p1-r1-10', (16, 3), ((13, 3), (11, 4), (8, 5)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_arc('p2-r1-1', (14, 21), (18, 21), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (18, 21), (14, 21), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (11, 13), (11, 13))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (21, 13), (21, 13))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
