"""Independent 32px profile of slender-pear-shaped-vase.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'cd5f7537-8a7a-4054-b479-eedbb6a2ed1e'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/bottle_cd5f7537-8a7a-4054-b479-eedbb6a2ed1e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cd5f7537-8a7a-4054-b479-eedbb6a2ed1e', 'pictographic-primitives/decoration/batch-01/bottle_cd5f7537-8a7a-4054-b479-eedbb6a2ed1e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/slender-pear-shaped-vase',)
SOLO_SOURCE_ICON_IDS = ('slender-pear-shaped-vase',)
REFERENCE_EXPORT_SHA256 = '7c0ccbe3e08fb6d1ef2674b2c4cefe741d761d2bc3b74f75cf8ed2ef8fb7d92b'

class Drawing(Sub32):
    icon_id = 'slender-pear-shaped-vase-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'decoration'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 2), (22, 2))
        self.add_bezier('p1-r1-2', (22, 2), ((21, 4), (21, 6), (21, 7)))
        self.add_bezier('p1-r1-3', (21, 7), ((21, 9), (21, 10), (22, 12)))
        self.add_bezier('p1-r1-4', (22, 12), ((23, 15), (27, 15), (27, 21)))
        self.add_bezier('p1-r1-5', (27, 21), ((27, 26), (22, 30), (16, 30)))
        self.add_bezier('p1-r1-6', (16, 30), ((10, 30), (5, 26), (5, 21)))
        self.add_bezier('p1-r1-7', (5, 21), ((5, 15), (9, 15), (10, 12)))
        self.add_bezier('p1-r1-8', (10, 12), ((11, 10), (11, 9), (11, 7)))
        self.add_bezier('p1-r1-9', (11, 7), ((11, 6), (11, 4), (10, 2)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
