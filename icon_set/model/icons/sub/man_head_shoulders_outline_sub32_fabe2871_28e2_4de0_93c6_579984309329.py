"""Independent 32px profile of man-head-shoulders-outline.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'fabe2871-28e2-4de0-93c6-579984309329'
SOURCE_PATH = 'pictographic-primitives/photography/man_fabe2871-28e2-4de0-93c6-579984309329.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fabe2871-28e2-4de0-93c6-579984309329', 'pictographic-primitives/photography/man_fabe2871-28e2-4de0-93c6-579984309329.svg'),)
PROFILE_SOURCE_KEYS = ('solo/man-head-shoulders-outline',)
SOLO_SOURCE_ICON_IDS = ('man-head-shoulders-outline',)
REFERENCE_EXPORT_SHA256 = '49be0ec3d8f72c2837c6bd1eb5b01cf0c292408a493deb9f7778281fed18efe0'

class Drawing(Sub32):
    icon_id = 'man-head-shoulders-outline-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/photography'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 2), (19, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_arc('p2-r1-1', (19, 2), (23, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (23, 6), (23, 12))
        self.add_line('p3-r1-2', (23, 12), (19, 19))
        self.add_line('p3-r1-3', (19, 19), (19, 22))
        self.add_line('p3-r1-4', (19, 22), (24, 24))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_arc('p4-r1-1', (24, 24), (27, 30), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (5, 30), (8, 24), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (8, 24), (13, 22))
        self.add_line('p6-r1-2', (13, 22), (13, 19))
        self.add_line('p6-r1-3', (13, 19), (9, 12))
        self.add_line('p6-r1-4', (9, 12), (9, 6))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', closed=False)
        self.add_arc('p7-r1-1', (9, 6), (13, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p7-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p3-r1-4', 'p4-r1-1')
        self.relate("connect", 'p5-r1-1', 'p6-r1-1')
        self.relate("connect", 'p6-r1-4', 'p7-r1-1')
