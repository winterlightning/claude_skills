"""Independent 32px profile of airplane-top-view-rounded-wings.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3d6cd0c8-32b5-4b44-85b4-ced44e8263e3'
SOURCE_PATH = 'pictographic-primitives/travel/plane_3d6cd0c8-32b5-4b44-85b4-ced44e8263e3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3d6cd0c8-32b5-4b44-85b4-ced44e8263e3', 'pictographic-primitives/travel/plane_3d6cd0c8-32b5-4b44-85b4-ced44e8263e3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/airplane-top-view-rounded-wings',)
SOLO_SOURCE_ICON_IDS = ('airplane-top-view-rounded-wings',)
REFERENCE_EXPORT_SHA256 = 'fb4447582230d026b2568ca5211b41e60f1eebd3e3151a344cbe3a61af0633b2'

class Drawing(Sub32):
    icon_id = 'airplane-top-view-rounded-wings-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'travel'
    categories = ('travel', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (16, 28))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 20), (16, 12))
        self.add_line('p2-r1-2', (16, 12), (30, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (10, 30), (16, 26))
        self.add_line('p3-r1-2', (16, 26), (22, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p2-r1-2')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-2')
