"""Independent 32px profile of person-with-center-parted-hair.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '194e0c8a-520e-4ab3-9a3e-2d1ab17a737a'
SOURCE_PATH = 'pictographic-primitives/avatars/woman_194e0c8a-520e-4ab3-9a3e-2d1ab17a737a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('194e0c8a-520e-4ab3-9a3e-2d1ab17a737a', 'pictographic-primitives/avatars/woman_194e0c8a-520e-4ab3-9a3e-2d1ab17a737a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-with-center-parted-hair',)
SOLO_SOURCE_ICON_IDS = ('person-with-center-parted-hair',)
REFERENCE_EXPORT_SHA256 = '289e8424138ee365ea9675a60bced483833aa53253ef39ca5fab2d919caa37bc'

class Drawing(Sub32):
    icon_id = 'person-with-center-parted-hair-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'avatars'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (9, 9), (23, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_arc('p2-r1-1', (23, 9), (9, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (9, 9), (6, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (23, 9), (26, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_bezier('p5-r1-1', (9, 9), ((13, 9), (15, 8), (16, 6)))
        self.add_bezier('p5-r1-2', (16, 6), ((17, 8), (20, 9), (23, 9)))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (5, 30), (5, 24))
        self.add_arc('p6-r1-2', (5, 24), (10, 19), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (10, 19), (16, 19))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (16, 19), (22, 19))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_arc('p9-r1-1', (22, 19), (27, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p9-r1-2', (27, 24), (27, 30))
        self.add_contour('path-9-1', 'p9-r1-1', 'p9-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-1', 'p4-r1-1')
        self.relate("connect", 'p1-r1-1', 'p5-r1-1')
        self.relate("connect", 'p1-r1-1', 'p5-r1-2')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p5-r1-1')
        self.relate("connect", 'p2-r1-1', 'p5-r1-2')
        self.relate("connect", 'p3-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-2')
        self.relate("connect", 'p6-r1-2', 'p7-r1-1')
        self.relate("connect", 'p7-r1-1', 'p8-r1-1')
        self.relate("connect", 'p8-r1-1', 'p9-r1-1')
