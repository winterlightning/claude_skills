"""Independent 32px profile of flower.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '6a1ecbd5-e710-49ac-8aeb-04d4c78b521a'
SOURCE_PATH = 'pictographic-primitives/nature/flower_6a1ecbd5-e710-49ac-8aeb-04d4c78b521a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6a1ecbd5-e710-49ac-8aeb-04d4c78b521a', 'pictographic-primitives/nature/flower_6a1ecbd5-e710-49ac-8aeb-04d4c78b521a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/flower',)
SOLO_SOURCE_ICON_IDS = ('flower',)
REFERENCE_EXPORT_SHA256 = '51cc4c763baa08420b102f5d5fb8f3ba1d2ad2d45d821a57ae893618297bea25'

class Drawing(Sub32):
    icon_id = 'flower-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
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
