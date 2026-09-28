"""Independent 32px profile of bread.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '8ddeed7d-559d-4b14-9b46-092f255cb54a'
SOURCE_PATH = 'pictographic-primitives/symbol/bread_8ddeed7d-559d-4b14-9b46-092f255cb54a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8ddeed7d-559d-4b14-9b46-092f255cb54a', 'pictographic-primitives/symbol/bread_8ddeed7d-559d-4b14-9b46-092f255cb54a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bread',)
SOLO_SOURCE_ICON_IDS = ('bread',)
REFERENCE_EXPORT_SHA256 = 'f56ad0a977d1d9e7e7ca775b36a2dde8e64393840b0fc066f21b407cab95c519'

class Drawing(Sub32):
    icon_id = 'bread-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 2), ((27, 2), (30, 5), (30, 8)))
        self.add_bezier('p1-r1-2', (30, 8), ((30, 11), (28, 12), (28, 13)))
        self.add_line('p1-r1-3', (28, 13), (28, 28))
        self.add_bezier('p1-r1-4', (28, 28), ((28, 28), (27, 29), (27, 29)))
        self.add_bezier('p1-r1-5', (27, 29), ((27, 30), (26, 30), (25, 30)))
        self.add_line('p1-r1-6', (25, 30), (16, 30))
        self.add_line('p1-r1-7', (16, 30), (7, 30))
        self.add_bezier('p1-r1-8', (7, 30), ((6, 30), (5, 30), (5, 29)))
        self.add_bezier('p1-r1-9', (5, 29), ((5, 29), (4, 28), (4, 28)))
        self.add_line('p1-r1-10', (4, 28), (4, 13))
        self.add_bezier('p1-r1-11', (4, 13), ((4, 12), (2, 11), (2, 8)))
        self.add_bezier('p1-r1-12', (2, 8), ((2, 5), (5, 2), (16, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
