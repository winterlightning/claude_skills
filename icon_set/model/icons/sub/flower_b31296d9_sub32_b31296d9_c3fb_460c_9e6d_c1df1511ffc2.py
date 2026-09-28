"""Independent 32px profile of flower-b31296d9.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b31296d9-c3fb-460c-9e6d-c1df1511ffc2'
SOURCE_PATH = 'pictographic-primitives/nature/flower_b31296d9-c3fb-460c-9e6d-c1df1511ffc2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b31296d9-c3fb-460c-9e6d-c1df1511ffc2', 'pictographic-primitives/nature/flower_b31296d9-c3fb-460c-9e6d-c1df1511ffc2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/flower-b31296d9',)
SOLO_SOURCE_ICON_IDS = ('flower-b31296d9',)
REFERENCE_EXPORT_SHA256 = '9079ec4486ddecad63a3746d448c1273457be5fe97e544c5be8577e179dfb4ae'

class Drawing(Sub32):
    icon_id = 'flower-b31296d9-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'nature'
    categories = ('nature', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 2), ((20, 2), (22, 4), (22, 9)))
        self.add_bezier('p1-r1-2', (22, 9), ((23, 9), (24, 9), (25, 9)))
        self.add_bezier('p1-r1-3', (25, 9), ((28, 9), (30, 11), (30, 14)))
        self.add_bezier('p1-r1-4', (30, 14), ((30, 18), (28, 20), (25, 21)))
        self.add_bezier('p1-r1-5', (25, 21), ((25, 22), (26, 23), (26, 25)))
        self.add_bezier('p1-r1-6', (26, 25), ((26, 28), (23, 30), (21, 30)))
        self.add_bezier('p1-r1-7', (21, 30), ((18, 30), (17, 28), (16, 26)))
        self.add_bezier('p1-r1-8', (16, 26), ((15, 28), (14, 30), (11, 30)))
        self.add_bezier('p1-r1-9', (11, 30), ((9, 30), (6, 28), (6, 25)))
        self.add_bezier('p1-r1-10', (6, 25), ((6, 23), (7, 22), (7, 21)))
        self.add_bezier('p1-r1-11', (7, 21), ((4, 20), (2, 18), (2, 14)))
        self.add_bezier('p1-r1-12', (2, 14), ((2, 11), (4, 9), (7, 9)))
        self.add_bezier('p1-r1-13', (7, 9), ((8, 9), (9, 9), (10, 9)))
        self.add_bezier('p1-r1-14', (10, 9), ((10, 4), (12, 2), (16, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', closed=False)
        self.add_line('p2-r1-1', (16, 16), (16, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
