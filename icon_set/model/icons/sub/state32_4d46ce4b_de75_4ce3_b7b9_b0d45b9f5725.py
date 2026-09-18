"""Independent 32px profile of state32-4d46ce4b-de75-4ce3-b7b9-b0d45b9f5725.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4d46ce4b-de75-4ce3-b7b9-b0d45b9f5725'
SOURCE_PATH = 'icon_set/assets/combination-state32/4d46ce4b-de75-4ce3-b7b9-b0d45b9f5725.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4d46ce4b-de75-4ce3-b7b9-b0d45b9f5725', 'icon_set/assets/combination-state32/4d46ce4b-de75-4ce3-b7b9-b0d45b9f5725.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '1841b5c4badb1b17f67e118b284ffafeb96d0e7e557901cd834dacda16798e57'

class Drawing(Sub32):
    icon_id = 'state32-4d46ce4b-de75-4ce3-b7b9-b0d45b9f5725'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 18), ((2, 25), (7, 30), (14, 30)))
        self.add_bezier('p1-r1-2', (14, 30), ((20, 30), (25, 25), (25, 18)))
        self.add_bezier('p1-r1-3', (25, 18), ((25, 12), (20, 7), (14, 7)))
        self.add_bezier('p1-r1-4', (14, 7), ((7, 7), (2, 12), (2, 18)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (21, 7), ((21, 9), (23, 11), (25, 11)))
        self.add_bezier('p2-r1-2', (25, 11), ((28, 11), (30, 9), (30, 7)))
        self.add_bezier('p2-r1-3', (30, 7), ((30, 4), (28, 2), (25, 2)))
        self.add_bezier('p2-r1-4', (25, 2), ((23, 2), (21, 4), (21, 7)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
