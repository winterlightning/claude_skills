"""Independent 32px profile of skate-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '77e5b55a-d6f9-48ba-b7e0-1e1880592f39'
SOURCE_PATH = 'pictographic-primitives/symbol/skate 1_77e5b55a-d6f9-48ba-b7e0-1e1880592f39.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('77e5b55a-d6f9-48ba-b7e0-1e1880592f39', 'pictographic-primitives/symbol/skate 1_77e5b55a-d6f9-48ba-b7e0-1e1880592f39.svg'),)
PROFILE_SOURCE_KEYS = ('solo/skate-1',)
SOLO_SOURCE_ICON_IDS = ('skate-1',)
REFERENCE_EXPORT_SHA256 = '26510fc2f7b3a8c42da4b4b69b05f9981f664b97c478d9614a4127dc8dfb82fd'

class Drawing(Sub32):
    icon_id = 'skate-1-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (4, 2), (17, 2))
        self.add_line('p1-r1-2', (17, 2), (17, 9))
        self.add_bezier('p1-r1-3', (17, 9), ((17, 14), (22, 14), (26, 17)))
        self.add_bezier('p1-r1-4', (26, 17), ((28, 18), (30, 20), (30, 22)))
        self.add_line('p1-r1-5', (30, 22), (5, 22))
        self.add_bezier('p1-r1-6', (5, 22), ((3, 22), (2, 20), (2, 18)))
        self.add_bezier('p1-r1-7', (2, 18), ((2, 15), (4, 14), (4, 11)))
        self.add_line('p1-r1-8', (4, 11), (4, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (5, 30), (5, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (17, 30), (17, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (28, 30), (28, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
