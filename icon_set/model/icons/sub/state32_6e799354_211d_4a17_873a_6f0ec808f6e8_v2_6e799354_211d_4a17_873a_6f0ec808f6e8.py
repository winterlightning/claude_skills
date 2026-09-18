# Variant of state32-6e799354-211d-4a17-873a-6f0ec808f6e8; parent file remains unchanged.
"""Independent 32px profile of state32-6e799354-211d-4a17-873a-6f0ec808f6e8.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '6e799354-211d-4a17-873a-6f0ec808f6e8'
SOURCE_PATH = 'icon_set/assets/combination-state32/6e799354-211d-4a17-873a-6f0ec808f6e8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6e799354-211d-4a17-873a-6f0ec808f6e8', 'icon_set/assets/combination-state32/6e799354-211d-4a17-873a-6f0ec808f6e8.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '5f61e75816bab9b1d413cb50ea0c8467e766b60aefb3f293af4e2da3e28b4c9a'

class DrawingVariant2(Sub32):
    icon_id = 'state32-6e799354-211d-4a17-873a-6f0ec808f6e8-v2'
    variant_of = 'state32-6e799354-211d-4a17-873a-6f0ec808f6e8'
    variant_label = 'Separate the actual at-sign bowl and stem junction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (24, 29), ((21, 30), (19, 30), (17, 30)))
        self.add_bezier('p1-r1-2', (17, 30), ((8, 30), (2, 23), (2, 16)))
        self.add_bezier('p1-r1-3', (2, 16), ((2, 14), (3, 11), (5, 9)))
        self.add_bezier('p1-r1-4', (5, 9), ((8, 4), (12, 2), (17, 2)))
        self.add_bezier('p1-r1-5', (17, 2), ((23, 2), (30, 7), (30, 15)))
        self.add_bezier('p1-r1-6', (30, 15), ((30, 16), (30, 17), (29, 18)))
        self.add_bezier('p1-r1-7', (29, 18), ((28.333333333333332, 21.333333333333332), (26.666666666666668, 23), (24, 23)))
        self.add_bezier('p1-r1-8', (24, 23), ((22, 23), (21, 22), (21, 20)))
        self.add_line('p1-r1-9', (21, 20), (21, 11))
        self.add_bezier('p1-r1-10', (21, 11), ((20, 9), (18, 9), (16, 9)))
        self.add_bezier('p1-r1-11', (16, 9), ((13, 9), (9, 12), (9, 17)))
        self.add_bezier('p1-r1-12', (9, 17), ((9, 21), (12, 23), (15, 23)))
        self.add_bezier('p1-r1-13', (15, 23), ((18, 23), (21, 21), (21, 17)))
        self.add_contour('outer', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_contour('bowl', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', closed=False)
        self.relate('connect','outer','bowl')
        self.relate('connect', 'p1-r1-9', 'p1-r1-13')
