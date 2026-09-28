"""Independent 32px profile of brain-artificial-intelligence.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '74d6ac6c-9f6f-4183-9ee6-960cbc7f4216'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/brain_74d6ac6c-9f6f-4183-9ee6-960cbc7f4216.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('74d6ac6c-9f6f-4183-9ee6-960cbc7f4216', 'pictographic-primitives/artificial-intelligence/brain_74d6ac6c-9f6f-4183-9ee6-960cbc7f4216.svg'),)
PROFILE_SOURCE_KEYS = ('solo/brain-artificial-intelligence',)
SOLO_SOURCE_ICON_IDS = ('brain-artificial-intelligence',)
REFERENCE_EXPORT_SHA256 = 'daadf07e500782e1a2320b8975fae080ff3567f131ef7098e2951db827eafd67'

class Drawing(Sub32):
    icon_id = 'brain-artificial-intelligence-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 7), ((16, 4), (14, 2), (11, 2)))
        self.add_bezier('p1-r1-2', (11, 2), ((8, 2), (7, 4), (7, 8)))
        self.add_bezier('p1-r1-3', (7, 8), ((4, 8), (2, 11), (2, 14)))
        self.add_bezier('p1-r1-4', (2, 14), ((2, 18), (4, 20), (5, 21)))
        self.add_bezier('p1-r1-5', (5, 21), ((5, 22), (5, 23), (5, 23)))
        self.add_bezier('p1-r1-6', (5, 23), ((5, 27), (7, 30), (11, 30)))
        self.add_bezier('p1-r1-7', (11, 30), ((14, 30), (16, 28), (16, 25)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_bezier('p2-r1-1', (7, 8), ((7, 11), (7, 13), (9, 13)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (16, 7), ((16, 4), (18, 2), (21, 2)))
        self.add_bezier('p3-r1-2', (21, 2), ((24, 2), (25, 4), (25, 8)))
        self.add_bezier('p3-r1-3', (25, 8), ((28, 8), (30, 11), (30, 14)))
        self.add_bezier('p3-r1-4', (30, 14), ((30, 18), (28, 20), (27, 21)))
        self.add_bezier('p3-r1-5', (27, 21), ((27, 22), (27, 23), (27, 23)))
        self.add_bezier('p3-r1-6', (27, 23), ((27, 27), (25, 30), (21, 30)))
        self.add_bezier('p3-r1-7', (21, 30), ((18, 30), (16, 28), (16, 25)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
        self.add_bezier('p4-r1-1', (25, 8), ((25, 11), (25, 13), (23, 13)))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (16, 7), (16, 25))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-1', 'p5-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-7', 'p3-r1-7')
        self.relate("connect", 'p1-r1-7', 'p5-r1-1')
        self.relate("connect", 'p3-r1-1', 'p5-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-3', 'p4-r1-1')
        self.relate("connect", 'p3-r1-7', 'p5-r1-1')
