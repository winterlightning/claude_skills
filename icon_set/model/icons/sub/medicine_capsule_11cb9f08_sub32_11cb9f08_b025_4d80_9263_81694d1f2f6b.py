"""Independent 32px profile of medicine-capsule-11cb9f08.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '11cb9f08-b025-4d80-9263-81694d1f2f6b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pill_11cb9f08-b025-4d80-9263-81694d1f2f6b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('11cb9f08-b025-4d80-9263-81694d1f2f6b', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pill_11cb9f08-b025-4d80-9263-81694d1f2f6b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/medicine-capsule-11cb9f08',)
SOLO_SOURCE_ICON_IDS = ('medicine-capsule-11cb9f08',)
REFERENCE_EXPORT_SHA256 = 'af29d98b4ba333a72f22bd1762fee5133f572d988e9113722e7d1cb5a27725d7'

class Drawing(Sub32):
    icon_id = 'medicine-capsule-11cb9f08-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'health'
    categories = ('health', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 18), (10, 11))
        self.add_line('p1-r1-2', (10, 11), (14, 5))
        self.add_bezier('p1-r1-3', (14, 5), ((16, 3), (18, 2), (21, 2)))
        self.add_bezier('p1-r1-4', (21, 2), ((22, 2), (24, 3), (25, 4)))
        self.add_bezier('p1-r1-5', (25, 4), ((27, 5), (28, 7), (28, 10)))
        self.add_bezier('p1-r1-6', (28, 10), ((28, 11), (28, 13), (27, 14)))
        self.add_line('p1-r1-7', (27, 14), (22, 21))
        self.add_line('p1-r1-8', (22, 21), (18, 27))
        self.add_bezier('p1-r1-9', (18, 27), ((16, 29), (14, 30), (11, 30)))
        self.add_bezier('p1-r1-10', (11, 30), ((10, 30), (8, 29), (7, 28)))
        self.add_bezier('p1-r1-11', (7, 28), ((5, 27), (4, 25), (4, 22)))
        self.add_bezier('p1-r1-12', (4, 22), ((4, 21), (4, 19), (5, 18)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (10, 11), (22, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-7', 'p2-r1-1')
        self.relate("connect", 'p1-r1-8', 'p2-r1-1')
