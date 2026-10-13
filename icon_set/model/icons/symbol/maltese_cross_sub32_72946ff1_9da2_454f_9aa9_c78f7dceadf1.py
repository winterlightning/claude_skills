"""Independent 32px profile of maltese-cross.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '72946ff1-9da2-454f-9aa9-c78f7dceadf1'
SOURCE_PATH = 'pictographic-primitives/symbol/maltese cross_72946ff1-9da2-454f-9aa9-c78f7dceadf1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('72946ff1-9da2-454f-9aa9-c78f7dceadf1', 'pictographic-primitives/symbol/maltese cross_72946ff1-9da2-454f-9aa9-c78f7dceadf1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/maltese-cross',)
SOLO_SOURCE_ICON_IDS = ('maltese-cross',)
REFERENCE_EXPORT_SHA256 = 'a98ae6b307625d709e82495a854a2d52df25bb5e2ba8f964ab9ff457c62704f0'

class Drawing(Sub32):
    icon_id = 'maltese-cross-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 2), (22, 2))
        self.add_line('p1-r1-2', (22, 2), (20, 12))
        self.add_line('p1-r1-3', (20, 12), (30, 10))
        self.add_line('p1-r1-4', (30, 10), (30, 22))
        self.add_line('p1-r1-5', (30, 22), (20, 20))
        self.add_line('p1-r1-6', (20, 20), (22, 30))
        self.add_line('p1-r1-7', (22, 30), (10, 30))
        self.add_line('p1-r1-8', (10, 30), (12, 20))
        self.add_line('p1-r1-9', (12, 20), (2, 22))
        self.add_line('p1-r1-10', (2, 22), (2, 10))
        self.add_line('p1-r1-11', (2, 10), (12, 12))
        self.add_line('p1-r1-12', (12, 12), (10, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=True)
