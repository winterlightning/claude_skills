"""Independent 32px profile of curly-brackets.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b0b92f6f-2602-450a-ad0e-3d84e809ce25'
SOURCE_PATH = 'pictographic-primitives/programing/curly brackets_b0b92f6f-2602-450a-ad0e-3d84e809ce25.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b0b92f6f-2602-450a-ad0e-3d84e809ce25', 'pictographic-primitives/programing/curly brackets_b0b92f6f-2602-450a-ad0e-3d84e809ce25.svg'),)
PROFILE_SOURCE_KEYS = ('solo/curly-brackets',)
SOLO_SOURCE_ICON_IDS = ('curly-brackets',)
REFERENCE_EXPORT_SHA256 = '07d8ed1d62ffef983feb1106bd6871dc7c865353987cb48e50d23a262921aaaf'

class Drawing(Sub32):
    icon_id = 'curly-brackets-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'programing'
    categories = ('programing', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (12, 2), ((7, 2), (7, 6), (7, 9)))
        self.add_bezier('p1-r1-2', (7, 9), ((7, 13), (7, 16), (2, 16)))
        self.add_bezier('p1-r1-3', (2, 16), ((7, 16), (7, 19), (7, 23)))
        self.add_bezier('p1-r1-4', (7, 23), ((7, 26), (7, 30), (12, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (20, 2), ((25, 2), (25, 6), (25, 9)))
        self.add_bezier('p2-r1-2', (25, 9), ((25, 13), (25, 16), (30, 16)))
        self.add_bezier('p2-r1-3', (30, 16), ((25, 16), (25, 19), (25, 23)))
        self.add_bezier('p2-r1-4', (25, 23), ((25, 26), (25, 30), (20, 30)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
