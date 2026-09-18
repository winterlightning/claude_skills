"""Independent 32px profile of smart.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7'
SOURCE_PATH = 'pictographic-primitives/state/smart_a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7', 'pictographic-primitives/state/smart_a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/smart',)
SOLO_SOURCE_ICON_IDS = ('smart',)
REFERENCE_EXPORT_SHA256 = '09cd865c43d3540992d1184e677cbc210e361c060348f4c51a48a9340af15d7b'

class Drawing(Sub32):
    icon_id = 'smart-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 12), ((7, 7), (10, 5), (16, 5)))
        self.add_bezier('p1-r1-2', (16, 5), ((22, 5), (25, 7), (30, 12)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (6, 20), ((10, 17), (12, 15), (16, 15)))
        self.add_bezier('p2-r1-2', (16, 15), ((20, 15), (22, 17), (26, 20)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (12, 27), ((13, 26), (14, 25), (16, 25)))
        self.add_bezier('p3-r1-2', (16, 25), ((18, 25), (19, 26), (20, 27)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
