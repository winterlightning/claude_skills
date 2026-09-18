"""Independent 32px profile of building-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a6adecf4-5959-4f91-a3a7-5bdffc5bac69'
SOURCE_PATH = 'pictographic-primitives/building/building 1_a6adecf4-5959-4f91-a3a7-5bdffc5bac69.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a6adecf4-5959-4f91-a3a7-5bdffc5bac69', 'pictographic-primitives/building/building 1_a6adecf4-5959-4f91-a3a7-5bdffc5bac69.svg'),)
PROFILE_SOURCE_KEYS = ('solo/building-1',)
SOLO_SOURCE_ICON_IDS = ('building-1',)
REFERENCE_EXPORT_SHA256 = '519ccd77a4e3268a3a032ee8173d71c0af662aeea4929dff227dd0f07677ff94'

class Drawing(Sub32):
    icon_id = 'building-1-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'building'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 30), (5, 2))
        self.add_line('p1-r1-2', (5, 2), (27, 15))
        self.add_line('p1-r1-3', (27, 15), (27, 30))
        self.add_line('p1-r1-4', (27, 30), (5, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (13, 19), (18, 19))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
