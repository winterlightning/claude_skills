"""Independent 32px profile of head.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '97903c22-da46-4913-b7f3-4e20608ab202'
SOURCE_PATH = 'pictographic-primitives/symbol/head_97903c22-da46-4913-b7f3-4e20608ab202.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('97903c22-da46-4913-b7f3-4e20608ab202', 'pictographic-primitives/symbol/head_97903c22-da46-4913-b7f3-4e20608ab202.svg'),)
PROFILE_SOURCE_KEYS = ('solo/head',)
SOLO_SOURCE_ICON_IDS = ('head',)
REFERENCE_EXPORT_SHA256 = 'd27ad831e583471c53307cb4db052d724b7c26ab8cbdee9ee01187d219f0408e'

class Drawing(Sub32):
    icon_id = 'head-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 30), (8, 22))
        self.add_bezier('p1-r1-2', (8, 22), ((8, 18), (5, 17), (5, 12)))
        self.add_bezier('p1-r1-3', (5, 12), ((5, 6), (9, 2), (15, 2)))
        self.add_bezier('p1-r1-4', (15, 2), ((20, 2), (24, 6), (24, 12)))
        self.add_line('p1-r1-5', (24, 12), (27, 19))
        self.add_line('p1-r1-6', (27, 19), (24, 19))
        self.add_line('p1-r1-7', (24, 19), (24, 23))
        self.add_bezier('p1-r1-8', (24, 23), ((24, 24), (24, 24), (24, 25)))
        self.add_bezier('p1-r1-9', (24, 25), ((23, 26), (22, 26), (22, 26)))
        self.add_line('p1-r1-10', (22, 26), (19, 26))
        self.add_line('p1-r1-11', (19, 26), (19, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
