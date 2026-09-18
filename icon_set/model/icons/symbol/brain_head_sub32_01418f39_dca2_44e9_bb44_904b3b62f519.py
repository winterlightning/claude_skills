"""Independent 32px profile of brain-head.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '01418f39-dca2-44e9-bb44-904b3b62f519'
SOURCE_PATH = 'pictographic-primitives/health/brain head_01418f39-dca2-44e9-bb44-904b3b62f519.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('01418f39-dca2-44e9-bb44-904b3b62f519', 'pictographic-primitives/health/brain head_01418f39-dca2-44e9-bb44-904b3b62f519.svg'),)
PROFILE_SOURCE_KEYS = ('solo/brain-head',)
SOLO_SOURCE_ICON_IDS = ('brain-head',)
REFERENCE_EXPORT_SHA256 = '4e9fb983bb72e4d7a71f42f95ae21478cbcefd1d64aa79e1a11360a2539f7039'

class Drawing(Sub32):
    icon_id = 'brain-head-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (24, 30), (24, 22))
        self.add_bezier('p1-r1-2', (24, 22), ((24, 18), (27, 17), (27, 12)))
        self.add_bezier('p1-r1-3', (27, 12), ((27, 6), (23, 2), (17, 2)))
        self.add_bezier('p1-r1-4', (17, 2), ((12, 2), (8, 6), (8, 12)))
        self.add_line('p1-r1-5', (8, 12), (5, 19))
        self.add_line('p1-r1-6', (5, 19), (8, 19))
        self.add_line('p1-r1-7', (8, 19), (8, 23))
        self.add_bezier('p1-r1-8', (8, 23), ((8, 24), (8, 24), (8, 25)))
        self.add_bezier('p1-r1-9', (8, 25), ((9, 26), (10, 26), (10, 26)))
        self.add_line('p1-r1-10', (10, 26), (13, 26))
        self.add_line('p1-r1-11', (13, 26), (13, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', closed=False)
