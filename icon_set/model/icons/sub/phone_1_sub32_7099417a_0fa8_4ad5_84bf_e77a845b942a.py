"""Independent 32px profile of phone-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7099417a-0fa8-4ad5-84bf-e77a845b942a'
SOURCE_PATH = 'pictographic-primitives/state/phone 1_7099417a-0fa8-4ad5-84bf-e77a845b942a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7099417a-0fa8-4ad5-84bf-e77a845b942a', 'pictographic-primitives/state/phone 1_7099417a-0fa8-4ad5-84bf-e77a845b942a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/phone-1',)
SOLO_SOURCE_ICON_IDS = ('phone-1',)
REFERENCE_EXPORT_SHA256 = '91967b4615ba3d49472b77e8b22566423fdc34d633fe8e67a7453e22b60c00cb'

class Drawing(Sub32):
    icon_id = 'phone-1-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 2), (13, 7))
        self.add_bezier('p1-r1-2', (13, 7), ((14, 7), (14, 8), (14, 8)))
        self.add_bezier('p1-r1-3', (14, 8), ((14, 10), (12, 11), (11, 12)))
        self.add_bezier('p1-r1-4', (11, 12), ((13, 16), (16, 19), (20, 21)))
        self.add_bezier('p1-r1-5', (20, 21), ((21, 19), (22, 18), (23, 18)))
        self.add_bezier('p1-r1-6', (23, 18), ((24, 18), (25, 19), (25, 19)))
        self.add_line('p1-r1-7', (25, 19), (30, 25))
        self.add_bezier('p1-r1-8', (30, 25), ((30, 28), (27, 30), (24, 30)))
        self.add_bezier('p1-r1-9', (24, 30), ((13, 28), (2, 18), (2, 8)))
        self.add_bezier('p1-r1-10', (2, 8), ((2, 5), (4, 2), (7, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
