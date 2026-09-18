"""Independent 32px profile of cupped-hand-facing-right.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1ab29135-e724-4766-8bba-d4d0f8b7b6d5'
SOURCE_PATH = 'pictographic-primitives/business/begging hand ask_1ab29135-e724-4766-8bba-d4d0f8b7b6d5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1ab29135-e724-4766-8bba-d4d0f8b7b6d5', 'pictographic-primitives/business/begging hand ask_1ab29135-e724-4766-8bba-d4d0f8b7b6d5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cupped-hand-facing-right',)
SOLO_SOURCE_ICON_IDS = ('cupped-hand-facing-right',)
REFERENCE_EXPORT_SHA256 = 'b826b683ec4ccced4119d52af613d4e90985586549ee2795fd3c8791e94c61e6'

class Drawing(Sub32):
    icon_id = 'cupped-hand-facing-right-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'business'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 10), ((6, 8), (8, 5), (12, 5)))
        self.add_bezier('p1-r1-2', (12, 5), ((15, 5), (17, 8), (20, 9)))
        self.add_bezier('p1-r1-3', (20, 9), ((22, 10), (22, 11), (22, 13)))
        self.add_bezier('p1-r1-4', (22, 13), ((22, 14), (22, 15), (20, 16)))
        self.add_line('p1-r1-5', (20, 16), (27, 10))
        self.add_bezier('p1-r1-6', (27, 10), ((28, 9), (29, 9), (29, 9)))
        self.add_bezier('p1-r1-7', (29, 9), ((30, 9), (30, 10), (30, 12)))
        self.add_bezier('p1-r1-8', (30, 12), ((30, 12), (30, 12), (30, 12)))
        self.add_bezier('p1-r1-9', (30, 12), ((30, 19), (23, 27), (16, 27)))
        self.add_bezier('p1-r1-10', (16, 27), ((10, 27), (8, 22), (2, 22)))
        self.add_line('p1-r1-11', (2, 22), (2, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
        self.add_line('p2-r1-1', (20, 16), (12, 13))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
