"""Independent 32px profile of maltese-cross.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

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
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 2), (22, 2))
        self.add_bezier('p1-r1-2', (22, 2), ((21, 5), (20, 7), (20, 9)))
        self.add_bezier('p1-r1-3', (20, 9), ((20, 10), (20, 11), (21, 11)))
        self.add_bezier('p1-r1-4', (21, 11), ((21, 12), (22, 12), (23, 12)))
        self.add_bezier('p1-r1-5', (23, 12), ((25, 12), (27, 11), (30, 10)))
        self.add_line('p1-r1-6', (30, 10), (30, 22))
        self.add_bezier('p1-r1-7', (30, 22), ((27, 21), (25, 20), (23, 20)))
        self.add_bezier('p1-r1-8', (23, 20), ((22, 20), (21, 20), (21, 21)))
        self.add_bezier('p1-r1-9', (21, 21), ((20, 21), (20, 22), (20, 23)))
        self.add_bezier('p1-r1-10', (20, 23), ((20, 25), (21, 27), (22, 30)))
        self.add_line('p1-r1-11', (22, 30), (10, 30))
        self.add_bezier('p1-r1-12', (10, 30), ((11, 27), (12, 25), (12, 23)))
        self.add_bezier('p1-r1-13', (12, 23), ((12, 22), (12, 21), (11, 21)))
        self.add_bezier('p1-r1-14', (11, 21), ((11, 20), (10, 20), (9, 20)))
        self.add_bezier('p1-r1-15', (9, 20), ((7, 20), (5, 21), (2, 22)))
        self.add_line('p1-r1-16', (2, 22), (2, 10))
        self.add_bezier('p1-r1-17', (2, 10), ((5, 11), (7, 12), (9, 12)))
        self.add_bezier('p1-r1-18', (9, 12), ((10, 12), (11, 12), (11, 11)))
        self.add_bezier('p1-r1-19', (11, 11), ((12, 11), (12, 10), (12, 9)))
        self.add_bezier('p1-r1-20', (12, 9), ((12, 7), (11, 5), (10, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', closed=False)
